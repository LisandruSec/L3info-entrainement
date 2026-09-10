# Conversion d’unités 
# Ecrire une fonction qui réalise une conversion d’unité de masse, 
# en prenant en entrée la valeur et l’unité de départ ainsi que l’unité d’arrivée, et retourne la valeur convertie. 
# Exemple : conversion_masse(45, “kg”, “g”) devra retourner 45000.

unite_masse = {"t": 1, "q": 2, "10kg": 3, "kg": 4, "hg": 5, "dag": 6, "g": 7, "dg": 8, "cg": 9, "mg": 10} # modification 2

def conversion_masse(valeurD: float, unitéD: str, unitéA: str) -> float:
    valeurA = valeurD
    if unite_masse.get(unitéD) > unite_masse.get(unitéA):
        valeurA = valeurD / (10 ** (unite_masse.get(unitéD)-unite_masse.get(unitéA)))
    elif unite_masse.get(unitéD) < unite_masse.get(unitéA):
        valeurA = valeurD * (10 ** (unite_masse.get(unitéA)-unite_masse.get(unitéD)))
    return valeurA

print(conversion_masse(4500, "g", "kg"))
print(conversion_masse(45, "t", "g"))
print(conversion_masse(45, "q", "g"))
print(conversion_masse(45, "10kg", "g"))
print(conversion_masse(45, "kg", "g"), "kg à g")
print(conversion_masse(45, "hg", "g"))
print(conversion_masse(45, "dag", "g"))
print(conversion_masse(45, "g", "g"))
print(conversion_masse(45, "dg", "g"))
print(conversion_masse(45, "cg", "g"))