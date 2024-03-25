import unittest
from unittest import TestCase

from domeniu.nota import Nota
from domeniu.problema import Problema
from domeniu.student import Student
from infrastructura.repo_note import RepoNote
from infrastructura.repo_probleme import RepoProbleme
from validare.validator_nota import ValidatorNota
from validare.validator_problema import ValidatorProblema
from validare.validator_student import ValidatorStudent
from infrastructura.repo_studenti import RepoStudenti



class TesteUnittest(unittest.TestCase):

    def setUp(self):
        self.validator_student = ValidatorStudent()
        self.repo_student = RepoStudenti()
        self.student = Student(1, "Calin", 211)

        self._validator_problema = ValidatorProblema()
        self.repo_probleme = RepoProbleme()
        self.problema = Problema(1,"mate","10-12")

        self.validator_nota = ValidatorNota()
        self.repo_nota = RepoNote()
        self.nota = Nota(1,1,1,9)

    def tearDown(self):
        pass

    def remove_all(self, path):
        with open(path, "w"):
            pass

    def test_domain(self):
        self.assertEqual(self.student.get_id_student(),1)
        self.assertEqual(self.student.get_nume(),"Calin")
        self.assertEqual(self.student.get_grupa(),211)

        self.assertEqual(self.problema.get_id_problema(), 1)
        self.assertEqual(self.problema.get_descriere(), "mate")
        self.assertEqual(self.problema.get_deadline(), "10-12")

        self.assertEqual(self.nota.get_id_nota(), 1)
        self.assertEqual(self.nota.get_student(), 1)
        self.assertEqual(self.nota.get_problema(), 1)
        self.assertEqual(self.nota.get_nota(), 9)

    def test_repo(self):
        #Adaugare
        self.repo_student.adauga_student(self.student)
        self.assertEqual(len(self.repo_student.get_all()),1)

        self.repo_probleme.adauga_problema(self.problema)
        self.assertEqual(len(self.repo_probleme.get_all()), 1)

        self.repo_nota.adauga_nota(self.nota)
        self.assertEqual(len(self.repo_nota.get_all()), 1)

        #Cautare
        self.assertEqual(self.repo_student.cauta_student(self.student.get_id_student()),self.student)

        self.assertEqual(self.repo_probleme.cauta_problema_dupa_id(self.problema.get_id_problema()), self.problema)

        #Stergere
        self.repo_student.sterge_student(self.student.get_id_student())
        self.assertEqual(len(self.repo_student.get_all()), 0)

        self.repo_probleme.stergere_problema_dupa_id(self.problema.get_id_problema())
        self.assertEqual(len(self.repo_probleme.get_all()), 0)

        self.repo_nota.sterge_nota_dupa_id(self.nota.get_id_nota())
        self.assertEqual(len(self.repo_nota.get_all()), 0)


