class ValidatorNota:
    def __init__(self):
        pass

    def valideaza(self, nota):
        erori = ""
        if nota.get_nota() < 0 or nota.get_nota() > 10:
            erori += "nota invalida"
        if len(erori)>0:
            raise ValidError(erori)