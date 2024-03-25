from domeniu.student import Student
from infrastructura.repo_studenti import RepoStudenti


class FileRepoStudenti(RepoStudenti):

    def __init__(self,calea_catre_fisier_studenti):
        RepoStudenti.__init__(self)
        self.__calea_catre_fisier_studenti = calea_catre_fisier_studenti

    def adauga_student(self,student):
        self.__read_all_from_file()
        RepoStudenti.adauga_student(self,student)
        self.__write_all_to_file()

    def __read_all_from_file(self):
        with open(self.__calea_catre_fisier_studenti,"r") as f:
            lines = f.readlines()
            self._studenti.clear()
            for line in lines:
                line = line.strip()
                if line != "":
                    parti = line.split(",")
                    id_student = int(parti[0])
                    nume = str(parti[1])
                    grupa = int(parti[2])
                    student = Student(id_student, nume, grupa)
                    self._studenti[id_student] = student

    def __write_all_to_file(self):
        with open(self.__calea_catre_fisier_studenti,"w") as f:
            for student in self._studenti.values():
                f.write(str(student)+"\n")

    def modifica_student(self,student):
        self.__read_all_from_file()
        RepoStudenti.modifica_student(self, student)
        self.__write_all_to_file()

    def sterge_student(self, id_student):
        self.__read_all_from_file()
        RepoStudenti.sterge_student(self, id_student)
        self.__write_all_to_file()

    def cauta_student(self, id_student):
        self.__read_all_from_file()
        return RepoStudenti.cauta_student(self,id_student)

    def get_all(self):
        self.__read_all_from_file()
        return RepoStudenti.get_all(self)

    def size(self):
        return RepoStudenti.size(self)

    def __len__(self):
        self.__read_all_from_file()
        return RepoStudenti.__len__(self)
