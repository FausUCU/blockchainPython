#1) Write a normal function that accepts another function as an argument. Output the result of that other function in your “normal” function.
def normal_function(function,args):
    other=function(args)
    print(other)
def first_arg(a):
    return a*3
def second_arg(b):
    return b+b+b+b+b+b
normal_function(first_arg,12)
normal_function(second_arg,33)

#2) Call your “normal” function by passing a lambda function – which performs any operation of your choice – as an argument.

lambda_fun=lambda el:el+13
normal_function(lambda_fun,6)

print("="*40)

#3) Tweak your normal function by allowing an infinite amount of arguments on which your lambda function will be executed.     

def normal_function_tweak(function,*args):
    
    total=map(function,*args)
    print (list(total))

lots=[1,2,3,4,5,6]
normal_function_tweak(lambda_fun,lots)


#4) Format the output of your “normal” function such that numbers look nice and are centered in a 20 character column.

def normal_function_tweak_nice(function,*args):
    
    total=map(function,*args)
    total_list=list(total)
    for a in total_list:
        print('{:20}'.format(a))
        
normal_function_tweak_nice(lambda_fun,lots)

