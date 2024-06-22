from abc import ABC, abstractmethod

#4.	Тест, экзамен, выпускной экзамен, испытание.

class Challenge(ABC):
    @abstractmethod
    def passtest():
        pass

class Test(Challenge):
    def __init__(self, predmet):
        self.predmet = predmet

    def passtest(self):
        print(f'От ваших ответов зависит оценка по предмету {self.predmet}\n')

class Exam(Test):
    def __init__(self, tasks):
        self.tasks = tasks

    def passtest(self):
        print(f'Для завершения этого теста нужно ответить на {self.tasks} вопросов\n')

class FinalExam(Exam):
    def __init__(self, cams):
        self.cams = cams
        
    def passtest(self):
        print(f'На этом тесте за вами наблюдало {self.cams} камер\n')

test = Test('математика')
exam = Exam(15)
finalexam = FinalExam(3)

test.passtest()
exam.passtest()
finalexam.passtest()

    #  Двигатель, дизель, двигатели внутреннего сгорания и реактивный

class Motor(ABC):
    @abstractmethod
    def start():
        pass

class Fuelmotor(Motor):
    def __init__(self, type):
        self.type = type

    def start(self):
        print(f'Двигатель потребляет {self.type} бензин\n')

class Dizelmotor(Motor):
    def __init__(self, turnover):
        self.turnover = turnover

    def start(self):
        print(f'Двигатель совершает {self.turnover} оборотов в минуту\n')

class Reactivmotor(Motor):
    def __init__(self, power):
        self.power = power
        
    def start(self):
        print(f'Двигатель вырабатывает {self.power} мощьности\n')

fuelmotor = Fuelmotor("аи-92")
dizelmotor = Dizelmotor(250)
reactivmotor = Reactivmotor("1200 Вт")

fuelmotor.start()
dizelmotor.start()
reactivmotor.start()