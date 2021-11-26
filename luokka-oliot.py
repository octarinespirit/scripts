class Oppilas:
    def __init__(self, nimi, pisteet):
        self.name = nimi
        self.pisteet = pisteet

    def keskiarvo(self):
        return sum(self.pisteet) / len(self.pisteet)

oppilas1 = Oppilas('Joonas Symbio', [70, 88, 90, 99])
oppilas2= Oppilas('Pertti Toukolainen', [50, 85, 90, 60])

print(oppilas1.pisteet)
print(oppilas1.keskiarvo())