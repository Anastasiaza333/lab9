from lab1.Lab1 import Lab1
from lab2.Lab2 import Lab2
from lab3.Lab3 import Lab3
from lab4.Lab4 import Lab4
from lab5.Lab5 import Lab5
from lab7.Lab7 import Lab7
from lab8.Lab8 import Lab8


class Runner:
    def __init__(self):

        self.labs = {
            "1": Lab1(),
            "2": Lab2(),
            "3": Lab3(),
            "4": Lab4(),
            "5": Lab5(),
            "7": Lab7(),
            "8": Lab8(),
            # Додайте всі лабораторні роботи.
        }

    def run_lab(self, lab_number: str):
        if lab_number in self.labs:
            self.labs[lab_number].execute()
        else:
            print("Невірний вибір. Спробуйте ще раз.")

    def show_menu(self):
        print("Оберіть лабораторну роботу для запуску:")
        for number in self.labs:
            print(f" {number} - Лабораторна робота {number}")
        print(" 0 - Вийти")