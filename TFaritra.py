import ConnectionSql, ConversionDate, re

class TFaritra():
    def __init__(self, NomFaritra = ""):
        self._NomFaritra = NomFaritra
        
        self.conversion = ConversionDate.ConversionDate()

        self.conn = ConnectionSql.ConnectionSql(database="Fiangonana")

    def connectionDataBase(self):
        # return Connection.Connection("Membres.db").seconnecter()
        return self.conn.connectionSql()

    def _setNomFaritra(self , nouveau_faritra):
        pattern = r"F[1-9]_.*"
        if not re.match(pattern, nouveau_faritra):
            raise ValueError("nom faritra incorrect")
        else :
            self._NomFaritra = nouveau_faritra

    def _getNomFaritra(self):
        return self._NomFaritra

    NomFaritra = property(_getNomFaritra, _setNomFaritra)

    def inserer_dans_table_Faritra(self):
        connexion =  self.connectionDataBase()
        cursor = connexion.cursor()
        nouveau_utilisateur = (None, self._getNomFaritra())
        cursor.execute("""INSERT INTO Faritra VALUES(%s, %s)""", nouveau_utilisateur)
        connexion.commit()
        cursor.close()
        connexion.close()
    
    def getFaritra(self):
        connexion = self.connectionDataBase()
        cursor = connexion.cursor()
        cursor.execute("SELECT NomFaritra FROM Faritra")
        reponse = [faritra[0] for faritra in cursor.fetchall()]
        cursor.close()
        connexion.close()
        return reponse

if __name__=="__main__":
    faritra = TFaritra()
    print(faritra.getFaritra())
    

