# To construct a string from the words in an array, starting with the 0th character from each word, you can simply iterate over each word in the array and take the first character of each word to form a new string.

def construct_string_from_first_chars(arr):
    # Initialize an empty string to hold the result
    result = ''
    
    # Iterate over each word in the array
    for word in arr:
        # Check if the word is not empty to avoid IndexError
        if word:
            # Append the 0th character of each word to the result string
            result += word[0]
    
    return result

def construct_string_by_char_position(arr):
    # Initialize an empty string to hold the result
    result = ''
    
    # Find the length of the longest word to know the maximum number of iterations
    max_length = max(len(word) for word in arr) if arr else 0
    
    # Iterate over each character position
    for i in range(max_length):
        # Iterate over each word in the array
        for word in arr:
            # Check if the word has an ith character
            if len(word) > i:
                # Append the ith character of the word to the result string
                result += word[i]
    
    return result

# Example usage
arr = ["Lalit", "is", "a", "good", "buy"]
result = construct_string_from_first_chars(arr)

resultNth = construct_string_by_char_position(arr)

print("Output with Oth Position: " + result) 
print("Output with nth character: " + resultNth)  

