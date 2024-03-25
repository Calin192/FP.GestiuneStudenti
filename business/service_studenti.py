from domeniu.student import Student
from random import randint,choice



class ServiceStudenti:

    def __init__(self,validator_student,file_repo_studenti):
        self.__validator_student = validator_student
        self.__file_repo_studenti = file_repo_studenti

    def adauga_student(self,id_student,nume,grupa):
        student = Student(id_student, nume, grupa)
        self.__validator_student.valideaza(student)
        self.__file_repo_studenti.adauga_student(student)

    def modifica_student(self,id_student,nume,grupa):
        student = Student(id_student, nume, grupa)
        self.__validator_student.valideaza(student)
        self.__file_repo_studenti.modifica_student(student)

    def cauta_student(self,id_student):
        return self.__file_repo_studenti.cauta_student(id_student)

    def generare_student(self,n):
        '''
        functie recursiva
        cel mai bun caz: complexitate O(n)
        cel mai rau caz: complexitate O(n^2)
        :param n:
        :return:
        '''
        a=["Calin","Balin","Alin","Malin","Kalin","Palin","Aalin","Nilac","Lanic","Ailnc","Linca"]
        id_student = randint(1,200)
        grupa = randint(211,218)
        nume = choice(a)
        if n != 0:
            for student in self.__file_repo_studenti.get_all():
                while student.get_id_student() == id_student:
                    id_student = randint(1,200)
            self.adauga_student(id_student,nume,grupa)
            n=n-1
            return self.generare_student(n)

    def size(self):
        self.__file_repo_studenti.size()

    def get_all_studenti(self):
        return self.__file_repo_studenti.get_all()
