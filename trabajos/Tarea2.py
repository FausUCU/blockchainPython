namesTest=["bob","damian","tito","roberspier","bill"]

# Assigment 1
def len_of_names(names):
    for i in names:
        print(len(i))

# Assigment 2
def len_of_names5(names):
    for i in names:
        if len(i)>5:
            print(len(i))

# Assigment 3
def len_of_names_5_n(names):
    for i in names:
        if len(i)>5 and ("n" in i or "N" in i):
            print(i)

# Assigment 4

def len_of_names_empty(names):
    while len(names)!=0:
        n=names.pop(0)
        if len(n)>5 and ("n" in n or "N" in n):
            print(n)

#test 1
len_of_names(namesTest)
#test 2
len_of_names5(namesTest)
#test 3
len_of_names_5_n(namesTest)
#test 4
len_of_names_empty(namesTest)