message = input(">")


emoji = {
    ":)" : "😊",
    ":(" : "😞",
    ":D" : "😃",
    ":O" : "😮",
    ":P" : "😜",
    ":|" : "😐"}



words = message.split(" ")

output = ""

for word in words:
    output += emoji.get(word, word) + " "

print(output)
