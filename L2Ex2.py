changeWordsStartingWitha = ["apple", "alligator", "armor", "fixtures"]

items = [word[0] for word in changeWordsStartingWitha]

for items in changeWordsStartingWitha:
    if items.startswith("a"):
        print(items+".Hello")
    else:
        break

print(items)
