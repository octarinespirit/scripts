#Given the below class:
class Cat:
    laji = 'kissa'
    def __init__(self, nimi, ika):
        self.ika = nimi
        self.ika = ika


# 1 Instantiate the Cat object with 3 cats
kisu1 = Cat('Viiru', 11)
kisu2 = Cat('Miuku', 14)
kisu3 = Cat('Pullero', 18)

# 2 Create a function that finds the oldest cat
def vanhin(*cats):
    vanhin = max(kisu1.ika, kisu2.ika, kisu3.ika)
    return vanhin


# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2

print(f"Vanhin kissa on {vanhin(kisu1.ika, kisu2.ika, kisu3.ika)} vuotta vanha.")