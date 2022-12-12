#There is a list with dictionaries, in each dictionary the key is the name of the language, and the meaning is a 
# word in that language, it is necessary to divide this dictionary into several files, each of which will store the meaning 
# of the word on in Russian, and hyphenated - the meaning of this word in another language from the dictionary. 
# The file name should match the language:

translation = [{'ru':'яблоко','en':'apple','es': 'manzana'},
                {'ru':'помидор','en':'tomato','es': 'tomate'}]
#creating empty dictionaries for sorting values
ru = []
en = []
es = []
#creating an algorithm for sorting values
for dict in translation:
    for language, words in dict.items():
        "Filter words by lists"
        if language == "ru":
            ru.append(words)
        if language == "en":
            en.append(words)
        if language == "es":
            es.append(words)
#creating files and recording
en_file = open("C:/Users/Desktop/python/en.txt" , 'w')
en_file.write(ru[0] + " - " + en[0] + "\n" + ru[1] + " - " + en[1])
es_file = open("C:/Users/Desktop/python/es.txt" , 'w')
es_file.write((ru[0] + " - " + es[0] + "\n" + ru[1] + " - " + es[1]))