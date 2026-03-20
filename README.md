# Number Cycle Detection Project

## 📌 Project Overview

This project is a Python program that analyzes number transformations using binary and decimal conversions.
The program generates a sequence of numbers starting from a user input and detects when the sequence repeats (cycle detection).

---

## ⚙️ How the Program Works

1. User enters a positive integer.
2. The number is converted from decimal to binary.
3. The binary number is reversed.
4. It is converted back to decimal.
5. The value increases by 2.
6. The process repeats until a cycle is detected.

----

## 📂 Project Files

* `project.py` → Main Python program
* `amplitude.txt` → Stores the detected cycle and period
* `depart.txt` → Stores the starting number entered by the user

---

## ▶️ How to Run

Make sure Python 3 is installed, then run:

```
python project.py
```

Enter a number when asked.

---

## 📊 Example Output

Input:

```
39
```

Output:

```
{'cycle': '39#59#57#41#39#', 'period': 4}
```

---

## 👨‍💻 Authors

University Project by:

* ABDIHAFITH
* BILAL

