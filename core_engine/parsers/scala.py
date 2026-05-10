import re
from core_engine.utils.utils import clean_doc, BLOCK_DOC_CONTENT, extract_doc_before
from core_engine.utils.logger_config import setup_logger

logger = setup_logger()

def analyze_scala(content):
    """Extraherar Scala-klasser, objekt och metoder/funktioner med regional analys."""
    classes = []

    # 1. Hitta klasser/objekt (Class/Object header analysis)
    pattern_class_header = re.compile(
        r"(/\*\*(?P<doc>"+BLOCK_DOC_CONTENT+r")\*/\s*)?"
        r"(?:(?:abstract|case|sealed|lazy)?\s*)*"
        r"(?P<type>object|class)\s+(?P<name>\w+)(?:\s*\(.*?\))?\s*\{",
        re.DOTALL
    )

    content_processed_end = 0
    for m in pattern_class_header.finditer(content):
        cls_name = m.group("name")
        cls_type = m.group("type").capitalize()
        cls_doc = clean_doc(m.group("doc")) if m.group("doc") else None
        header_end = m.end()

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
            logger.warning("Kunde inte hitta avslutande klammer för %s %s", cls_type, cls_name)
            continue

        body = content[header_end:end_idx]
        cls = {"name": cls_name, "doc": cls_doc, "methods": [], "type": cls_type}

        pattern_method = re.compile(
            r"(/\*\*(?P<doc>"+BLOCK_DOC_CONTENT+r")\*/\s*)"
            r"(?:\s*(?:def|val|var|lazy|override|private|protected)?\s*)*"
            r"def\s+(?P<name>\w+)\s*\(",
            re.DOTALL
        )

        for mm in pattern_method.finditer(body):
            mname = mm.group("name")
            mdoc = clean_doc(mm.group("doc")) if mm.group("doc") else None
            cls["methods"].append({"name": mname, "doc": mdoc})

        classes.append(cls)
        content_processed_end = max(content_processed_end, end_idx + 1)

    remaining_content = content[content_processed_end:] if content_processed_end < len(content) else ""
    pattern_standalone_func = r"/\*\*(?P<doc>"+BLOCK_DOC_CONTENT+r")\*/\s*def\s+(?P<name>\w+)\s*\("
    functions = extract_doc_before(pattern_standalone_func, remaining_content)

    if not classes and not functions:
        file_comment_match = re.match(r"^\s*/\*\s*(?P<doc>.*?)\s*\*/", content, re.DOTALL)
        if file_comment_match:
            doc = clean_doc(file_comment_match.group("doc"))
            if doc:
                functions.append({"name": "Script", "doc": doc})

    return classes, functions
