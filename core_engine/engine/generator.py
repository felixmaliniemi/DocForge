"""
Generates documentation from source code using language-specific parsers.
"""

import webbrowser
from datetime import datetime
from pathlib import Path
from core_engine.config.mapping import MAPPING
from core_engine.utils.utils import read_file
from core_engine.services.translator import translate
from core_engine.parsers.fallback import analyze_fallback
from core_engine.utils.logger_config import setup_logger

logger = setup_logger()

def analyze_file(filepath: Path):
    """Analyze a file and return classes and functions with docstrings."""
    ext = filepath.suffix.lower()
    analyzer = MAPPING.get(ext, analyze_fallback)
    content = read_file(filepath)
    try:
        return analyzer(content)
    except Exception: # pylint: disable=broad-exception-caught
        return [], []


def generate_documentation(
    project_path,
    output_file=None,
    output_format="html",
    language="en",
    excluded_dirs=None,
    excluded_files=None
):
    """Generates documentation in TXT, Markdown, or HTML."""

    project_path = Path(project_path).resolve()
    excluded_dirs = excluded_dirs or []
    excluded_files = set(excluded_files or [])
    supported_exts = tuple(MAPPING.keys())

    file_count = 0
    function_count = 0

    # Determine default output file
    if output_file is None:
        if output_format == "md":
            output_file = "documentation.md"
        elif output_format == "html":
            output_file = "documentation.html"
        else:
            output_file = "documentation.txt"

    # List files
    files_to_process = [project_path] if project_path.is_file() else list(project_path.rglob("*"))

    # TXT or Markdown output
    if output_format in ("txt", "md"):
        with open(output_file, "w", encoding="utf-8") as out:
            if output_format == "md":
                out.write(f"# Project: {project_path}\n\n")
            else:
                out.write(f"Project: {project_path}\n\n")

            for path in files_to_process:
                if path.is_dir() or path.name in excluded_files or any(part in excluded_dirs for part in path.parts):
                    continue
                if path.suffix.lower() not in supported_exts:
                    continue

                relpath = path.relative_to(project_path).as_posix()
                file_count += 1
                out.write(f"## File: {relpath}\n\n" if output_format == "md" else f"File: {relpath}\n\n")

                classes, functions = analyze_file(path)

                for cls in classes:
                    doc = cls.get("doc") or "(no documentation)"
                    doc_trans = translate(doc, language) if language.lower() != "none" else doc
                    if output_format == "md":
                        out.write(f"### Class: {cls['name']}\n```\n{doc_trans}\n```\n\n")
                    else:
                        out.write(f"Class: {cls['name']}\n")
                        for line in doc_trans.splitlines():
                            out.write(f"    {line}\n")
                        out.write("\n")
                    for m in cls.get("methods", []):
                        m_doc = m.get("doc") or "(no documentation)"
                        m_trans = translate(m_doc, language) if language.lower() != "none" else m_doc
                        if output_format == "md":
                            out.write(f"#### Method: {m['name']}\n```\n{m_trans}\n```\n\n")
                        else:
                            out.write(f"  Method: {m['name']}\n")
                            for line in m_trans.splitlines():
                                out.write(f"      {line}\n")
                            out.write("\n")

                for f in functions:
                    doc = f.get("doc") or "(no documentation)"
                    doc_trans = translate(doc, language) if language.lower() != "none" else doc
                    if output_format == "md":
                        out.write(f"### Function: {f['name']}\n```\n{doc_trans}\n```\n\n")
                    else:
                        out.write(f"Function: {f['name']}\n")
                        for line in doc_trans.splitlines():
                            out.write(f"    {line}\n")
                        out.write("\n")

            # Footer
            if output_format == "md":
                out.write(f"\n**Total files:** {file_count}\n")
            else:
                out.write(f"\nTotal files: {file_count}\n")

    # HTML output
    elif output_format == "html":
        # Build tree structure
        tree = {}
        for path in files_to_process:
            if path.is_dir() or path.name in excluded_files or any(part in excluded_dirs for part in path.parts):
                continue
            if path.suffix.lower() in supported_exts:
                relpath = path.relative_to(project_path).as_posix()
                parts = relpath.split("/")
                node = tree
                for part in parts[:-1]:
                    node = node.setdefault(part, {"_files": {}, "_sub": {}})["_sub"]
                node.setdefault("_files", {})[parts[-1]] = path

        def build_menu_html(node, parent_id=""):
            html = "<ul>\n"
            for folder, content in node.items():
                if folder in ("_files", "_sub"):
                    continue
                folder_id = f"{parent_id}{folder}_"
                html += f"<li><span class='collapsible'>{folder}</span>\n"
                html += "<ul class='content'>\n"
                html += build_menu_html(content["_sub"], parent_id=folder_id)
                for fname, _ in node.get("_files", {}).items():
                    file_id = parent_id + fname.replace(".", "_")
                    html += f"<li><span class='file-link' data-file-id='{file_id}'>{fname}</span></li>\n"
                html += "</ul></li>\n"
            for fname, _ in node.get("_files", {}).items():
                file_id = parent_id + fname.replace(".", "_")
                html += f"<li><span class='file-link' data-file-id='{file_id}'>{fname}</span></li>\n"
            html += "</ul>\n"
            return html

        def embed_file_content(node, parent_id=""):
            nonlocal file_count, function_count
            html = ""
            for folder, content in node.items():
                if folder in ("_files", "_sub"):
                    continue
                folder_id = f"{parent_id}{folder}_"
                html += embed_file_content(content["_sub"], parent_id=folder_id)
                for fname, fpath in content["_files"].items():
                    file_id = folder_id + fname.replace(".", "_")
                    classes, functions = analyze_file(fpath)
                    file_count += 1
                    function_count += len(functions) + sum(len(c.get("methods", [])) for c in classes)
                    html += f"<div id='{file_id}' data-file-content style='display:none'>\n<h2>{fname}</h2>\n"
                    for cls in classes:
                        doc = cls.get("doc") or "(no documentation)"
                        doc_trans = translate(doc, language) if language.lower() != "none" else doc
                        html += f"<h3>Class: {cls['name']}</h3><pre>{doc_trans}</pre>\n"
                        for m in cls.get("methods", []):
                            m_doc = m.get("doc") or "(no documentation)"
                            m_doc_trans = translate(m_doc, language) if language.lower() != "none" else m_doc
                            html += f"<h4>Method: {m['name']}</h4><pre>{m_doc_trans}</pre>\n"
                    for f in functions:
                        doc = f.get("doc") or "(no documentation)"
                        doc_trans = translate(doc, language) if language.lower() != "none" else doc
                        html += f"<h3>Function: {f['name']}</h3><pre>{doc_trans}</pre>\n"
                    html += "</div>\n"
            for fname, fpath in node.get("_files", {}).items():
                file_id = parent_id + fname.replace(".", "_")
                classes, functions = analyze_file(fpath)
                file_count += 1
                function_count += len(functions) + sum(len(c.get("methods", [])) for c in classes)
                html += f"<div id='{file_id}' data-file-content style='display:none'>\n<h2>{fname}</h2>\n"
                for cls in classes:
                    doc = cls.get("doc") or "(no documentation)"
                    doc_trans = translate(doc, language) if language.lower() != "none" else doc
                    html += f"<h3>Class: {cls['name']}</h3><pre>{doc_trans}</pre>\n"
                    for m in cls.get("methods", []):
                        m_doc = m.get("doc") or "(no documentation)"
                        m_doc_trans = translate(m_doc, language) if language.lower() != "none" else m_doc
                        html += f"<h4>Method: {m['name']}</h4><pre>{m_doc_trans}</pre>\n"
                for f in functions:
                    doc = f.get("doc") or "(no documentation)"
                    doc_trans = translate(doc, language) if language.lower() != "none" else doc
                    html += f"<h3>Function: {f['name']}</h3><pre>{doc_trans}</pre>\n"
                html += "</div>\n"
            return html

        with open(output_file, "w", encoding="utf-8") as out:
            out.write("<!DOCTYPE html>\n<html lang='en'><head><meta charset='UTF-8'>\n<title>Documentation</title>\n")
            out.write("""
<style>
body { display:flex; font-family:sans-serif; margin:0; }
#menu { width:250px; background:#f5f5f5; padding:10px; overflow:auto; height:100vh; }
#content { flex:1; padding:20px; overflow:auto; }
.collapsible { cursor:pointer; user-select:none; display:block; padding:5px; }
.content { display:none; padding-left:15px; }
.file-link { cursor:pointer; color:blue; text-decoration:underline; display:block; padding:2px 0; }
pre { background:#eee; padding:10px; overflow-x:auto; }
</style>
</head><body>
<div id="menu">
<h2>Documentation</h2>
""")
            out.write(build_menu_html(tree))
            out.write("</div>\n<div id='content'><h2>Contents</h2><p>Click a file in the menu to display its documentation.</p>\n")
            out.write(embed_file_content(tree))
            out.write(f"<hr><p><strong>Total files:</strong> {file_count}<br>")
            out.write(f"<strong>Total functions/methods:</strong> {function_count}<br>")
            out.write(f"<em>Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</em></p>\n")
            out.write("</div>\n")

            out.write("""
<script>
var coll = document.getElementsByClassName("collapsible");
for (let i=0;i<coll.length;i++){
    coll[i].addEventListener("click", function(){
        var next = this.nextElementSibling;
        if(next && next.classList.contains("content")){
            next.style.display = next.style.display==="block"?"none":"block";
        }
    });
}

var fileLinks = document.getElementsByClassName("file-link");
for (let i=0;i<fileLinks.length;i++){
    fileLinks[i].addEventListener("click", function(){
        var fileId = this.getAttribute("data-file-id");
        var nodes = document.querySelectorAll("[data-file-content]");
        nodes.forEach(n => n.style.display = "none");
        var target = document.getElementById(fileId);
        if(target) target.style.display = "block";
        target.scrollIntoView({behavior:"smooth"});
    });
}
</script>
</body></html>
""")
        webbrowser.open(output_file)

    logger.info("✅ Documentation saved in %s", output_file)
