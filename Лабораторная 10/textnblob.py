from textblob import TextBlob

text = "Отец мой Андрей Петрович Гринев в молодости своей служил при графе Минихе и вышел в отставку премьер-майором в 17.. году. С тех пор жил он в своей Симбирской деревне, где и женился на девице Авдотье Васильевне Ю., дочери бедного тамошнего дворянина. Нас было девять человек детей. Все мои братья и сестры умерли во младенчестве."

# Создание объекта TextBlob
blob = TextBlob(text)

# Анализ тональности текста
sentiment = blob.sentiment

# Вывод результатов
print("Тональность текста:")
print("Оценка тональности: ", sentiment.polarity)
print("Оценка субъективности: ", sentiment.subjectivity)

# Извлечение предложений
sentences = blob.sentences

print("\nПредложения:")
for sentence in sentences:
    print(sentence)

# Извлечение слов
words = blob.words

print("\nСлова:")
for word in words:
    print(word)
