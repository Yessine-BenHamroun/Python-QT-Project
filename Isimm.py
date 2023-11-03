from Etudiant import Etudiant
from Matiere import Matiere
import re

class Isimm:
    def __init__(self):
        self.listEtudiant=[]
        self.listMatiere=[]
        self.listNote=[]
    
    
    def insExiste(self,ins):
        for i in self.listEtudiant:
            if i.num ==ins:
                return 1
        return 0
    
    def codeExiste(self,code):
        for i in self.listMatiere:
            if i.code ==code:
                return 1
        return 0
    
    def verif_num_inscri(self,n_inscri):
        if len(n_inscri)==8 :
            return True
        else:
            return False

    def verif_nom(self,name):
        if 3<=len(name)<=20 and name.isalpha():
            return True
        return False

    def verif_prenom(self,last_name):
        if 3<=len(last_name)<=20 and last_name.isalpha():
            return True
        return False
    
    def verif_adresse(self,adress):
        if 4<len(adress)<50:
            return True
        return False

    def verif_mail(self,email):
        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        if(re.search(regex,email)):   
            return True
        return False

    def verif_tel(self,tel):
        if len(tel)==8:
            return True
        else:
            return False
        
    def verif_code(self,code):
        if len(code)==3:
            return True
        else:
            return False
    
    def verif_desi(self,desi):
        if len(desi)>=3:
            return True
        else:
            return False
    
    def verif_coef(self,coef):
        if 4.0>=float(coef)>0.0:
            return True
        else:
            return False
    
    def verif_note(self,note):
        if 20.0>=float(note)>=0.0:
            return True
        else:
            return False
    
    
    def ajoutEtudiant(self,e):
        self.listEtudiant.append(e)
    
    def suppInscri(self,numIns):
        for i in self.listEtudiant:
            if i.num==numIns:
                self.listEtudiant.remove(i)
    
    def suppSec(self,sec):
        new=[]
        for i in self.listEtudiant:
            if i.section!=sec:
                new.append(i)
        self.listEtudiant=new
    def suppNiv(self,niveau):
        new=[]
        for i in self.listEtudiant:
            if i.niv!=niveau:
                new.append(i)
        self.listEtudiant=new
    
    def suppSecNiv(self,sec,niveau):
        new=[]
        for i in self.listEtudiant:
            if i.section!=sec or i.niv!=niveau:
                new.append(i)
        self.listEtudiant=new
    
    def mdfAdr(self,ins,adr):
        for i in self.listEtudiant:
            if i.num==ins:
                i.adresse=adr
                break
    
    def mdfTel(self,ins,nTel):
        for i in self.listEtudiant:
            if i.num==ins:
                i.tel=nTel
                break
    
    def mdfMail(self,ins,mai):
        for i in self.listEtudiant:
            if i.num==ins:
                i.mail=mai
                break

    def rechIns(self,ins):
        new=[]
        for i in self.listEtudiant:
            if i.num==ins:
                new.append(i)
                break
        return new
    
    def rechSec(self,sec):
        new=[]
        for i in self.listEtudiant:
            if i.section==sec:
                new.append(i)
        return new
    
    def rechSecNiv(self,sec,niveau):
        new=[]
        for i in self.listEtudiant:
            if i.section==sec and i.niv==niveau:
                new.append(i)
        return new

    def rechNiv(self,niveau):
        new=[]
        for i in self.listEtudiant:
            if i.niv==niveau:
                new.append(i)
        return new
    
    def afficherListe(self):
        for i in self.listEtudiant:
            print(i.display())
        
    def afficherListeMat(self):
        for i in self.listMatiere:
            print(i.display())
        
    def ajoutMatiere(self,m):
        self.listMatiere.append(m)
    
    def suppMat(self,c):
        for i in self.listMatiere:
            if i.code==c:
                self.listMatiere.remove(i)
    
    def mdfNom(self,c,n):
        for i in self.listMatiere:
            if i.code==c:
                i.desi=n
                break
    
    def mdfCoef(self,c,coe):
        for i in self.listMatiere:
            if i.code==c:
                i.coef=coe
                break
    
    def rechCode(self,c):
        new=[]
        for i in self.listMatiere:
            if i.code==c:
                new.append(i)
                break
        return new
    
    def rechSecM(self,sec):
        new=[]
        for i in self.listMatiere:
            if i.section==sec:
                new.append(i)
        return new

    def rechSecSem(self,sec,sem):
        new=[]
        for i in self.listMatiere:
            if i.section==sec and i.sem==sem:
                new.append(i)
        return new
    
    def ajoutNote(self,n):
        self.listNote.append(n)
        
    def suppNote(self,n,c):
        for i in self.listNote:
            if i.num==n and i.code==c:
                self.listNote.remove(i)
    
    def mdfNote(self,n,c,d,e):
        for i in self.listNote:
            if i.num==n and i.code==c:
                i.ds=d
                i.ex=e
                break
    
    def afficherListeNote(self):
        for i in self.listNote:
            print(i.display())
            
    def rechInsNote(self,ins):
        new=[]
        for i in self.listNote:
            if i.num==ins:
                new.append(i)
        return new
    
    def rechNum(self,n):
        new=[]
        for i in self.listNote:
            if i.num==n:
                new.append(i)
                break
        return new

    def rechSecNivNote(self,sec,niv):
        new=[]
        for i in self.listEtudiant:
            if i.section==sec and i.niv==niv:
                for j in self.listNote:
                    if i.num==j.num:
                        new.append(j)
                
        return new
    
    def insEtud(self,n):
        for i in self.listEtudiant:
            if i.num==n:
                return i
    
    def rechSemM(self,sem):
        new=[]
        for i in self.listMatiere:
            if i.sem==sem:
                new.append(i)
        return new

    def rechSemNote(self,sem):
        mat=self.rechSemM(sem)
        new=[]
        for i in mat:
            for j in self.listNote:
                if i.code==j.code:
                    new.append(j)
        return new
    
    def rechInsSem(self,num,sem):
        etu=self.insEtud(num)
        note=self.rechSemNote(sem)
        new=[]
        for i in note:
            if i.num==etu.num:
                new.append(i)
        return new
        
    
    def moyGen(self,ins):
        note=self.rechInsNote(ins)
        s=0.0
        c=0.0
        for i in note:
            for j in self.listMatiere:
                if i.code==j.code:
                    c+=float(j.coef)
                    s+=(float(i.ds)*0.3+float(i.ex)*0.7)*float(j.coef)
        return s/c
    
    def totCoef(self,ins):
        note=self.rechInsNote(ins)
        c=0.0
        for i in note:
            for j in self.listMatiere:
                if i.code==j.code:
                    c+=float(j.coef)
        return c
    
    def moyMat(self,ins,code):
        note=self.rechInsNote(ins)
        s=0.0
        for i in note:
            if i.code==code:
                s=(float(i.ds)*0.3+float(i.ex)*0.7)
                break
        return s
        
    def desMat(self,code):
        for i in self.listMatiere:
            if i.code == code:
                return i.desi
            
    def coefMat(self,code):
        for i in self.listMatiere:
            if i.code == code:
                return i.coef
            
    def moySem(self,ins,sem):
        note=self.rechInsNote(ins)
        s=0.0
        c=0.0
        for i in note:
            for j in self.listMatiere:
                if i.code==j.code and j.sem==sem:
                    c+=float(j.coef)
                    s+=(float(i.ds)*0.3+float(i.ex)*0.7)*float(j.coef)
        return s/c
    
    def admiSec(self,sec):
        etu=self.rechSec(sec)
        new=[]
        for i in etu:
            if self.moyGen(i.num)>=10.0:
                new.append(i)
        return new
    
    def redSec(self,sec):
        etu=self.rechSec(sec)
        new=[]
        for i in etu:
            if self.moyGen(i.num)<10.0:
                new.append(i)
        return new
    
    def admiIsimm(self):
        new=[]
        for i in self.listEtudiant:
            if self.moyGen(i.num)>=10.0:
                new.append(i)
        return new
    
    def redIsimm(self):
        new=[]
        for i in self.listEtudiant:
            if self.moyGen(i.num)<10.0:
                new.append(i)
        return new
