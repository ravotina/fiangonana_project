import ConnectionSql

class Tmpifidy():
    def __init__(self , Nom_user_valider = ""):
        self._Nom_user_valider = Nom_user_valider
        self.conn = ConnectionSql.ConnectionSql(database="Fiangonana")
    def connectionDataBase(self):
        return self.conn.connectionSql()
        # return Connection.Connection("Membres.db").seconnecter()
    
    def _setNom_user_valider(self, Nom_user_valider):
        if Nom_user_valider == "" :
            raise ValueError("Nom user valider ilay fifiadianana")
        else :
            self._Nom_user_valider = Nom_user_valider
    
    def _getNom_user_valider(self):
        return self._Nom_user_valider
    
    Nom_user_valider = property(_getNom_user_valider, _setNom_user_valider)
    
    def inserer_dans_table_Mpifidy(self):
        connexion =  self.connectionDataBase()
        cursor = connexion.cursor()
        nouveau_user_valide_fifidianana = (None, self._getNom_user_valider())
        cursor.execute("""INSERT INTO Condidah VALUES(%s, %s)""", nouveau_user_valide_fifidianana)
        connexion.commit()
        cursor.close()
        connexion.close()

    def last_id_de_mpifidy(self , user_valider):
        connexion = self.connectionDataBase()
        cursor = connexion.cursor()
        cursor.execute("SELECT IdMpfidy FROM membres WHERE LOWER(Nom_user_valider) = LOWER('%s') ORDER BY IdMpfidy DESC LIMIT 1",(user_valider, ))
        reponse = cursor.fetchone()
        cursor.close()
        connexion.close()
        if reponse :
            return reponse[0]
        else :
            return ""

    
    def get_liste_user(self, sexe):
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