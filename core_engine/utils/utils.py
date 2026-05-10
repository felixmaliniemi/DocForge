"""Utility functions for DocGen."""

import re
from .logger_config import setup_logger

logger = setup_logger()

BLOCK_DOC_CONTENT = r'(?:[^*]|\*(?!/))*'
INDENT_L2_CONT = '              '  # 14 spaces for Class/Function
INDENT_L4_CONT = '                  '  # 18 spaces for Method

def read_file(filepath: str) -> str:
    """Reads the entire contents of a file."""
    try:
        with open(filepath, "r", encoding="utf-8", errors="replace") as f:
            return f.read()
    except FileNotFoundError:
        logger.error("Could not read file %s: File not found", filepath)
    except OSError as e:
        logger.error("Could not read file %s: %s", filepath, e)
    return ""

def clean_doc(doc: str) -> str | None:
    """Cleans a docblock from syntax and unnecessary characters."""
    if not doc:
        return None
    doc = doc.strip()
    doc = re.sub(r"^/\*\*\s*|^/\*\s*|\s*\*/$", "", doc)
    lines = doc.splitlines()
    cleaned = []
    for line in lines:
        line = line.strip()
        line = re.sub(r"^(\*|#|%|///|//|--)\s*", "", line)
        if line:
            cleaned.append(line)
    return "\n".join(cleaned).strip()

def extract_doc_before(pattern: str, content: str, flags=0):
    """Extracts docblock located before a class or function using regex."""
    matches = []
    for m in re.finditer(pattern, content, flags | re.DOTALL):
        doc = m.group("doc") if "doc" in m.groupdict() else None
        name = m.group("name") if "name" in m.groupdict() else "(no function/class)"
        matches.append({"name": name, "doc": clean_doc(doc)})
    return matches

def format_doc_for_output(doc: str, continuation_indent: str) -> str:
    """Preserves line breaks and indentation for the output file."""
    if not doc or doc == "(no documentation found)":
        return doc
    return doc.replace('\n', '\n' + continuation_indent)
