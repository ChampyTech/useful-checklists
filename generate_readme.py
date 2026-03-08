import os

BASE_DIR = "."
OUTPUT_FILE = "README.md"

EXCLUDE_FILES = {"CONTRIBUTING.md", "LICENSE.md", "README.md"}
EXCLUDE_DIRS = {".git", ".github", "__pycache__"}

HEADER = """# 🔨 A Curated List of Useful Checklists

<p>
  <img alt="Contributions welcome" src="https://img.shields.io/badge/Contributions-welcome-green">
  <img alt="License MIT" src="https://img.shields.io/badge/License-MIT-orange">
</p>

A curated list of useful checklists for everyday life, productivity, travel, health, and more.

📬 **Want to contribute?** Check the [CONTRIBUTING.md](CONTRIBUTING.md) file and open a pull request or an issue. Even small contributions are welcome!

## 🔨 Checklists

> [!TIP]
> Use **Ctrl+F** (Windows/Linux/Chromebook) or **⌘+F** (Mac) to search through the collection and find exactly what you need.

"""

FOOTER = """## 🙏 Contributing

Check the [CONTRIBUTING.md](CONTRIBUTING.md) file and open a pull request or an issue. Even small contributions are welcome!

## ⚠️ Disclaimer

By utilizing this repository, you acknowledge that this project is not associated with, sponsored by, or endorsed by any organizations, professionals, or experts in the fields covered by the checklists mentioned.
Always adapt checklists to your specific context and verify current regulations and standards.

## 🎫 License

This project is licensed under the [MIT License](LICENSE.md).
"""


def format_name(filename):
    name = os.path.splitext(filename)[0]
    name = name.replace("_", " ")
    return name


sections = {}

for root, dirs, files in os.walk(BASE_DIR):

    dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]

    rel_dir = os.path.relpath(root, BASE_DIR)

    if rel_dir == ".":
        continue

    md_files = [
        f for f in files
        if f.endswith(".md") and f not in EXCLUDE_FILES
    ]

    if not md_files:
        continue

    section = os.path.basename(rel_dir)

    sections.setdefault(section, [])

    for file in sorted(md_files):
        path = os.path.join(rel_dir, file).replace("\\", "/")
        title = format_name(file)
        sections[section].append((title, path))


with open(OUTPUT_FILE, "w", encoding="utf-8") as f:

    f.write(HEADER)

    for section in sorted(sections):
        f.write(f"### {section}\n\n")

        for title, path in sections[section]:
            f.write(f"- [{title}]({path})\n")

        f.write("\n")

    f.write(FOOTER)

print("README.md generated successfully.")