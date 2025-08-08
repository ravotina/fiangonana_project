import tkinter, mysql.connector, TMembres, ConnectionSql
from tkinter import messagebox
import ConnectionSql, ApplicationClient

class ConnectPass():
    def __init__(self, master):
        self.master = master
        
        self.font = ("Bell MT", 12, "bold")
        self.padx = 2
        self.pady = 2

        self.varAddresseIP = tkinter.StringVar()

        self.membre = TMembres.TMembres()
        
        self.connexion = None

        self.frame = tkinter.Frame(self.master)
        self.frame.grid(row=0, column=0, sticky=tkinter.NSEW)
        self.lblInsererIP = tkinter.Label(self.frame, text="Addresse IP", font=self.font)
        self.lblInsererIP.grid(row=0, column=0, padx=self.padx, pady=self.pady)
        self.txtInsererIP = tkinter.Entry(self.frame, font=self.font, textvariable=self.varAddresseIP, justify=tkinter.CENTER)
        self.txtInsererIP.grid(row=0, column=1, padx=self.padx, pady=self.pady)
        self.btnValider = tkinter.Button(self.frame, text="VALIDER", font=self.font, command=self.valider)
        self.btnValider.grid(row=1, column=1, sticky=tkinter.NSEW, padx=self.padx, pady=self.pady)

    
    def valider(self):
        try :
            self.conn = ConnectionSql.ConnectionSql(host=self.varAddresseIP.get(), user="root", database="Fiangonana")
            connex = self.conn.connectionSql()
            ApplicationClient.ApplicationClient(self.master)
        except :
            messagebox.showerror("ERREUR", message="connexion echoué")

if __name__=="__main__":
    root = tkinter.Tk()
    App = ConnectPass(root)
    root.mainloop()
        

        