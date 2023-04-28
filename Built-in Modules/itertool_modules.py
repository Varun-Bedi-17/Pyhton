from ast import operator
from code import InteractiveConsole
import itertools
#---------------------------- Three types of infinite iterators -------------------------------------

# 1. count(start_number , step ) - Return infinitely from start_number with skipping values provided by step.
# print(type(itertools.count(10))) # itertool.count
# print(itertools.count(10))  # count(10)
# for i in itertools.count(10,2):
#     if i == 20:
#         break
#     else:
#         print(i, end = " ")  #  10 12 14 16 18


# 2. cycle("string") - Return all elements in cyclic manner which are passed in function
# print(type(itertools.cycle("10")))
# count = 1  # itertools.cycle
# for i in itertools.cycle("ABC"):
#     if count == 8:
#         break
#     else:
#         print(i, end = " ")
#         count += 1  #  A B C A B C A

# []- Shows optional


# 3. repeat(num , [stop_value]) - Return passed number infinite times untill stop_value is provided. 
# print(list(itertools.repeat(5))) # Gives memorerror as this is infinite
# print(itertools.repeat(30,5)) # repeat(30,5)
# print(list(itertools.repeat(10,6)))  #  [10, 10, 10, 10, 10, 10]


# ------------------------------- Terminating iterators ----------------------------------------
import operator


# 1. accumulate(iterable, [func, initial = None]) 
# print(itertools.accumulate([1,7,9]))  #  itertools object at ..
# print(list(itertools.accumulate("157")))  #  ['1', '15', '157']
# print(list(itertools.accumulate((1,7,5))))  #  [1, 8, 13]
# print(list(itertools.accumulate([1,3,5,7],operator.mul)))  #  [1, 3, 15, 105]
# print(tuple(itertools.accumulate([2,5,8,9],operator.mul, initial = 5)))  #  (5, 10, 50, 400, 3600)


# 2. chain(*iterable)
# print(list(itertools.chain("AB","EF","HI")))  #  ['A', 'B', 'E', 'F', 'H', 'I']
# print(*itertools.chain("AB","EF","HI"))  #  A B E F H I
# print(list(itertools.chain(154,256,765)))  #  int object is not iterable
# print(list(itertools.chain((1,4,5), (3,4,6), (1,5,3))))  #  [1, 4, 5, 3, 4, 6, 1, 5, 3]


# 3. compress(data, selectors) - Return only those element of data whic has value of True(1)
# print(*itertools.compress("ABCDEFG", [1, 0, 0, 1, 1, 0, 1]))  #  A D E G
# print(*itertools.compress([[1,2], [3,4], [5,6], [7,8]], [1, 0, 1, 1]))  #  [1, 2] [5, 6] [7, 8]

# 4. dropwhile(func, iterable) - Return all elements when one statement is false.
# print(*itertools.dropwhile(lambda x: x<5, [1,4,6,4,1]))  #  6 4 1


# 5. filterfalse(func, iterable) - Return all elements when the function(condition) is false.
# print(*itertools.filterfalse(lambda x : x % 2 == 0, range(10)))  #  1, 3, 5, 7, 9

# 6. grouprby(iterable, key = None) - Returns consecutive key and groups from iterable.
# for k,g in itertools.groupby("AAABBCCCCCDDDE"):
    # print(*g)  #  A A A\n B B\n C C C C C\n D D D\n E
    # print(k, end =" ")  # A B C D E

# a_list = [("Animal", "cat"), 
#           ("Animal", "dog"), 
#           ("Bird", "peacock"), 
#           ("Bird", "pigeon")]
  
  # an_iterator = itertools.groupby(a_list, lambda x : x[0])
# for key, group in an_iterator:
#     key_and_group = {key : list(group)}
#     print(key_and_group)


# 7. islice(iterable,start,stop[,step]) - Return selected elements from iterable
# print(list(itertools.islice("ABCDEFG",2)))  #  ['A', 'B']
# print(list(itertools.islice("ABCDEFG",2,6)))  #  ['C', 'D', 'E', 'F']
# print(list(itertools.islice("ABCDEFG",2,6,2)))  #  ['C', 'E']

# 8. starmap(func,iter)
# print(list(itertools.starmap(max,((2,4,6),(6,9,5), (7,5,8)))))  #  [6, 9, 8]

# 9. takewhile(func, iterable) - Opposite of dropwhile
# print(*itertools.takewhile(lambda x: x<5, [1,4,6,4,1]))  #  1 4

# 10. zip_longest(*iterables, fillvalue = None)
# print(*itertools.zip_longest("ABCDE","abcd"))  #  ('A', 'a') ('B', 'b') ('C', 'c') ('D', 'd') ('E', None)
# print(*itertools.zip_longest("ABCDE","abc", fillvalue= "#"))  #  ('A', 'a') ('B', 'b') ('C', 'c') ('D', '#') ('E', '#')






