
lyrics = open('grace.txt').read().split()

lenght_overall = len(lyrics)
print(lenght_overall)

unique_words = set(lyrics)
print(unique_words)


lenght_unique = len(unique_words)
print(lenght_unique)


word_dict = {}
for item in unique_words:
    word_dict[item] = 0
    print(word_dict)

for item in lyrics:
    word_dict[item] = word_dict[item] + 1
    print(word_dict)


sort_dict = sorted(word_dict.items(), key=lambda i: i[1], reverse=True)
print(sort_dict)

top10_sliced = sort_dict[0:10]
print(top10_sliced)

with open("resultado_grace.txt", "a") as f:
    print('Musica: Grace, by: Jeff Bucley', file=f)
    '\n'
    print('Todas as palavras que aparecem: ', lenght_overall, file=f)
    print('Palavras unicas que mais aparecem', lenght_unique, file=f)
    print('Top 10 de palavras que mais aparecem', top10_sliced, file=f)



