import ConnectionSql
import re

class TMembres():
    def __init__(self, IdMembre = "", Faritra = "", FicheNumero = "", Anarana = "", Fanampiny = "", Genre = "", 
    Ray = "", Reny = "", Vady = "", Fanompoana = "", Asa = "", Talenta = "", Adiresy = "",
    Telephone = "Aucun numero", Email = "", Pseudo= "" , Fanamariana=""):
        self._IdMembre = IdMembre
        self._Faritra = Faritra
        self._FicheNumero = FicheNumero
        self._Anarana = Anarana
        self.Fanampiny =  Fanampiny
        self._Genre = Genre
        self.Ray = Ray
        self.Reny = Reny
        self.Vady = Vady
        self.Fanompona = Fanompoana
        self.Asa = Asa
        self.Talenta = Talenta
        self.Adiresy = Adiresy
        self._Telephone = Telephone
        self._Email = Email
        self.Pseudo = Pseudo
        self.Fanamariana = Fanamariana

        self.conn = ConnectionSql.ConnectionSql(database="Fiangonana")

    def connectionDataBase(self):
        return self.conn.connectionSql()
        # return Connection.Connection("Membres.db").seconnecter()
    
    def _setIdMembre(self, IdMembre):
        if IdMembre == 0:
            raise ValueError("selectioner un membre svp")
        else :
            self._IdMembre = IdMembre
    
    def _getIdMembre(self):
        return self._IdMembre
    
    def _setTelephone(self, new_telephone):
        if len(new_telephone) < 10 and len(new_telephone) > 0:
            raise ValueError("verfier le numero telephone svp")
        else :
            self._Telephone = new_telephone
    
    def _getTelephone(self):
        return self._Telephone
    
    def _setEmail(self, new_email):
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        match = re.match(pattern, new_email)
        if not match and len(new_email) > 0 :
            raise ValueError("Addresse e-mail invalide")
        else :
            self._Email = new_email
    
    def _getEmail(self):
        return self._Email
    
    def _setAnarana(self, nouveau_anarana):
        if nouveau_anarana.strip() == "":
            raise ValueError("Entrer un nom svp")
        else:
            self._Anarana = nouveau_anarana
    
    def _getAnarana(self):
        return self._Anarana

    def _getFaritra(self):
        return self._Faritra
    
    def _setFaritra(self, nouveau_faritra):
        if nouveau_faritra.strip() == "":
            raise ValueError("Entrer 'Faritra' svp")
        else :
            self._Faritra = nouveau_faritra
    
    def _getFicheNumero(self):
        return self._FicheNumero
    
    def _setFicheNumero(self, nouveau_fiche):
        if nouveau_fiche.strip() == "":
            raise ValueError("Entrer 'Fiche Ankohonana' svp")
        if nouveau_fiche[0]!='F':
            raise ValueError("Numéro Ankohonana incorrect\n Ex : F30001")
        if " " in nouveau_fiche:
            raise ValueError("tsy asina espace ny Numéro Ankohonana")
        if len(nouveau_fiche)>=2 and nouveau_fiche[1]>= '6':
            raise ValueError("Numéro Ankohonana incorrect")
        else :
            self._FicheNumero = nouveau_fiche
    
    def _setGenre(self, nouveau_genre):
        self._Genre = nouveau_genre

    def _getGenre(self):
        return self._Genre

    IdMembre = property(_getIdMembre, _setIdMembre)
    Telephone = property(_getTelephone, _setTelephone)
    Email = property(_getEmail, _setEmail)
    Anarana = property(_getAnarana, _setAnarana)
    Faritra = property(_getFaritra, _setFaritra)
    FicheNumero = property(_getFicheNumero, _setFicheNumero)
    Genre = property (_getGenre, _setGenre)


    def inserer_dans_table(self):
        """atao le cursor.close raha MYSQL leiz"""
        connexion =  self.connectionDataBase()
        cursor = connexion.cursor()
        nouveau_utilisateur = (None, self._getFaritra(), self._getFicheNumero(), self._getAnarana(), self.Fanampiny,self._getGenre(), self.Ray, self.Reny, self.Vady, self.Fanompona, self.Asa, self.Talenta, self.Adiresy, self._getTelephone(), self._getEmail(), self.Pseudo , self.Fanamariana)
        cursor.execute("""INSERT INTO Membres VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""", nouveau_utilisateur)
        connexion.commit()
        cursor.close() 
        connexion.close()
    
    def afficher_contenue(self):
        connexion = self.connectionDataBase()
        cursor = connexion.cursor()
        cursor.execute("SELECT * FROM Membres")
        resultats = cursor.fetchall()
        cursor.close()
        connexion.close()
        return resultats
    
    def suprimer_tout(self):
        connexion = self.connectionDataBase()
        cursor = connexion.cursor()
        cursor.execute("DELETE FROM Membres")
        connexion.commit()
        cursor.close()
        connexion.close()
    
    def getContentTable(self):
        connexion = self.connectionDataBase()
        cursor = connexion.cursor()
        cursor.execute("SELECT * FROM Membres")
        reponse = [(res[0], res[2], res[3], res[4] ,res[13]) for res in cursor.fetchall()]
        cursor.close()
        connexion.close()
        return tuple(reponse)
    
    def getMembre(self, idMembre):
        connexion = self.connectionDataBase()
        cursor = connexion.cursor()
        cursor.execute("SELECT * FROM Membres WHERE idMembre=%s", (idMembre, ))
        reponse = cursor.fetchone()
        cursor.close()
        connexion.close()
        return reponse
    
    def getMembreNonBatiser(self):
        membre_non_batiser = "SELECT * FROM Membres WHERE IdMembre NOT IN (SELECT IdMembre FROM Batisa)"
        connexion = self.connectionDataBase()
        cursor = connexion.cursor()
        cursor.execute(membre_non_batiser)
        reponse = cursor.fetchall()
        cursor.close()
        connexion.close()
        return reponse
    
    def getMembreBatiser(self, daty_doner):
        # membre_batiser = "SELECT * FROM Membres WHERE IdMembre IN (SELECT IdMembre FROM Batisa WHERE year(Daty) = %s AND Daty <> '1700-01-01'", (daty_doner, )
        connexion = self.connectionDataBase()
        cursor = connexion.cursor()
        cursor.execute("SELECT IdMembre, FicheNumero, Anarana, Fanampiny, Telephone FROM Membres WHERE IdMembre IN (SELECT IdMembre FROM Batisa WHERE year(Daty) = %s AND Daty <> '1700-01-01')", (daty_doner, ))
        reponse = cursor.fetchall()
        cursor.close()
        connexion.close()
        return reponse
    
    def getMembreMpivady(self, daty_doner):
        connexion = self.connectionDataBase()
        cursor = connexion.cursor()
        cursor.execute("SELECT IdMembre, FicheNumero, Anarana, Fanampiny, Telephone FROM Membres WHERE IdMembre IN (SELECT IdMembre1 FROM Fanamasinana WHERE year(Daty) = %s AND Daty <> '1700-01-01')", (daty_doner, ))
        reponse = cursor.fetchall()
        cursor.close()
        connexion.close()
        return reponse
    
    def getMembreMpandray(self , daty_doner):
        # membre_mpandray = "SELECT * FROM Membres WHERE IdMembre IN (SELECT IdMembre FROM Mpandray Daty <> '1700-01-01')"
        connexion = self.connectionDataBase()
        cursor = connexion.cursor()
        cursor.execute("SELECT IdMembre, FicheNumero, Anarana, Fanampiny, Telephone FROM Membres WHERE IdMembre IN (SELECT IdMembre FROM mpandray WHERE year(Daty) = %s AND Daty <> '1700-01-01')", (daty_doner, ))
        reponse = cursor.fetchall()
        cursor.close()
        connexion.close()
        return reponse
    
    def getMembreBatiserSyMpandray(self):
        membre_mpandray = "SELECT * FROM Membres WHERE IdMembre IN (SELECT IdMembre FROM Mpandray Daty <> '1700-01-01' ) AND IdMembre IN (SELECT IdMembre FROM Batisa Daty <> '1700-01-01')"
        connexion = self.connectionDataBase()
        cursor = connexion.cursor()
        cursor.execute(membre_mpandray)
        reponse = cursor.fetchall()
        cursor.close()
        connexion.close()
        return reponse
    
    def getFaritra(self, IdMembre):
        connexion = self.connectionDataBase()
        cursor = connexion.cursor()
        cursor.execute("SELECT Faritra FROM Membres WHERE IdMembre =%s",(IdMembre, ))
        reponse = cursor.fetchone()
        cursor.close()
        connexion.close()
        if reponse:
            return reponse[0]
        else :
            return ""
    
    def getFicheNumero(self, IdMembre):
        connexion = self.connectionDataBase()
        cursor = connexion.cursor()
        cursor.execute("SELECT FicheNumero FROM Membres WHERE IdMembre =%s",(IdMembre, ))
        reponse = cursor.fetchone()
        cursor.close()
        connexion.close()
        if reponse:
            return reponse[0]
        else :
            return ""

    def getAnarana(self, IdMembre):
        connexion = self.connectionDataBase()
        cursor = connexion.cursor()
        cursor.execute("SELECT Anarana FROM Membres WHERE IdMembre =%s",(IdMembre, ))
        reponse = cursor.fetchone()
        cursor.close()
        connexion.close()
        if reponse:
            return reponse[0]
        else :
            return ""
    
    def getFanampiny(self, IdMembre):
        connexion = self.connectionDataBase()
        cursor = connexion.cursor()
        cursor.execute("SELECT Fanampiny FROM Membres WHERE IdMembre =%s",(IdMembre, ))
        reponse = cursor.fetchone()
        cursor.close()
        connexion.close()
        if reponse:
            return reponse[0]
        else :
            return ""
    
    def getGenre(self, IdMembre):
        connexion = self.connectionDataBase()
        cursor = connexion.cursor()
        cursor.execute("SELECT Genre FROM Membres WHERE IdMembre =%s",(IdMembre, ))
        reponse = cursor.fetchone()
        cursor.close()
        connexion.close()
        if reponse:
            return reponse[0]
        else :
            return ""
    
    def getRay(self, IdMembre):
        connexion = self.connectionDataBase()
        cursor = connexion.cursor()
        cursor.execute("SELECT Ray FROM Membres WHERE IdMembre =%s",(IdMembre, ))
        reponse = cursor.fetchone()
        cursor.close()
        connexion.close()
        if reponse:
            return reponse[0]
        else :
            return ""
    
    def getReny(self, IdMembre):
        connexion = self.connectionDataBase()
        cursor = connexion.cursor()
        cursor.execute("SELECT Reny FROM Membres WHERE IdMembre =%s",(IdMembre, ))
        reponse = cursor.fetchone()
        cursor.close()
        connexion.close()
        if reponse:
            return reponse[0]
        else :
            return ""
    
    def getVady(self, IdMembre):
        connexion = self.connectionDataBase()
        cursor = connexion.cursor()
        cursor.execute("SELECT Vady FROM Membres WHERE IdMembre =%s",(IdMembre, ))
        reponse = cursor.fetchone()
        cursor.close()
        connexion.close()
        if reponse:
            return reponse[0]
        else :
            return ""
    
    def getFanompona(self, IdMembre):
        connexion = self.connectionDataBase()
        cursor = connexion.cursor()
        cursor.execute("SELECT Fanompona FROM Membres WHERE IdMembre =%s",(IdMembre, ))
        reponse = cursor.fetchone()
        cursor.close()
        connexion.close()
        if reponse:
            return reponse[0]
        else :
            return ""
    
    # def getSampana(self, IdMembre):
    #     connexion = self.connectionDataBase()
    #     cursor = connexion.cursor()
    #     cursor.execute("SELECT Sampana FROM Membres WHERE IdMembre =?",(IdMembre, ))
    #     reponse = cursor.fetchone()
    #     connexion.close()
    #     if reponse:
    #         return reponse[0]
    #     else :
    #         return ""
    
    # def getFianarana(self, IdMembre):
    #     connexion = self.connectionDataBase()
    #     cursor = connexion.cursor()
    #     cursor.execute("SELECT Fianarana FROM Membres WHERE IdMembre =?",(IdMembre, ))
    #     reponse = cursor.fetchone()
    #     connexion.close()
    #     if reponse:
    #         return reponse[0]
    #     else :
    #         return ""
    
    def getAsa(self, IdMembre):
        connexion = self.connectionDataBase()
        cursor = connexion.cursor()
        cursor.execute("SELECT Asa FROM Membres WHERE IdMembre =%s",(IdMembre, ))
        reponse = cursor.fetchone()
        cursor.close()
        connexion.close()
        if reponse:
            return reponse[0]
        else :
            return ""
    
    def getTalenta(self, IdMembre):
        connexion = self.connectionDataBase()
        cursor = connexion.cursor()
        cursor.execute("SELECT Talenta FROM Membres WHERE IdMembre =%s",(IdMembre, ))
        reponse = cursor.fetchone()
        cursor.close()
        connexion.close()
        if reponse:
            return reponse[0]
        else :
            return ""
    
    def getAdiresy(self, IdMembre):
        connexion = self.connectionDataBase()
        cursor = connexion.cursor()
        cursor.execute("SELECT Adiresy FROM Membres WHERE IdMembre =%s",(IdMembre, ))
        reponse = cursor.fetchone()
        cursor.close()
        connexion.close()
        if reponse:
            return reponse[0]
        else :
            return ""
    
    def getTelephone(self, IdMembre):
        connexion = self.connectionDataBase()
        cursor = connexion.cursor()
        cursor.execute("SELECT Telephone FROM Membres WHERE IdMembre =%s",(IdMembre, ))
        reponse = cursor.fetchone()
        cursor.close()
        connexion.close()
        if reponse:
            return reponse[0]
        else :
            return ""

    def getEmail(self, IdMembre):
        connexion = self.connectionDataBase()
        cursor = connexion.cursor()
        cursor.execute("SELECT Email FROM Membres WHERE IdMembre =%s",(IdMembre, ))
        reponse = cursor.fetchone()
        cursor.close()
        connexion.close()
        if reponse:
            return reponse[0]
        else :
            return ""
    
    def getPseudo(self, IdMembre):
        connexion = self.connectionDataBase()
        cursor = connexion.cursor()
        cursor.execute("SELECT Pseudo FROM Membres WHERE IdMembre =%s",(IdMembre, ))
        reponse = cursor.fetchone()
        cursor.close()
        connexion.close()
        if reponse:
            return reponse[0]
        else :
            return ""

    def getFanamarihana(self , IdMembre):
        connexion = self.connectionDataBase()
        cursor = connexion.cursor()
        cursor.execute("SELECT Fanamariana FROM Membres WHERE IdMembre =%s",(IdMembre, ))
        reponse = cursor.fetchone()
        cursor.close()
        connexion.close()
        if reponse:
            return reponse[0]
        else :
            return ""
    
    def modifier_membre(self, IdMembre):
        connexion = self.connectionDataBase()
        cursor = connexion.cursor()
        membre_modifier = (self._getFaritra(), self._getFicheNumero(), self._getAnarana(), self.Fanampiny, self._getGenre(), self.Ray, self.Reny, self.Vady, self.Fanompona, self.Asa, self.Talenta, self.Adiresy, self._getTelephone(), self._getEmail(), self.Pseudo,  self.Fanamariana , IdMembre)
        cursor.execute("UPDATE Membres SET Faritra=%s, FicheNumero=%s, Anarana=%s, Fanampiny=%s, Genre=%s, Ray=%s, Reny=%s, Vady=%s, Fanompona=%s, Asa=%s, Talenta=%s, Adiresy=%s, Telephone=%s, Email=%s, Pseudo=%s , Fanamariana=%s WHERE IdMembre=%s", membre_modifier)
        connexion.commit()
        cursor.close()
        connexion.close()

    def getMontantAdidyParFaritra(self, Month=0, Year="", Faritra=""):
        criteres = list()
        connexion = self.connectionDataBase()
        cursor = connexion.cursor()
        requette  = "SELECT Membres.Faritra, SUM(Adidy.Adidy) AS Montant FROM Adidy JOIN Membres ON Adidy.IdMembre = Membres.IdMembre WHERE 1 = 1"
        if Month != 0:
            requette += " AND MONTH(Adidy.Daty) = %s"
            criteres.append(Month)
        if Year.strip() != "" :
            requette += " AND YEAR(Adidy.Daty) = %s"
            criteres.append(Year)
        if Faritra.strip() != "":
            requette += " AND Membres.Faritra LIKE %s"
            criteres.append("%" + Faritra + "%")
        requette += " GROUP BY Membres.Faritra"
        cursor.execute(requette, tuple(criteres))
        reponse = cursor.fetchall()
        cursor.close()
        connexion.close()
        return reponse
    
    
    def getMontantAdidyParAnkohonana(self, Month=0, Year="", FicheNumero=""):
        criteres = list()
        connexion = self.connectionDataBase()
        cursor = connexion.cursor()
        requette  = "SELECT Membres.FicheNumero, SUM(Adidy.Adidy) AS Montant FROM Adidy JOIN Membres ON Adidy.IdMembre = Membres.IdMembre WHERE 1 = 1"
        if Month != 0:
            requette += " AND MONTH(Adidy.Daty) = %s"
            criteres.append(Month)
        if Year.strip() != "":
            requette += " AND YEAR(Adidy.Daty) = %s"
            criteres.append(Year)
        if FicheNumero.strip() != "":
            requette += " AND Membres.FicheNumero LIKE %s"
            criteres.append("%" + FicheNumero + "%")
        requette += " GROUP BY Membres.FicheNumero"
        cursor.execute(requette, tuple(criteres))
        reponse = cursor.fetchall()
        cursor.close()
        connexion.close()
        return reponse

    def getAllFicheNumero(self):
        connexion = self.connectionDataBase()
        cursor = connexion.cursor()
        cursor.execute("SELECT DISTINCT(FicheNumero) FROM Membres")
        reponse = [FicheNumero[0] for FicheNumero in cursor.fetchall()]
        cursor.close()
        connexion.close()
        return reponse

if __name__=="__main__":
    Membres = TMembres()
    # Membres.Faritra = 'Analamanga'
    # Membres.FicheNumero = '0026'
    # Membres.Anarana = "Ity Le Izy"
    # Membres.Fanampiny = "Letoto"
    # Membres.Ray="Ray"
    # Membres.Genre=""
    # Membres.Reny = "Reny"
    # Membres.Vady = "Vady"
    # Membres.Fanompona = "Manompo"
    # Membres.Asa ="Asa antrano"
    # Membres.Talenta = "Talenta gasy"
    # Membres.Adiresy = "Marambitsy"
    # Membres.Telephone = "0341245622"
    # Membres.Email = "example@gmail.com"
    # Membres.Pseudo="example"
    # Membres.Fanamariana="Fanamarihana"
    # Membres.modifier_membre(8)
    print(Membres.getMembreBatiser(2000))
