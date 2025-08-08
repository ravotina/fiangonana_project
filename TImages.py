import ConnectionSql

class TImages():
    def __init__(self, NomImage = "" , IdMembre = ""):
        self._NomImage = NomImage
        self._IdMembre = IdMembre
        self.conn = ConnectionSql.ConnectionSql(database="Fiangonana")
    def connectionDataBase(self):
        return self.conn.connectionSql()
        # return Connection.Connection("Membres.db").seconnecter()
    
    def _setNomImage(self, nouveau_image):
        if nouveau_image.strip() == "":
            raise ValueError("aucune image selectionner")
        else :
            self._NomImage = nouveau_image
    
    def _getNomImage(self):
        return self._NomImage
    
    def _setIdMembre(self, IdMembre):
        if IdMembre == 0:
            raise ValueError("aucun membre selectionner")
        else :
            self._IdMembre = IdMembre
    
    def _getIdMembre(self):
        return self._IdMembre
    
    NomImage = property(_getNomImage, _setNomImage)
    IdMembre = property(_getIdMembre, _setIdMembre)
    
    def inserer_dans_table_image(self):
        connexion =  self.connectionDataBase()
        cursor = connexion.cursor()
        nouveau_image = (None, self._getNomImage() , self._getIdMembre())
        cursor.execute("""INSERT INTO Images VALUES(%s, %s ,%s)""", nouveau_image)
        connexion.commit()
        cursor.close()
        connexion.close()
    
    def getNomImage(self, IdMembre):
        connexion = self.connectionDataBase()
        cursor = connexion.cursor()
        cursor.execute("SELECT NomImage FROM Images WHERE IdMembre =%s",(IdMembre, ))
        reponse = cursor.fetchone()
        cursor.close()
        connexion.close()
        if reponse :
            return reponse[0]
        else :
            return ""

if __name__=="__main__":
    pass