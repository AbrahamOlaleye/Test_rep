import re

def load_bias_words(file_path):
    """
    Load bias-indicating words from a given file.
    
    Args:
    file_path (str): The path to the text file containing the list of bias-indicating words.
    
    Returns:
    set: A set of words read from the file, transformed to lower case for case-insensitive comparison.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        bias_words = set(word.strip().lower() for word in file.readlines())
    return bias_words

def check_bias(user_input, bias_words):
    """
    Check if the user's input contains any of the bias-indicating words loaded from the file.
    
    Args:
    user_input (str): Text input provided by the user.
    bias_words (set): A set of words that are considered bias-indicating.
    
    Returns:
    tuple: A boolean indicating if biased words were found and a set of the biased words found.
    """
    # Normalize and split the input
    words_in_input = set(re.findall(r'\b\w+\b', user_input.lower()))
    
    # Find intersection of input words and bias words
    biased_words = words_in_input.intersection(bias_words)
    
    # Return True if biased words are found, else False
    return bool(biased_words), biased_words

def main():
    """
    Main function to handle user interaction and bias checking.
    
    Prompts the user for the filename and input, checks for bias, and prints out results.
    """
    file_path = input("Please enter the filename containing bias-indicating words: ")
    bias_words = load_bias_words(file_path)
    
    user_input = input("Please enter a sentence to check for bias: ")
    is_biased, found_words = check_bias(user_input, bias_words)
    
    if is_biased:
        print(f"The input is considered biased. Biased words detected: {found_words}")
    else:
        print("The input does not contain biased words.")

if __name__ == "__main__":
    main()
