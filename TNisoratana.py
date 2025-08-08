import datetime
import ConnectionSql, ConversionDate
from datetime import date


class TNisoratana():
    def __init__(self , idPersonne1 = "", idPersonne2 = "" , DatyNisoratana = ""):
        self._idPersonne1 = idPersonne1
        self._idPersonne2 = idPersonne2
        self._DatyNisoratana = DatyNisoratana

        self.conversion = ConversionDate.ConversionDate()

        self.conn = ConnectionSql.ConnectionSql(database="Fiangonana")
        
    def connectionDataBase(self):
        return self.conn.connectionSql()
        # return Connection.Connection("Membres.db").seconnecter()

    def _setDatyNisoratana(self , date_string):
        if date_string.strip() == "":
            self._DatyNisoratana = "01-01-1700"
        else :
            date_object = self.conversion.converteToDate(date_string)
            date_actuelle = datetime.date.today()
            if (date_object.date() > date_actuelle):
                raise ValueError("Date future")
            else:
                self._DatyNisoratana = date_string

    def _getDatyNisoratana(self):
        return self.conversion.getDate(self._DatyNisoratana)

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

    DatyNisoratana = property(_getDatyNisoratana, _setDatyNisoratana)
    idPersonne1 = property(_getidPersonne1, _setidPersonne1)
    idPersonne2 = property(_getidPersonne2, _setidPersonne2)

    def inserer_dans_table_Nisoratana(self):
        connexion =  self.connectionDataBase()
        cursor = connexion.cursor()
        nouveau_utilisateur = (None, self._getidPersonne1() , self._getidPersonne2() , self._getDatyNisoratana())
        cursor.execute("""INSERT INTO Nisoratana VALUES(%s, %s, %s, %s)""", nouveau_utilisateur)
        connexion.commit()
        cursor.close()
        connexion.close()

    def getNisoratanaLahy(self, IdMembre1):
        connexion = self.connectionDataBase()
        cursor = connexion.cursor()
        cursor.execute("SELECT * FROM Nisoratana WHERE IdMembre1=%s", (IdMembre1, ))
        reponse = cursor.fetchone()
        cursor.close()
        connexion.close()
        return reponse

    def getNisoratanaVavy(self, IdMembre2):
        connexion = self.connectionDataBase()
        cursor = connexion.cursor()
        cursor.execute("SELECT * FROM Nisoratana WHERE IdMembre2=%s", (IdMembre2, ))
        reponse = cursor.fetchone()
        cursor.close()
        connexion.close()
        return reponse
    
    def getDaty(self, IdMembre):
        connexion = self.connectionDataBase()
        cursor = connexion.cursor()
        cursor.execute("SELECT Daty FROM Nisoratana WHERE IdMembre1=%s OR IdMembre2=%s",(IdMembre, IdMembre))
        reponse = cursor.fetchone()
        cursor.close()
        connexion.close()
        if reponse :
            return reponse[0].strftime("%d-%m-%Y")
        else :
            return ""


if __name__=="__main__":
    soratra = TNisoratana()
    print(soratra.getDaty(1))

