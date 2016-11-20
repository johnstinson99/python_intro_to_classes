import string
print(string.ascii_lowercase)

def sort_item(my_tuple):
    return my_tuple[1]
mylist = [('b', 567), ('c', 4), ('a', 123)]
mylist.sort()
print(mylist)
mylist.sort(key=sort_item)
print(mylist)