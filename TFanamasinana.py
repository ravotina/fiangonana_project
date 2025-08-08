import datetime
import ConnectionSql, ConversionDate
from datetime import date

class TFanamasinana():
    def __init__(self , idPersonne1 = "", idPersonne2 = "" , DatyFanamasinana = "", ToeranaFanamasinana = ""):
        self._idPersonne1 = idPersonne1
        self._idPersonne2 = idPersonne2
        self._DatyFanamasinana = DatyFanamasinana
        self.ToeranaFanamasinana = ToeranaFanamasinana

        self.conversion = ConversionDate.ConversionDate()
        
        self.conn = ConnectionSql.ConnectionSql(database="Fiangonana")
    def connectionDataBase(self):
        return self.conn.connectionSql()
        # return Connection.Connection("Membres.db").seconnecter()

    def _setDatyFanamasinana(self , date_string):
        if date_string.strip() == "":
            self._DatyFanamasinana = "01-01-1700"
        else :
            date_object = self.conversion.converteToDate(date_string)
            date_actuelle = datetime.date.today()
            if (date_object.date() > date_actuelle):
                raise ValueError("Date future")
            else:
                self._DatyFanamasinana = date_string

    def _getDatyFanamasinana(self):
        return self.conversion.getDate(self._DatyFanamasinana)

    def _setToeranaFanamasinana(self , toernaB_string):
        self.ToeranaFanamasinana=toernaB_string

    def _getToeranaFanamasinana(self):
        return self.ToeranaFanamasinana

    def _setidPersonne1(self , idMembre1):
        if idMembre1 == 0 :
            raise ValueError("selectionner un identifiant avant d'enregistrer")
        else:
            self._idPersonne1 = idMembre1

    def _getidPersonne1(self):
        return self._idPersonne1

    def _setidPersonne2(self , idMembre2):
        if idMembre2 == 0 :
            raise ValueError("selectionner un identifiant avant d'enregistrer")
        else:
            self._idPersonne2 = idMembre2

    def _getidPersonne2(self):
        return self._idPersonne2

    DatyFanamasinana = property(_getDatyFanamasinana, _setDatyFanamasinana)
    idPersonne1 = property(_getidPersonne1, _setidPersonne1)
    idPersonne2 = property(_getidPersonne2, _setidPersonne2)

    def inserer_dans_table_Fanamasinana(self):
        connexion =  self.connectionDataBase()
        cursor = connexion.cursor()
        nouveau_utilisateur = (None, self._getidPersonne1() , self._getidPersonne2(), self._getDatyFanamasinana(), self.ToeranaFanamasinana)
        cursor.execute("""INSERT INTO Fanamasinana VALUES(%s, %s, %s,%s ,%s)""", nouveau_utilisateur)
        connexion.commit()
        cursor.close()
        connexion.close()

    def getFanamasinanaLahy(self, IdMembre1):
        connexion = self.connectionDataBase()
        cursor = connexion.cursor()
        cursor.execute("SELECT * FROM Fanamasinana WHERE IdMembre1=%s", (IdMembre1, ))
        reponse = cursor.fetchone()
        cursor.close()
        connexion.close()
        return reponse

    def getFanamasinanaVavy(self, IdMembre2):
        connexion = self.connectionDataBase()
        cursor = connexion.cursor()
        cursor.execute("SELECT * FROM Fanamasinana WHERE IdMembre2=%s", (IdMembre2, ))
        reponse = cursor.fetchone()
        cursor.close()
        connexion.close()
        return reponse
    
    def getDaty(self, IdMembre):
        connexion = self.connectionDataBase()
        cursor = connexion.cursor()
        cursor.execute("SELECT Daty FROM Fanamasinana WHERE IdMembre1=%s or IdMembre2=%s",(IdMembre, IdMembre))
        reponse = cursor.fetchone()
        cursor.close()
        connexion.close()
        if reponse:
            return reponse[0].strftime("%d-%m-%Y")
        else :
            return ""
    
    def getToerana(self, IdMembre):
        connexion = self.connectionDataBase()
        cursor = connexion.cursor()
        cursor.execute("SELECT Toerana FROM Fanamasinana WHERE IdMembre1=%s or IdMembre2=%s",(IdMembre, IdMembre))
        reponse = cursor.fetchone()
        cursor.close()
        connexion.close()
        if reponse:
            return reponse[0]
        else :
            return ""

if __name__=="__main__":
   pass


