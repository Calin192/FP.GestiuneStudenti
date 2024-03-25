from domeniu.problema import Problema
from random import randint,choice

class ServiceProbleme:

    def __init__(self,validator_problema,file_repo_probleme):
        self.__validator_problema = validator_problema
        self.__repo_probleme = file_repo_probleme

    def adauga_problema(self,id_problema,descriere,deadline):
        problema = Problema(id_problema,descriere,deadline)
        self.__validator_problema.valideaza(problema)
        self.__repo_probleme.adauga_problema(problema)

    def modifica_problema(self,id_problema,descriere,deadline):
        problema = Problema(id_problema, descriere, deadline)
        self.__validator_problema.valideaza(problema)
        self.__repo_probleme.modifica_problema(problema)

    def cauta_problema(self,id_problema):
        return self.__repo_probleme.cauta_problema_dupa_id(id_problema)

    def generare_problema(self,n):
        '''
        functie recursiva
        :return:
        '''
        a=["mate","romana","info","sport","chimie","biologie"]
        b=["10-9","10-10","10-11","10-12"]
        id_problema = randint(1,200)
        deadline = choice(b)
        descriere = choice(a)
        if n != 0:
            for student in self.__repo_probleme.get_all():
                while student.get_id_problema() == id_problema:
                    id_problema = randint(1, 200)
            self.adauga_problema(id_problema, descriere, deadline)
            n = n - 1
            return self.generare_problema(n)

    def sterge_problema(self,id_problema):
        self.__repo_probleme.stergere_problema_dupa_id(id_problema)

    def get_all_probleme(self):
        return self.__repo_probleme.get_all()