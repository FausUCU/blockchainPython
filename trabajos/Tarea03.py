# Creat a list of "person" dictionaries whit a name, age and List of hobbies for each person. Fill in any data you want

person1={'name':'Bob','age':21,'hobbies':['TV','cooking','football']}
person2={'name':'Sam','age':35,'hobbies':['domino','woodworking']}
person3={'name':'Bill','age':101,'hobbies':['TV']}
person4={'name':'Martha','age':42,'hobbies':['Wrestling','Magic: the gathering']}
person5={'name':'Stuart','age':19,'hobbies':['cooking','painting']}

persons=[person1,person2,person3,person4,person5]

#Use List comprehension to convert the lis of persons in a lis of names

persons_name=[p['name'] for p in persons]

#print(persons_name)

#Use a list comprehension to check whether all persons are older than 20

all_more_that_20=all(p['age']>20 for p in persons)

print(all_more_that_20)

#Copy the person list such that you can safely edit the name of the first person (without changing the original list).


new_persons=[p.copy() for p in persons]
print(new_persons[0])
print(persons[0])
print("======="*20)
person_new={'name':'Robert','age':33,'hobbies':['TV','cooking','football','Dancing']}
new_persons[0]=person_new
print(new_persons[0])
print(persons[0])

#5) Unpack the persons of the original list into different variables and output these variables.

person_a, person_b, person_c, person_d, person_e = persons

print(person_a)
print(person_b)
print(person_c)
print(person_d)
print(person_e)