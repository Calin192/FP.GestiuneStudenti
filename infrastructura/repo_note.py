from erori.repo_error import RepoError

class RepoNote:

    def __init__(self):
        self._note = {}

    def adauga_nota(self,nota):
        if nota.get_id_nota() in self._note:
            raise RepoError("nota existenta!")
        self._note[nota.get_id_nota()] = nota

    def sterge_nota_dupa_id(self,id_nota):
        if id_nota not in self._note or self._note[id_nota].get_sters()==True:
            raise RepoError("nota inexistenta!")
        self._note[id_nota].sterge()

    def get_all(self):
        note = []
        for nota_id in self._note:
            if self._note[nota_id].get_sters() == False:
                note.append(self._note[nota_id])
        return note

    def __len__(self):
        return len(self._note)
