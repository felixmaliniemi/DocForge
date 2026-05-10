import re
from core_engine.utils.utils import clean_doc, BLOCK_DOC_CONTENT

def analyze_sql(content):
    """Extraherar block- och radkommentarer ovanför SQL CREATE-definitioner"""
    classes = []
    functions = []

    # Hitta CREATE-definitioner med doc
    pattern_def = re.compile(
        r"(?P<doc>(?:\s*--[^\n]*\n|\s*/\*"+BLOCK_DOC_CONTENT+r"\*/)*)\s*"
        r"(?:CREATE\s+(?:OR\s+REPLACE\s+)?)"
        r"(TABLE|VIEW|FUNCTION|PROCEDURE)\s+(?P<name>[\w.]+)",
        re.DOTALL | re.IGNORECASE
    )

    def_positions = []
    for m in pattern_def.finditer(content):
        doc_raw = m.group("doc")
        doc = clean_doc(doc_raw)
        if doc and doc.strip():
            name = m.group("name")
            def_type = m.group(2).upper()
            classes.append({"name": f"{def_type}: {name}", "doc": doc})
        def_positions.append((m.start(), m.end()))

    # Script-dokumentation som inte är kopplad till CREATE
    pattern_script = re.compile(r"/\*\s*(?P<doc>"+BLOCK_DOC_CONTENT+r")\s*\*/", re.DOTALL)
    for m in pattern_script.finditer(content):
        pos = m.start()
        if not any(start <= pos <= end for start, end in def_positions):
            functions.append({"name": "Script", "doc": clean_doc(m.group("doc"))})
            break

    return classes, functions
