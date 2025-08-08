import ConnectionSql

class TFifidiananaL():
    def __init__(self , IdMpifidy = "" ,IdCondidah =""):
        self._IdMpifidy = IdMpifidy
        self._IdCondidah = IdCondidah
        self.conn = ConnectionSql.ConnectionSql(database="Fiangonana")
    def connectionDataBase(self):
        return self.conn.connectionSql()
        # return Connection.Connection("Membres.db").seconnecter()
    
    def _setIdMpifidy(self, IdMpifidy):
        if IdMpifidy == 0 or IdMpifidy == "":
            raise ValueError("Numero Mpifidy svp!!")
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
    
    def inserer_dans_table_FifidiananaL(self):
        connexion =  self.connectionDataBase()
        cursor = connexion.cursor()
        nouveau_condidah = (None, self._getIdMpifidy() , self._getIdCondidah())
        cursor.execute("""INSERT INTO FifidiananaL VALUES(%s, %s , %s)""", nouveau_condidah)
        connexion.commit()
        cursor.close()
        connexion.close()


    def tester_les_mpifidy_existe(self, Numero_mpify):
        try:
            connexion = self.connectionDataBase()
            with connexion.cursor() as cursor:
                cursor.execute("SELECT 1 FROM Fifidiananal WHERE NumeroMpifidy=%s", (Numero_mpify, ))
                result = cursor.fetchall()
                print(result)
                if not result: 
                    return 0
                else:
                    return 1
        finally:
            if connexion:
                connexion.close()

    def tester_les_mpifidy_existe_Ajour(self, Numero_mpify):
        try:
            connexion = self.connectionDataBase()
            with connexion.cursor() as cursor:
                cursor.execute("SELECT 1 FROM fifidiananaajour WHERE NumeroMpifidy=%s", (Numero_mpify, ))
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
                cursor.execute("SELECT 1 FROM vatomanakeryl WHERE Numero=%s", (Numero_mpify, ))
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
                cursor.execute("SELECT 1 FROM vatomatyl WHERE Numero=%s", (Numero_mpify, ))
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
                cursor.execute("SELECT 1 FROM vatofotsyl WHERE Numero=%s", (Numero_mpify, ))
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
        cursor.execute("SELECT NumeroCondidah FROM FifidiananaL WHERE NumeroMpifidy=%s", (Idmpifidy, ))
        reponse = [IdSampana[0] for IdSampana in cursor.fetchall()]
        cursor.close()
        connexion.close()
        return reponse

    def suprimer_fifidianana_voter(self, idMpifidy):
        connexion = self.connectionDataBase()
        cursor = connexion.cursor()
        FifidiananaL_suprimer = (idMpifidy, )
        cursor.execute("DELETE FROM FifidiananaL WHERE NumeroMpifidy=%s", FifidiananaL_suprimer)
        connexion.commit()
        cursor.close()
        connexion.close()

    
    def get_fidin_Mpifidy(self, idMpifidy_recherch):
        connexion = self.connectionDataBase()
        cursor = connexion.cursor()
        cursor.execute("SELECT * FROM FifidiananaL WHERE FifidiananaL.NumeroMpifidy=%s",(idMpifidy_recherch, ))
        reponse = cursor.fetchone()
        cursor.close()
        connexion.close()
        if reponse :
            return reponse[0]
        else :
            return ""

if __name__=="__main__":
    pass