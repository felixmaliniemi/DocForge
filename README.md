<div align="center">

# 📘 DocForge
**The intelligent multi-language documentation generator for modern codebases.**

[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Multi-Language](https://img.shields.io/badge/25%2B_Languages-Supported-00C7B7?style=for-the-badge)](#features)
[![Output](https://img.shields.io/badge/TXT%20%7C%20MD%20%7C%20HTML-Generated-FF6F00?style=for-the-badge)](#features)
[![CLI](https://img.shields.io/badge/CLI-Interactive-8E44AD?style=for-the-badge)](#usage)

---

### "Turn code into knowledge. Instantly."
*A powerful documentation engine that transforms source code into structured, readable documentation across 25+ programming languages.*

</div>

---

## ✨ Core Functionality

### 🧠 Code Intelligence Engine
DocForge automatically scans and analyzes source code structures:
* **Class Extraction:** Detects class definitions across languages
* **Function Parsing:** Extracts functions and methods with docstrings/comments
* **Smart Context Detection (language-aware parsing per file type):** Language-aware parsing logic per file type

---

### 🌍 Multi-Language Support
Supports 25+ programming languages with dedicated parsers:
* Python, JavaScript, TypeScript
* Java, C, C++, C#
* Go, Rust, Swift, Kotlin
* PHP, Ruby, Lua, Perl
* SQL, HTML, CSS, Bash, and more

---

### 📄 Output Generation System
Generate documentation in multiple formats:
* **TXT:** Clean structured text output
* **Markdown:** Developer-friendly documentation
* **HTML:** Interactive file-tree documentation viewer

---

### 🌐 Translation Layer (Optional)
* Translate documentation to:
  * English (`en`)
  * Swedish (`sv`)
* Uses Google Translate integration (optional dependency)

---

### ⚙️ Interactive CLI
Simple terminal-based workflow:
* Select project folder
* Choose output format
* Enable/disable translation
* Generate documentation instantly

---

## 🛠 Tech Stack

| Layer | Technology | Purpose |
| :--- | :--- | :--- |
| **Core Engine** | Python | Parsing & generation logic |
| **CLI** | Python CLI | User interaction layer |
| **Parsing System** | Custom parsers | Language-specific analysis |
| **Translation** | Googletrans | Optional localization |
| **Output Layer** | HTML / Markdown / TXT | Documentation formats |
| **Architecture** | Modular engine design | Scalable codebase structure |

---

## 🚀 Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/docforge.git

cd docforge

pip install googletrans==4.0.0rc1
```

Optional: Translation features require googletrans.
The tool works fully without it.

🚀 Usage
▶ Run the CLI
```bash
python -m core_engine.cli.cli
```
---

🧭 Interactive Flow

You will be promted for:

* 📁 Project path
* 📄 Output format (txt, md, html)
* 🌍 Translation language (en, sv, none)

---

📌 Example
* Project folder or file [./]: ./my-project
* Format (txt/md/html) [txt]: md
* Translation (en/sv/none) [none]: en

Output:
* documentation.md

---

🏗 Project Structure
```bash
DocForge/
├── core_engine/
│ ├── cli/ # CLI interface
│ ├── engine/ # Core generation engine
│ ├── config/ # Mapping system
│ ├── parsers/ # Language-specific parsers
│ ├── utils/ # Utilities + logger
│ └── services/ # Translation service
│
├── test_files/ # Example codebases
├── vscode-extension/ # Future VSCode integration
└── README.md
```
---

⚙️ How It Works
1. 📂 File Discovery

Scans project directories and filters supported file types

2. 🧩 Parsing Layer

Each language uses a dedicated parser module

3. 🧠 Extraction Engine

Extracts:

* Classes
* Methods
* Functions
* Documentation comments

4. 🌐 Translation (Optional)

Converts extracted documentation into target language

5. 📄 Output Generation

Formats results into TXT / Markdown / HTML

6. 💾 Export

Saves documentation file to disk

---

🚫 Exclusions

DocForge automatically ignores:

* core_engine/
* vscode-extension/
* __pycache__/
* .git/
* node_modules/

---

🔮 Roadmap
* VS Code extension integration
* CLI flags (--exclude, --format)
* Config file support
* Faster incremental parsing
* Package distribution (pip install docforge)
* Advanced HTML UI search system

---

🤝 Development Philosophy

DocForge was built as a modular, extensible system designed for:

* scalability across languages
* clean parser separation
* future IDE integration
* automation of documentation workflows

---

📜 License

MIT License

<div align="center">

Built for developers who hate writing documentation — but love clean code.

</div>