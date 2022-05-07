dict1 = {"Jean" : (20, "Developpeur"), "Paul" : (30, "Ingénieur")}
dict2 = {"Emilie" : (30, "Professeur"), "Marc" : (25, "Footballer")}

# repertoir_complet = dict1 | dict2
dict1 |= dict2 # dict1 = dict1 | dict2
# dict1.update(dict2) 

print(dict1)