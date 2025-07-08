#!/usr/bin/env python3
import os
import sys

from pathlib import Path

def count_solved_problems(repo_root: Path) -> int:
    count = 0
    for difficulty in ['easy', 'medium', 'hard']:
        diff_path = repo_root / difficulty
        if diff_path.exists() and diff_path.is_dir():
            count += sum(1 for item in diff_path.iterdir() if item.is_dir())
    return count

def update_readme_badge(repo_root: Path, solved_count: int):
    readme_path = repo_root / "README.md"

    if not readme_path.exists():
        print(f"[ERROR] README.md not found at {readme_path}")
        sys.exit(1)

    with readme_path.open("r", encoding="utf-8") as f:
        lines = f.readlines()

    new_lines = []
    replaced = False

    for line in lines:
        if line.strip().startswith("![Solved]("):
            new_line = f"![Solved](https://img.shields.io/badge/solved-{solved_count}-brightgreen)\n"
            new_lines.append(new_line)
            replaced = True
            print(f"[INFO] Updated badge line to: {new_line.strip()}")
        else:
            new_lines.append(line)

    if not replaced:
        print("[WARN] No existing solved badge line found, adding badge to the top of README.")
        new_lines.insert(1, f"![Solved](https://img.shields.io/badge/solved-{solved_count}-brightgreen)\n")

    with readme_path.open("w", encoding="utf-8") as f:
        f.writelines(new_lines)

    print(f"[INFO] README.md updated successfully with solved count: {solved_count}")

if __name__ == "__main__":
    # Calculate the repository root robustly
    repo_root = Path(__file__).resolve().parents[2]
    print(f"[INFO] Using repository root: {repo_root}")

    solved_count = count_solved_problems(repo_root)
    print(f"[INFO] Total solved problems counted: {solved_count}")

    update_readme_badge(repo_root, solved_count)
