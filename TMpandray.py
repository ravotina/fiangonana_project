import datetime
import ConnectionSql, ConversionDate
from datetime import date

class TMpandray():
    def __init__(self, idPersonne = "" , DatyMpandray = "", ToeranaMpandray = ""):
        self._idPersonne = idPersonne
        self._DatyMpandray = DatyMpandray
        self.ToeranaMpandray = ToeranaMpandray
        
        self.conversion = ConversionDate.ConversionDate()
        self.conn = ConnectionSql.ConnectionSql(database="Fiangonana")
        
    def connectionDataBase(self):
        return self.conn.connectionSql()
        # return Connection.Connection("Membres.db").seconnecter()

    def _setDatyMpandray(self , date_string):
        if date_string.strip() == "":
            self._DatyMpandray = "01-01-1700"
        else :
            date_object = self.conversion.converteToDate(date_string)
            date_actuelle = datetime.date.today()
            if date_object.date() > date_actuelle:
                raise ValueError("Date future")
            else:
                self._DatyMpandray = date_string

    def _getDatyMpandray(self):
        return self.conversion.getDate(self._DatyMpandray)

    def _setToeranaMpandray(self , toernaB_string):
        self.ToeranaMpandray=toernaB_string

    def _getToeranaMpandray(self):
        return self.ToeranaMpandray

    def _setidPersonne(self , idMembre):
        if idMembre == 0 :
            raise ValueError("selectionner un identifiant avant d'enregistrer")
        else:
            self._idPersonne = idMembre

    def _getidPersonne(self):
        return self._idPersonne

    DateMpandray = property(_getDatyMpandray, _setDatyMpandray)
    idPersonne = property(_getidPersonne, _setidPersonne)

    def inserer_dans_table_Mpandray(self):
        connexion =  self.connectionDataBase()
        cursor = connexion.cursor()
        nouveau_utilisateur = (None, self._getidPersonne(), self._getDatyMpandray() , self.ToeranaMpandray)
        cursor.execute("""INSERT INTO Mpandray VALUES(%s, %s, %s,%s)""", nouveau_utilisateur)
        connexion.commit()
        cursor.close()
        connexion.close()
    
    def getMpandray(self, idMembre):
        connexion = self.connectionDataBase()
        cursor = connexion.cursor()
        cursor.execute("SELECT * FROM Mpandray WHERE idMembre=%s", (idMembre, ))
        reponse = cursor.fetchone()
        cursor.close()
        connexion.close()
        return reponse
    
    def getDaty(self, IdMembre):
        connexion = self.connectionDataBase()
        cursor = connexion.cursor()
        cursor.execute("SELECT Daty FROM Mpandray WHERE IdMembre =%s",(IdMembre, ))
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
        cursor.execute("SELECT Toerana FROM Mpandray WHERE IdMembre =%s",(IdMembre, ))
        reponse = cursor.fetchone()
        cursor.close()
        connexion.close()
        if reponse :
            return reponse[0]
        else :
            return ""
    
    def modifier_mpandray(self, IdMembre):
        connexion = self.connectionDataBase()
        cursor = connexion.cursor()
        membre_modifier = (self._getDatyMpandray(), self.ToeranaMpandray, IdMembre)
        cursor.execute("UPDATE Mpandray SET Daty=%s, Toerana=%s WHERE IdMembre=%s", membre_modifier)
        connexion.commit()
        cursor.close()
        connexion.close()
    
    def isExiste (self, DateMpandray, ToeranaMpandray):
        connexion = self.connectionDataBase()
        cursor = connexion.cursor()
        cursor.execute("SELECT IdMpandray FROM Mpandray WHERE Daty =%s AND Toerana =%s ",(DateMpandray, ToeranaMpandray))
        reponse = cursor.fetchone()
        cursor.close()
        connexion.close()
        if reponse :
            return True
        else :
            return False


if __name__=="__main__":
    pass