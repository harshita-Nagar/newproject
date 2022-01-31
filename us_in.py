def get_handle():
    handle=input("Enter the Twitter user name:")
    return handle

h=get_handle()
length=len(h)
print("Your Twitter user name has",length,"character.")