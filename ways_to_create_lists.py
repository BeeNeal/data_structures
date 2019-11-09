n = 5
lst1 = [0] * n
# [0, 0, 0, 0, 0]  
# Can be good to make lists this way when making boards for games

s = "Brittany Jewell Neal"
# list comprehension
lst2 = [char.lower() for char in s]
x = " ".join(lst2)
print(x)

# built in list operation
lst3 = list(s)
i = lst3.index(" ")
print(lst3[:i])
# ['B', 'r', 'i', 't', 't', 'a', 'n', 'y']

lst4 = [s]
# ['Brittany']