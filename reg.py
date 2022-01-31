import re
# txt="the city is beautiful."
# x=re.search("^the.*beautiful$", txt)
# if x:
#     print("yes, there is a match")
# else:
#     print("don't have any match")

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
 if x:
        5print("YES! We have a match!")
    else:
        print("No match")
