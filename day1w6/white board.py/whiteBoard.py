# You probably know the "like" system from Facebook and other pages. People can "like" blog posts, pictures or other items. We want to create the text that should be displayed next to such an item.

# Implement the function which takes an array containing the names of people that like an item. It must return the display text as shown in the examples:

# []                                -->  "no one likes this"
# ["Peter"]                         -->  "Peter likes this"
# ["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
# ["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
# ["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"
# Note: For 4 or more names, the number in "and 2 others" simply increases.


def likes(alist):
    if not alist:
        return 'no one likes this'
    elif len(alist) == 1:
        return f'{alist[0]} likes this'
    elif len(alist) == 2:
        return f'{alist[0]} and {alist[1]} like this'
    elif len(alist) == 3:
        return f'{alist[0]}, {alist[1]} and {alist[2]} like this'
    elif len(alist) >= 4:
        return f'{alist[0]}, {alist[1]} and {(len(alist) - 2)} others like this'


print(likes(["Alex", "Jacob", "Mark", "Max", "John"]))