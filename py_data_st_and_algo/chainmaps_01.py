from collections import ChainMap

my_first_dic = {
    "Jan": 1,
    "Feb": 2,
    "Mar": 3,
    "Apr": 4,
    "May": 5,
    "Jun": 6
}
my_first_dic = { k:v for v,k in my_first_dic.items()}

list_sec_half = ["Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
list_seco_half = [ 7, 8, 9, 10, 11, 12]

my_second_dic = dict(zip(list_sec_half, list_seco_half))
my_second_dic = { k:v for v,k in my_second_dic.items()}


my_year = ChainMap(my_first_dic, my_second_dic)
print(my_year)
print(my_year[6])
print( True if  "May" in my_year else False)