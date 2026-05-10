import re
from core_engine.utils.utils import clean_doc

def analyze_javascript(content):
    """Extraherar JavaScript-funktioner med formella JSDoc docblocks (/** ... */)"""
    functions = []

    # Mönster för funktioner med docblock före (endast /** ... */)
    pattern_func = (
        r"(?:/\*\*(?P<doc>.*?)\*/\s*)?"
        r"(?:function\s+(?P<name>\w+)\s*\(|\s*(?P<name2>\w+)\s*=\s*function\s*\()"
    )

    for m in re.finditer(pattern_func, content, re.DOTALL):
        func_name = m.group("name") or m.group("name2")
        func_doc = clean_doc(m.group("doc")) if m.group("doc") else None

        if func_name:
            if not func_doc:
                func_doc = "(ingen dokumentation hittades)"

            functions.append({"name": func_name, "doc": func_doc})

    return [], functions
