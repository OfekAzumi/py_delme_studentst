from enum import Enum
import os
import pickle


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def save_data(data, file_path='db.pkl'):
    with open(file_path, 'wb') as file:
        pickle.dump(data, file)


def load_data(file_path='db.pkl'):
    try:
        with open(file_path, 'rb') as file:
            return (pickle.load(file))
    except FileNotFoundError:
        return []

class Stud_Acs(Enum): #students actions
    Add = 0
    Add_Test = 1
    Print_all = 2
    Print_best = 3
    Print_worst = 4
    Exit = 5

class Test:
    def __init__(self,prf='def', grade = 11) -> None: #proffesion and grade, if not, X/11 - fail
        self.prf = prf
        self.grade = grade
    
    def __str__(self) -> str:
        return f'{self.prf} : {self.grade}'
    
class Student:
    def __init__(self, name='def', age='0') -> None:
        self.name = name
        self.age = age
        self.tests = [] #tests list
    
    def addTest(self):
        self.tests.append(Test(input('enter proffestion: '), int(input('enter grade: '))))

    def average(self):
        if self.tests:
            sum = 0
            for tst in self.tests:
                sum += tst.grade
            return (sum/len(self.tests))
        else: return ("no tests")

    def __str__(self) -> str:
        return f'{self.name} , {self.age} | {self.average()}'