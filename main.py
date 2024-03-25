

from infrastructura_file.file_repo_probleme import FileRepoProbleme
from testare.unittest import TesteUnittest
from validare.validator_student import ValidatorStudent
from validare.validator_problema import ValidatorProblema
from validare.validator_nota import ValidatorNota
from infrastructura.repo_note import RepoNote
from infrastructura.repo_probleme import RepoProbleme
from infrastructura.repo_studenti import RepoStudenti
from business.service_note import ServiceNote
from business.service_probleme import ServiceProbleme
from business.service_studenti import ServiceStudenti
from prezentare.consola import UI
from testare.teste import *
from infrastructura_file.file_repo_studenti import FileRepoStudenti

#1,Calin,211
#2,Balin,212
#3,Alin,211
#4,Kalin,888
#5,Nilac,112

if __name__ == '__main__':
    validator_student = ValidatorStudent()
    validator_probleme = ValidatorProblema()
    validator_nota = ValidatorNota()

    repo_studenti = RepoStudenti()
    repo_probleme = RepoProbleme()
    repo_note = RepoNote()

    calea_catre_fisier_studenti = "studenti.txt"
    file_repo_studenti = FileRepoStudenti(calea_catre_fisier_studenti)

    calea_catre_fisier_probleme = "probleme.txt"
    file_repo_probleme = FileRepoProbleme(calea_catre_fisier_probleme)

    service_studenti = ServiceStudenti(validator_student,file_repo_studenti)
    service_probleme = ServiceProbleme(validator_probleme,file_repo_probleme)
    service_note = ServiceNote(validator_nota,repo_note,file_repo_studenti,file_repo_probleme)

    consola = UI(service_studenti,service_probleme,service_note)

    teste = teste()
    teste.run_teste()

    teste_fisier = TesteUnittest()
    #unittest.main()

    consola.run()
