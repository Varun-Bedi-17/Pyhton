class HashTable():
    def __init__(self, max_size):
        self.data_list = [None] * max_size

    def hashMap(self, a_string):
        number = 0
        for a_char in a_string:
            number += ord(a_char)
        result = number % len(self.data_list)
        return result

    def insert(self, key, value):
        index = self.hashMap(key)
        self.data_list[index] = (key,value)

    def find(self, key):
        index = self.hashMap(key)
        kv = self.data_list[index]
        if kv is None:
            return None    
        k, val = kv
        return val

    def update(self, key, value):
        index = self.hashMap(key)
        self.data_list[index] = (key, value)

    def list_all(self):
        return [kv[0] for kv in self.data_list if kv is not None]




hash = HashTable(4096)
# print(len(hash.data_list))
# print(hash.data_list[99])

# print(hash.hashMap(""))
# print(hash.hashMap("Aakash"))
# print(hash.hashMap("Don O Leary"))


hash.insert("Aakash", 99999967543)
hash.insert("Hemanth", 8756789432)
print(hash.find("Aakash"))

hash.update("Hemanth", 7564325686)
hash.update("Jagdish", 6754987654)          # If value is not present it insert key,value in list(data_list)

print(hash.list_all())


# thars why we need linear probing..

hash.insert("listen", 200)
hash.insert("silent", 90)

print(hash.find("listen"))
print(hash.find("silent"))

print(hash.hashMap("listen"))
print(hash.hashMap("silent"))