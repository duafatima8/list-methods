student = {
    "name" : "dua",
    "age" : 16,
    "grade" : "A"
}

student["age"] = "18"
student["city"] = "khi"
print(student.keys())
print(student.values())
print(student.items())


numbers = ["1" ,"2" ,"3","4","5","6"]
print(numbers)
numbers.append("7")
numbers.insert(0,"zero")
print(numbers)


names = ["dua","ali","zara","haram","zaviyar","zoya"]
print(names)
names.remove("ali")
print(names)
names.pop(3)
print(names)
names.clear()
print(names)



digits =[3,34,0,96,45,8,865,7,]
print(digits)
digits.sort()
print(digits)
digits.sort(reverse=True)
print(digits)
digits.reverse()
print(digits)

a = [1 , 3 ,4,7,9,5]
print(a)
b = a.copy()
b.append(34)
print(b)
c = a.copy()
c.pop(3)
print(c)



last = [2,4,6,2,8,2,10,2,13,2]
print(last.count(2))
print(last.index(6))