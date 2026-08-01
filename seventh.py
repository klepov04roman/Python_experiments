secret = 7  
guess = None

while guess != secret:
    guess = int(input("1-10"))
    if guess < secret:
        print("Занадто мало")
    elif guess > secret:
        print("Занадто багато")
    else:
        print("Вітаю, ти вгадав!")