from core_engine.utils.utils import extract_doc_before

def analyze_perl(content):
    """Extraherar Perl-funktioner där en sekvens av #-kommentarer behandlas som docblock."""
    # Måste använda #
    pattern_func = r"(#\s*(?P<doc>.*?)\n)+\s*sub\s+(?P<name>\w+)"
    functions = extract_doc_before(pattern_func, content)

    return [], functions
