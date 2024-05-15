import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk import pos_tag, ne_chunk


nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')

text = "Отец мой Андрей Петрович Гринев в молодости своей служил при графе Минихе и вышел в отставку премьер-майором в 17.. году. С тех пор жил он в своей Симбирской деревне, где и женился на девице Авдотье Васильевне Ю., дочери бедного тамошнего дворянина. Нас было девять человек детей. Все мои братья и сестры умерли во младенчестве."
tokens = word_tokenize(text)
pos_tags = pos_tag(tokens)
print("Части речи:")
print(pos_tags)

named_entities = ne_chunk(pos_tags)
print("\nИменованные сущности:")
print(named_entities)

text = "Пример текста для токенизации."
tokens = word_tokenize(text)
print(tokens)
