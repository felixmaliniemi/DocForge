import re
from core_engine.utils.utils import clean_doc

def analyze_matlab(content):
    """Extraherar MATLAB-funktioner och docstrings (sekvens av %-kommentarer ovanför function)"""
    functions = []

    # Matcha en eller flera kommentarer (%) direkt ovanför en function-rad
    pattern_func = (
        r"(?P<doc>(?:%\s*.*\n)+)"  # en eller flera kommentarsrader
        r"\s*function\s+.*=\s*(?P<name>\w+)\s*\("  # function-definition
    )

    for m in re.finditer(pattern_func, content, re.MULTILINE):
        doc = clean_doc(m.group("doc"))
        name = m.group("name")
        functions.append({"name": name, "doc": doc})

    # Ta med top-level script-kommentarer som inte följs av function
    pattern_script = r"(?P<doc>(?:%\s*.*\n)+)(?!\s*function)"
    for m in re.finditer(pattern_script, content, re.MULTILINE):
        doc = clean_doc(m.group("doc"))
        functions.append({"name": "Script", "doc": doc})

    return [], functions
