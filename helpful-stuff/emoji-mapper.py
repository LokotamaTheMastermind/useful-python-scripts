emojis = {
    "happy": [
        "😀",
        "😁",
        "😂",
        "🤣",
        "😃",
        "😄",
        "😅",
        "😆",
        "😉",
        "😊",
        "😋",
        "😎",
        "🙂",
        "🙃",
        "🤓",
        "😝",
        "😜",
    ]
}

print(type(emojis))

print("")
question = input("What emoji are you looking for? |> ")
print("")

if question != "":
    emoji = emojis.get(question, "Sorry couldn't find emoji, please reference EMOJIS.md ...")
    if type(emojis) == "dict":
        for emoji in emojis:
            print(f"The results of the emoji search are -> {emoji}")
else:
    print("Sorry the is no emoji with a blank space ...")
