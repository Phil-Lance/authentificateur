# faire un authentificateur pour usager. L'usager doit avoir 18 ans ou plus.


user: str = input('Quel est ton nom?: ')
age: str = input("Quel est ton age?: ")

print(f'Bonjour {user}! Vous avez {age} ans.')

if int(age) >= 18:
    print("Bienvenue, vous pouvez entrer!")
elif int(age) > 12 <= 17:
    print('Bienvenue! Toutefois, vous etes mineure et avez un acces limitee a la zone sans alchool.')
else:
    print('Desole, vous etes mineure. Meilleur chance la prochaine fois!')