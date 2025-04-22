def count_words(book_text):
    words = book_text.split()
    return len(words)

def count_characters(book_text):
    text = book_text.lower()
    characters = {}
    for char in text:
        if char in characters:
            characters[char] += 1
        else:
            characters[char] = 1
    return characters  # Don't forget to return the dictionary!
def sort_chars_by_count(char_dict):
    # Create a list to hold our dictionaries
    chars_list = []
    
    # Convert each key-value pair to a dictionary, skipping non-alphabetical characters
    for char, count in char_dict.items():
        if char.isalpha():  # Only include alphabetical characters
            chars_list.append({"char": char, "count": count})
    
    # Define a helper function to tell sort() what to sort by
    def sort_on(dict):
        return dict["count"]
    
    # Sort the list by count in descending order
    chars_list.sort(reverse=True, key=sort_on)
    
    return chars_list