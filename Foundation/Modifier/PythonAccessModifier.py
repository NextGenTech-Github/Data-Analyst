class Student:
    FirstName = 'John'
    LastName = 'Doe'
    _BirthDate = '01.01.1970'
    __age = 0
    __schoolName = 'XYZ School' # private class attribute

    def __init__(self, firstname, lastname,birthdate,age):
        self.FirstName = firstname  # public instance attribute
        self.LastName = lastname # public instance attribute
        self._BirthDate = birthdate # public instance attribute
        self.__age = age # public instance attribute
        self__schoolName = 'XYZ School' # private class attribute
        self.__salary=age # private instance attribute

    def __display(self):  # private method
	    print('This is private method.')

std = Student("Lalit","Sharma","01.01.1972","50")
print(std.FirstName,std.LastName)
print(std._BirthDate)

# print(std.__schoolName) #AttributeError
# print(std.__display())  #AttributeError