class Dog:
    # Class variable (shared by all instances)
    kind = 'canine' 

    def __init__(self, name):
        # Instance variable (unique to each instance)
        self.name = name


d = Dog('Fido')
e = Dog('Buddy')


print(f"{d.name} is a {d.kind}") 
print(f"{e.name} is a {e.kind}") 


print(f"Dog d's name: {d.name}") 
print(f"Dog e's name: {e.name}") 
