"""
mapping.py

Maps file extensions to language-specific parsers.
Used by the documentation generator to select the correct parser.
"""

from core_engine.parsers.bash import analyze_bash
from core_engine.parsers.c import analyze_c
from core_engine.parsers.cpp import analyze_cpp
from core_engine.parsers.csharp import analyze_csharp
from core_engine.parsers.css import analyze_css
from core_engine.parsers.go import analyze_go
from core_engine.parsers.html import analyze_html
from core_engine.parsers.java import analyze_java
from core_engine.parsers.javascript import analyze_javascript
from core_engine.parsers.kotlin import analyze_kotlin
from core_engine.parsers.lua import analyze_lua
from core_engine.parsers.matlab import analyze_matlab
from core_engine.parsers.perl import analyze_perl
from core_engine.parsers.php import analyze_php
from core_engine.parsers.powershell import analyze_powershell
from core_engine.parsers.python import analyze_python
from core_engine.parsers.r_lang import analyze_r_lang
from core_engine.parsers.ruby import analyze_ruby
from core_engine.parsers.rust import analyze_rust
from core_engine.parsers.scala import analyze_scala
from core_engine.parsers.sql import analyze_sql
from core_engine.parsers.swift import analyze_swift
from core_engine.parsers.typescript import analyze_typescript

MAPPING = {
    ".sh": analyze_bash,        # # ...
    ".bash": analyze_bash,      # # ...
    ".c": analyze_c,            # /** ... */
    ".cpp": analyze_cpp,        # /** ... */
    ".h": analyze_cpp,          # /** ... */
    ".cs": analyze_csharp,      # /** ... */
    ".css": analyze_css,        # /* ... */
    ".go": analyze_go,          # /** ... */
    ".html": analyze_html,      # <!-- ... -->
    ".htm": analyze_html,       # <!-- ... -->
    ".java": analyze_java,      # /** ... */
    ".js": analyze_javascript,  # /** ... */
    ".kt": analyze_kotlin,      # /** ... */
    ".lua": analyze_lua,        # --[[ ... ]]
    ".m": analyze_matlab,       # % ... above function
    ".pl": analyze_perl,        # #' ...
    ".pm": analyze_perl,        # #' ...
    ".php": analyze_php,        # /** ... */
    ".ps1": analyze_powershell, # <# ... #>
    ".py": analyze_python,      # """ ... """
    ".r": analyze_r_lang,       # #' ...
    ".rb": analyze_ruby,        # =begin ... =end
    ".rs": analyze_rust,        # /// ... or /** ... */
    ".scala": analyze_scala,    # /** ... */
    ".sql": analyze_sql,        # /* ... */
    ".swift": analyze_swift,    # /// ... or /** ... */
    ".ts": analyze_typescript,  # /** ... */
}
