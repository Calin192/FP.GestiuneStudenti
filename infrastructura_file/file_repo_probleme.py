from domeniu.problema import Problema
from infrastructura.repo_probleme import RepoProbleme


class FileRepoProbleme(RepoProbleme):

    def __init__(self,calea_catre_fisier_probleme):
        RepoProbleme.__init__(self)
        self.__calea_catre_fisier_probleme = calea_catre_fisier_probleme

    def adauga_problema(self,problema):
        self.__read_all_from_file()
        RepoProbleme.adauga_problema(self,problema)
        self.__write_all_to_file()

    def __read_all_from_file(self):
        with open(self.__calea_catre_fisier_probleme,"r") as f:
            lines = f.readlines()
            self._probleme.clear()
            for line in lines:
                line = line.strip()
                if line != "":
                    parti = line.split(",")
                    id_problema = int(parti[0])
                    descriere = str(parti[1])
                    deadline = str(parti[2])
                    problema = Problema(id_problema, descriere, deadline)
                    self._probleme[id_problema] = problema

    def __write_all_to_file(self):
        with open(self.__calea_catre_fisier_probleme,"w") as f:
            for problema in self._probleme.values():
                if problema.get_sters() == False:
                    f.write(str(problema)+"\n")

    def modifica_problema(self,problema):
        self.__read_all_from_file()
        RepoProbleme.modifica_problema(self, problema)
        self.__write_all_to_file()

    def sterge_problema(self, id_problema):
        self.__read_all_from_file()
        RepoProbleme.stergere_problema_dupa_id(self, id_problema)
        self.__write_all_to_file()

    def cauta_problema_dupa_id(self, id_problema):
        self.__read_all_from_file()
        return RepoProbleme.cauta_problema_dupa_id(self,id_problema)

    def get_all(self):
        self.__read_all_from_file()
        return RepoProbleme.get_all(self)

    def size(self):
        return RepoProbleme.size(self)

    def __len__(self):
        self.__read_all_from_file()
        return RepoProbleme.__len__(self)
