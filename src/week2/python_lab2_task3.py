
"""
Lab 3.3 – Operator Frequency Counter

Goals:
- Practice using strings and dictionaries.
- Count character frequencies in user-provided text.

Instructions:
1. Ask the user for an arithmetic expression, e.g. "3 + 5 * (2 - 1) + 7 / 2".
2. Count how many times each operator occurs:
   +  -  *  /  (  )
3. Store counts in a dictionary.
4. Print the result.
"""

# Lab 3.3 – Operator Frequency Counter

# TODO: Get input from the user
expression = input("Enter an arithmetic expression: ")

operators = ['+', '-', '*', '/', '(', ')']

# TODO: Initialize frequency dictionary
operator_counts = {op: 0 for op in operators}

# TODO: Count operator occurrences
for char in expression:
    if char in operator_counts:
        operator_counts[char] += 1

# TODO: Print results
print("\n--- Operator Frequency ---")
print("Operator counts:", operator_counts)

print("\nOperators found in the expression:")
found_operators = {op: count for op, count in operator_counts.items() if count > 0}
if found_operators:
    print(found_operators)
else:
    print("No operators from the list were found.")