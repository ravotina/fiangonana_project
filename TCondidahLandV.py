import ConnectionSql

class TCondidahLandV():
    def __init__(self , NumeroCondidah = "" , Nom ="" , Prenom = "" ,Nom_image = ""):
        self._NumeroCondidah = NumeroCondidah
        self._Nom = Nom
        self._Prenom = Prenom
        self._Nom_image = Nom_image
        self.conn = ConnectionSql.ConnectionSql(database="Fiangonana")
    def connectionDataBase(self):
        return self.conn.connectionSql()
        # return Connection.Connection("Membres.db").seconnecter()
    
    def _setNumeroCondidah(self, NumeroCondidah):
        if NumeroCondidah == 0:
            raise ValueError("aucun membre selectionner")
        else :
            self._NumeroCondidah = NumeroCondidah

    def _getNumeroCondidah(self):
        return self._NumeroCondidah


    def _setNom(self, Nom):
        if Nom == "":
            raise ValueError("Anarana tsy mitombina")
        else :
            self._Nom = Nom

    def _getNom(self):
        return self._Nom


    def _setPrenom(self, Prenom):
        self._Prenom = Prenom

    def _getPrenom(self):
        return self._Prenom

    def _setNom_image(self, Nom_image):
        self._Nom_image = Nom_image

    def _getNom_image(self):
        return self._Nom_image


    
    NumeroCondidah = property(_getNumeroCondidah, _setNumeroCondidah)
    Nom = property(_getNom, _setNom)
    Prenom = property(_getPrenom, _setPrenom)
    Nom_image = property(_getNom_image, _setNom_image)

    def getCondidahL(self):
        connexion = self.connectionDataBase()
        cursor = connexion.cursor()
        cursor.execute("SELECT NumeroCondidah FROM CondidahL")
        reponse = [condidah[0] for condidah in cursor.fetchall()]
        cursor.close()
        connexion.close()
        return reponse

    def getCondidahV(self):
        connexion = self.connectionDataBase()
        cursor = connexion.cursor()
        cursor.execute("SELECT NumeroCondidah FROM CondidahV")
        reponse = [condidah[0] for condidah in cursor.fetchall()]
        cursor.close()
        connexion.close()
        return reponse
    
    def inserer_dans_table_CondidahL(self):
        """atao le cursor.close raha MYSQL leiz"""
        connexion =  self.connectionDataBase()
        cursor = connexion.cursor()
        nouveau_utilisateur = (None, self._getNumeroCondidah , self._getNom , self._getPrenom , self._getNom_image)
        cursor.execute("""INSERT INTO CondidahL VALUES(%s, %s, %s, %s, %s)""", nouveau_utilisateur)
        connexion.commit()
        cursor.close() 
        connexion.close()

    def inserer_dans_table_CondidahV(self):
        """atao le cursor.close raha MYSQL leiz"""
        connexion =  self.connectionDataBase()
        cursor = connexion.cursor()
        nouveau_utilisateur = (None, self._getNumeroCondidah , self._getNom , self._getPrenom , self._getNom_image)
        cursor.execute("""INSERT INTO CondidahV VALUES(%s, %s, %s, %s, %s)""", nouveau_utilisateur)
        connexion.commit()
        cursor.close() 
        connexion.close()

    def getCondidahInfoL(self):
        # membre_batiser = "SELECT * FROM Membres WHERE IdMembre IN (SELECT IdMembre FROM Batisa WHERE year(Daty) = %s AND Daty <> '1700-01-01'", (daty_doner, )
        connexion = self.connectionDataBase()
        cursor = connexion.cursor()
        cursor.execute("SELECT FicheNumero, NumeroCondidah , Nom , Prenom , NomImage FROM CondidahL")
        reponse = cursor.fetchall()
        cursor.close()
        connexion.close()
        return reponse

    def getCondidahInfoV(self):
        # membre_batiser = "SELECT * FROM Membres WHERE IdMembre IN (SELECT IdMembre FROM Batisa WHERE year(Daty) = %s AND Daty <> '1700-01-01'", (daty_doner, )
        connexion = self.connectionDataBase()
        cursor = connexion.cursor()
        cursor.execute("SELECT FicheNumero, NumeroCondidah , Nom , Prenom , NomImage FROM CondidahV")
        reponse = cursor.fetchall()
        cursor.close()
        connexion.close()
        return reponse

    


if __name__=="__main__":
    pass