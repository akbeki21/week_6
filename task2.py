# Task 1 

# class Student:
#     def __init__(self, name, lastname, department, year_of_entrance):
#         self.n = name
#         self.l = lastname
#         self.d = department
#         self.y = year_of_entrance


#     def get_student_info(self):
#         print(f'{self.n} {self.l} поступил в {self.y} году на факультет: {self.d}.')

    
# info = Student(name = 'Ваня', lastname = 'Иванов', year_of_entrance = 2018, department = 'Программирование')
# info.get_student_info()



# Task 2

# class BankAccount:
    
#     def __init__(self):
#         self.balance = 150

#     def withdraw(self, amount):
#         amount = int(input("How much you want to withdraw : "))
#         if self.balance > amount:
#             print(f'Your current balance is {self.balance - amount}')

#         else:
#             print("You don't have enough money")



#     def deposit(self, amount):
#         amount = int(input("How much you want to deposit : "))
#         print(f'Your current balance is {self.balance + amount}')


# account = BankAccount()
# account.deposit(int)


# Task 3

# class Airplane:
#     def __init__(self, mark, model, year, max_speed):
#         self.mark = mark
#         self.model = model
#         self.year = year
#         self.max_speed = 0
#         self.odometer = 0
#         self.is_flying = False


#     def take_off(self):
#         self.is_flying = True
#         about_off = f"{self.mark} {self.model} was take off."
#         return about_off

#     def fly(self, km):
#         self.odometer += km
#         about_to_fly = f"{self.mark} flew {self.odometer}km during the flying {self.max_speed} km/h."
#         return about_to_fly

#     def land(self):
#             self.is_flying = False
#             about_land = f"{self.mark} landed, the odometer shows {self.odometer}km."
#             return about_land

# start = Airplane("Turkish Airlines","342-545","1995",675)
# print(start.take_off())
# print(start.fly(100))
# print(start.land())