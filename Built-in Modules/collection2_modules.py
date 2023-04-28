import collections

# 1. Defaultdict(default) - It is used to provide some default values for the key that does not exist and never raises a KeyError.
dic = collections.defaultdict(lambda:"not")
dic["name"] = "Varun"
dic["age"] = 17
# print(dic)  #  defaultdict(None, {'name': 'Varun', 'age': 17})
# print(dic["dob"])  # not

# print(dic.__missing__("name"))  #  not

# d = collections.defaultdict(list)  #  defaultdict is created with values that are list.
# d["name"] = "abc"
# d["age"] = 17,87
# print(d)  #  defaultdict(<class 'list'>, {'name': 'abc', 'age': (17, 87)})
# print(d["dob"])  #  []

# s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
# d = collections.defaultdict(list)
# for k, v in s:
#     d[k].append(v)
# print(d)  #  defaultdict(<class 'list'>, {'yellow': [1, 3], 'blue': [2, 4], 'red': [1]})

# s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
# d = collections.defaultdict(int)
# for k, v in s:
#     d[k].append(v)
# print(d)  #  int has no attribute append

# s = 'mississippi'
# d = collections.defaultdict(int)
# for k in s:
#     d[k] += 1

# print(d)  #  defaultdict(<class 'int'>, {'m': 1, 'i': 4, 's': 4, 'p': 2})


# 2. Ordereddict([items]) - It remembers the order in whic kry is created
d = collections.OrderedDict()
d["a"] = 1
d["b"] = 2
d["c"] = 3
# print(d)  #  OrderedDict([('a', 1), ('b', 2), ('c', 3)])

# d["b"] = 6
# print(d)  #  OrderedDict([('a', 1), ('b', 6), ('c', 3)])  Position of key remains unchanged

# d.pop("b")
# print(d)
# d["b"] =2
# print(d)  #  OrderedDict([('a', 1), ('c', 3), ('b', 2)])  create key at the last.

# d.popitem(last=False)  #  remove first element if last is false.
# print(d)  #  OrderedDict([('b', 2), ('c', 3)])

# d.move_to_end("b",last= True)  # move to first if last if false.
# print(d)  #  OrderedDict([('a', 1), ('c', 3), ('b', 2)])



# 3. UserDict() - This container is used when someone wants to create their own dictionary with some modified or new functionality.. Similar for userlist and userstring.
# class MyDict(collections.UserDict): 
        
#     # Function to stop deletion 
#     # from dictionary 
#     def __del__(self): 
#         raise RuntimeError("Deletion not allowed") 
            
#     # Function to stop pop from  
#     # dictionary 
#     def pop(self, s = None): 
#         raise RuntimeError("Deletion not allowed") 
            
#     # Function to stop popitem  
#     # from Dictionary 
#     def popitem(self, s = None): 
#         raise RuntimeError("Deletion not allowed") 
        
# # Driver's code 
# d = MyDict({'a':1, 
#     'b': 2, 
#     'c': 3})
    
# d.pop(1)