import ConnectionSql

class MombaNyVato():
    def __init__(self , IdMpifidy = "" ):
        self._IdMpifidy = IdMpifidy
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
    
    IdMpifidy = property(_getIdMpifidy, _setIdMpifidy)




    def inserer_dans_table_FifidiananaLAjourEny(self):
        connexion =  self.connectionDataBase()
        cursor = connexion.cursor()
        nouveau_condidah = (None, self._getIdMpifidy() , "ENY")
        cursor.execute("""INSERT INTO fifidiananaajour VALUES(%s, %s , %s)""", nouveau_condidah)
        connexion.commit()
        cursor.close() 
        connexion.close()

    def inserer_dans_table_FifidiananaLAjourTsia(self):
        connexion =  self.connectionDataBase()
        cursor = connexion.cursor()
        nouveau_condidah = (None, self._getIdMpifidy() , "TSIA")
        cursor.execute("""INSERT INTO fifidiananaajour VALUES(%s, %s , %s)""", nouveau_condidah)
        connexion.commit()
        cursor.close()
        connexion.close()

    def inserer_dans_table_vatomanakeryL(self):
        connexion =  self.connectionDataBase()
        cursor = connexion.cursor()
        nouveau_condidah = (None, self._getIdMpifidy() )
        cursor.execute("""INSERT INTO vatomanakeryL VALUES(%s, %s)""", nouveau_condidah)
        connexion.commit()
        cursor.close()
        connexion.close()
    
    def inserer_dans_table_vatomanakeryV(self):
        connexion =  self.connectionDataBase()
        cursor = connexion.cursor()
        nouveau_condidah = (None, self._getIdMpifidy())
        cursor.execute("""INSERT INTO vatomanakeryV VALUES(%s, %s)""", nouveau_condidah)
        connexion.commit()
        cursor.close()
        connexion.close()

    def inserer_dans_table_vatoFotsyL(self):
        connexion =  self.connectionDataBase()
        cursor = connexion.cursor()
        nouveau_condidah = (None, self._getIdMpifidy() )
        cursor.execute("""INSERT INTO vatofotsyl VALUES(%s, %s)""", nouveau_condidah)
        connexion.commit()
        cursor.close()
        connexion.close()

    def inserer_dans_table_vatoFotsyV(self):
        connexion =  self.connectionDataBase()
        cursor = connexion.cursor()
        nouveau_condidah = (None, self._getIdMpifidy() )
        cursor.execute("""INSERT INTO vatofotsyV VALUES(%s, %s)""", nouveau_condidah)
        connexion.commit()
        cursor.close()
        connexion.close()

    def inserer_dans_table_vatoMatyL(self):
        connexion =  self.connectionDataBase()
        cursor = connexion.cursor()
        nouveau_condidah = (None, self._getIdMpifidy() )
        cursor.execute("""INSERT INTO vatoMatyL VALUES(%s, %s)""", nouveau_condidah)
        connexion.commit()
        cursor.close()
        connexion.close()

    def inserer_dans_table_vatoMatyV(self):
        connexion =  self.connectionDataBase()
        cursor = connexion.cursor()
        nouveau_condidah = (None, self._getIdMpifidy() )
        cursor.execute("""INSERT INTO vatoMatyV VALUES(%s, %s)""", nouveau_condidah)
        connexion.commit()
        cursor.close()
        connexion.close()





    def suprimer_fifidianana_vatomanakeryL(self, idMpifidy):
        connexion = self.connectionDataBase()
        cursor = connexion.cursor()
        FifidiananaL_suprimer = (idMpifidy, )
        cursor.execute("DELETE FROM vatomanakeryL WHERE Numero=%s", FifidiananaL_suprimer)
        connexion.commit()
        cursor.close()
        connexion.close()

    def suprimer_fifidianana_vatomanakeryV(self, idMpifidy):
        connexion = self.connectionDataBase()
        cursor = connexion.cursor()
        FifidiananaL_suprimer = (idMpifidy, )
        cursor.execute("DELETE FROM vatomanakeryV WHERE Numero=%s", FifidiananaL_suprimer)
        connexion.commit()
        cursor.close()
        connexion.close()

    def suprimer_fifidianana_vatoFotsyL(self, idMpifidy):
        connexion = self.connectionDataBase()
        cursor = connexion.cursor()
        FifidiananaL_suprimer = (idMpifidy, )
        cursor.execute("DELETE FROM vatoFotsyL WHERE Numero=%s", FifidiananaL_suprimer)
        connexion.commit()
        cursor.close()
        connexion.close()

    def suprimer_fifidianana_vatoFotsyV(self, idMpifidy):
        connexion = self.connectionDataBase()
        cursor = connexion.cursor()
        FifidiananaL_suprimer = (idMpifidy, )
        cursor.execute("DELETE FROM vatoFotsyV WHERE Numero=%s", FifidiananaL_suprimer)
        connexion.commit()
        cursor.close()
        connexion.close()

    def suprimer_fifidianana_vatoMatyL(self, idMpifidy):
        connexion = self.connectionDataBase()
        cursor = connexion.cursor()
        FifidiananaL_suprimer = (idMpifidy, )
        cursor.execute("DELETE FROM vatoMatyL WHERE Numero=%s", FifidiananaL_suprimer)
        connexion.commit()
        cursor.close()
        connexion.close()

    def suprimer_fifidianana_vatoMatyV(self, idMpifidy):
        connexion = self.connectionDataBase()
        cursor = connexion.cursor()
        FifidiananaL_suprimer = (idMpifidy, )
        cursor.execute("DELETE FROM vatoMatyV WHERE Numero=%s", FifidiananaL_suprimer)
        connexion.commit()
        cursor.close()
        connexion.close()

if __name__=="__main__":
    pass