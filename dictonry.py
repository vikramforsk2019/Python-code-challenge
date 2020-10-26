test={}
test["A"]=[1,2,3]
tets["B"]=[3,4,5]

#///////

list(map(lambda x, y: x+y, test["A"], test["B"]))

list(map(lambda x, y: x+y, zip(test["A"], test["B"])))

map(lambda x: x+y, test["A"], test["B"])
list(map(lambda x: add(x, y), test["A"], test["B"]))