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

def update_readme_badge(repo_root: Path, solved_count: int) -> bool:
    readme_path = repo_root / "README.md"

    if not readme_path.exists():
        print(f"[ERROR] README.md not found at {readme_path}")
        sys.exit(1)

    with readme_path.open("r", encoding="utf-8") as f:
        original_lines = f.readlines()

    new_lines = []
    replaced = False

    for line in original_lines:
        if line.strip().startswith("![Solved]("):
            new_line = (
                f"![Solved](https://img.shields.io/badge/solved-{solved_count}-brightgreen)\n"
            )
            if line != new_line:
                new_lines.append(new_line)
                replaced = True
                print(f"[INFO] Updated badge line to: {new_line.strip()}")
            else:
                print("[INFO] Badge already up-to-date.")
                return False  # No changes needed
        else:
            new_lines.append(line)

    if not replaced:
        print("[WARN] No solved badge found — inserting new badge.")
        new_lines.insert(
            1,
            f"![Solved](https://img.shields.io/badge/solved-{solved_count}-brightgreen)\n"
        )
        replaced = True

    with readme_path.open("w", encoding="utf-8") as f:
        f.writelines(new_lines)

    print(f"[INFO] README.md updated successfully with solved count: {solved_count}")

    return replaced

if __name__ == "__main__":
    # Calculate the repository root robustly
    repo_root = Path(__file__).resolve().parents[2]
    print(f"[INFO] Using repository root: {repo_root}")

    solved_count = count_solved_problems(repo_root)
    print(f"[INFO] Total solved problems counted: {solved_count}")

    changed = update_readme_badge(repo_root, solved_count)

    marker_path = repo_root / ".badge_updated"
    if marker_path.exists():
        marker_path.unlink()

    if not changed:
        print("[INFO] No changes made to solved badge")
        sys.exit(0)  # Exit success, but no commit needed
    else:
        print("[INFO] Created .badge_updated to indicate solved badge was updated successfully.")
        marker_path.write_text("1")
        sys.exit(0)  # Exit success and create mark file
