# def reverse_sting(str):
#     chaine = []
#     for i in range(0, len(str)):
#         chaine.append(str[i])
#     chaine_inverser = []
#     for i in range(0, len(chaine)):
#         chaine_inverser.append(chaine[-(i +1)])
#     final = "".join(chaine_inverser)
#     return final

def reverse_sting(str):
    r = ""
    for c in str:
        r = c + r
    return r

a = input("Dite ce que vous voulez : ")
reverse = reverse_sting(a)
print(reverse)

print(a[-1::-1])