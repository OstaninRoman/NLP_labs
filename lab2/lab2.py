import gensim

pos = ["вещица_NOUN", "шкаф_NOUN"]

model_path = "cbow.txt"

word2vec = gensim.models.KeyedVectors.load_word2vec_format(
    model_path, binary=False
)

dist = word2vec.most_similar(positive=pos, topn=20)

targets = {"безделушка", "комод"}
found = set()
count = 0

for word, similarity in dist:
    if not word.endswith("_NOUN"):
        continue

    count += 1
    print(f"{count}. {word}: {similarity:.4f}")

    if word in targets:
        found.add(word)

    if count == 10:
        break

if found == targets:
    print("Оба заданных слова попали в первую десятку.")
else:
    print("Нужно подобрать другую комбинацию слов.")
