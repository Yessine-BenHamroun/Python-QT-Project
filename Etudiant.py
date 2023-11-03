class Etudiant:
    def __init__(self, num,nom,prenom,date,adresse,mail,tel,section,niv):
        self.num=num
        self.nom=nom
        self.prenom=prenom
        self.date=date
        self.adresse=adresse
        self.mail=mail
        self.tel=tel
        self.section=section
        self.niv=niv

    def display(self):
        return "["+self.num+","+self.nom+","+self.prenom+","+self.date+","+self.adresse+","+self.mail+","+self.tel+","+self.section+","+self.niv+"]"


