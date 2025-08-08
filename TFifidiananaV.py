import ConnectionSql

class TFifidiananaV():
    def __init__(self , IdMpifidy = "" ,IdCondidah =""):
        self._IdMpifidy = IdMpifidy
        self._IdCondidah = IdCondidah
        self.conn = ConnectionSql.ConnectionSql(database="Fiangonana")
    def connectionDataBase(self):
        return self.conn.connectionSql()
        # return Connection.Connection("Membres.db").seconnecter()
    
    def _setIdMpifidy(self, IdMpifidy):
        if IdMpifidy == 0:
            raise ValueError("id mpifidy introuvalbe")
        else :
            self._IdMpifidy = IdMpifidy
    
    def _getIdMpifidy(self):
        return self._IdMpifidy

    def _setIdCondidah(self, IdCondidah):
        if IdCondidah == 0:
            raise ValueError("id mpifidy introuvalbe")
        else :
            self._IdCondidah = IdCondidah
    
    def _getIdCondidah(self):
        return self._IdCondidah
    
    IdMpifidy = property(_getIdMpifidy, _setIdMpifidy)
    IdCondidah = property(_getIdCondidah, _setIdCondidah)
    
    def inserer_dans_table_FifidiananaV(self):
        connexion =  self.connectionDataBase()
        cursor = connexion.cursor()
        nouveau_condidah = (None, self._getIdMpifidy() , self._getIdCondidah())
        cursor.execute("""INSERT INTO FifidiananaV VALUES(%s, %s , %s)""", nouveau_condidah)
        nouveau_condidah_voting = (self._getIdCondidah())
        cursor.execute("""UPDATE voting SET vote = vote + 1 WHERE NumeroCandidat = %s""", (nouveau_condidah_voting,))
        connexion.commit()
        cursor.close()
        connexion.close()



    def tester_les_mpifidy_existe(self, Numero_mpify):
        try:
            connexion = self.connectionDataBase()
            with connexion.cursor() as cursor:
                cursor.execute("SELECT 1 FROM FifidiananaV WHERE NumeroMpifidy=%s", (Numero_mpify, ))
                result = cursor.fetchall()
                print(result)
                if not result: 
                    return 0
                else:
                    return 1
        finally:
            if connexion:
                connexion.close()

    def tester_les_mpifidy_existe_dans_vato_manakery(self, Numero_mpify):
        try:
            connexion = self.connectionDataBase()
            with connexion.cursor() as cursor:
                cursor.execute("SELECT 1 FROM vatomanakeryv WHERE Numero=%s", (Numero_mpify, ))
                result = cursor.fetchall()
                print(result)
                if not result: 
                    return 0
                else:
                    return 1
        finally:
            if connexion:
                connexion.close()

    def tester_les_mpifidy_existe_dans_vato_maty(self, Numero_mpify):
        try:
            connexion = self.connectionDataBase()
            with connexion.cursor() as cursor:
                cursor.execute("SELECT 1 FROM vatomatyv WHERE Numero=%s", (Numero_mpify, ))
                result = cursor.fetchall()
                print(result)
                if not result: 
                    return 0
                else:
                    return 1
        finally:
            if connexion:
                connexion.close()

    def tester_les_mpifidy_existe_dans_vato_fotsy(self, Numero_mpify):
        try:
            connexion = self.connectionDataBase()
            with connexion.cursor() as cursor:
                cursor.execute("SELECT 1 FROM vatofotsyv WHERE Numero=%s", (Numero_mpify, ))
                result = cursor.fetchall()
                print(result)
                if not result: 
                    return 0
                else:
                    return 1
        finally:
            if connexion:
                connexion.close()
    

    def getIdVoafidy(self, Idmpifidy):
        connexion = self.connectionDataBase()
        cursor = connexion.cursor()
        cursor.execute("SELECT NumeroCondidah FROM FifidiananaV WHERE NumeroMpifidy=%s", (Idmpifidy, ))
        reponse = [IdSampana[0] for IdSampana in cursor.fetchall()]
        cursor.close()
        connexion.close()
        return reponse

    def suprimer_fifidianana_voter(self, idMpifidy):
        connexion = self.connectionDataBase()
        cursor = connexion.cursor()
        FifidiananaV_suprimer = (idMpifidy, )
        cursor.execute("DELETE FROM FifidiananaV WHERE NumeroMpifidy=%s", FifidiananaV_suprimer)
        connexion.commit()
        cursor.close()
        connexion.close()

    def getlesvoafidy(self, idMpifidy):
        # membre_batiser = "SELECT * FROM Membres WHERE IdMembre IN (SELECT IdMembre FROM Batisa WHERE year(Daty) = %s AND Daty <> '1700-01-01'", (daty_doner, )
        connexion = self.connectionDataBase()
        cursor = connexion.cursor()
        FifidiananaV_suprimer = (idMpifidy, )
        cursor.execute("SELECT NumeroCondidah FROM FifidiananaV WHERE NumeroMpifidy=%s", FifidiananaV_suprimer)
        reponse = cursor.fetchall()
        cursor.close()
        connexion.close()
        return reponse
    
    def manalavatoazo(self , numeroCondidah):
        connexion =  self.connectionDataBase()
        cursor = connexion.cursor()
        nouveau_condidah_voting = (numeroCondidah)
        cursor.execute("""UPDATE voting SET vote = vote - 1 WHERE NumeroCandidat = %s""", (nouveau_condidah_voting,))
        connexion.commit()
        cursor.close()
        connexion.close()

    
    def get_fidin_Mpifidy(self, idMpifidy_recherch):
        connexion = self.connectionDataBase()
        cursor = connexion.cursor()
        cursor.execute("SELECT * FROM FifidiananaV WHERE FifidiananaV.NumeroMpifidy=%s",(idMpifidy_recherch, ))
        reponse = cursor.fetchone()
        cursor.close()
        connexion.close()
        if reponse :
            return reponse[0]
        else :
            return ""

if __name__=="__main__":
    pass