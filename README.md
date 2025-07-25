# TriangleCheck
A simple Python script that checks if three given lengths can form a triangle using the triangle inequality theorem.

# 🔺 Triangle Inequality Checker

This is a command-line Python script that determines whether three given side lengths can form a valid triangle.

The program prompts the user to enter three numbers, one for each side of the triangle, and then checks if they satisfy the triangle inequality theorem. It's a fundamental geometry problem solved with simple conditional logic in Python.

## How to Use

1.  Make sure you have Python installed on your system.
2.  Save the code as a `.py` file (e.g., `TriangleCheck.py`).
3.  Open your terminal or command prompt and navigate to the file's directory.
4.  Run the script with the following command:
    ```sh
    python TriangleCheck.py
    ```
5.  Enter the three side lengths as prompted, one by one. The program will then print whether or not these lengths can form a triangle.

## Logic

The program is based on the **Triangle Inequality Theorem**, which states that for any triangle, the sum of the lengths of any two sides must be greater than the length of the third side.

The script checks if all three of the following conditions are true:
* `side1 + side2 > side3`
* `side1 + side3 > side2`
* `side2 + side3 > side1`

If all conditions are met, the lengths can form a triangle. Otherwise, they cannot.
