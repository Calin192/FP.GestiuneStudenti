class Problema:

    def __init__(self,id_problema,descriere,deadline):
        self.__id_problema = id_problema
        self.__descriere = descriere
        self.__deadline = deadline
        self.__sters = False

    def sterge(self):
        self.__sters = True

    def get_id_problema(self):
        return self.__id_problema

    def get_descriere(self):
        return self.__descriere

    def get_deadline(self):
        return self.__deadline

    def set_descriere(self,descriere):
        self.__descriere = descriere

    def set_deadline(self,deadline):
        self.__deadline = deadline

    def get_sters(self):
        return self.__sters

    def __eq__(self, other):
        return self.__id_problema == other.__id_problema

    def __str__(self):
        return f"{self.__id_problema},{self.__descriere},{self.__deadline}"