def emoji_converter(message):
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
    return output


message = input('enter:     ')
b = emoji_converter(message)
print(b)