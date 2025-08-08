import datetime
import ConnectionSql, ConversionDate
from datetime import date

class TAdidy():
    def __init__(self, idPersonne = "" , Daty = "", Adidy = 100000):
        self._idPersonne = idPersonne
        self._Daty = Daty
        self._Adidy = Adidy

        self.conversion = ConversionDate.ConversionDate()
        self.conn = ConnectionSql.ConnectionSql(database="Fiangonana")
        
    def connectionDataBase(self):
        return self.conn.connectionSql()
        # return Connection.Connection("Membres.db").seconnecter()

    def _setDaty(self , date_string):
        date_object = self.conversion.converteToDate(date_string)
        date_actuelle = datetime.date.today()
        if (date_object.date() > date_actuelle):
            raise ValueError("Date future")
        else:
            self._Daty = date_string

    def _getDaty(self):
        return self.conversion.getDate(self._Daty)

    def _setAdidy(self , nouveau_adidy):
        if nouveau_adidy < 0:
            raise ValueError("montant invalide")
        else :
            self._Adidy = nouveau_adidy

    def _getAdidy(self):
        return self._Adidy

    def _setidPersonne(self , idMembre):
        if idMembre == 0 :
            raise ValueError("selectionner un identifiant avant d'enregistrer")
        else:
            self._idPersonne = idMembre

    def _getidPersonne(self):
        return self._idPersonne

    Daty= property(_getDaty, _setDaty)
    idPersonne = property(_getidPersonne, _setidPersonne)
    Adidy = property(_getAdidy, _setAdidy)

    def inserer_dans_table_adidy(self):
        connexion =  self.connectionDataBase()
        cursor = connexion.cursor()
        nouveau_utilisateur = (None, self._getidPersonne(), self._getDaty() , self._getAdidy())
        cursor.execute("""INSERT INTO Adidy VALUES(%s, %s, %s,%s)""", nouveau_utilisateur)
        connexion.commit()
        cursor.close()
        connexion.close()

    def getAdidy(self, IdMembre):
        connexion = self.connectionDataBase()
        cursor = connexion.cursor()
        cursor.execute("SELECT * FROM Adidy WHERE IdMembre=%s", (IdMembre, ))
        reponse = cursor.fetchall()
        cursor.close()
        connexion.close()
        return reponse

    def getTotalAdidy(self, IdMembre):
        connexion = self.connectionDataBase()
        cursor = connexion.cursor()
        cursor.execute("SELECT SUM(Adidy), IdMembre FROM Adidy WHERE IdMembre =%s GROUP BY IdMembre", (IdMembre, ))
        reponse = cursor.fetchone()
        cursor.close()
        connexion.close()
        if reponse :
            return reponse[0]
        else :
            return 0
    
if __name__=="__main__":
   adidy = TAdidy()
   print(adidy.getTotalAdidy(1))


