def afficher_table_multiplication(n):
    max = input("Quel le nombre max : ")
    min = input("Quel le nombre min : ")
    int_max = int(max)
    if int(min) > int_max:
        print("Erreur : Le nombre min ne peut pas etre supérieur au nombre max")
        return
    for i in range(int(min), int_max+1):
        print(f"{i} x {n} = {i * n}")
    print("---------fin de la table---------")


a = input("Quel table soutaitez vous execute ? ")
afficher_table_multiplication(int(a))
