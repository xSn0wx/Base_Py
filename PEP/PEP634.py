# a = 5
# if a == 10:
"""
while True:
    phrase = input("Parlez moi : ")
    if phrase == "bonjour" or phrase == "hello" or phrase == "salut":
        print("bonjour comment allez vous ? ")
        print()
    elif phrase == "bien":
        print("Je vais bien aussi")
        print()
    elif phrase == "bye":
        print("Au revoir")
        break
    else: 
        print("Je n'est pas compris")
        print()
        
"""


from turtle import bye


while True:
    phrase = input("Parlez moi : ")
    match phrase:
        case "bonjour" | "hello" | "salut":
            print("Bonjour comment allez vous ? ")
            print()
        case "bien":
            print("Je vais bien aussi")
            print()
        case "bye":
            print("Au revoir")
            print()
            break
        case _:   # wildcards
            print("Je n'est pas compris")
            print()

personne1 = {"nom": "Paul", "infos": (30, "Ingenieur informatique")}
personne2 = {"nom": "Marc", "age": 20}
personne3 = {"nom": "Jean", "age": 17, "metier": "étudiant"}
personne4 = {"nom": "Pierre"}
personne5 = {"nom": "Emilie", "age": 16}

personnes = (personne1, personne2, personne3, personne4, personne5)

for personne in personnes:
    match personne:
        case {"nom": nom, "infos": (age, metier)}:
            print(f"{nom}, {age} ans, {metier}")
        case {"nom": nom, "age": age, "metier": metier}:
            print(f"{nom}, {age} ans, {metier}")
        case {"nom": nom, "age": age} if age >= 18:
            print(f"{nom}, {age} ans")
        case {"nom": nom, "age": age}:
            print(f"{nom}, {age} ans (mineur)")
        case _:
            print("Format non supporté")
