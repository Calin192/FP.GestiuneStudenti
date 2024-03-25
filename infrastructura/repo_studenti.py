from erori.repo_error import RepoError


class RepoStudenti:

    def __init__(self):
        self._studenti = {}

    def adauga_student(self,student):
        if student.get_id_student() in self._studenti:
            raise RepoError("student existent!")
        self._studenti[student.get_id_student()] = student

    def sterge_student(self, id_student):
        if id_student not in self._studenti or self._studenti[id_student].get_sters() is True:
            raise RepoError("student inexistent!")
        self._studenti[id_student].sterge()

    def cauta_student(self, id_student):
        if id_student not in self._studenti or self._studenti[id_student].get_sters() is True:
            raise RepoError("student inexistent!")
        return self._studenti[id_student]

    def modifica_student(self,student):
        if student.get_id_student() not in self._studenti:
            raise RepoError("student inexistent!")
        self._studenti[student.get_id_student()]=student

    def get_all(self):
        studenti = []
        for studenti_id in self._studenti:
            if self._studenti[studenti_id].get_sters()==False:
                studenti.append(self._studenti[studenti_id])
        return studenti

    def size(self):
        return len(self._studenti)

    def __len__(self):
        return len(self._studenti)


