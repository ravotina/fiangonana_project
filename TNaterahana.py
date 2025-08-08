import datetime
import ConnectionSql, ConversionDate
from datetime import date
class TNahaterahana():
    def __init__(self,idPersonne = "" , DatyNahaterahana = "", ToeranaNahaterahana = ""):
        self._idPersonne = idPersonne
        self._DatyNahaterahana = DatyNahaterahana
        self.ToeranaNahaterahana = ToeranaNahaterahana

        self.conversion = ConversionDate.ConversionDate()
        self.conn = ConnectionSql.ConnectionSql(database="Fiangonana")

    def connectionDataBase(self):
        return self.conn.connectionSql()
        # return Connection.Connection("Membres.db").seconnecter()

    def _setDatyNahaterahana(self, date_string):
        if date_string.strip() == "":
            self._DatyNahaterahana = "01-01-1700"
        else :
            date_object = self.conversion.converteToDate(date_string)
            date_actuelle = datetime.date.today()
            if date_object.date() > date_actuelle:
                raise ValueError("Date future")
            else:
                self._DatyNahaterahana = date_string

    def _getDatyNahaterahana(self):
        return self.conversion.getDate(self._DatyNahaterahana)

    def _setToeranaNahaterahana(self , toernaB_string):
        self.ToeranaNahaterahana=toernaB_string

    def _getToeranaNahaterahana(self):
        return self.ToeranaNahaterahana

    def _setidPersonne(self , idMembre):
        if idMembre == 0 :
            raise ValueError("selectionner un identifiant avant d'enregistrer")
        else:
            self._idPersonne = idMembre

    def _getidPersonne(self):
        return self._idPersonne

    DateNahaterahana = property(_getDatyNahaterahana, _setDatyNahaterahana)
    idPersonne = property(_getidPersonne, _setidPersonne)

    def inserer_dans_table_Nahaterahana(self):
        connexion =  self.connectionDataBase()
        cursor = connexion.cursor()
        nouveau_utilisateur = (None , self._getidPersonne(), self._getDatyNahaterahana() , self.ToeranaNahaterahana)
        cursor.execute("""INSERT INTO Nahaterahana VALUES(%s, %s, %s, %s)""", nouveau_utilisateur)
        connexion.commit()
        cursor.close()
        connexion.close()
    
    def getNahaterahana(self, IdMembre):
        connexion = self.connectionDataBase()
        cursor = connexion.cursor()
        cursor.execute("SELECT * FROM Nahaterahana WHERE IdMembre=%s", (IdMembre, ))
        reponse = cursor.fetchone()
        cursor.close()
        connexion.close()
        return reponse
    
    def getAgeMin(self, AgeMin):
        connexion = self.connectionDataBase()
        cursor = connexion.cursor()
        cursor.execute("SELECT IdMembre, FicheNumero, Anarana, Fanampiny, Telephone FROM Membres WHERE IdMembre IN (SELECT IdMembre FROM v_age WHERE Age >=%s AND Age <= 120)", (AgeMin, ))
        reponse = cursor.fetchall()
        cursor.close()
        connexion.close()
        return reponse
    
    def getAgeMax(self, AgeMax):
        connexion = self.connectionDataBase()
        cursor = connexion.cursor()
        cursor.execute("SELECT IdMembre, FicheNumero, Anarana, Fanampiny, Telephone FROM Membres WHERE IdMembre IN (SELECT IdMembre FROM v_age WHERE Age <=%s AND Age <= 120)", (AgeMax, ))
        reponse = cursor.fetchall()
        cursor.close()
        connexion.close()
        return reponse

    def getAgeEntre(self, AgeMin, AgeMax):
        connexion = self.connectionDataBase()
        cursor = connexion.cursor()
        cursor.execute("SELECT IdMembre, FicheNumero, Anarana, Fanampiny, Telephone FROM Membres WHERE IdMembre IN (SELECT IdMembre FROM v_age WHERE Age >=%s AND Age <=%s AND Age <= 120)", (AgeMin, AgeMax))
        reponse = cursor.fetchall()
        cursor.close()
        connexion.close()
        return reponse
    
    def getDaty(self, IdMembre):
        connexion = self.connectionDataBase()
        cursor = connexion.cursor()
        cursor.execute("SELECT Daty FROM Nahaterahana WHERE IdMembre =%s",(IdMembre, ))
        reponse = cursor.fetchone()
        cursor.close()
        connexion.close()
        if reponse :
            return reponse[0].strftime("%d-%m-%Y")
        else :
            return ""
    
    def getToerana(self, IdMembre):
        connexion = self.connectionDataBase()
        cursor = connexion.cursor()
        cursor.execute("SELECT Toerana FROM Nahaterahana WHERE IdMembre =%s",(IdMembre, ))
        reponse = cursor.fetchone()
        cursor.close()
        connexion.close()
        if reponse :
            return reponse[0]
        else :
            return ""
    
    def modifier_nahaterahana(self, IdMembre):
        connexion = self.connectionDataBase()
        cursor = connexion.cursor()
        membre_modifier = (self._getDatyNahaterahana(), self.ToeranaNahaterahana, IdMembre)
        cursor.execute("UPDATE Nahaterahana SET Daty=%s, Toerana=%s WHERE IdMembre=%s", membre_modifier)
        connexion.commit()
        cursor.close()
        connexion.close()

if __name__=="__main__":
    nahaterahana = TNahaterahana()
    print(nahaterahana.getAgeMin(40))
