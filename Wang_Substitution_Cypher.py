string = 'abcdefghijklmnopqrstuvwxyz'

for i in string:
    if i == 'a' or i == 'A':
        i='&'
        print (i)
    elif i=='e' or i=='E':
        i='@'
        print (i)
    elif i=='i' or i =='I':
        i='$'
        print (i)
    elif i=='o' or i =='O':
        i='%'
        print (i)
    elif i=='u' or i =='U':
        i='^'
        print (i)
    else:
        print (i)
