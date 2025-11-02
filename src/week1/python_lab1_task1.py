"""
Task 1 – Simple Function with Arithmetic
---------------------------------------
Write a function `circle_area(radius)` that returns the area of a circle.
Formula: area = π × radius²
Use the math module for π.
Ask user for radius and print result with 2 decimals.
"""

import math

def circle_area(radius):
    """Return the area of a circle given its radius."""
    area = math.pi * (radius * radius)
    return area

if __name__ == "__main__":
    print("circle Area Calculater!")

    user_input_radius = input("please enter the radiyus of the circle: ")

    radius_num = float(user_input_radius)

    result_area = circle_area(radius_num)

    print(f"The area for radiyus {radius_num} is: {result_area:.2f}")

