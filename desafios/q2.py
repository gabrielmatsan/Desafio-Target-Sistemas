def count_a(word:str):
    return word.lower().count('a')


def count_letters(word:str):
    contagem = 0
     
    for i in range(len(word)):
        if word[i].lower() == 'a':
            contagem += 1
    return f'a letra a apareceu {contagem} vezes'
        


result = count_letters('poste')
print(result)