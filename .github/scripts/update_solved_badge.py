import os

def count_solved():
    count = 0
    for folder in ['easy', 'medium', 'hard']:
        if os.path.exists(folder):
            count += len([f for f in os.listdir(folder) if os.path.isdir(os.path.join(folder, f))])
    return count

def update_readme(count):
    with open("README.md", "r", encoding="utf-8") as f:
        lines = f.readlines()

    new_lines = []
    for line in lines:
        if line.strip().startswith("![Solved]("):
            new_line = f"![Solved](https://img.shields.io/badge/solved-{count}-green)\n"
            new_lines.append(new_line)
        else:
            new_lines.append(line)

    with open("README.md", "w", encoding="utf-8") as f:
        f.writelines(new_lines)

if __name__ == "__main__":
    solved_count = count_solved()
    update_readme(solved_count)
