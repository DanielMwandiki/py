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