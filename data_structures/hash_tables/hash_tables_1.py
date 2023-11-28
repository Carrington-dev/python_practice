def get_hash(key):
    h = 0
    
    for char in key:
        h += ord(char)

    print ( h % 100 )
        
    return h % 100


get_hash("mum 1")
get_hash("mum 2")
get_hash("mum 3")
get_hash("mum 5")
get_hash("1 mum")


context = {

"mum 1": 1,
"mum 2": 2,
"mum 3": 3,
"mum 4": 4,
"mum 5": 5,
"1 mum": 6,

}


print(context["1 mum"])
