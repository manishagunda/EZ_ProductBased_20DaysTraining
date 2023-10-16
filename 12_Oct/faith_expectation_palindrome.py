def is_palindrome(s):
    # Remove spaces and convert to lowercase for a case-insensitive check
    s = s.replace(" ", "").lower()
    # Compare the string with its reverse
    return s == s[::-1]

# Test cases
input_string = "madam"
print(is_palindrome(input_string))  # Expecting True
