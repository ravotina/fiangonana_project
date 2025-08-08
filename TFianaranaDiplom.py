import ConnectionSql

class TFianaranaDiplom():
    def __init__(self, IdFianaranaDiplom = "", IdMembre = "", Fianarana = "" , Diplom = ""):
        self._IdFianaranaDiplom = IdFianaranaDiplom
        self._IdMembre = IdMembre
        self._Fianarana = Fianarana
        self.Diplom = Diplom
        self.conn = ConnectionSql.ConnectionSql(database="Fiangonana")
    def connectionDataBase(self):
        return self.conn.connectionSql()
        # return Connection.Connection("Membres.db").seconnecter()

    def _setIdFianaranaDiplom(self, IdFianaranaDiplom):
        if IdFianaranaDiplom == 0:
            raise ValueError("selectioner un IdFianaranaDiplom svp")
        else :
            self._IdFianaranaDiplom = IdFianaranaDiplom
    
    def _getIdFianaranaDiplom(self):
        return self._IdFianaranaDiplom

    def _setIdMembre(self, IdMembre):
        if IdMembre == 0:
            raise ValueError("selectioner un membre svp")
        else :
            self._IdMembre = IdMembre

    def _getIdMembre(self):
        return self._IdMembre

    def _setFianarana(self, nouveau_fianarana):
        if nouveau_fianarana.strip() == "":
            raise ValueError("Entrer 'Fianarana' svp")
        else :
            self._Fianarana = nouveau_fianarana
    
    def _getFianarana(self):
        return self._Fianarana

    IdMembre = property(_getIdMembre, _setIdMembre)
    Fianarana = property(_getFianarana, _setFianarana)
    IdFianaranaDiplom = property(_getIdFianaranaDiplom, _setIdFianaranaDiplom)

    def inserer_dans_table_Fianarana_diplom(self):
        connexion =  self.connectionDataBase()
        cursor = connexion.cursor()
        nouveau_utilisateur = (None , self._getIdMembre(),self._getFianarana() , self.Diplom)
        cursor.execute("""INSERT INTO FianaranaDiplom VALUES(%s, %s, %s , %s)""", nouveau_utilisateur)
        connexion.commit()
        cursor.close()
        connexion.close()
    
    def getFianarana(self, IdFianaranaDiplom, IdMembre):
        connexion = self.connectionDataBase()
        cursor = connexion.cursor()
        cursor.execute("SELECT Fianarana FROM FianaranaDiplom WHERE IdMembre=%s and IdFianaranaDiplom=%s", (IdMembre, IdFianaranaDiplom))
        reponse = cursor.fetchone()
        cursor.close()
        connexion.close()
        if reponse :
            return reponse[0]
        else :
            return ""
    
    def getDiplome(self, IdFianaranaDiplom, IdMembre):
        connexion = self.connectionDataBase()
        cursor = connexion.cursor()
        cursor.execute("SELECT Diplom FROM FianaranaDiplom WHERE IdMembre=%s and IdFianaranaDiplom=%s", (IdMembre, IdFianaranaDiplom))
        reponse = cursor.fetchone()
        cursor.close()
        connexion.close()
        if reponse :
            return reponse[0]
        else :
            return ""

    def getIdFianaranaDilome(self, IdMembre):
        connexion = self.connectionDataBase()
        cursor = connexion.cursor()
        cursor.execute("SELECT IdFianaranaDiplom FROM FianaranaDiplom WHERE IdMembre=%s", (IdMembre, ))
        reponse = [IdFianarana[0] for IdFianarana in cursor.fetchall()]
        cursor.close()
        connexion.close()
        return reponse
    
    def modifier_fianarana_diplome(self, IdFianaranaDiplom, IdMembre):
        connexion = self.connectionDataBase()
        cursor = connexion.cursor()
        fianarana_modifier = (self._getFianarana(), self.Diplom, IdMembre, IdFianaranaDiplom)
        cursor.execute("UPDATE FianaranaDiplom SET Fianarana=%s, Diplom=%s WHERE IdMembre=%s and IdFianaranaDiplom=%s", fianarana_modifier)
        connexion.commit()
        cursor.close()
        connexion.close()
    
    def getFinaranaDiplomeMembre(self, IdMembre):
        connexion = self.connectionDataBase()
        cursor = connexion.cursor()
        cursor.execute("SELECT * FROM FianaranaDiplom WHERE IdMembre=%s", (IdMembre, ))
        reponse = [(etude[2], etude[3]) for etude in cursor.fetchall()]
        cursor.close()
        connexion.close()
        return reponse
       

if __name__=="__main__":
    fianarana_diplome  = TFianaranaDiplom()
    print(fianarana_diplome.getIdFianaranaDilome(3))
