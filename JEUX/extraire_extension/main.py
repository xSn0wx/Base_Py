def obtenir_information(f, liste, f2):
    nb_fois = int(len(liste)/2)
    split = extension(f)
    nb = 1
    nb_split = 0
    for i in range(nb_fois):
        for i in range(nb_fois):
            if liste[f"Extension{nb}"].lower() in split[nb_split]:
                print("yes")
                slice_valide = nb_split
                print(f2[slice_valide], "("+ liste[f"Rep{nb}"] + ")")
            break
            nb_split += 1
        nb += 1
    # [['notepad', 'exe'], ['mon', 'fichier', 'perso', 'doc'], ['notes', 'TXT'], ['vacances', 'jpeg'], ['planning'], ['data', 'dat']]



def extension(nom_fichier):
    split_list = []
    for i in nom_fichier:
        ext = i.split(".")
        split_list.append(ext)
    return split_list



fichiers = ["notepad.exe", "mon.fichier.perso.doc", "notes.TXT", "vacances.jpeg", "planning", "data.dat"]
fichiers2 = ["notepad.exe", "mon.fichier.perso.doc", "notes.TXT", "vacances.jpeg", "planning", "data.dat"]

ext_dict = {    
    "Extension1": ("doc"),
    "Rep1": ("Document Word"),
    "Extension2": ("jpeg"),
    "Rep2": ("Image JPEG"),
    "Extension3": ("exe"),
    "Rep3": ("Executable"),
    "Extension4": ("txt"),
    "Rep4": ("Document Texte")
}


obtenir_information(fichiers, ext_dict, fichiers2)