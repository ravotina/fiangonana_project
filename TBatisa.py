import datetime
import ConnectionSql, ConversionDate
from datetime import date

class TBatisa():
    def __init__(self,idPersonne = "" , DatyBatisa = "", ToeranaBatisa = ""):
        self._idPersonne = idPersonne
        self._DatyBatisa = DatyBatisa
        self.ToeranaBatisa = ToeranaBatisa

        self.conversion = ConversionDate.ConversionDate()
        self.conn = ConnectionSql.ConnectionSql(database="Fiangonana")
        
    def connectionDataBase(self):
        return self.conn.connectionSql()
        #return Connection.Connection("Membres.db").seconnecter()

    def _setDatyBatisa(self , date_string):
        if date_string.strip() == "":
            self._DatyBatisa = "01-01-1700"
        else :
            date_object = self.conversion.converteToDate(date_string)
            date_actuelle = datetime.date.today()
            if date_object.date() > date_actuelle:
                raise ValueError("Date future")
            else:
                self._DatyBatisa = date_string
        
       

    def _getDatyBatisa(self):
        return self.conversion.getDate(self._DatyBatisa)

    def _setToeranaBatisa(self , toernaB_string):
        self.ToeranaBatisa=toernaB_string

    def _getToeranaBatisa(self):
        return self.ToeranaBatisa

    def _setidPersonne(self , idMembre):
        if idMembre == 0 :
            raise ValueError("selectionner un identifiant avant d'enregistrer")
        else:
            self._idPersonne = idMembre

    def _getidPersonne(self):
        return self._idPersonne

    DateBatisa = property(_getDatyBatisa, _setDatyBatisa)
    idPersonne = property(_getidPersonne, _setidPersonne)

    def inserer_dans_table_batisa(self):
        connexion =  self.connectionDataBase()
        cursor = connexion.cursor()
        nouveau_utilisateur = (None, self.idPersonne, self._getDatyBatisa() , self.ToeranaBatisa)
        cursor.execute("""INSERT INTO Batisa VALUES(%s, %s, %s,%s)""", nouveau_utilisateur)
        connexion.commit()
        cursor.close()
        connexion.close()

    def getBatisa(self, IdMembre):
        connexion = self.connectionDataBase()
        cursor = connexion.cursor()
        cursor.execute("SELECT * FROM Batisa WHERE IdMembre=%s", (IdMembre, ))
        reponse = cursor.fetchone()
        cursor.close()
        connexion.close()
        return reponse
    
    def getDaty(self, IdMembre):
        connexion = self.connectionDataBase()
        cursor = connexion.cursor()
        cursor.execute("SELECT Daty FROM Batisa WHERE IdMembre =%s",(IdMembre, ))
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
        cursor.execute("SELECT Toerana FROM Batisa WHERE IdMembre =%s",(IdMembre, ))
        reponse = cursor.fetchone()
        cursor.close()
        connexion.close()
        if reponse :
            return reponse[0]
        else :
            return ""
    
    def modifier_batisa(self, IdMembre):
        connexion = self.connectionDataBase()
        cursor = connexion.cursor()
        membre_modifier = (self._getDatyBatisa(), self.ToeranaBatisa, IdMembre)
        cursor.execute("UPDATE Batisa SET Daty=%s, Toerana=%s WHERE IdMembre=%s", membre_modifier)
        connexion.commit()
        cursor.close()
        connexion.close()

    
if __name__=="__main__":
   pass


