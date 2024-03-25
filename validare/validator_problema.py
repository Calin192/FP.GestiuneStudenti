from erori.validation_error import ValidError


class ValidatorProblema:
    def __init__(self):
        pass


    def valideaza(self, problema):
        erori = ""
        if problema.get_id_problema()<0:
            erori += "problema invalida!\n"
        if problema.get_descriere()=="":
            erori += "descriere invalida\n"
        if len(erori)>0:
            raise ValidError(erori)