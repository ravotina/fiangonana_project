import datetime, os, shutil, socket, mysql.connector
import cv2
import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
from PIL import Image, ImageTk
import tkinter, TMembres, TBatisa, TNaterahana, TMpandray, TNisoratana, TFanamasinana, TImages, TFaritra
import os

class WebcamApp:
    def __init__(self, parent_window):
        self.font = ("Bell MT", 12, "bold")
        self.padx = 2
        self.pady = 2
        self.parent_window = parent_window
        self.parent_window.title("Capture de photo")
        self.frame = ttk.Frame(parent_window)
        self.frame.grid(row = 0, column=0)
        self.varId = tkinter.IntVar()
        self.membre = TMembres.TMembres()
        self.sary_insert = TImages.TImages()
        self.capture_button = ttk.Button(self.frame, text="Capturer une photo", command=self.capture_photo)
        self.capture_button.grid(row = 1, column = 0)

        self.status_label = ttk.Label(self.frame, text="", foreground="green")
        self.status_label .grid(row = 1, column = 1)
        self.varRechercheNom = tkinter.StringVar()


        self.panel = ttk.Label(self.frame)
        self.panel.grid(row = 0, column = 0 ,  columnspan = 2 )

        self.frame_recherches = tkinter.LabelFrame(self.frame, text="IDENTIFIANT")
        self.frame_recherches.grid(row=0, column=3, columnspan = 3 , sticky=tkinter.NSEW)
        self.frame_recherches.columnconfigure(0, weight=1)
        self.frame_recherches.rowconfigure(0, weight=1)

        self.cbxBarreRecherhe = tkinter.Entry(self.frame_recherches, font=self.font, textvariable = self.varRechercheNom, justify=tkinter.CENTER)
        self.cbxBarreRecherhe.grid(row=0, column = 0,sticky=tkinter.EW, padx=self.padx, pady=self.pady)

        self.cbxId = tkinter.Entry(self.frame_recherches, font=self.font, textvariable = self.varId, justify=tkinter.CENTER, width=2, state="disabled")
        self.cbxId.grid(row=0, column = 1, padx=self.padx, pady=self.pady)

        self.listResultats = tkinter.Listbox(self.frame_recherches, height=25 , width = 70)
        self.listResultats.grid(row=1, column=0, sticky=tkinter.NSEW, pady=2)

        self.scrollBar = tkinter.Scrollbar(self.frame_recherches, command=self.listResultats.yview)
        self.scrollBar.grid(row=1, column=1,  sticky=tkinter.NS)

        self.listResultats.configure(yscrollcommand=self.scrollBar.set)

        self.listResultats.configure(yscrollcommand=self.scrollBar.set)
        self.cbxBarreRecherhe.bind("<KeyRelease>", lambda event:self.recherche_options())
        self.listResultats.bind("<<ListboxSelect>>", self.recuprer_selection)

        self.cap = cv2.VideoCapture(0)
        if not self.cap.isOpened():
            # print("La webcam n'a pas pu être ouverte.")
            self.parent_window.quit()

        self.update_preview()

    def update_preview(self):
        ret, frame = self.cap.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(frame)
            img = ImageTk.PhotoImage(img)
            self.panel.img = img
            self.panel.configure(image=img)
        self.parent_window.after(10, self.update_preview)

    def capture_photo(self):
        ret, frame = self.cap.read()
        repertoire_courant = os.getcwd() + "\photo_membre"
        if ret:
            if self.varId.get() == 0 :
                self.status_label.config(text="selectionnez un membre svp.", foreground="red")
                self.parent_window.after(3000, self.clear_status)
            else:
                nom_image = str(self.varId.get()) + self.varRechercheNom.get() + ".jpg"
                repertoire_courant = os.getcwd() + "\photo_membre"
                chemin_complet = os.path.join(repertoire_courant, nom_image)
                cv2.imwrite(chemin_complet, frame)
                self.sary_insert.NomImage = nom_image
                self.sary_insert.IdMembre = self.varId.get()
                self.sary_insert.inserer_dans_table_image()
                self.status_label.config(text="La photo a été enregistrée avec succès.", foreground="green")
                self.parent_window.after(3000, self.clear_status)

    def clear_status(self):
        # Efface le contenu du status_label
        self.status_label.config(text="")

    def run(self):
        self.parent_window.mainloop()

    def getText(self, donnee_tuple):
        reponse = str(donnee_tuple[0]) + "-" + "N : " + str(donnee_tuple[1]) + " " + \
        donnee_tuple[2] + " " + donnee_tuple[3]
        return reponse

    def getOptions(self):
        options = self.membre.getContentTable()
        return options

    def recherche_options(self):
        recherche = self.cbxBarreRecherhe.get().lower()
        self.listResultats.delete(0, tkinter.END)
        for option in self.getOptions():
            if recherche in str(option[1]).lower() or recherche in option[2].lower() or recherche in option[3].lower():
                self.listResultats.insert(tkinter.END, self.getText(option))

    def recuprer_selection(self, *args):
        index = self.listResultats.curselection()
        if index:
            selection = self.listResultats.get(index)
        idMembre_str = selection.split("-")[0]
        idMembre=int(idMembre_str)
        self.varId.set(idMembre)
        self.varRechercheNom.set(self.membre.getAnarana(idMembre) + " " + self.membre.getFanampiny(idMembre))
        print(type(idMembre))
        print(self.varId.get())
        print(self.varRechercheNom.get())

if __name__ == "__main__":
    root = tk.Tk()
    app = WebcamApp(root)
    app.run()

