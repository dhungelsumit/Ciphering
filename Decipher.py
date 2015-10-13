import string
def inputt():
    key1=input("Enter the key ")
    key1=int(key1)
    key1=26-key1    
    if key1<1 or key1>26:
        inputt()
    else:
        return key1
key1=int(inputt())        
text=input("Enter text to be deciphered ")
length=len(text)
temp=0
text1=""
tmstr="\0"
for i in range(0,length):
    ord1=ord(text[i])
    if ord1>=97 and ord1<=122:
        temp=ord1+key1
        if temp>122:
           ord2=temp-122
           ordf=96+ord2
        else:
            ordf=ord1+key1
            
    elif ord1>=65 and ord1<=90:
        temp=ord1+key1
        if temp>90:
            ord2=temp-90
            ordf=65+ord2
        else:
            ordf=ord1+key1
    else:
        ordf=ord1
    text1=text1+chr(ordf)

print("DeCiphered Text",text1)
