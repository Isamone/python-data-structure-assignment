
# Question 1  : 
# Write a Python program that multiplies all the items in a list.

l = [2, 3, 6]

result =1 
for num in l:
     result = result * num
     print(result)

# Question 2
# Write a Python program to get a list, sorted in increasing order by the last element in each tuple, from a given list of non-empty tuples.
# Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

l = [(2,5),(1,2),(4,4), (2,3),(2,1)]
n = sorted(l)
print(n)

sorted_tuples = sorted(l, key=lambda each_tuple: each_tuple[-1])
print(sorted_tuples)

# Question 3 
# Write a Python program that combines two dictionaries by adding values for common keys.

d1 = {"a":100,"b":200,"c":300}
d2 = {"a":300,"b":200,"d":400}

# #to loop throught the keys and values

for k, v in d2.items():
     if k in d1:
         d1[k] += v
     else:
         d1[k] = v

print(d1)

# Question 4
# With a given integral number n, write a program to generate a dictionary that contains (i, i*i) so that is an integral number between 1 and n (both included). 
# Then the program should print the dictionary. Suppose the following input is supplied to the program: 8.

n = int(input("Enter a number: "))
result_dict = {}

for i in range(1, n+1):
     result_dict[i] = i*i

print(result_dict)

# Write a program to sort a tuple by its float element.
# For example: list= [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]

b = [("item1","12.20"),("item2","15.10"), ("item3","24.5")]
h = sorted(b)
print(h)
sorted_tuple = sorted(b, key=lambda y : float(y[-1]), reverse=True)
print(sorted_tuple)


# Question 5
# Write a program to sort a tuple by its float element.
# For example: list= [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
# Expected result: [('item3', '24.5'), ('item2', '15.10'), ('item1', '12.20')]

b = [("item1","12.20"),("item2","15.10"), ("item3","24.5")]
h = sorted(b)
print(h)
sorted_tuple = sorted(b, key=lambda y : float(y[-1]), reverse=True)
print(sorted_tuple)


# Question 6
# Write a Python program to create a set.
# Examples : {0, 1, 2, 3, 4}
# Write a Python program to iteration over sets.
# Write a Python program to add members in a set and to remove items from a given set.

my_set = {0, 1, 2, 3, 4}
for i in my_set:
     print(i)

my_set.add(5)
print(my_set)

my_set.add(6)
print(my_set)

my_set.remove(4)
print(my_set)

my_set.remove(5)
print(my_set)