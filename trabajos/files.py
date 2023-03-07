

with open('demo2.txt',mode='r+') as p:
    p.write("11111\n")
    p.write("2222\n")
    p.write("6666\n")
    p.write("3333\n")
    p.write("88888\n")
    line=p.readline()
    while line:
      print(line)
      line=p.readline()

print('----------------------Finito----------------------')


#f=open('demo.txt',mode='r')
#f.write('Holita desde los pytones')
#f.write("conteindoplu  ")
#file_content=f.read()
#print(file_content)
#linia=f.readline()
#while linia:
 #   print(linia)
  #  linia=f.readline()
#f.close()