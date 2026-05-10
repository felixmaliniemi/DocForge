import re
from core_engine.utils.utils import clean_doc

def analyze_lua(content):
    """Extraherar Lua-funktioner med formella docblocks i --[[ ... ]]"""
    classes = []
    functions = []

    # Ta bort filkommentar i början
    content = re.sub(r"^\s*--\[\[.*?\]\]\s*", "", content, flags=re.DOTALL)

    pattern_func = r"(?:--\[\[\s*(?P<doc>.*?)\s*\]\]\s*)?function\s+(?P<name>\w+)\s*\("
    for m in re.finditer(pattern_func, content, re.DOTALL):
        doc = clean_doc(m.group("doc")) if m.group("doc") else "(ingen dokumentation hittades)"
        functions.append({"name": m.group("name"), "doc": doc})

    return classes, functions
