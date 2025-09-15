#!/usr/bin/env python3
import os
import re
import sys
from pathlib import Path

def count_solved_problems(repo_root: Path) -> int:
    count = 0
    for difficulty in ['easy', 'medium', 'hard']:
        diff_path = repo_root / difficulty
        if diff_path.exists() and diff_path.is_dir():
            count += sum(1 for item in diff_path.iterdir() if item.is_dir())
    return count

def count_by_difficulty(repo_root: Path) -> dict:
    counts = {}
    targets = {"easy": 50, "medium": 50, "hard": 50}

    for level in targets:
        level_path = repo_root / level
        count = sum(1 for item in level_path.iterdir() if item.is_dir()) if level_path.exists() else 0
        counts[level] = (count, targets[level])
    return counts

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
            new_line = f"![Solved](https://img.shields.io/badge/solved-{solved_count}-brightgreen)\n"
            if line != new_line:
                new_lines.append(new_line)
                replaced = True
                print(f"[INFO] Updated badge line to: {new_line.strip()}")
            else:
                print("[INFO] Badge already up-to-date.")
                return False
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

    print(f"[INFO] README.md updated with solved count: {solved_count}")
    return replaced

def update_progress_section(repo_root: Path, counts: dict) -> bool:
    readme_path = repo_root / "README.md"
    with readme_path.open("r", encoding="utf-8") as f:
        content = f.read()

    new_progress = "\n".join([
        f"- Easy: {counts['easy'][0]} / {counts['easy'][1]} {'✅' if counts['easy'][0] else '🚧'}",
        f"- Medium: {counts['medium'][0]} / {counts['medium'][1]} {'✅' if counts['medium'][0] else '🚧'}",
        f"- Hard: {counts['hard'][0]} / {counts['hard'][1]} {'✅' if counts['hard'][0] else '🚧'}",
    ])

    updated, n = re.subn(
        r"- Easy: \d+ / \d+ .*\n- Medium: \d+ / \d+ .*\n- Hard: \d+ / \d+ .*",
        new_progress,
        content,
        flags=re.MULTILINE
    )

    if n == 0:
        print("[WARN] Progress section not found — no update made.")
        return False

    with readme_path.open("w", encoding="utf-8") as f:
        f.write(updated)

    print("[INFO] Progress section updated.")
    return True

def format_title(folder_name: str) -> str:
    parts = folder_name.split('_')[1:]
    return ' '.join(word.capitalize() for word in parts)

def get_solution_filename(folder_path: Path) -> str:
    folder_name = folder_path.name

    candidates = []
    for file in folder_path.iterdir():
        if file.suffix == ".py" and not file.stem.startswith("test"):
            if file.stem in folder_name:
                return file.name
            candidates.append(file.name)

    if candidates:
        return candidates[0]

    for file in folder_path.iterdir():
        if file.suffix == ".py":
            return file.name
    return ""

def extract_complexity(file_path: Path) -> tuple[str, str]:
    try:
        with file_path.open("r", encoding="utf-8") as f:
            content = f.read()
        time_match = re.search(r"Time Complexity:\s*([OΘ][^)]+?\))", content)
        space_match = re.search(r"Space Complexity:\s*([OΘ][^)]+?\))", content)
        time = time_match.group(1) if time_match else "O(?)"
        space = space_match.group(1) if space_match else "O(?)"
        return time, space
    except Exception as e:
        print(f"[WARN] Failed to extract complexity from {file_path}: {e}")
        return "O(?)", "O(?)"

def generate_table(repo_root: Path) -> str:
    rows = []
    header = "| No. | ID   | Title             | Difficulty | Solution | Time | Space |\n"
    divider = "|-----|------|-------------------|------------|----------|------|-------|\n"

    row_index = 1
    for difficulty in ['easy', 'medium', 'hard']:
        level_path = repo_root / difficulty
        if not level_path.exists():
            continue
        for problem_folder in sorted(level_path.iterdir()):
            if problem_folder.is_dir():
                id_ = problem_folder.name.split('_')[0]
                title = format_title(problem_folder.name)
                solution_file = get_solution_filename(problem_folder)
                solution_link = f"[Python](./{difficulty}/{problem_folder.name}/{solution_file})" if solution_file else "N/A"
                time, space = extract_complexity(problem_folder / solution_file) if solution_file else ("O(?)", "O(?)")
                rows.append(
                    f"| {row_index:<3} | {id_:<4} | {title:<17} | {difficulty.capitalize():<10} | {solution_link:<60} | {time} | {space} |"
                )
                row_index += 1

    return header + divider + '\n'.join(rows)

def update_table_solution(repo_root: Path) -> bool:
    readme_path = repo_root / "README.md"
    if not readme_path.exists():
        print(f"[ERROR] README.md not found at {readme_path}")
        return False
    
    with readme_path.open("r", encoding="utf-8") as f:
        content = f.read()

    table_content = generate_table(repo_root)

    pattern = re.compile(
        r"(<!-- SOLUTION_TABLE_START -->)(.*?)(<!-- SOLUTION_TABLE_END -->)",
        re.DOTALL
    )

    if not pattern.search(content):
        print("[WARN] Table markers not found in README.md — no update made.")
        return False

    updated_content = pattern.sub(rf"\1\n{table_content}\n\3", content)

    with readme_path.open("w", encoding="utf-8") as f:
        f.write(updated_content)

    print("[INFO] Table solution updated successfully.")
    return True

if __name__ == "__main__":
    repo_root = Path(__file__).resolve().parents[2]
    print(f"[INFO] Using repository root: {repo_root}")

    solved_count = count_solved_problems(repo_root)
    changed = update_readme_badge(repo_root, solved_count)

    counts = count_by_difficulty(repo_root)
    update_progress_section(repo_root, counts)

    update_table_solution(repo_root)

    marker_path = repo_root / ".solved_progress_marker"
    if marker_path.exists():
        marker_path.unlink()

    if not changed:
        print("[INFO] No changes made to solved badge")
        sys.exit(0)  # Exit success, but no commit needed
    else:
        print("[INFO] Created .solved_progress_marker to indicate solved badge was updated successfully.")
        marker_path.write_text("1")
        sys.exit(0)  # Exit success and create mark file

    print("[INFO] All README updates completed.")
