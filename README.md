# LeetCode Python Clean Code Showcase 🚀

![LeetCode](https://img.shields.io/badge/LeetCode-Active-brightgreen)
![Python](https://img.shields.io/badge/language-python-blue)
![License](https://img.shields.io/badge/license-MIT-blue.svg)
![visitors](https://visitor-badge.laobi.icu/badge?page_id=robert-nguyen-global-dev.leetcode-python-showcase)

👋 Hi, I'm Robert Nguyen.  
👨‍💻 **Python & Java Developer** working towards **Remote opportunities** with potential relocation.

This repository showcases **clean, readable Python solutions** to selected LeetCode problems, structured with test cases and organized for consistent daily practice and interview preparation.

---

## Why This Repo?

- Practicing algorithm and problem-solving with **clean, maintainable code**.
- Improving test-driven development mindset with `pytest`.
- Building a consistent daily habit to sharpen technical problem-solving skills.
- Preparing for **global remote opportunities** in Python and backend engineering roles.

---

## 📈 Progress Tracker
Below are real-time progress and build status for this repo.  
![Solved](https://img.shields.io/badge/solved-24-brightgreen)
![Build](https://github.com/robert-nguyen-global-dev/leetcode-python-showcase/actions/workflows/python-tests.yml/badge.svg)  
🎯 Target:
- [ ] 50 Easy
- [ ] 50 Medium
- [ ] 50 Hard

✅ Completed Problems:
- Easy: 24 / 50 ✅
- Medium: 0 / 50 🚧
- Hard: 0 / 50 🚧

<!-- SOLUTION_TABLE_START -->
| No. | ID   | Title             | Difficulty | Solution | Time | Space |
|-----|------|-------------------|------------|----------|------|-------|
| 1   | 0001 | Two Sum           | Easy       | [Python](./easy/0001_two_sum/two_sum.py)                     | O(n) | O(n) |
| 2   | 0013 | Roman To Int      | Easy       | [Python](./easy/0013_roman_to_int/roman_to_int.py)           | O(n) | O(1) |
| 3   | 0020 | Valid Parentheses | Easy       | [Python](./easy/0020_valid_parentheses/valid_parentheses.py) | O(n) | O(n) |
| 4   | 0021 | Merge Two Sorted Lists | Easy       | [Python](./easy/0021_merge_two_sorted_lists/merge_two_sorted_lists.py) | O(m + n) | O(1) |
| 5   | 0026 | Remove Duplicates Sorted Array | Easy       | [Python](./easy/0026_remove_duplicates_sorted_array/remove_duplicates_sorted_array.py) | O(n) | O(1) |
| 6   | 0070 | Climbing Stairs   | Easy       | [Python](./easy/0070_climbing_stairs/climbing_stairs.py)     | O(n) | O(1) |
| 7   | 0088 | Merge Sorted Array | Easy       | [Python](./easy/0088_merge_sorted_array/merge_sorted_array.py) | O(m + n) | O(1) |
| 8   | 0094 | Binary Tree Inorder Traversal | Easy       | [Python](./easy/0094_binary_tree_inorder_traversal/binary_tree_inorder_traversal.py) | O(n) | O(n) |
| 9   | 0101 | Symmetric Tree    | Easy       | [Python](./easy/0101_symmetric_tree/symmetric_tree.py)       | O(n) | O(h) |
| 10  | 0104 | Maximum Depth Binary Tree | Easy       | [Python](./easy/0104_maximum_depth_binary_tree/maximum_depth_binary_tree.py) | O(n) | O(h) |
| 11  | 0112 | Path Sum          | Easy       | [Python](./easy/0112_path_sum/path_sum.py)                   | O(n) | O(h) |
| 12  | 0121 | Best Time To Buy And Sell Stock | Easy       | [Python](./easy/0121_best_time_to_buy_and_sell_stock/best_time_to_buy_and_sell_stock.py) | O(n) | O(1) |
| 13  | 0125 | Valid Palindrome  | Easy       | [Python](./easy/0125_valid_palindrome/valid_palindrome.py)   | O(n) | O(n) |
| 14  | 0136 | Single Number     | Easy       | [Python](./easy/0136_single_number/single_number.py)         | O(n) | O(1) |
| 15  | 0141 | Linked List Cycle | Easy       | [Python](./easy/0141_linked_list_cycle/linked_list_cycle.py) | O(n) | O(1) |
| 16  | 0145 | Binary Tree Postorder | Easy       | [Python](./easy/0145_binary_tree_postorder/binary_tree_postorder.py) | O(n) | O(n) |
| 17  | 0160 | Intersection Of Two Linked Lists | Easy       | [Python](./easy/0160_intersection_of_two_linked_lists/intersection_of_two_linked_lists.py) | O(m + n) | O(1) |
| 18  | 0169 | Majority Element  | Easy       | [Python](./easy/0169_majority_element/majority_element.py)   | O(n) | O(1) |
| 19  | 0171 | Excel Column Number | Easy       | [Python](./easy/0171_excel_column_number/excel_column_number.py) | O(n) | O(1) |
| 20  | 0191 | Number Of 1 Bits  | Easy       | [Python](./easy/0191_number_of_1_bits/number_of_1_bits.py)   | O(k) | O(1) |
| 21  | 0202 | Happy Number      | Easy       | [Python](./easy/0202_happy_number/happy_number.py)           | O(log n) | O(1) |
| 22  | 0206 | Reverse Linked List | Easy       | [Python](./easy/0206_reverse_linked_list/reverse_linked_list.py) | O(n) | O(1) |
| 23  | 0217 | Contains Duplicate | Easy       | [Python](./easy/0217_contains_duplicate/contains_duplicate.py) | O(n) | O(n) |
| 24  | 0234 | Palindrome Linked List | Easy       | [Python](./easy/0234_palindrome_linked_list/palindrome_linked_list.py) | O(n) | O(1) |
<!-- SOLUTION_TABLE_END -->

This repository is updated regularly to track my algorithm practice, clean coding skills, and preparation for remote Python/backend engineering roles.

---

## Structure

- Problems are organized by difficulty:
    - `easy/`
    - `medium/`
    - `hard/`
- Each problem has its own folder:
    ```
    easy/0001_two_sum/
        ├── two_sum.py
        └── test_two_sum.py
    ```
- Each folder contains:
    - A clean Python solution.
    - Python tests for validation and practice.

---

## Installation

To set up the project locally and install required dependencies:

```bash
git clone https://github.com/robert-nguyen-global-dev/leetcode-python-showcase.git
cd leetcode-python-showcase
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```
✅ Note: It's recommended to use a virtual environment to isolate dependencies and ensure consistent behavior.

---

## Running Tests

🚀 To run all tests:
```bash
pytest -v
```
🚀 To test a specific problem:
```bash
pytest -v easy/0001_two_sum
```

---

## Contact

📫 Email: [robert.nguyen.global.dev@gmail.com](mailto:robert.nguyen.global.dev@gmail.com)  
🔗 GitHub: [robert-nguyen-global-dev](https://github.com/robert-nguyen-global-dev)  
💼 LinkedIn: [linkedin.com/in/robert-nguyen-global-dev](https://www.linkedin.com/in/robert-nguyen-global-dev/)

---

## License

This project is licensed under the [MIT License](LICENSE).  
Feel free to use and share for learning purposes.
