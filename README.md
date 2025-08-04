# TriangleCheck
A simple Python script that checks if three given lengths can form a triangle using the triangle inequality theorem.

# 🔺 Triangle Analyzer: Validator & Classifier

This is a command-line Python script that first determines if three given side lengths can form a valid triangle and, if so, classifies the triangle as **Equilateral**, **Isosceles**, or **Scalene**.

The program prompts the user to enter three numbers for the triangle's sides. It then validates them using the triangle inequality theorem and proceeds to classify the triangle type. 

## How to Use

1.  Make sure you have Python installed on your system.
2.  Save the code as a `.py` file (e.g., `TriangleCheck.py`).
3.  Open your terminal or command prompt and navigate to the file's directory.
4.  Run the script with the following command:
    ```sh
    python TriangleCheck.py
    ```
5.  Enter the three side lengths as prompted, one by one. The program will then print whether the lengths can form a triangle and, if so, what type.

## Logic

The program's logic is divided into two main parts:

### 1. Validation

First, it is based on the **Triangle Inequality Theorem**, which states that for any triangle, the sum of the lengths of any two sides must be greater than the length of the third side. The script checks if all three of the following conditions are true:
* `side1 + side2 > side3`
* `side1 + side3 > side2`
* `side2 + side3 > side1`

### 2. Classification

If the validation passes, a nested conditional block classifies the triangle:
* **Equilateral:** If all three sides are equal (`side1 == side2 == side3`).
* **Isosceles:** If any two sides are equal.
* **Scalene:** If all three sides are different.
