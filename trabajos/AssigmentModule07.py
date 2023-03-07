#1) Write a short Python script which queries the user for input (infinite loop with exit possibility) and writes the input to a file.
# import libreries
import json
import pickle

#2) Add another option to your user interface: The user should be able to output the data stored in the file in the terminal.


#3) Store user input in a list (instead of directly adding it to the file) and write that list to the file – both with pickle and json.

file2j=open('mod0703.txt',mode='w')
file2p=open('mod0703.p',mode='wb')

data=[]
cont_loop=True
while cont_loop:
    inp=input('your word: ')
    data.append(inp)
    end=input('pres e to end or othe to conitnue: ')
    if end=='e':
        cont_loop=False

for d in data:
    file2j.write(d)
for e in data:
    file2p.write(pickle.dumps(e))
file2j.close()
file2p.close()


#4) Adjust the logic to load the file content to work with pickled/ json data.