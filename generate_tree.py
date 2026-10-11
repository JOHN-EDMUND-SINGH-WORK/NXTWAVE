
from pathlib import Path

ROOT = Path(__file__).resolve().parent
README = ROOT / "README.md"

START_MARKER = "<!-- TREE_START -->"
END_MARKER = "<!-- TREE_END -->"

# Folders and files we don't want to display
IGNORED = {
    ".git",
    ".github",
    "__pycache__",
    ".venv",
    "venv",
    ".idea",
    ".vscode",
}

def build_tree(folder: Path, prefix: str = "") -> list[str]:
    items = sorted(
        [item for item in folder.iterdir() if item.name not in IGNORED],
        key=lambda item: (item.is_file(), item.name.lower()),
    )

    lines = []

    for index, item in enumerate(items):
        is_last = index == len(items) - 1
        branch = "└── " if is_last else "├── "
        lines.append(f"{prefix}{branch}{item.name}")

        if item.is_dir():
            extension = "    " if is_last else "│   "
            lines.extend(build_tree(item, prefix + extension))

    return lines

def main():
    content = README.read_text(encoding="utf-8")

    if START_MARKER not in content or END_MARKER not in content:
        raise ValueError(
            "README.md must contain TREE_START and TREE_END markers."
        )

    if content.index(START_MARKER) >= content.index(END_MARKER):
        raise ValueError("The tree markers are in the wrong order.")

    tree_lines = ["```text", ROOT.name, *build_tree(ROOT), "```"]
    tree = "\n".join(tree_lines)

    before, remaining = content.split(START_MARKER, 1)
    _, after = remaining.split(END_MARKER, 1)

    updated = (
        before
        + START_MARKER
        + "\n"
        + tree
        + "\n"
        + END_MARKER
        + after
    )

    if updated != content:
        README.write_text(updated, encoding="utf-8")
        print("README.md folder tree updated successfully!")
    else:
        print("README.md folder tree is already up to date.")

if __name__ == "__main__":
    main()
