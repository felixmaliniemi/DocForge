from core_engine.utils.utils import extract_doc_before

def analyze_go(content):
    """Extraherar Go-funktioner med /** ... */ blockkommentarer som docstrings."""
    pattern_func = r"/\*\*(?P<doc>.*?)\*/\s*func\s+(?P<name>\w+)\s*\("
    functions = extract_doc_before(pattern_func, content)

    return [], functions
