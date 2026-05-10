import re
from core_engine.utils.utils import clean_doc, BLOCK_DOC_CONTENT, extract_doc_before
from core_engine.utils.logger_config import setup_logger

logger = setup_logger()

def analyze_typescript(content):
    """Extraherar klasser, metoder och stand-alone funktioner 
       med JSDoc (/** ... */) genom regional analys."""
    classes = []

    # 1. Hitta klasser (Class header analysis)
    pattern_class_header = re.compile(
        r"(/\*\*(?P<doc>"+BLOCK_DOC_CONTENT+r")\*/\s*)?" # Optional Strict Docblock
        r"class\s+(?P<name>\w+)\s*\{", # Class definition and opening brace
        re.DOTALL
    )

    for m in pattern_class_header.finditer(content):
        cls_name = m.group("name")
        cls_doc = clean_doc(m.group("doc")) if m.group("doc") else None
        header_end = m.end()

        # Enkel klammerräkning för att hitta slutet på klasskroppen
        depth = 1
        i = header_end
        end_idx = None
        while i < len(content):
            ch = content[i]
            if ch == "{":
                depth += 1
            elif ch == "}":
                depth -= 1
                if depth == 0:
                    end_idx = i
                    break
            i += 1

        if end_idx is None:
            logger.warning("Kunde inte hitta avslutande klammer för klass %s", cls_name)
            continue

        body = content[header_end:end_idx]
        cls = {"name": cls_name, "doc": cls_doc, "methods": []}

        # 2. Hitta metoder inuti klasskroppen
        pattern_method = re.compile(
            r"(/\*\*(?P<doc>"+BLOCK_DOC_CONTENT+r")\*/\s*)"
            r"(?:\s*(?:public|private|protected|static|readonly)?\s*)*"
            r"(?P<name>\w+)\s*\(",
            re.DOTALL
        )

        for mm in pattern_method.finditer(body):
            mname = mm.group("name")
            mdoc = clean_doc(mm.group("doc")) if mm.group("doc") else None
            cls["methods"].append({"name": mname, "doc": mdoc})

        classes.append(cls)

    # 3. Stand-alone funktioner
    pattern_func = r"/\*\*(?P<doc>"+BLOCK_DOC_CONTENT+r")\*/\s*function\s+(?P<name>\w+)\s*\("
    functions = extract_doc_before(pattern_func, content)

    return classes, functions
