import re
from core_engine.utils.utils import clean_doc, BLOCK_DOC_CONTENT
from core_engine.utils.logger_config import setup_logger

logger = setup_logger()

def analyze_java(content):
    """Extraherar Java-klasser och metoder med regional analys baserat på klammerpar."""
    classes = []
    # Regex för klasshuvud: Valfri docblock, modifierare, class keyword, klassnamn, öppningsklammer
    pattern_class_header = re.compile(
        r"(/\*\*(?P<doc>"+BLOCK_DOC_CONTENT+r")\*/\s*)?"  # Optional Strict Docblock
        r"(?:public|private|protected)?\s*class\s+(?P<name>\w+)\s*\{",  # Class definition
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

        # Hitta metoder *endast* inuti klasskroppen
        pattern_method = re.compile(
            r"(/\*\*(?P<doc>"+BLOCK_DOC_CONTENT+r")\*/\s*)"
            r"(?:public|private|protected|static|private|protected|\s)+"
            r"[\w<>\[\]]+\s+"  # Returtyp
            r"(?P<name>\w+)\s*\(",
            re.DOTALL
        )

        for mm in pattern_method.finditer(body):
            mname = mm.group("name")
            mdoc = clean_doc(mm.group("doc")) if mm.group("doc") else None
            cls["methods"].append({"name": mname, "doc": mdoc})

        classes.append(cls)

    return classes, []
