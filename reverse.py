a = 1234
rev = 0
while(a>0):
    rem = a%10
    rev = rev*10+rem
    a//=10
    
print(rev)
