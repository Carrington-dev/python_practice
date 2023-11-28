class HashTable:
    def __init__(self, capacity = 4):
        self.array = [None] * capacity
    
    # def hash(self, key):
    #     length = len(self.array)
    #     count = 0
    #     for i in key:
    #         count += ord(i)
    #     return count % length

    def hash(self, key):
        length = len(self.array)
        return hash(key) % length
    
    def add(self, key, value):
        index = self.hash(key)

        if self.array[index]  is not None:
             
             for item in self.array:
                if item[0] == key:
                    item[1] = value
                    break
                else:
                    self.array.append([key, value])
        else:
            self.array[index] = []
            self.array[index].append([key, value])
        
        if self.is_full():
            self.double()

    
    def get(self, key):
        index = self.hash(key)
        if self.array[index] is None:
            raise KeyError()
        else:
            for item in self.array[index]:
                if item[0] == key:
                    return item[1]
            
            raise KeyError()
    
    def is_full(self):
        items = 0

        for item in self.array:
            if item is not None:
                items += 1
        
        return items > len(self.array) / 2
    
    def double(self):
        ht2 = HashTable(capacity=len(self.array) * 2)
        
        for i in range(len(self.array)):
            if self.array[i] is None:
                continue

            for item in self.array[i]:
                item.add(item[0], item[1])
        
        self.array = ht2.array

    def __setitem__(self, key, value):
        self.add(key, value)
    

    def __getitem__(self, key):
        self.get(key)




ht = HashTable()
# Using __setitem__

print(ht.hash("foo"))
ht["foo"] = "bar"

# using __getitem__
val = ht["foo"]

print(val)


"""
# using __contains__
if "foo" in ht:
    print("Exist!")
    
# using __iter__
for kvp in ht:
    print(kvp)
"""
    

