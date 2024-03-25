from erori.repo_error import RepoError


class RepoProbleme:

    def __init__(self):
        self._probleme = {}

    def adauga_problema(self,problema):
        if problema.get_id_problema() in self._probleme:
            raise RepoError("problema existenta!")
        self._probleme[problema.get_id_problema()] = problema

    def stergere_problema_dupa_id(self,id_problema):
        if id_problema not in self._probleme or self._probleme[id_problema].get_sters()==True:
            raise RepoError("problema inexistenta!")
        self._probleme[id_problema].sterge()

    def cauta_problema_dupa_id(self,id_problema):
        if id_problema not in self._probleme or self._probleme[id_problema].get_sters() is True:
            raise RepoError("problema inexistenta!")
        return self._probleme[id_problema]

    def modifica_problema(self,problema):
        if problema.get_id_problema() not in self._probleme:
            raise RepoError("problema inexistenta!")
        self._probleme[problema.get_id_problema()]=problema

    def get_all(self):
        probleme = []
        for probleme_id in self._probleme:
            if self._probleme[probleme_id].get_sters() == False:
                probleme.append(self._probleme[probleme_id])
        return probleme

    def size(self):
        return len(self._probleme)

    def __len__(self):
        return len(self._probleme)