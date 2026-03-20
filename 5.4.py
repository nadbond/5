import random
correct=0
error=0
print("Игра на сложение для детей. Игра закончится после трёх ошибок. Удачи!")
while error < 3:
    num1=random.randint(1,10)
    num2=random.randint(1,10)
    correct_answer=num1+num2
    user_answer=int(input(f"{num1}+{num2}="))
    if user_answer == correct_answer:
        print("Правильно!")
        correct += 1
    else:
        print("Ответ не верный.")
        error += 1
print("Игра окончена! Ты все равно умничка!")