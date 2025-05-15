#Boolean  true =1 ,False = 0

print(10<11)

#a = 10

#a+=1 (a=a+1)

#a == 10

#a !=10 

print(10<9)

print(10==9)


#Arithmetic => +,-,/,%,*

#Assignment => =,+= ,-=,/= ,%= (z+=1  , z=z+1)

#Comparison => == != < > <= >= (10<12) 

#Logical  =>  and or not (1200<1300) and (4000<5000)

#BitWise => & , | , ~

#List

Number = [1,2,3,4.5,True,"surya"]
#findIndex
print(Number[1])
#NegativeIntex
print(Number[-1])
#Range
print(Number[1:5])
#EndRange
print(Number[:4])
#StartRange
print(Number[2:])

#Negativerange
print(Number[-3:-1])


#findValue

if "surya" in Number:
    print("yes surya Here")


#ChangeListValue

Number[1]="Erode"
print(Number)

#ChangeRange Value

Number[0:3]=["One","two","Three"]
print(Number)

#InserData
Number.insert(2,"KiA")
print(Number)

#Append

Number.append("green")
#print(Number)

#Extend
Arr=["BMW","KIA","AUDI"]

Number.extend(Arr)
print(Number)

#Remove
Number.remove("KIA")
print(Number)


#Pop(index)

Number.pop(3)
print(Number)

#delete

del Number[5]
print(Number)


#Clear
Number.clear()
print(Number)
