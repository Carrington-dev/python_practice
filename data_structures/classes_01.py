import os
import hashlib


class WriteCoordinateError(Exception):
    pass


class Person:
    def __init__(self, name, personality, age, password=None, robot=None):
        self.name = name
        self.personality = personality
        self.age = age
        self.password = password
        
        self.robot = robot

    @property
    def password(self):
        raise AttributeError("Password is write-only")

    @password.setter
    def password(self, plaintext):
        salt = os.urandom(32)
        self._hashed_password = hashlib.pbkdf2_hmac(
            "sha256", plaintext.encode("utf-8"), salt, 100_000
        )

    def introduceSelf(self):
        if self.robot != None:
             print(f"""My name is {self.name}.
                   \nI think I am {self.personality}.
                   \nI am {self.age} years old.
                   \nMy robot is {self.robot.name}.
                   \nHe is {self.robot.age} years old.
                   \nHe is {self.robot.color} in color.""")
        else:
            print(f"""My name is {self.name}.
                   \nI think I am {self.personality}.
                   \nI am {self.age} years old.""")

            
    def incrementAge(self):
        self.age += 1
        return self.age

    def decrementAge(self):
        #raise WriteCoordinateError("Can not decrease the person's age!")
        #self.age -= 1
        #return self.age
        pass
    

class Robot:
    def __init__(self, name, color, age):
        self.name = name
        self.color = color
        self.age = age

    def incrementAge(self):
        self.age += 1
        return self.age

    def decrementAge(self):
        self.age -= 1

r1 = Robot("Robogon", "silver", 2)
p1 = Person(name="Carrington", personality= "very quiet",age = 25, password = "wereffd", robot=r1)

#print(p1.password("wwrrrrrr"))
p1._hashed_password
p1.introduceSelf()
r1.incrementAge()
p1.incrementAge()
p1.incrementAge()
p1.decrementAge()
p1.incrementAge()
p1.incrementAge()



