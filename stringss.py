Text="gmail@com"
l=len(Text)
ntext=""
for i in range(0,l):
    if Text[i].isupper():
        ntext=ntext+Text[i].lower()
    elif Text[i].isalpha():
        ntext = ntext +Text[i].upper()
    else:
        ntext= ntext + 'bb'
print(ntext)
