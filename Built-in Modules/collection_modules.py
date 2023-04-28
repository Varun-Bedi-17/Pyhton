import collections

#  1. Chainmap(*dict) - Used to combine many dictionaries into one unit
# d1 = {"a" : 1, "b" : 2}
# d2 = {"c" : 3, "d" : 4}
# d3 = {"e" : 5, "f" : 6}
# c = collections.ChainMap(d1,d2)
# print(c)  #  ChainMap({'a': 1, 'b': 2}, {'c': 3, 'd': 4})
# print(c.maps)  #  [{'a': 1, 'b': 2}, {'c': 3, 'd': 4}]
# print(c.keys())  #  KeysView(ChainMap({'a': 1, 'b': 2}, {'c': 3, 'd': 4}))
# print(list(c.keys()))  #  ['c', 'd', 'a', 'b']
# print(list(c.values()))  #  [3, 4, 1, 2]

# c1 = c.new_child(d3)
# print(c1.maps)  #  [{'e': 5, 'f': 6}, {'a': 1, 'b': 2}, {'c': 3, 'd': 4}]
# print(*reversed(c1.maps)) #  {'c': 3, 'd': 4} {'a': 1, 'b': 2} {'e': 5, 'f': 6}



# 2. Counter()  -  
# print(collections.Counter(['a', 'a', 'b', 'b', 'b','b', 'a', 'c', 'c']))  #  Counter({'b': 4, 'a': 3, 'c': 2})
# print(collections.Counter(('a', 'a', 'b', 'b', 'b','b', 'a', 'c', 'c')))  #  Counter({'b': 4, 'a': 3, 'c': 2})
# print(collections.Counter({"a" : 4, "b" : 5, "c" : 2}))  #  Counter({'b': 5, 'a': 4, 'c': 2})
# print(collections.Counter("AABBCCCDDDAAABB"))  #  Counter({'A': 5, 'B': 4, 'C': 3, 'D': 3})
# print(collections.Counter(a = 4, b = 5, c = 2))  #  Counter({'b': 5, 'a': 4, 'c': 2})


# c1 = collections.Counter([1,1,1,2,2,2,2,2,3,3,4])
# c2 = collections.Counter([1,1,2,2,2,2,3,4,4,4,4])
# print(*c1.elements())  #  1 1 1 2 2 2 2 2 3 3 4

# print(c1.most_common(2))  # Prints 2 most common elements in c1   [(2, 5), (1, 3)]

# c1.subtract(c2)  # subtract c1 from c2
# print(c1)  #  Counter({1: 1, 2: 1, 3: 1, 4: -3})

# print(c1.total(), c2.total())  #  11 11

# c1.update([1,1,1,1,4,4])  # Update existing
# print(c1)  #  Counter({1: 7, 2: 5, 4: 3, 3: 2}



# 3. deque(list,[max_len]) - Make list as deque
# print(collections.deque("AAVGT"))  #  deque(['A', 'A', 'V', 'G', 'T'])
# print(collections.deque(["avd", "cdf", "lkj"])) #  deque(['avd', 'cdf', 'lkj'])
# print(collections.deque((1,2,5,3,6,7)))  #  deque([1, 2, 5, 3, 6, 7])

d = collections.deque([22, 22, 33, 76, 565, 38, 87])
# d.append(33)
# print(d)  #  deque([22, 33, 76, 565, 38, 87, 33])

# d.appendleft(87)
# print(d)  #  deque([87, 22, 33, 76, 565, 38, 87])

# d.pop()
# print(d)  #  deque([22, 33, 76, 565, 38])

# d.popleft()
# print(d)  #  deque([33, 76, 565, 38])

# print(d.count(22))  #  2

# d.extend([54,67])
# print(d)  #  deque([22, 22, 33, 76, 565, 38, 87, 54, 67])

# d.extendleft([45,76,98])
# print(d)  #  deque([98, 76, 45, 22, 22, 33, 76, 565, 38, 87])

# d.insert(3,4)  # insert 4 at 3 position
# print(d)  #  deque([22, 22, 33, 4, 76, 565, 38, 87])

# d.index(i,[start,stop])
# d = collections.deque([22, 33, 76, 565, 38, 87])
# print(d.index(22))  #  0
# print(d.index(22,1,5))  #  1

# d.remove(22)  #  Removes first occurence of 22 and raise value error if not found
# print(d)  #  deque([22, 33, 76, 565, 38, 87])

# d.reverse()
# print(d)  #  deque([87, 38, 565, 76, 33, 22, 22])

# d.rotate()
# print(d)  #  deque([87, 22, 22, 33, 76, 565, 38])
# d.rotate(3)
# print(d)  #  deque([76, 565, 38, 87, 22, 22, 33])
# d.rotate(-1)
# print(d)  #  deque([565, 38, 87, 22, 22, 33, 76])

# d1 = d.copy()
# print(d1)  #  deque([22, 22, 33, 76, 565, 38, 87])

# d1.clear()
# print(d1)  #  deque([])



# 4. namedtuple(typename, field_names, *, rename=False, defaults=None, module=None)
s = collections.namedtuple('Student',"name, age, dob",defaults=["abc",2,1998])  #  s = collections.namedtuple('Student',[name, age, dob])  

s1 = s("Varun", 23, 2002)
# print(s1[1])  #  23
# print(s1.name)  #  Varun
# print(s1[1]+s1[2])  # 2025

# name,age,dob = s1
# print(name,age,dob)  #  Varun 23 2002

# s2 = "Raghav, 22, 2003"
# print(s._make(s2))  #  TypeError: Expected 3 arguments, got 16
# s2 = "Raghav", 22, 2003
# print(s._make(s2))  #  Student(name='Raghav', age=22, dob=2003)

# print(s1._asdict())  #  {'name': 'Varun', 'age': 23, 'dob': 2002}  To return ordered dict

# dic = {"name" : "Sarthak", "age": 25, "dob": 2000}
# print(s(**dic))  #  Student(name='Sarthak', age=25, dob=2000)  To return namedtuple from dictionary

# print(s1._fields)  #  ('name', 'age', 'dob')

# print(s1._replace(name = "Chuchu", age = 24))  #  Student(name='Chuchu', age=24, dob=2002)

# print(s1._field_defaults)  #  print(s1._field_defaults)

# s2 = s()
# print(s2)  #  Print eror missing arguments if default is not provided



