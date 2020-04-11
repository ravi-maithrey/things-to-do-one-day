class example:
    name = "name"
    age = 18
    def __init__(self):
        print("No input given")
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("Values added")
    def disp():
        print(name, "/n", age)

ex = example()
ex.disp
ex = example("ravi", 19)
ex.disp