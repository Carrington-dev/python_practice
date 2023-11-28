class HashMap:
    def __init__(self, capacity = 4):
        self.capacity = capacity
        self.array = [ None for i in range(self.capacity)]
    

    def get_hash(self, key):
        k = 0
        for char in key:
            k += ord(char)
        
        return k % len(self.array)
    

    def __setitem__(self, key, value):
        index = self.get_hash(key)
        self.array[index] = value

        if self.is_full():
            self.double()

    
    def __getitem__(self, key):
        index = self.get_hash(key)
        #return self.array[index]
        for item in self.array[index]:
            if item[0] == key:
                return item[1]

    def __delitem__(self, key):
        index = self.get_hash(key)
        #self.array[index] = None
        for child_index, item in enumerate(self.array[index]):
            if item[0] == key:
                del self.array[index][child_index]
                
    
    def is_full(self):
        length = len(self.array)
        filled_items = 0

        for item in self.array:
            if item is not None:
                filled_items += 1

        print(filled_items)
        
        return (length  / 2) > filled_items
    
    def double(self):
        hm = HashMap(capacity=(len(self.array))*2)

        for i in range(len(self.array)):
            hm.array[i] = self.array[i]
        
        self.array = hm.array



    
context = HashMap()

context['my_name'] = "Carrington"
context["surname"] = "Muleya"
context["area"] = "Tshapfutshe"
context["aera"] = "Lutumba"

print(context.array)
print(context.is_full())

my_list = [ 0 for i in range(200)]



print(context.array)
print(context.is_full())