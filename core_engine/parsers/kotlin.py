import re
from core_engine.utils.utils import clean_doc
from core_engine.utils.logger_config import setup_logger

logger = setup_logger()

def analyze_kotlin(content):
    """Extraherar Kotlin-klasser och funktioner med formella docblocks (/** ... */)."""
    classes = []
    functions = []

     # Hitta klasser och deras positioner (header + kropp)
    class_header_re = re.compile(
        r"(?:/\*\*(?P<doc>.*?)\*/\s*)?class\s+(?P<name>\w+)\s*{", re.DOTALL)
    class_regions = []

    for m in class_header_re.finditer(content):
        cls_name = m.group("name")
        cls_doc = clean_doc(m.group("doc")) if m.group("doc") else None
        header_end = m.end()

        # Enkel klammerräkning för att hitta slutet
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
            logger.warning("Kunde inte hitta slutklammer för klass %s", cls_name)
            continue

        body = content[header_end:end_idx]
        cls = {"name": cls_name, "doc": cls_doc, "methods": []}

        # Hitta metoder inuti klasskroppen
        method_re = re.compile(r"(?:/\*\*(?P<doc>.*?)\*/\s*)?fun\s+(?P<name>\w+)\s*\(", re.DOTALL)
        for mm in method_re.finditer(body):
            mname = mm.group("name")
            mdoc = clean_doc(mm.group("doc")) if mm.group("doc") else None
            cls["methods"].append({"name": mname, "doc": mdoc})

        classes.append(cls)
        class_regions.append((m.start(), end_idx + 1))

    # Top-level funktioner utanför klasser
    remaining = []
    last = 0
    for start, end in sorted(class_regions):
        if last < start:
            remaining.append(content[last:start])
        last = end
    if last < len(content):
        remaining.append(content[last:])

    remaining_text = "\n".join(remaining)

    top_func_re = re.compile(r"(?:/\*\*(?P<doc>.*?)\*/\s*)?fun\s+(?P<name>\w+)\s*\(", re.DOTALL)
    for m in top_func_re.finditer(remaining_text):
        fname = m.group("name")
        fdoc = clean_doc(m.group("doc")) if m.group("doc") else "(ingen dokumentation hittades)"
        functions.append({"name": fname, "doc": fdoc})

    return classes, functions
