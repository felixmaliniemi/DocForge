import re
from core_engine.utils.utils import clean_doc, extract_doc_before

def analyze_powershell(content):
    """Extraherar PowerShell-funktioner med #-kommentarer som docblock"""
    classes = []
    functions = []

    pattern_func = r"(#\s*(?P<doc>.*?)\n)+\s*function\s+(?P<name>\w+)"
    functions = extract_doc_before(pattern_func, content)

    # Top-level doc → Script
    if not functions:
        top_doc = re.match(r"(#\s*(?P<doc>.*?)\n)+", content)
        if top_doc:
            functions.append({"name": "Script", "doc": clean_doc(top_doc.group("doc"))})

    return classes, functions
