## LAB 1 
## STRING MANIPULATION -- PALINDROME VARIANTS

def is_palindrome(s):
    """Return true IF S is a Palindrome otherwise False"""
    return s == s[::-1]

def can_be_palindrome(s):
    for i in range(len(s)):
        safi = s[:i] + s[i+1:]
        if safi == safi[::-1]:
            return True 
    return False

def palindrome_strings(strings):
    return [s for s in strings if s == s[::-1]]









## NUMERICAL PATTERNS = PRIME PATTERNS 

def is_prime(n):
    """Return true if n is a prime number"""
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
    
def primes_less_than(n):
    return [i for i in range(2, n) if is_prime(i)]

def are_coprime(a, b):
    def gcd(x, y):
        while y != 0:
            x, y = y, x % y
        return x
    return gcd(a, b) == 1







## DATA STRUCTURES: DICTIONARY VALUE RETRIEVAL 

def get_value(d, key): 
    return d.get(key, None)

def key_with_highest_value(dictionary):
    return max(dictionary, key=dictionary.get)

def keys_above_threshold(dictionary, threshold):
    return [k for k, v in dictionary.items() if v > threshold]






# DATA STRUCTURES : DIFFERENT STRUCTURES 
# MUTABLE = lists
# IMMUTABLE = tuples, strings, numbers
# SEQUENTIAL = Lists, Strings
# NON-SEQUENTIAL = Dictionaries, Sets, Tuples





# ALGORITHM QUESTION

def multiply_adjacent_elements():
    """Return the product of adjacent elements in a list"""
    numbers = []
    while True:
        num = input("Enter an integer (type 'done' when finished): ")
        if num == "done":
            break
        numbers.append(int(num))
    for i in range(1, len(numbers)):
        numbers[i] *= numbers[i - 1]
    print(numbers)
    repeat = input("Would you like to repeat the process? (yes/no): ")
    if repeat.lower() == "yes":
        multiply_adjacent_elements()
    else:
        print("You can leave from the backdoor LOL")





# Test Cases
print(is_palindrome("CAR"))  
print(can_be_palindrome("MOTORBIKE"))  
print(palindrome_strings(["GYM", "WHATS GOOD", "CAR", "EARTH"]))  
print(is_prime(7))  
print(primes_less_than(20))  
print(are_coprime(5, 13))  
print(get_value({'a': 1, 'b': 2, 'c': 3}, 'b'))  
print(key_with_highest_value({'a': 1, 'b': 2, 'c': 3}))  
print(keys_above_threshold({'a': 10, 'b': 20, 'c': 30}, 15))  
multiply_adjacent_elements()  











