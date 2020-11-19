import time 
from datetime import datetime
from functools import wraps


# Task 1
# def main(func):
#     def wrapper():
#         now = datetime.now()
#         if now.hour > 9 and now.hour < 21:
#             func()
#         else:
#             print("You are too noisy!")      
#     return wrapper


# @main
# def say_whee():
#     a = "Wheee!"
#     print(a)

# say_whee()



# Task 2
# def timer(func):
#     def wrapper():
#         start = datetime.now()
#         result = func()
#         print(datetime.now() - start)
#         return result
#     return wrapper



# @timer
# def isdigit():
#     digit = input("Enter any number: ")
#     digit = int(digit)

#     if digit %2 ==0:
#         print("This number is even")
#     else:
#         print("This number is odd")
    

# print(isdigit())



# Task 3
# def repeat(num_times):
#     def repeat_func(func):
#         def wrapper(*args, **kwargs):
#             for _ in range(num_times):
#                 value = func(*args, **kwargs)
            
#         return wrapper
#     return repeat_func


# @repeat(num_times=5)
# def function(name):
#     print(f"{name}")

# function('Python')




# Task 4
# dict_ = {"amorremia": 23456, "akbeki": 21050, "chudoy_": 67859}

# def users(function):
#     def wrapper(username, password):
#         global dict_
#         for key, value in dict_.items():
#             if key == username and value == password:
#                 function(username, password)
                
#             elif key != username and value == password:
#                 raise Exception('Username is not defined!!!!')
                
#             elif key == username and value != password:
#                 raise Exception('Password is not defined!!!!')
                
            
#     return wrapper


# @users
# def login(username, password):
#     print(f'Wellcome, {username}')

# login('akbeki', 21050)



# Task 5
# def decoration(func):
#     def wrapper(a, b=1, *args, **kwargs):
#         print("Calling testFunc (", args, kwargs, ')')
#         print('argument a:', a)
#         print('argument b:', b)
#         print('argument args:', args)
#         print('argument kwargs:', kwargs)
        
        
#         print('Finished testFunc', func(a, b, *args, **kwargs))
#     return wrapper

# @decoration
# def testFunc(a, b=1, *args, **kwargs):
#     return a + b
    
# testFunc(2, 3, 4, 5, c=6, d=7)    
# print()
# testFunc(2, c=5, d=6) 
# print()
# testFunc(10)