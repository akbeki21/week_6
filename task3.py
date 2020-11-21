# Task 1

# class ContactList(list):

#     def search_by_name(self, name):
#         self.name = name
#         some_list = []
#         for n in self:
#             if n == name:
#                 some_list.append(n)
#             else:
#                 continue
#             return some_list


# all_contacts = ContactList(['Beki', 'Elima', 'Bema'])

# a = all_contacts.search_by_name('Bema')
# print(a)




# Task 2

# class User:

#     name = 'Lily'
#     lastname = 'Swan'
#     age = '26'
    

#     def describe_user(self):
#         self.name 
#         self.lastname 
#         self.age 
#         print(f"Hello, let's meet {self.name} {self.lastname}. She is {self.age} years old")

#     def greet_user(self):
#         print(f"Hello, {self.name}. Nice to meeet you!")


# class Admin(User):
#     privileges = ["разрешено добавлять сообщения", "разрешено удалять пользователей", "разрешено банить пользователей"]

#     def show_privileges(self):
#         self.privileges
#         print(self.privileges)


# test = User()
# test.describe_user()
# test.greet_user()
# admin = Admin()
# admin.show_privileges()
# admin.first_name = 'Admin'
# admin.describe_user()
# admin.greet_user()



# Task 3

# class House:
#     type_ = 'Летний домик'
#     house_area = 30
#     remaining_area = 0
#     furniture = {"кровать": 5, "шкаф": 2, "стол": 1, "стулья": 5}

#     area = 0
#     for a in furniture.values():
#         area += a
        
#     remaining_area = house_area - area

#     def about_house(self):
#         print(f"Тип : {self.type_}")
#         print(f"Площадь дома равна: {self.house_area} км2.")
#         print(f"Свободная площадь равна: {self.remaining_area} км2.")
#         print(f"Список мебели в доме: {self.furniture}.")
    

# house = House()
# house.about_house()





