class Student:

    def __str__(self):
        return f'{self.full_name} is {self.age} years old, and is in Cohort {self.cohort}'

    @property
    def first_name(self):
        try:
            return self.__first_name
        except AttributeError:
            return ""
    @property
    def last_name(self):
        try:
            return self.__last_name
        except AttributeError:
            return ""
    @property
    def age(self):
        try:
            return self.__age
        except AttributeError:
            return 0
    @property
    def cohort(self):
        try:
            return self.__cohort
        except AttributeError:
            return 0
    @property
    def full_name(self):
        try:
            return f"{self.__first_name} {self.__last_name}"
        except AttributeError:
            return ""

    @first_name.setter
    def first_name(self, name):
        if type(name) is str:
            self.__first_name = name
        else:
            raise TypeError('Value must be a string')
    @last_name.setter
    def last_name(self, name):
        if type(name) is str:
            self.__last_name = name
        else:
            raise TypeError('Value must be a string')
    @age.setter
    def age(self, age):
        if type(age) is int:
            self.__age = age
        else:
            raise TypeError('Value must be an integer')
    @cohort.setter
    def cohort(self, cohort):
        if type(cohort) is int:
            self.__cohort = cohort
        else:
            raise TypeError('Value must be an integer')

patty = Student()
patty.first_name = "Patty"
patty.last_name = "Mayonnaise"
patty.age = 14
patty.cohort = 45

# Read-only value, can't reset. Throws AttributeError
# patty.full_name = "Patty Mustard"

doug = Student()
doug.first_name = "Doug"
doug.last_name = "Funnie"
doug.age = 15
doug.cohort = 46

print(patty)
print(doug)

