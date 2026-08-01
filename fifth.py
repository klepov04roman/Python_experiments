
def checkscore(scoreparam):
 if 90 <= scoreparam <= 100:
    print("Відмінно")
 elif 70 <= scoreparam <= 89:
    print("Добре")
 elif 50 <= scoreparam <= 69:
    print("Задовільно")
 elif 0 <= scoreparam <= 49:
    print("Незадовільно")
 else:
    print("Число не в діапазоні 0–100")
checkscore(60)