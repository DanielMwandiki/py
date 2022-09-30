#strings
from cgi import print_arguments


first_name = "John"
surname = "Doe"
print("My first name is {}. My family name is {}".format(first_name, surname))

#numbers
my_int = 50
sentence = "The total comes to: "

print(sentence + str(my_int))

#dictionary

user = {"family_name":"Mwandiki"}
#print (user)
#read content inside dict
#print (user["family_name"])
#update dict
user["family_name"] = "Nduati"
print (user)
#delete
del user["family_name"]
print (user)
user["family_name"] = "Doroniko"
print (user)

#list
fruit = ["apples", "oranges", "bananas"]
print (fruit)
print (len(fruit))
print (fruit[-1])
fruit.append("kiwi")
print (fruit)
fruit.insert(2, "passoin fruit")
print (fruit)
print (sorted(fruit))
print (fruit)
fruit.sort()
print (fruit)
fruit.reverse()
print (fruit)
del fruit[1]
print (fruit)
favourite_fruit = fruit.pop()
print (favourite_fruit)
fresh_fruit = fruit.pop(1)
print (fresh_fruit)
fruit.remove('bananas')
print (fruit)