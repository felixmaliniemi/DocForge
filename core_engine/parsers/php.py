import re
from core_engine.utils.utils import clean_doc

def analyze_php(content):
    """Extraherar PHP-funktioner och script-dokumentation med formella docblocks"""
    classes = []

    pattern_func = r"(?:/\*\*(?P<doc_block>.*?)\*/\s*)?function\s+(?P<name>\w+)\s*\("
    functions_list = []
    func_positions = []

    for m in re.finditer(pattern_func, content, re.DOTALL):
        doc = clean_doc(m.group("doc_block"))
        name = m.group("name")
        functions_list.append({"name": name, "doc": doc})
        func_positions.append((m.start(), m.end()))

    # Fria top-level docblock → Script
    pattern_script = r"/\*\*(?P<doc>.*?)\*/"
    for m in re.finditer(pattern_script, content, re.DOTALL):
        pos = m.start()
        if not any(start <= pos <= end for start, end in func_positions):
            functions_list.append({"name": "Script", "doc": clean_doc(m.group("doc"))})
            break

    return classes, functions_list
