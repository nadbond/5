n=int(input("введите количество слов: "))
result=""
for i in range(n):
    result = result + input(f"введите слово {i+1}: ") + " "
print(result)
