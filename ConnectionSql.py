import mysql.connector

class ConnectionSql():
    def __init__(self, host = "localhost", user="root", password = "", database = "fiangonana"):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
    
    def connectionSql(self):
        connection = mysql.connector.connect(host=self.host, user=self.user, password=self.password, database = self.database)
        return connection
    
    def requete(self):
        connexion = self.connectionSql()
        cursor = connexion.cursor()
        cursor.execute("SELECT * FROM membres")
        reponse = cursor.fetchall()
        connexion.close()
        return reponse
    
if __name__=="__main__":
    connectsql = ConnectionSql(database="Fiangonana")
    print(connectsql.requete())

