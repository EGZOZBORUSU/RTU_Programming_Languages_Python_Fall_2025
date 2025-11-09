
"""
Lab 3.4 – Functional Tools Practice

Goals:
- Learn to apply functional tools (`map`, `filter`, `zip`).
- Compare functional style to list comprehensions.

Instructions:
Given:
    prices = [12.5, 9.9, 15.0, 22.3, 5.0]
    quantities = [2, 5, 1, 3, 4]

1. Use map() and a lambda to compute total cost for each item (price * quantity).
2. Use filter() to keep only totals above 30.
3. Use zip() to pair prices with quantities.
4. Try doing the same using list comprehensions for comparison.
"""


prices = [12.5, 9.9, 15.0, 22.3, 5.0]
quantities = [2, 5, 1, 3, 4]

print("--- Lab 3.4 Results ---")
print(f"Prices: {prices}")
print(f"Quantities: {quantities}")
print("-" * 30)

# TODO: Compute totals using map()
totals_iterator = map(lambda pair: pair[0] * pair[1], zip(prices, quantities))
totals = list(totals_iterator)

# TODO: Filter totals above 30
high_totals_iterator = filter(lambda total: total > 30, totals)
high_totals = list(high_totals_iterator)

# TODO: Pair prices and quantities with zip()
pairs_iterator = zip(prices, quantities)
pairs = list(pairs_iterator)

# TODO: Repeat using list comprehensions
totals_comp = [p * q for p, q in zip(prices, quantities)]

high_totals_comp = [total for total in totals_comp if total > 30]

# TODO: Print results
print("--- Functional Style (map, filter) ---")
print("Totals:", totals)
print("Totals > 30:", high_totals)
print("Price-quantity pairs:", pairs)

print("\n--- List Comprehension Style ---")
print("Totals (comprehension):", totals_comp)
print("Totals > 30 (comprehension):", high_totals_comp)

print("\nComparison:")
print(f"Totals match: {totals == totals_comp}")
print(f"High totals match: {high_totals == high_totals_comp}")