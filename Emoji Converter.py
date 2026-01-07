#Using dictionary

messageinput = input("> ")
#Good Morning :) split this into 3 part
message = messageinput.split(" ")
print(message)
emojis = {
    ":)": "😊",
    ":(": "😭"
}
output = ""
for word in message:
    output += emojis.get(word, word) + " "
print(output)