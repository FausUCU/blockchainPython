namelist = ['Carol','Bob','Francis','Nathaniel']#list are made with "[]" not "()"

for name in namelist:
    for chr in name:
        if chr in ['n', 'N']:
            print ("The name "+ name +" has a character 'n' or 'N'")
        if len(name) > 5:
            print('The length of your name '+name+' is '+(str(len(name))))
        else:
            print ('Character in'+name+'is less than 5')

while namelist: #it will print the entire list each time
    print(namelist)
    namelist.pop()
"""
namelist = ('Carol','Bob','Francis','Nathaniel') #list are made with "[]" not "()"
#list are made with "[]" not "()"
for name in namelist:
    for chr in name:
        if chr in ('n', 'N'): #same as above
             #you are chequing each character in each word, it takes more work and if there's more that one "n" in the word it print it repeatedly
            print ("The name (name) has a character 'n' or 'N'")
            #to do a reference in printing, close the string add a "+" and the variable. ej print("words words"+name+"words")
    if len(name) > 5: #because your loop runs for each character of each word, each word is checked multiple times
        print ('The length of your name '(name)' is (len(name))')
        # the lent of names should be a string ej. str(len(name)))
    else:
    print ('Character in (name) is less than 5')
while namelist:
    print(namelist)
    namelist.pop()
"""