"""
cli.py
-----------------------
Interactive CLI for DocGen - Documentation Generator
-----------------------
"""
import os
from core_engine.engine.generator import generate_documentation
from core_engine.utils.logger_config import setup_logger

def cli_main():
    """Run the documentation generator interactively."""

    # Set up logger
    setup_logger(level="INFO")

    # Ask the user for project folder or file
    default_path = os.getcwd()
    path = input(f"Project folder or file [{default_path}]: ").strip() or default_path

    # Ask for output format
    output_format = input("Format (txt/md/html) [txt]: ").strip().lower()
    if output_format not in ("txt", "md", "html"):
        print("Invalid format, default 'txt' will be used.")
        output_format = "txt"

    # Ask for translation language
    language = input("Translation (en/sv/none) [none]: ").strip().lower()
    if language not in ("en", "sv", "none"):
        print("Invalid language, default 'none' will be used.")
        language = "none"

    # Internal files and directories to always exclude
    internal_files = { "cli.py" }
    internal_dirs = [
    "core_engine",
    "vscode-extension",
    "__pycache__",
    ".git",
    "node_modules"
    ]

    # Determine output file name
    if output_format == "md":
        output_file = "documentation.md"
    elif output_format == "html":
        output_file = "documentation.html"
    else:
        output_file = "documentation.txt"

    excluded_files = set(internal_files)
    excluded_files.add(output_file)

    # Run the documentation generator
    generate_documentation(
        project_path=path,
        output_file=output_file,
        output_format=output_format,
        language=language,
        excluded_dirs=internal_dirs,
        excluded_files=excluded_files
    )

if __name__ == "__main__":
    cli_main()
