# Dictionary
ThisDis = {
    "NAME":"SURYA",
    "AGE":12,
    "CITY":"ERODE",
    "CITY":"CHENNAI",
    "COLOR": ["RED","BLUE","GREEN"]
    }

print(ThisDis)
print(ThisDis["NAME"])
print(len(ThisDis))

#DICTIONARY CONSTRUCTOR

Disct = dict(name="Rajini",Age=79)

#print(Disct)

#KEY = PROPERTY    VALUE = VALUE
x=ThisDis.keys()
print(x)

#Value
print(ThisDis.values())

#items
print(ThisDis.items())

#Change Value

ThisDis["CITY"]="NewYork"
print(ThisDis)

#Update
ThisDis.update({"NAME":"VIJAY"})
print(ThisDis)

#Add DATA
ThisDis["Year"]=1996
print(ThisDis)

#Add Data Form Update keyWord ;

ThisDis.update({"Model":1999})
print(ThisDis)





















