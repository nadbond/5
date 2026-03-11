result=""
while True:
    n = input(f"введите слово: ")
    if n == "stop":
        break
    result = result + n + " "
print(result)