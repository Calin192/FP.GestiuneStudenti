from domeniu.student import Student
from domeniu.nota import Nota


class ServiceNote:

    def __init__(self,validator_nota,repo_note,file_repo_studenti,file_repo_probleme):
        self.__validator_nota = validator_nota
        self.__repo_note = repo_note
        self.__repo_studenti = file_repo_studenti
        self.__repo_probleme = file_repo_probleme

    def nota_frecventa(self):
        list = [0]*11
        max = 0
        ok = 0
        for self.__nota in self.__repo_note.get_all():
            list[self._nota.get_nota()] += 1
            if max < list[self._nota.get_nota()]:
                max = list[self._nota.get_nota()]
                ok = self._nota.get_nota()
        return ok


    def sortare_medie(self):
        '''
        calculeaza media fiecarui student si dupa compara cu 5
        :return:
        '''
        list = []
        for student in self.__repo_studenti.get_all():
            sum = 0
            nr = 0
            for nota in self.__repo_note.get_all():
                if nota.get_student() == student:
                    sum += nota.get_nota()
                    nr += 1
            medie = float(sum/nr)
            if medie < 5:
                list1 = [student.get_nume(),medie]
                list.append(list1)
        return list

    def sortare_nota(self,id_problema):
        '''
        sorteaza notele descrescator de la o problema
        :param id_problema:
        :return:
        '''
        #list = {}
        #for nota in self.__repo_note.get_all():
        #    if nota.get_problema().get_id_problema() == id_problema and nota.get_sters() == False:
        #        student = nota.get_student()
        #        list[student.get_id_student()] = nota.get_nota()
        #lista_sortata = sorted(list.items(), key=lambda x:x[1], reverse = True)
        #return lista_sortata
        list = []
        for nota in self.__repo_note.get_all():
            if nota.get_problema().get_id_problema() == id_problema and nota.get_sters() == False:
                student = nota.get_student()
                lista = [student.get_id_student(),nota.get_nota()]
                list.append(lista)
        for i in range(len(list)):
            min = i
            for j in range(i,len(list)):
                if list[j][1] > list[min][1]:
                    min = j
            list[i], list[min] = list[min], list[i]
        return list

    def sortare_nota_si_nume(self,id_problema):
        #sortare nota
        list = []
        for nota in self.__repo_note.get_all():
            if nota.get_problema().get_id_problema() == id_problema and nota.get_sters() == False:
                student = nota.get_student()
                lista = [student.get_id_student(), nota.get_nota()]
                list.append(lista)
        for i in range(len(list)):
            min = i
            for j in range(i, len(list)):
                if list[j][1] > list[min][1]:
                    min = j
            list[i], list[min] = list[min], list[i]


        # sortare nume
        left = 0
        right = len(list) - 1
        while left <= right:
            for i in range(left, right):
                if self.__repo_studenti.cauta_student(list[i][0]).get_nume() > self.__repo_studenti.cauta_student(list[i+1][0]).get_nume():
                    list[i], list[i + 1] = list[i + 1], list[i]
            right -= 1
            for i in range(right, left, -1):
                if self.__repo_studenti.cauta_student(list[i][0]).get_nume() < self.__repo_studenti.cauta_student(list[i+1][0]).get_nume():
                    list[i], list[i - 1] = list[i - 1], list[i]
            left += 1

        return list

    def sortare_nume(self,id_problema):
        '''
        sorteaza studentii alfabetic de la o problema
        :param id_problema:
        :return:
        '''
        #list = {}
        #for nota in self.__repo_note.get_all():
        #    if nota.get_problema().get_id_problema() == id_problema and nota.get_sters() == False:
        #        student = nota.get_student()
        #        list[student.get_nume()] = nota.get_nota()
        #lista_sortata = sorted(list, key=lambda x:x[0], reverse=False)
        #return lista_sortata
        list = []
        for nota in self.__repo_note.get_all():
            if nota.get_problema().get_id_problema() == id_problema and nota.get_sters() == False:
                student = nota.get_student()
                lista = [student.get_nume(), nota.get_nota()]
                list.append(lista)
        left = 0
        right = len(list) - 1
        while left <= right:
            for i in range(left, right):
                if list[i][0] > list[i + 1][0]:
                    list[i], list[i + 1] = list[i + 1], list[i]
            right -= 1
            for i in range(right, left, -1):
                if list[i - 1][0] > list[i][0]:
                    list[i], list[i - 1] = list[i - 1], list[i]
            left += 1
        return list


    def adauga_nota(self,id_nota,id_student,id_problema,nota_):
        '''
        adauga nota cu idul cerut, id student, id problema si nota de la tastatura
        :param id_nota:  idul notei
        :param id_student: idul studentului
        :param id_problema: idul problemei
        :param nota_: nota in sine
        :return:
        '''
        student = self.__repo_studenti.cauta_student(id_student)
        problema = self.__repo_probleme.cauta_problema_dupa_id(id_problema)
        nota = Nota(id_nota,student,problema,nota_)
        self.__validator_nota.valideaza(nota)
        self.__repo_note.adauga_nota(nota)


    def sterge_student_si_notele_lui(self,id_student):
        '''
        sterge studentul si notele lui, numai daca exista o nota
        pentru studentul cu idul cerut
        :param id_student:
        :return:
        '''
        student = self.__repo_studenti.cauta_student(id_student)
        note = self.__repo_note.get_all()
        note_studenti = [x for x in note if x.get_student() == student]
        for nota_student in note_studenti:
            self.__repo_note.sterge_nota_dupa_id(nota_student.get_id_nota())
        self.__repo_studenti.sterge_student(id_student)


#    def get_sefi_promotie(self):
#        info_studenti = {}
 #       note = self.__repo_note.get_all()
 #       for nota in note:
 #           id_student_nota = nota.get_student().get_id_student()
 #           valoare_nota = nota.get_note()
 #           if id_student_nota not in info_studenti:
 #               info_studenti[id_student_nota] = []
 #           info_studenti[id_student_nota].append(valoare_nota)
 #       sefi_promotie = []
 #       for id_student in info_studenti:
 #          student = self.__repo_studenti.cauta_student_dupa_id(id_student)
 #           nume_student = student.get_nume()
 #           medie_student = sum(info_studenti[id_student])/len(info_studenti[id_student])
 #           sef_promotie_dto = SefPromotieDTO(nume_student,medie_student)
 #           sefi_promotie.append(sef_promotie_dto)
 #       sefi_promotie.sort(reverse=True)
 #       return sefi_promotie[:3]

    def get_all_note(self):
        '''
        returneaza toate notele
        :return:
        '''
        return self.__repo_note.get_all()
