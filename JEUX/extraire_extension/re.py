def obtenir_information(ext, definition):
    for i in definition:
        if ext.lower() == i[0].lower():
            return i[1]
    return None



def extraire_extension(fich):
    ext = fich.split(".")
    if len(ext) > 1:
        return ext[-1]
    return None



fichiers = ("notepad.exe", "mon.fichier.perso.doc", "notes.TXT", "vacances.jpeg", "planning", "data.dat")

definition_extensions = (("doc", "Document Word"),
                        ("exe", "Executable"),
                        ("txt", "Document Texte"),
                        ("jpeg", "Image JPEG"))

"""definition_extensions_dict = {"doc": "Document Word",
                        "exe": "Executable",
                        "txt": "Document Texte",
                        "jpeg": "Image JPEG"}"""


for fichier in fichiers:
    ext = extraire_extension(fichier)
    if ext:
        definition = obtenir_information(ext, definition_extensions)
        if not definition:
            print(fichier, "Extention inconnue")
    else:
        print(fichier, "n'a pas d'extention")
        break
    print(fichier, "(" + definition + ")")


        
