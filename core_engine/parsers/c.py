from core_engine.utils.utils import extract_doc_before

def analyze_c(content):
    """Extraherar C-funktioner med **ENDAST** formella docblocks (/** ... */)"""
    # Mönster för docblock + funktionsdefinition
    pattern_docblock = r"/\*\*(?P<doc>.*?)\*/\s*\w+\s+(?P<name>\w+)\s*\([^)]*\)\s*{"
    functions = extract_doc_before(pattern_docblock, content)

    return [], functions
