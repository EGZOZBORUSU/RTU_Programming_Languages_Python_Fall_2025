"""
Lab 3.1 – Simple Datasets and Aggregates

Goals:
- Create and manipulate Python lists and dictionaries.
- Compute aggregates such as sum, average, max, and min.

Instructions:
1. Create a list `temperatures` with daily temperatures for one week.
2. Create a dictionary `city_population` with at least 5 cities and their populations.
3. Compute:
   - The average temperature.
   - The maximum and minimum population.
   - The total population of all cities.
4. Print your results in a clear, formatted way.
"""

# Lab 3.1 – Simple Datasets and Aggregates

# TODO: Create the datasets - up to you to fill in the data
temperatures = [22.5, 24.0, 26.5, 27.0, 25.5, 23.0, 21.5]
city_population = {
    "Istanbul": 15840000,
    "Ankara": 5747000,
    "Izmir": 4394000,
    "Antalya": 2548000,
    "Bursa": 3101000
}

# TODO: Compute aggregates

# Temperature calculations
average_temperature = sum(temperatures) / len(temperatures)

# Population calculations
populations = city_population.values()
total_population = sum(populations)
largest_population = max(populations)
min_population = min(populations) # The task also required the min population.

# Find the city with the largest population
largest_city = ""
for city, population in city_population.items():
    if population == largest_population:
        largest_city = city
        break

# TODO: Print results
print("--- Weekly Analysis ---")
print(f"Average Temperature: {average_temperature:.2f}C")
print("\n--- City Population Analysis ---")
print(f"Total Population: {total_population:,}")
print(f"Smallest Population (Min): {min_population:,}")
print(f"Largest Population (Max): {largest_population:,} ({largest_city})")