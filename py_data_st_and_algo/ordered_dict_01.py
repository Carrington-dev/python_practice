import collections
od1= collections.OrderedDict()
od1['one'] = 1
od1['two'] = 2
od2 = collections.OrderedDict()
od2['two'] = 2
od2['one'] = 1
print(dict(od1), f"\n{dict(od2)}")
print(od1==od2)