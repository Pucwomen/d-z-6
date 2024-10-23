my_dict={"lena":1990,"vasya":1980,"gena":1987}
print(my_dict)
print(my_dict.get("lena"))
print(my_dict.get("yna"))
my_dict.update({"max":1983,"alex":1965})
print(my_dict)
print(my_dict.pop("lena"))
print(my_dict)

my_set={2.0,"bye",(1,2,3)}
print(my_set)
my_set.update([4,8])
print(my_set)
my_set.remove(4)
print(my_set)