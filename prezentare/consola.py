from erori.repo_error import RepoError
from erori.validation_error import ValidError
class UI:

    def __init__(self,service_studenti,service_probleme,service_note):
        self.__service_studenti = service_studenti
        self.__service_probleme = service_probleme
        self.__service_note = service_note
        self.__comenzi = {
            #"sefi_promotie": self.__ui_sefi_promotie,
            "adauga_student" : self.__ui_adauga_student,
            "print_studenti" : self.__ui_print_studenti,
            "sterge_student_si_notele_lui" : self.__ui_sterge_student_si_note,
            "modifica_student" : self.__ui_modifica_student,
            "adauga_problema" : self.__ui_adauga_problema,
            "print_probleme" : self.__ui_print_probleme,
            "modifica_problema" : self.__ui_modifica_problema,
            "sterge_problema" : self.__ui_sterge_problema,
            "print_comenzi" : self.__ui_print_comenzi,
            "cauta_student" : self.__ui_cauta_student,
            "cauta_problema" : self.__ui_cauta_problema,
            "adauga_nota" : self.__ui_adauga_nota,
            "print_note" : self.__ui_print_note,
            "generare_studenti" : self.__ui_generare_studenti,
            "generare_probleme" : self.__ui_generare_probleme,
            "sortare_alfabetic" : self.__ui_sortare_alfabetic,
            "sortare_nota" : self.__ui_sortare_nota,
            "sortare_medie" : self.__ui_sortare_medie,
            "nota_frecventa" : self.__ui_nota_frecventa,
            "sortare_nota_nume" : self.__ui_sortare_nota_nume,
        }

    def __ui_nota_frecventa(self):
        if len(self.__params)!=0:
            print("numar parametri invalid")
            return
        nota=self.__service_note.nota_frecventa()
        print(nota)

    def __ui_sortare_medie(self):
        if len(self.__params)!=0:
            print("numar parametri invalid")
            return
        list = self.__service_note.sortare_medie()
        for i in list:
            print(i[0],i[1])

    def __ui_sortare_nota_nume(self):
        if len(self.__params)!=1:
            print("numar parametri invalid")
            return
        id_problema = int(self.__params[0])
        lista_sortata = self.__service_note.sortare_nota_si_nume(id_problema)
        for i in lista_sortata:
            student_id = i[0]
            nota = i[1]
            print(self.__service_studenti.cauta_student(student_id).get_nume(),nota)


    def __ui_sortare_nota(self):
        if len(self.__params)!=1:
            print("numar parametri invalid")
            return
        id_problema = int(self.__params[0])
        lista_sortata = self.__service_note.sortare_nota(id_problema)
        for i in lista_sortata:
            student_id = i[0]
            nota = i[1]
            print(self.__service_studenti.cauta_student(student_id).get_nume(),nota)

    def __ui_sortare_alfabetic(self):
        if len(self.__params)!=1:
            print("numar parametri invalid")
            return
        id_problema = int(self.__params[0])
        lista_sortata = self.__service_note.sortare_nume(id_problema)
        print(lista_sortata)
        """for i in lista_sortata:
            student_id = i[0]
            nota =  
            print(self.__service_studenti.cauta_student(student_id).get_nume(),nota)
        """

    def __ui_generare_studenti(self):
        if len(self.__params)!=1:
            print("numar parametri invalid")
            return
        n=int(self.__params[0])
        self.__service_studenti.generare_student(n)
        print("studenti generati cu succes")

    def __ui_generare_probleme(self):
        if len(self.__params)!=1:
            print("numar parametri invalid")
            return
        n=int(self.__params[0])
        self.__service_probleme.generare_problema(n)
        print("probleme generate cu succes")

    def __ui_adauga_nota(self):
        if len(self.__params)!=4:
            print("numar parametri invalid")
            return
        id_nota = int(self.__params[0])
        id_student = int(self.__params[1])
        id_problema = int(self.__params[2])
        nota = int(self.__params[3])
        self.__service_note.adauga_nota(id_nota,id_student,id_problema,nota)
        print("nota adaugata cu succes!")

    def __ui_cauta_problema(self):
        if len(self.__params)!=1:
            print("numar parametri invalid")
            return
        id_problema = int(self.__params[0])
        print(self.__service_probleme.cauta_problema(id_problema))

    def __ui_cauta_student(self):
        if len(self.__params)!=1:
            print("numar parametri invalid")
            return
        id_student = int(self.__params[0])
        print(self.__service_studenti.cauta_student(id_student))


    def __ui_print_comenzi(self):
        l=1
        for cheie in self.__comenzi:
            print(f"{l}.{cheie}")
            l=l+1

    def __ui_sefi_promotie(self):
        if len(self.__params)!=0:
            print("numar parametri invalid")
            return
        sefi_promotie = self.__service_note.get_sefi_promotie()
        for sef_promotie in sefi_promotie:
            print(sef_promotie)

    def __ui_modifica_student(self):
        if len(self.__params) != 3:
            print("numar parametri invalid")
            return
        id_student = int(self.__params[0])
        nume = self.__params[1]
        grupa = self.__params[2]
        self.__service_studenti.modifica_student(id_student, nume, grupa)
        print(f"studentul cu idul {id_student} modificat cu succes")

    def __ui_modifica_problema(self):
        if len(self.__params) != 3:
            print("numar parametri invalid")
            return
        id_problema = int(self.__params[0])
        descriere = self.__params[1]
        deadline = self.__params[2]
        self.__service_probleme.modifica_problema(id_problema, descriere, deadline)
        print(f"problema cu idul {id_problema} modificat cu succes")

    def __ui_sterge_student_si_note(self):
        if len(self.__params)!=1:
            print("numar parametri invalid")
            return
        id_student = int(self.__params[0])
        self.__service_note.sterge_student_si_notele_lui(id_student)
        print(f"studentul cu idul {id_student} si notele lui sterse cu succes!")

    def __ui_sterge_problema(self):
        if len(self.__params)!=1:
            print("numar parametri invalid")
            return
        id_problema = int(self.__params[0])
        self.__service_probleme.sterge_problema(id_problema)
        print(f"problema cu idul {id_problema} a fost stearsa cu succes!")

    def __ui_print_studenti(self):
        if len(self.__params)!=0:
            print("numar parametri invalid")
            return
        studenti = self.__service_studenti.get_all_studenti()
        if self.__service_studenti.size()==0:
            print("nu exista studenti in aplicatie!")
            return
        for student in studenti:
            print(student)

    def __ui_print_probleme(self):
        if len(self.__params)!=0:
            print("numar parametri invalid")
            return
        probleme = self.__service_probleme.get_all_probleme()
        if len(probleme)==0:
            print("nu exista probleme in aplicatie!")
            return
        for problema in probleme:
            print(problema)

    def __ui_print_note(self):
        if len(self.__params)!=0:
            print("numar parametri invalid")
            return
        note = self.__service_note.get_all_note()
        if len(note)==0:
            print("nu exista note in aplicatie!")
            return
        for nota in note:
            print(nota)

    def __ui_adauga_student(self):
        if len(self.__params)!=3:
            print("numar parametri invalid")
            return
        id_student = int(self.__params[0])
        nume = self.__params[1]
        grupa = int(self.__params[2])
        self.__service_studenti.adauga_student(id_student,nume,grupa)
        print("student adaugat cu succes!")

    def __ui_adauga_problema(self):
        if len(self.__params)!=3:
            print("numar parametri invalid")
            return
        id_problema = int(self.__params[0])
        descriere = self.__params[1]
        deadline = self.__params[2]
        self.__service_probleme.adauga_problema(id_problema,descriere,deadline)
        print("problema adaugata cu succes!")

    def run(self):
        while True:
            comanda = input(">>>")
            comanda = comanda.strip()
            if comanda == "":
                continue
            if comanda == "exit":
                return
            parti = comanda.split()
            nume_comanda = parti[0]
            self.__params = parti[1:]
            if nume_comanda in self.__comenzi:
                try:
                    self.__comenzi[nume_comanda]()
                except ValueError:
                    print("Eroare UI: tip numeric invalid")
                except ValidError as ve:
                    print(f"Valid Error:{ve}")
                except RepoError as re:
                    print(f"Repo Error:{re}")
            else:
                print("comanda invalida!")
