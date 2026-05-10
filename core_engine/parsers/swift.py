import re
from core_engine.utils.utils import clean_doc, BLOCK_DOC_CONTENT

def analyze_swift(content):
    """Extraherar Swift-docstrings (/// eller /** ... */) ovanför funktioner och klasser/structs"""
    pattern_func = re.compile(
    # 1. Block Doc (/** ... */) - strikt capture
    r"(?:/\*\*(?P<doc_block>"+BLOCK_DOC_CONTENT+r")\*/\s*)?" 
    # 2. Eller Line Doc (///) - robust consecutive lines
    r"(?P<doc_line_full>(?:///\s*.*?\n\s*)+)?" 
    # 3. Definition
    r"\s*func\s+(?P<name>\w+)\s*\("
    , re.DOTALL | re.MULTILINE
    )

    functions = []
    for m in pattern_func.finditer(content):
        doc = m.group("doc_block") or m.group("doc_line_full")
        name = m.group("name")
        functions.append({"name": name, "doc": clean_doc(doc)})

    # --- Classes/Structs ---
    pattern_class = re.compile(
        # 1. Block Doc (/** ... */) - strikt capture
        r"(?:/\*\*(?P<doc_block>"+BLOCK_DOC_CONTENT+r")\*/\s*)?" 
        # 2. Eller Line Doc (///) - robust consecutive lines
        r"(?P<doc_line_full>(?:///\s*.*?\n\s*)+)?" 
        # 3. Definition
        r"\s*(?:class|struct)\s+(?P<name>\w+)"
        , re.DOTALL | re.MULTILINE
    )

    classes = []
    for m in pattern_class.finditer(content):
        doc = m.group("doc_block") or m.group("doc_line_full")
        name = m.group("name")
        classes.append({"name": name, "doc": clean_doc(doc)})

    return classes, functions
