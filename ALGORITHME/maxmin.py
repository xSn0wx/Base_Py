#Par len
def get_min_and_max_words(sentence):
    chaine = sentence.split(" ")
    chaine.sort()
    return max(chaine, key=len), min(chaine, key=len)

# par alphabetique
# def get_min_and_max_words_sorted(sentence):
#     chaine = sentence.split(" ")
#     max_word, min_word = get_min_and_max_words(sentence)
#     all_max_word = [w for w in chaine if len(w) == len(max_word)]
#     all_min_word = [w for w in chaine if len(w) == len(min_word)]
#     all_min_word.sort()
#     all_max_word.sort()
#     return all_min_word[0], all_max_word[0]


s = "Un chasseur sachant chasser sait chasser sans son chien"
min_word, max_word = get_min_and_max_words(s)

print("Mot le plus petit :", min_word)
print("Mot le plus long :", max_word)
