import re
from core_engine.utils.utils import clean_doc

def analyze_css(content):
    """Extraherar CSS-kommentarer och element/block med blockkommentarer (/* ... */)"""
    classes = []
    functions = []

    # Filkommentar → Script
    file_comment_match = re.match(r"^\s*/\*\s*(?P<doc>.*?)\s*\*/", content, re.DOTALL)
    if file_comment_match:
        functions.append({"name": "Script", "doc": clean_doc(file_comment_match.group("doc"))})

    start_pos = file_comment_match.end() if file_comment_match else 0
    remaining_content = content[start_pos:]

    # Blockkommentar ovanför selektor → Classes
    pattern = r"/\*\s*(?P<doc>.*?)\s*\*/\s*(?P<name>[^{\s]+)\s*{"
    for m in re.finditer(pattern, remaining_content, re.DOTALL | re.MULTILINE):
        classes.append({"name": m.group("name"), "doc": clean_doc(m.group("doc"))})

    return classes, functions
