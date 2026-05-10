import ast

def analyze_python(content):
    """Analyserar Pythonkod och extraherar klasser, funktioner och formella docstrings (''')"""
    classes = []
    functions = []

    tree = ast.parse(content)

    for node in ast.walk(tree):
        if isinstance(node, ast.ClassDef):
            classes.append({
                "name": node.name,
                "doc": ast.get_docstring(node),
                "methods": [
                    {"name": m.name, "doc": ast.get_docstring(m)}
                    for m in node.body if isinstance(m, ast.FunctionDef)
                ]
            })
        elif isinstance(node, ast.FunctionDef):
            functions.append({"name": node.name, "doc": ast.get_docstring(node)})

    return classes, functions
