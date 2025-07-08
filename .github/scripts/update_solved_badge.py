import os

def count_solved():
    repo_root = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    count = 0
    for folder in ['easy', 'medium', 'hard']:
        folder_path = os.path.join(repo_root, folder)
        if os.path.exists(folder_path):
            count += len([f for f in os.listdir(folder_path) if os.path.isdir(os.path.join(folder_path, f))])
    return count

def update_readme(count):
    repo_root = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    readme_path = os.path.join(repo_root, "README.md")

    with open(readme_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    new_lines = []
    for line in lines:
        if line.strip().startswith("![Solved]("):
            new_line = f"![Solved](https://img.shields.io/badge/solved-{count}-brightgreen)\n"
            new_lines.append(new_line)
        else:
            new_lines.append(line)

    with open(readme_path, "w", encoding="utf-8") as f:
        f.writelines(new_lines)

if __name__ == "__main__":
    solved_count = count_solved()
    print(f"Solved count: {solved_count}")
    update_readme(solved_count)
