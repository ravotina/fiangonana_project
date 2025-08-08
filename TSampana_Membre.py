import ConnectionSql

class TSampana_Membre():
    def __init__(self, IdSampanaMembre = "", IdSampana = "", IdMembre = ""):
        self.IdSampanaMembre = IdSampanaMembre
        self._IdSampana = IdSampana
        self._IdMembre = IdMembre
        self.conn = ConnectionSql.ConnectionSql(database="Fiangonana")
    def connectionDataBase(self):
        return self.conn.connectionSql()
        # return Connection.Connection("Membres.db").seconnecter()

    def _setIdMembre(self, IdMembre):
        if IdMembre == 0:
            raise ValueError("selectioner un membre svp")
        else :
            self._IdMembre = IdMembre

    def _getIdMembre(self):
        return self._IdMembre

    def _setIdSampana(self, IdSampana):
         self._IdSampana = IdSampana

    def _getIdSampana(self):
        return self._IdSampana
    
    IdMembre = property(_getIdMembre, _setIdMembre)
    IdSampana = property(_getIdSampana, _setIdSampana)


    def inserer_dans_table_Sampana_Membre(self):
        connexion =  self.connectionDataBase()
        cursor = connexion.cursor()
        nouveau_utilisateur = (None,self._getIdSampana(), self._getIdMembre())
        cursor.execute("""INSERT INTO SampanaMembre VALUES(%s, %s, %s)""", nouveau_utilisateur)
        connexion.commit()
        cursor.close()
        connexion.close()

    def getIdSampana(self, IdMembre):
        connexion = self.connectionDataBase()
        cursor = connexion.cursor()
        cursor.execute("SELECT IdSampana FROM SampanaMembre WHERE IdMembre=%s", (IdMembre, ))
        reponse = [IdSampana[0] for IdSampana in cursor.fetchall()]
        cursor.close()
        connexion.close()
        return reponse
    
    def suprimer_sampana_membre(self, IdMembre):
        connexion = self.connectionDataBase()
        cursor = connexion.cursor()
        membre_suprimer = (IdMembre, )
        cursor.execute("DELETE FROM SampanaMembre WHERE IdMembre=%s", membre_suprimer)
        connexion.commit()
        cursor.close()
        connexion.close()

if __name__=="__main__":
    Sampana_Membre = TSampana_Membre()
    print(Sampana_Membre.getIdSampana(1))
