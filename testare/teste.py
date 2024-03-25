from domeniu.student import Student
from infrastructura.repo_probleme import RepoProbleme
from prezentare.consola import UI
from business.service_studenti import ServiceStudenti
from validare.validator_problema import ValidatorProblema
from validare.validator_student import ValidatorStudent
from erori.validation_error import ValidError
from infrastructura.repo_studenti import RepoStudenti
from erori.repo_error import RepoError
from domeniu.problema import Problema
from domeniu.nota import Nota
from validare.validator_nota import ValidatorNota
from infrastructura.repo_note import RepoNote
from business.service_note import ServiceNote

class teste(object):
    def __init__(self):
        self.__id_student = 10
        self.__nume = "Calin"
        self.__grupa = 211
        self.__student = Student(self.__id_student, self.__nume, self.__grupa)

        self.__id_problema = 1
        self.__descriere = "mate"
        self.__deadline = "10-12"
        self.__problema = Problema(self.__id_problema,self.__descriere,self.__deadline)

    def run_teste(self):
        self.__teste_student()
        self.__teste_validator()
        self.__teste_repo_studenti()
        self.__teste_problema()
        self.__teste_repo_probleme()
        self.__teste_note()
        self.__teste_sortare()


    def __teste_problema(self):
        assert (self.__problema.get_id_problema() == self.__id_problema)
        assert (self.__problema.get_descriere() == self.__descriere)
        assert (self.__problema.get_deadline() == self.__deadline)

        __descriere_noua = "romana"
        __deadline_nou = "10-9"
        self.__problema.set_descriere(__descriere_noua)
        self.__problema.set_deadline(__deadline_nou)
        assert (self.__problema.get_descriere() == __descriere_noua)
        assert (self.__problema.get_deadline() == __deadline_nou)

        clona_problema = Problema(self.__id_problema, None, None)
        assert (self.__problema == clona_problema)

    def __teste_student(self):
        assert (self.__student.get_id_student()==self.__id_student)
        assert (self.__student.get_nume()==self.__nume)
        assert (self.__student.get_grupa() == self.__grupa)

        __nume_nou = "Balin"
        __grupa_noua = 212
        self.__student.set_nume(__nume_nou)
        self.__student.set_grupa(__grupa_noua)
        assert (self.__student.get_nume()==__nume_nou)
        assert (self.__student.get_grupa()==__grupa_noua)

        clona_student = Student(self.__id_student, None, None)
        assert (self.__student == clona_student)

    def __teste_validator(self):
        self.__validator = ValidatorStudent()

        self.__validator.valideaza(self.__student)

        id_student = -1
        nume = ""
        __student_gresit = Student(id_student, nume, 0)
        try:
            self.__validator.valideaza(__student_gresit)
            assert False
        except ValidError as ve:
            assert str(ve) == "id invalid!\nnume invalid!\n"

        self.__validator = ValidatorProblema()

        self.__validator.valideaza(self.__problema)

        id_problema = -1
        descriere = ""
        __problema_gresita = Problema(id_problema, descriere, 0)
        try:
            self.__validator.valideaza(__problema_gresita)
            assert False
        except ValidError as ve:
            assert str(ve) == "problema invalida!\ndescriere invalida\n"

    def __teste_repo_studenti(self):
        self.__repo_studenti = RepoStudenti()
        assert len(self.__repo_studenti) == 0
        self.__repo_studenti.adauga_student(self.__student)
        assert len(self.__repo_studenti) == 1

        try:
            self.__repo_studenti.adauga_student(self.__student)
            assert False
        except RepoError as re:
            assert (str(re) == "student existent!")

        self.__nume_nou = "Balin"
        self.__grupa_noua = 212
        self.__student_modificat = Problema(self.__id_student, self.__nume_nou, self.__grupa_noua)
        assert len(self.__repo_studenti) == 1

        self.__id_student_inexistent = 40
        student_inexistent = Student(self.__id_student_inexistent, None, 0)
        try:
            self.__repo_studenti.modifica_student(student_inexistent)
            assert False
        except RepoError as re:
            assert (str(re) == "student inexistent!")

        alt_student = Student(self.__id_student_inexistent, self.__nume_nou, self.__grupa_noua)
        self.__repo_studenti.adauga_student(alt_student)
        assert len(self.__repo_studenti.get_all()) == 2

        self.__repo_studenti.sterge_student(self.__id_student_inexistent)
        assert len(self.__repo_studenti.get_all()) == 1


    def __teste_repo_probleme(self):
        self.__repo_probleme = RepoProbleme()
        assert len(self.__repo_probleme) == 0
        self.__repo_probleme.adauga_problema(self.__problema)
        assert len(self.__repo_probleme) == 1

        try:
            self.__repo_probleme.adauga_problema(self.__problema)
            assert False
        except RepoError as re:
            assert str(re) == "problema existenta!"

        self.__descriere_noua = "romana"
        self.__deadline_nou = "10-9"
        self.__problema_modificata = Problema(self.__id_problema,self.__descriere_noua,self.__deadline_nou)
        assert len(self.__repo_probleme) == 1

        self.__id_problema_inexistenta = 40
        problema_inexistenta = Problema(self.__id_problema_inexistenta,None,0)
        try:
            self.__repo_probleme.modifica_problema(problema_inexistenta)
            assert False
        except RepoError as re:
            assert (str(re) == "problema inexistenta!")

        alta_problema = Problema(self.__id_problema_inexistenta,self.__descriere_noua,self.__deadline_nou)
        self.__repo_probleme.adauga_problema(alta_problema)
        assert len(self.__repo_probleme.get_all()) == 2

        self.__repo_probleme.stergere_problema_dupa_id(self.__id_problema_inexistenta)
        assert len(self.__repo_probleme.get_all()) == 1

    def __teste_note(self):
        self.__repo_note = RepoNote()
        self.__student = Student(self.__id_student, self.__nume, self.__grupa)
        self.__problema = Problema(self.__id_problema, self.__descriere, self.__deadline)
        id_nota = 1
        nota = 9
        self.__nota = Nota(id_nota,self.__id_student,self.__id_problema,nota)
        assert (self.__nota.get_id_nota() == id_nota)
        assert (self.__nota.get_nota() == nota)
        self.__repo_studenti.sterge_student(self.__id_student)
        assert len(self.__repo_note.get_all()) == 0

    def __teste_sortare(self):
        self.__validator_nota = ValidatorNota()
        self.__repo_note = RepoNote()
        self.__repo_student = RepoStudenti()
        self.__repo_probleme = RepoProbleme()
        self.__service_note = ServiceNote(self.__validator_nota,self.__repo_note,self.__repo_studenti,self.__repo_probleme)

        self.__repo_student.adauga_student(self.__student)
        self.__repo_probleme.adauga_problema(self.__problema)

        self.__id2 = 11
        self.__nume2 = "Aalin"
        self.__grupa2 = 211
        self.__student2 = Student(self.__id2, self.__nume2, self.__grupa2)
        self.__repo_student.adauga_student(self.__student2)

        self.__id2 = 12
        self.__nume2 = "Balin"
        self.__grupa2 = 211
        self.__student3 = Student(self.__id2, self.__nume2, self.__grupa2)
        self.__repo_student.adauga_student(self.__student3)

        self.__id_nota = 1
        self.__nota = 9
        self.__nota1 = Nota(self.__id_nota,self.__student,self.__problema,self.__nota)
        self.__repo_note.adauga_nota(self.__nota1)

        self.__id_nota = 2
        self.__nota = 10
        self.__nota2 = Nota(self.__id_nota,self.__student2,self.__problema,self.__nota)
        self.__repo_note.adauga_nota(self.__nota2)

        self.__id_nota = 3
        self.__nota = 8
        self.__nota3 = Nota(self.__id_nota, self.__student3, self.__problema, self.__nota)
        self.__repo_note.adauga_nota(self.__nota3)


        lista = self.__service_note.sortare_nota(self.__problema.get_id_problema())
        assert lista == [[11, 10], [10, 9], [12, 8]]

        lista = self.__service_note.sortare_nume(self.__problema.get_id_problema())
        assert lista == [['Aalin', 10], ['Balin', 8], ['Calin', 9]]

        self.__id_nota = 4
        self.__nota = 6
        self.__nota4 = Nota(self.__id_nota, self.__student, self.__problema, self.__nota)
        self.__repo_note.adauga_nota(self.__nota4)

        lista = self.__service_note.sortare_medie()
        assert lista == []


