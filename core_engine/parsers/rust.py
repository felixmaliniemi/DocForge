import re
from core_engine.utils.utils import clean_doc, BLOCK_DOC_CONTENT

def analyze_rust(content):
    """Extraherar **endast** formell Rust-dokumentation (/// och /** ... */)."""
    # Kombinerat mönster för att fånga antingen block-doc eller rad-doc
    pattern_doc = (
        r"(?:/\*\*(?P<doc_block>"+BLOCK_DOC_CONTENT+r")\*/\s*)?" 
        r"(?P<doc_line_full>(?:///\s*.*?\n\s*)+)?"
    )

    # Funktioner (fn)
    pattern_func = re.compile(pattern_doc + r"\s*fn\s+(?P<name>\w+)\s*\(", re.DOTALL | re.MULTILINE)
    functions = []
    for m in pattern_func.finditer(content):
        doc = m.group("doc_block") or m.group("doc_line_full")
        if doc and doc.strip():
            functions.append({"name": m.group("name"), "doc": clean_doc(doc)})

    # Structs (struct)
    pattern_struct = re.compile(pattern_doc + r"\s*struct\s+(?P<name>\w+)", re.DOTALL | re.MULTILINE)
    classes = []
    for m in pattern_struct.finditer(content):
        doc = m.group("doc_block") or m.group("doc_line_full")
        if doc and doc.strip():
            classes.append({"name": m.group("name"), "doc": clean_doc(doc)})

    return classes, functions
