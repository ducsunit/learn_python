# class User:
#     def __init__(self, name, password):
#         self.name = name #public
#         self._role = "user" #protected
#         self.__password = password #private

#     def check_password(self, pw):
#         return pw == self.__password
    
# user = User("An", "1234")

# print(user.name)
# print(user._role)
# print(user.__password) -> error

# getter and setter
class User:
    def __init__(self, name):
        self.name = name
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if(len(value) < 2):
            raise ValueError("Tên quá ngắn !")
        self._name = value
user = User("An")
print(user.name)

user.name = "Binh"
print(user.name)