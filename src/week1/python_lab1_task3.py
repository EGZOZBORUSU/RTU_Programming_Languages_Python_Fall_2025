"""
Task 3 – Function with Combined Logic
------------------------------------
Write a function `analyze_sentence(text)` that returns:
1. total character count (len)
2. word count (split)
3. whether it contains the word "Python" (case-insensitive)
Return results as a tuple and print summary in main.
"""

def analyze_sentence(text):
    count_chars = len(text)

    words_list = text.split()
    count_words = len(words_list)

    has_python = 'python' in text.lower()

    return (count_chars, count_words, has_python)

if __name__ == "__main__":
    print("Sentence Analizer Tool!")

    user_sentense = input("Pls type a sentense to analize: ")

    results_tuple = analyze_sentence(user_sentense)

    char_cunt = results_tuple[0]
    word_cunt = results_tuple[1]
    has_py = results_tuple[2]

    print("\nAnaliz is complete:")
    print(f"Total charecters (with spaces): {char_cunt}")
    print(f"Number of words: {word_cunt}")
    print(f"Dous it have the word 'Python'?: {has_py}")
