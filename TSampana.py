import ConnectionSql, ConversionDate

class TSampana():
    def __init__(self, NomSampana = ""):
        self._NomSampana = NomSampana
        
        self.conversion = ConversionDate.ConversionDate()
        self.conn = ConnectionSql.ConnectionSql(database="Fiangonana")
        
    def connectionDataBase(self):
        return self.conn.connectionSql()
        # return Connection.Connection("Membres.db").seconnecter()

    def _setNomSampana(self, nouveau_anarana):
        if (nouveau_anarana.strip() == ""):
            raise ValueError("Le Nom Sampana est Obligatoire")
        else :
            self._NomSampana = nouveau_anarana

    def _getNomSampana(self):
        return self._NomSampana
    
    NomSampana = property(_getNomSampana, _setNomSampana)

    def inserer_dans_table_Sampana(self):
        connexion =  self.connectionDataBase()
        cursor = connexion.cursor()
        nouveau_utilisateur = (None, self._getNomSampana())
        cursor.execute("""INSERT INTO Sampana VALUES(%s, %s)""", nouveau_utilisateur)
        connexion.commit()
        cursor.close()
        connexion.close()

    def getSampana(self):
        connexion = self.connectionDataBase()
        cursor = connexion.cursor()
        cursor.execute("SELECT NomSampana FROM Sampana")
        reponse = [Sampana[0] for Sampana in cursor.fetchall()]
        cursor.close()
        connexion.close()
        return reponse
    
    def getIdSamapana(self, NomSampana):
        connexion = self.connectionDataBase()
        cursor = connexion.cursor()
        cursor.execute("SELECT IdSampana FROM Sampana WHERE NomSampana=%s", (NomSampana, ))
        reponse = cursor.fetchone()
        cursor.close()
        connexion.close()
        if reponse :
            return reponse[0]
        else :
            return 0
    
    def getNomSampana(self, IdSampana):
        connexion = self.connectionDataBase()
        cursor = connexion.cursor()
        cursor.execute("SELECT NomSampana FROM Sampana WHERE IdSampana=%s", (IdSampana, ))
        reponse = cursor.fetchone()
        cursor.close()
        connexion.close()
        if reponse :
            return reponse[0]
        else :
            return ""


if __name__=="__main__":
    Sampana = TSampana()
    print(Sampana.getNomSampana("1"))
