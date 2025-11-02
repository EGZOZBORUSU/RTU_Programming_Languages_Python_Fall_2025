"""
Task 4 – Text-based Arithmetic Analyzer
--------------------------------------
Create a text-based analyzer that:
1. Counts non-space characters.
2. Counts words.
3. Extracts numbers and computes their sum and average.
Use helper functions:
- count_characters(text)
- count_words(text)
- extract_numbers(text)
- analyze_text(text)
Print formatted summary in main.
"""
import re

def count_characters(text):
    """
    Counts the total number of non-space characters in the given text.

    Args:
        text (str): The input string.

    Returns:
        int: The count of all characters excluding whitespace.
    """
    return len("".join(text.split()))

def count_words(text):
    """
    Counts the number of words in the given text.

    Args:
        text (str): The input string.

    Returns:
        int: The total count of words.
    """
    return len(text.split())

def extract_numbers(text):
    """
    Finds and extracts all numerical values (integers and floats) from the text.

    Args:
        text (str): The input string.

    Returns:
        list[float]: A list of all extracted numbers converted to floats.
    """
    number_strings = re.findall(r'[-+]?\b\d+\.?\d*\b', text)

    numbers = []
    for num_str in number_strings:
        try:
            numbers.append(float(num_str))
        except ValueError:
            continue

    return numbers

def analyze_text(text):
    """
    Analyzes the text for character count, word count, number sum, and average.

    Args:
        text (str): The input string to analyze.

    Returns:
        dict: A dictionary containing the analysis results.
    """
    char_count = count_characters(text)
    word_count = count_words(text)
    numbers = extract_numbers(text)

    total_sum = sum(numbers)
    num_count = len(numbers)

    average = total_sum / num_count if num_count > 0 else 0

    return {
        "non_space_chars": char_count,
        "word_count": word_count,
        "extracted_numbers": numbers,
        "sum_of_numbers": total_sum,
        "average_of_numbers": average
    }

if __name__ == "__main__":
    print("--- Text-based Arithmetic Analyzer ---")

    sample_text = input("Please enter a sentence containing words and numbers (e.g., 'The invoice total is 45.75, plus 10 percent tax, making it 50.325 total.'):\n")

    analysis_results = analyze_text(sample_text)

    print("\n--- Analysis Summary ---")
    print(f"1. Non-Space Character Count: {analysis_results['non_space_chars']}")
    print(f"2. Word Count:              {analysis_results['word_count']}")
    print("-" * 30)

    numbers_extracted = analysis_results['extracted_numbers']

    if numbers_extracted:
        print(f"3. Arithmetic Analysis ({len(numbers_extracted)} numbers found):")
        print(f"   Extracted Numbers: {numbers_extracted}")
        print(f"   Sum of Numbers:    {analysis_results['sum_of_numbers']:.2f}")
        print(f"   Average of Numbers: {analysis_results['average_of_numbers']:.2f}")
    else:
        print("3. Arithmetic Analysis: No numbers were found in the provided text.")
