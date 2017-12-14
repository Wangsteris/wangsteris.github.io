acc=0
x=int(input('Please enter in a number to go to:   '))
def rec(n):
    if n==1:
        return 1
        print ('+')
    else:
        return rec(n-1)*3

for i in range (1,x):
    acc=acc+rec(i)
    if i <= 1:
        print(rec(i))
    elif i >1 and i <x-1:
        print ('+')
        print (rec(i))
    else:
        print ('=')
        print (acc)
    

