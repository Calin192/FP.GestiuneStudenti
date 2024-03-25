from infrastructura.repo_studenti import RepoStudenti
from domeniu.student import Student
from domeniu.problema import Problema


class Nota:

    def __init__(self,id_nota,student,problema,nota):
        self.__id_nota = id_nota
        self.__student = student
        self.__problema = problema
        self.__nota = nota
        self.__sters = False

    def get_id_nota(self):
        return self.__id_nota

    def get_student(self):
        return self.__student

    def get_problema(self):
        return self.__problema

    def get_sters(self):
        return self.__sters

    def get_nota(self):
        return self.__nota

    def set_nota(self,nota):
        self.__nota = nota

    def sterge(self):
        self.__sters = True

    def __str__(self):
        return f"{self.__id_nota},{self.__student.get_id_student()},{self.__problema.get_id_problema()},{self.__nota}"
