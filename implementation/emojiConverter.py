emoji = {
    ":)" : "😊",
    ":(" : "😞",
    ":D" : "😃",
    ":O" : "😮",
    ":P" : "😜",
    ":|" : "😐"}


message = input(">")

words = message.split(" ")

output = ""

for word in words:
    output += emoji.get(word, word) + " "

print(output)
