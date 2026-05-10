from core_engine.utils.utils import extract_doc_before

def analyze_ruby(content):
    """Extraherar Ruby-klasser och funktioner med =begin ... =end docblocks."""
    pattern_func = r"(?:=begin\s*(?P<doc>.*?)\s*=end\s*)?\s*def\s+(?P<name>\w+)"
    pattern_class = r"(?:=begin\s*(?P<doc>.*?)\s*=end\s*)?\s*class\s+(?P<name>\w+)"

    classes = extract_doc_before(pattern_class, content)
    functions = extract_doc_before(pattern_func, content)

    return classes, functions
