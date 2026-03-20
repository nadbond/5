Word=input("Введите слово: ")
Word_lover = Word.lower()
if "ф" in Word_lover:
    print("Ого! Это редкое слово!")
else:
    print("Эх, это не очень редкое слово...")