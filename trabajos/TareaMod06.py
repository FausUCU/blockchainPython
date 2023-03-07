#1) Import the random function and generate both a random number between 0 and 1 as well as a random number between 1 and 10.
import random
rand01=random.randrange(0,2) #randrange selects a random numbers betwen the 2 numbers selected but allways less that the second one
rand02=random.randrange(1,11)
#print(rand01)
#print(rand02)
#2) Use the datetime library together with the random number to generate a random, unique value.
import datetime
current_time=datetime.datetime.utcnow() #i get the current time mm-yy-dd, Houre-minute-second-milisend in datime format
time_string=str(current_time) #convewrt the previus date in a string
timeMili=int(time_string[-5:-1]) #i select the milisecons as an int
randomFin=random.randrange(timeMili) #i use the milisecond as a range for am random selection
print(randomFin)




