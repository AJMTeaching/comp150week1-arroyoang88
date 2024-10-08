# ------------------------------------------------------------------------

### Lab Exercise 1: Lists in Python
#creating my_list
1. Create a list called my_list with the values [1, 5, 'apple', 20.5].
2. Using indexing, print the value 'apple' from my_list.
3. Add the value 10 to the end of my_list using the append() method. Print the updated list.
4. Remove the value 20.5 from my_list using the remove() method. Print the updated list.
5. Reverse the order of the elements in my_list using a method. Print the reversed list.

my_list = [1, 5, 'apple', 20.5]
print(my_list[2])
my_list.append(10)
print(my_list)
my_list.remove(20.5)
print(my_list)
reversed(my_list)


# Problem 2
1. Create a dictionary called person with keys 'name', 'age', 'job' and values 'John', 30, 'teacher'.
2. Print the value corresponding to the 'job' key.
3. Add a new key-value pair: 'city': 'Paris' to the person dictionary. Print the updated dictionary.
person|={"city": "Paris"}
4. Remove the 'age' key-value pair from person. Print the updated dictionary.
5. Iterate through the person dictionary and print out each key-value pair on a separate line.
dict[str, int]:
dict(name=John,age=30,job=teacher)
dict[key]=value
print[person('job)']
def print[key(job)]= teacher
def remove_key=dict[str, int]:
    del dict[age]
dict(name)
dict(name)=John
dict(age)
dict(age)=30
dict(job)
NameError: name 'job' is not defined


# -----------------------------------------------------------------------------


# Importing sys for test function
import sys
my_list=(1,2,3)
def test_remove_elements(my_list):
my_list.assertEqual(add_elements([1,2,3]))


# Custom Test Function
def test(did_pass):'FAILED'
    """ Print the result of a test. """
    linenum = sys._getframe(1).f_lineno 
      # Get the caller's line number.
    msg = f"Test at line {linenum} {'PASSED' if did_pass else 'FAILED'}."
    print(msg)
    'FAILED'


# Function 1: count_vowels
def count_vowels(s: str) -> int:
    """
    Count the number of vowels in a string.

    Parameters:
    - s (str): The input string

    Returns:
    - int: The number of vowels in the string
    """
    # TODO: Implement this function
    pass

vowels = "aeiouAEIOU"
for character in s:
    if character in vowels:
        count = count + 1

# Unit Tests for count_vowels
def test_count_vowels():
    test(count_vowels("hello") == 2)
    test(count_vowels("why") == 0)
    test(count_vowels("aeiou") == 5)
    test(count_vowels("") == 0)
    test(count_vowels("bcdfg") == 0)
    test(count_vowels("aeiouAEIOU") == 10)
    test(count_vowels("HELLO") == 2)
    test(count_vowels("aEiOu") == 5)
    test(count_vowels("a e i o u") == 5)
    test(count_vowels("rhythm") == 0)
    test(count_vowels(house) == 2)
    test(count_vowels(computer) == 2)
    test(count_vowels(a,i,o) == 3)


# Function 2: merge_lists
def merge_lists(list1: list, list2: list) -> list:

if list1[i1] < list2[i2]:
    merge_list.append(list1[i1])
    if i1 + 1 == len(list1):
        for item in list2[i2:]:
            merged_list.append(item)
        else:
            i1 = +1

    else:
        merged_list.append(list2[i2])
        if i2 + 1 == len(list2):
            for item in list[i1:]:
                merged_list.append(item)

            else:
                i2 += 1
        
        return merged_list
            


    """
    Merge two sorted lists into a single sorted list.

    Parameters:
    - list1 (list): The first sorted list
    - list2 (list): The second sorted list

    Returns:
    - list: A new sorted list containing all elements from list1 and list2
    """
    # TODO: Implement this function
    pass


# Unit Tests for merge_lists
def test_merge_lists():
    list1 = [1, 3, 5]
    list2 = [2, 4, 6]
    merged = merge_lists(list1, list2)
    test(merged == [1, 2, 3, 4, 5, 6])
    test(merge_lists([], []) == [])
    test(merge_lists([1], [2]) == [1, 2])
    test(merge_lists([1, 1], [2, 2]) == [1, 1, 2, 2])
    test(merge_lists([1, 3, 5], []) == [1, 3, 5])
    test(merge_lists([], [2, 4, 6]) == [2, 4, 6])
    test(merge_lists([1, 2, 3], [4, 5, 6]) == [1, 2, 3, 4, 5, 6])
    test(merge_lists([1, 3, 5, 7, 9], [2, 4, 6, 8, 10]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    test(merge_lists([1, 1, 2, 3], [1, 2, 2, 3]) == [1, 1, 1, 2, 2, 2, 3, 3])

    def test_merge_list():
    list1 = [10, 20, 30]
    list2 = [40, 50, 60]
merged = merge_list(list1, list2)
test(merged == [10, 20, 30, 40, 50, 60])

# Function 3: word_lengths
def test_word_lengths():
    words = [goodbye, tall, people]
     lengths = word_lengths(words)
    test(lengths == [7, 4, 6])
    test(word_lengths([]) == [])
    test(word_lengths(["tall"]) == [4])

    list_of_words_lengths = []
    for happiness in words:
        list_of_word_lengths.append(len(happiness))
    return list_of_word_lengths
    
    """
    # TODO: Implement this function
    pass


# Unit Tests for word_lengths
def test_word_lengths():
    words = ["hello", "world", "python"]
    lengths = word_lengths(words)
    test(lengths == [5, 5, 6])
    test(word_lengths([]) == [])
    test(word_lengths(["word"]) == [4])
    test(word_lengths(["short", "mediummm", "longesttttt"]) == [5, 8, 11])
    test(word_lengths(["", "a", "ab", "abc"]) == [0, 1, 2, 3])
    test(word_lengths(["  ", "a b", " c "]) == [2, 3, 3])


# Function 4: reverse_string
def reverse_string(s: str) -> str:
    """
    Reverse a string.

    Parameters:
    - s (str): The input string

    Returns:
    - str: The reversed string
    """
    # TODO: Implement this function
    pass


# Unit Tests for reverse_string
def test_reverse_string():
    text = "python"
    reversed_text = reverse_string(text)
    test(reversed_text == "nohtyp")
    test(reverse_string("") == "")
    test(reverse_string("a") == "a")
    test(reverse_string("aaa") == "aaa")
    test(reverse_string("Hello, World!") == "!dlroW ,olleH")
    test(reverse_string("12345") == "54321")
    test(reverse_string("  spaces  ") == "  secaps  ")


# Function 5: intersection
def intersection(list1: list, list2: list) -> list:
    """
    Find the intersection of two lists.

    Parameters:
    - list1 (list): The first list
    - list2 (list): The second list

    Returns:
    - list: The intersection of the two lists
intersection_list = []
for item in list1:
    if item in list2:
        intersection_list.append(item)
    return list(set(intersection_list))

    """
    # TODO: Implement this function
    pass


# Unit Tests for intersection
def test_intersection():
    list1 = [1, 2, 3, 4]
    list2 = [3, 4, 5, 6]
    result = intersection(list1, list2)
    test(result == [3, 4])
    test(intersection([], []) == [])
    test(intersection([1, 2], [3, 4]) == [])
    test(intersection([1, 2], [1, 2]) == [1, 2])
    test(intersection([1, 2, 2, 3], [2, 2, 3, 4]) == [2, 3])
    test(intersection([1, 2, 3], [4, 5, 6]) == [])
    test(intersection([1, 2, 3], [1, 2, 3]) == [1, 2, 3])


# Test Suite
def test_suite():
    print(f"Count Vowels Test Results:")
    test_count_vowels()
    print(f"Merge Lists Test Results:")
    test_merge_lists()
    print(f"Word Lengths Test Results:")
    test_word_lengths()
    print(f"Reverse String Test Results:")
    test_reverse_string()
    print(f"Intersection Test Results:")
    test_intersection()


test_suite()
