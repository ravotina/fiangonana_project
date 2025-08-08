import ConnectionSql

class Tcondidah():
    def __init__(self , IdMembre = ""):
        self._IdMembre = IdMembre
        self.conn = ConnectionSql.ConnectionSql(database="Fiangonana")
    def connectionDataBase(self):
        return self.conn.connectionSql()
        # return Connection.Connection("Membres.db").seconnecter()
    
    def _setIdMembre(self, IdMembre):
        if IdMembre == 0:
            raise ValueError("aucun membre selectionner")
        else :
            self._IdMembre = IdMembre

    def _getIdMembre(self):
        return self._IdMembre
    
    IdMembre = property(_getIdMembre, _setIdMembre)
    
    def inserer_dans_table_condidah(self):
        connexion =  self.connectionDataBase()
        cursor = connexion.cursor()
        nouveau_condidah = (None, self._getIdMembre())
        cursor.execute("""INSERT INTO Condidah VALUES(%s, %s)""", nouveau_condidah)
        connexion.commit()
        cursor.close()
        connexion.close()

    def getCondidah(self):
        connexion = self.connectionDataBase()
        cursor = connexion.cursor()
        cursor.execute("SELECT IdMembre FROM condidah")
        reponse = [condidah[0] for condidah in cursor.fetchall()]
        cursor.close()
        connexion.close()
        return reponse

    def getNumerodeCondidah(self, IdMembre):
        connexion = self.connectionDataBase()
        cursor = connexion.cursor()
        cursor.execute("SELECT IdCondidah FROM condidah WHERE IdMembre=%s", (IdMembre, ))
        reponse = [idcondidah[0] for idcondidah in cursor.fetchall()]
        cursor.close()
        connexion.close()
        return reponse
    
    def getCondidahparsexe(self, sexe):
        connexion = self.connectionDataBase()
        cursor = connexion.cursor()
        cursor.execute("SELECT * FROM Condidah WHERE Condidah.IdMembre IN(SELECT Membres.IdMembre from Membres where Membres.Genre=%s)",(sexe, ))
        reponse = cursor.fetchone()
        cursor.close()
        connexion.close()
        if reponse :
            return reponse[0]
        else :
            return ""

if __name__=="__main__":
    pass