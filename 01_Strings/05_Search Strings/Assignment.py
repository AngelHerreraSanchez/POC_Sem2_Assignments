text= input("Enter some text: ")

result = text.find("the")

if result == -1:
    print("the word is not in the string")
else:
    print("The word the is in the string")

print(text.find('the'))