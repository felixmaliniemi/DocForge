from .c import analyze_c

def analyze_cpp(content):
    """Extraherar C++-funktioner med **ENDAST** formella docblocks (/** ... */)"""
    return analyze_c(content)
