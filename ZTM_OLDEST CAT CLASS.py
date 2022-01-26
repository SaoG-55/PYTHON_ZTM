# Given the below class:
class Cat:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age
    @staticmethod
    def oldest(*args):
        # 2 method that finds the oldest cat
        return max(args) 



# 1 Instantiate the Cat object with 3 cats
cat1 = Cat('jimmy', 2)
cat2 = Cat('jerry', 3)
cat3 = Cat('jimjam',1)

print(f"1st cat is {cat1.name} and age is {cat1.age} ")
print(f"2nd cat is {cat2.name} and age is {cat2.age} ")
print(f"3rd cat is {cat3.name} and age is {cat3.age} ")

#  "The oldest cat is x years old.".  #
print(f"the oldest cat among the lot is {Cat.oldest(cat1.age,cat2.age,cat3.age)} years old")
