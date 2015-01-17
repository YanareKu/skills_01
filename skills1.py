# Things you should be able to do.

number_party = [-5, 6, 4, 8, 15, 16, 23, 42, 2, 7]
word_party = [ "What", "about", "the", "Spam", "sausage", "spam", "spam", "bacon", "spam", "tomato", "and", "spam"]

# Write a function that takes a list of numbers and returns a new list with only the odd numbers.
def all_odd(number_list):
    new_list = []
    for number in number_list:
        if number % 2 != 0:
            new_list.append(number)
    print "List of only odd numbers:", new_list
    return new_list

all_odd(number_party)

# Write a function that takes a list of numbers and returns a new list with only the even numbers.
def all_even(number_list):
    new_list = []
    for number in number_list:
        if number % 2 == 0:
            new_list.append(number)
    print "List of only even numbers:", new_list
    return new_list

all_even(number_party)

# Write a function that takes a list of strings and (creates?) a new list with all strings of length 4 or greater.
def long_words(word_list):
    new_list = []
    # commented out bits were doubling effort, unnecessary
    # index = 0
    for word in word_list:
        if len(word) >= 4:
        # if len(word_list[index]) >= 4:
            new_list.append(word)
        # index += 1
    print "List of words with 4 or more characters:", new_list
    return new_list

long_words(word_party)

# Write a function that finds the smallest element in a list of integers and returns it.
def smallest(number_list):
    new_list = sorted(number_list)
    print "This is the smallest number in our list", new_list[0]
    return new_list[0]

smallest(number_party)

# Write a function that finds the largest element in a list of integers and returns it.
def largest(number_list):
    new_list = sorted(number_list)
    print "This is the largest number in our list", new_list[-1]
    return new_list[-1]

largest(number_party)

# Write a function that takes a list of numbers and returns a new list of all those numbers divided by two.
def halvesies(number_list):
    new_list = []
    for num in number_list:
        new_num = (num / 2.0)
        new_list.append(new_num)
    print "List of halvesies:", new_list
    return new_list

halvesies(number_party)

# Write a function that takes a list of words and returns a list of all the lengths of those words.
def word_lengths(word_list):
    new_list = [len(word) for word in word_list]
    print "List of word lengths:", new_list
    return new_list

word_lengths(word_party)

# Write a function (using iteration) that sums all the numbers in a list.
def sum_numbers(number_list):
    total = 0
    for num in number_list:
        total += num
    print "The total of list is:", total
    return total

sum_numbers(number_party)

# Write a function that multiplies all the numbers in a list together.
def mult_numbers(number_list):
    total = 1
    for num in number_list:
        total = total * num
    print "All the numbers in this list multiplied equal:", total
    return total

mult_numbers(number_party)

# Write a function that joins all the strings in a list together (without using the join method) and returns a single string.
def join_strings(word_list):
    a = ""
    for word in word_list:
        a = a + word
    print a
    return a

join_strings(word_party)

# Write a function that takes a list of integers and returns the average (without using the avg method)
def average(number_list):
    """add numbers together
    divide sum by number of numbers
    return result"""
    average = sum_numbers(number_list) / len(number_list)
    print "The average of all integers in this list is:", average
    return average

average(number_party)