'''str="madammadam"
i.count number of palindomic substring
ii. count longest palindromic string
iii.smallest palindromic substring which is not 1 in length
T.L=1 sec 1<=n<=10^5'''
def is_palindrome(s):
    return s == s[::-1]

def count_palindromic_substrings(s):
    count = 0
    n = len(s)

    for i in range(n):
        for j in range(i, n):
            if is_palindrome(s[i:j+1]):
                count += 1

    return count

def longest_palindromic_substring(s):
    n = len(s)
    max_len = 0
    result = ""

    for i in range(n):
        for j in range(i, n):
            substring = s[i:j+1]
            if is_palindrome(substring) and len(substring) > max_len:
                max_len = len(substring)
                result = substring

    return result

def smallest_non_unit_palindromic_substring(s):
    n = len(s)

    for i in range(n):
        for j in range(i, n):
            substring = s[i:j+1]
            if is_palindrome(substring) and len(substring) > 1:
                return substring

    return None

# Example usage:
s = "madammadam"

# i. Count the number of palindromic substrings
count = count_palindromic_substrings(s)
print("i. Number of palindromic substrings:", count)

# ii. Find the longest palindromic substring
longest_palindrome = longest_palindromic_substring(s)
print("ii. Longest palindromic substring:", longest_palindrome)

# iii. Find the smallest palindromic substring which is not 1 in length
smallest_non_unit_palindrome = smallest_non_unit_palindromic_substring(s)
print("iii. Smallest non-unit palindromic substring:", smallest_non_unit_palindrome)

