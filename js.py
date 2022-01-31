

book={}
book["Tom"]={'name':'tom','address':'1 red street','phone':672524}

book["Tonny"]={'name':'tonny','address':'2 street plaza','phone':898756}
import json
s=json.dumps(book)
print(s)
with open("c://flask practice//book.txt","w") as f:
    f.write(s)
