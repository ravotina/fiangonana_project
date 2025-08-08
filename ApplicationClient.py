import datetime, os, shutil, socket, mysql.connector
import tkinter, TMembres, TBatisa, TNaterahana, TMpandray, TNisoratana, TFanamasinana, TImages, TFaritra, TSampana, TSampana_Membre, TFianaranaDiplom , TAdidy , Fakana_sary , Tcondidah , TCondidahLandV , TFifidiananaL , TFifidiananaV , MombaNyVato
from tkinter import TclError, messagebox, filedialog, ttk, PhotoImage
from PIL import ImageTk, Image
import cv2
import subprocess
import random

class ApplicationClient():
    def __init__(self, window):
        self.window  = window
        self.window.title("GESTION FIANGONANA")
        self.window.resizable(False, False)

        self.padx = 5
        self.pady = 5

        self.font = ("Bell MT", 12, "bold")
        self.background = "dark blue"

        self.width_canvas = 548
        self.height_canvas = 256

        self.frame_application = tkinter.Frame(self.window)
        self.frame_application.grid(row=0, column=0, sticky=tkinter.NSEW)

        self.canevas_image = tkinter.Canvas(self.frame_application, background="black", width=self.width_canvas, height=self.height_canvas)
        self.canevas_image.grid(row=0, column=0, columnspan=2, sticky=tkinter.NSEW, padx=self.padx, pady=self.pady)

        self.inserer_image_acceuil()
    
        self.lblFrameBtnEnregistrer = tkinter.LabelFrame(self.frame_application, text = "ENREGISTREMENT")
        self.lblFrameBtnEnregistrer.grid(row=1, column=0, padx=self.padx, pady=self.pady)

        self.lblFrameBtnRecherche = tkinter.LabelFrame(self.frame_application, text = "AUTRE")
        self.lblFrameBtnRecherche.grid(row=1, column=1, sticky = tkinter.NSEW, padx=self.padx, pady=self.pady)

        self.btnInformationPerso = tkinter.Button(self.lblFrameBtnEnregistrer, font=self.font, fg="white", text="Informations Personnels", background=self.background, command=self.information_personnel)
        self.btnInformationPerso.grid(row=0, column=0, sticky = tkinter.NSEW, padx=self.padx, pady=self.pady)

        self.btnAutreInformation = tkinter.Button(self.lblFrameBtnEnregistrer, font=self.font, fg="white", text="Autre Informations", background=self.background, command=self.autre_informations)
        self.btnAutreInformation.grid(row=0, column=1, sticky = tkinter.NSEW, padx=self.padx, pady=self.pady)

        self.btnfifiadianana = tkinter.Button(self.lblFrameBtnEnregistrer, font=self.font, fg="white", text="Fifidianana Lahy", background=self.background, command=self.effectuer_fifiadianana)
        self.btnfifiadianana.grid(row=1, column=0, sticky = tkinter.NSEW, padx=self.padx, pady=self.pady)

        self.btnfifiadianana = tkinter.Button(self.lblFrameBtnEnregistrer, font=self.font, fg="white", text="Fifidianana Vavy", background=self.background, command=self.effectuer_fifiadianana_vevavy)
        self.btnfifiadianana.grid(row=1, column=1, sticky = tkinter.NSEW, padx=self.padx, pady=self.pady)

        # self.btnFanambadina = tkinter.Button(self.lblFrameBtnEnregistrer, font=self.font, text="Fanambadiana", fg="white", background=self.background, command=self.fanambadina)
        # self.btnFanambadina.grid(row=1, column=0, sticky = tkinter.NSEW, padx=self.padx, pady=self.pady)

        # self.btnAdidy = tkinter.Button(self.lblFrameBtnEnregistrer, font=self.font, text="Adidy", fg="white", background=self.background, command=self.adidy)
        # self.btnAdidy.grid(row=1, column=1, sticky = tkinter.NSEW, padx=self.padx, pady=self.pady)

        self.btnEffectuerRecherche = tkinter.Button(self.lblFrameBtnRecherche, font=self.font, text="Effectuer Recherche", fg="white", background=self.background, command=self.effectuer_recherche)
        self.btnEffectuerRecherche.grid(row=0, column=0, padx=self.padx, pady=self.pady)

        self.btnQuiter = tkinter.Button(self.lblFrameBtnRecherche, font=self.font, text="Quiter", fg="white", background="dark red", command=self.window.quit)
        self.btnQuiter.grid(row=1, column=0, sticky=tkinter.NSEW, padx=self.padx, pady=self.pady)

        self.btnAddresseIP = tkinter.Button(self.lblFrameBtnRecherche, font=self.font, text="Addresse IP", fg="white", background=self.background, command=self.afficher_IP)
        self.btnAddresseIP.grid(row=2, column=0, sticky=tkinter.NSEW, padx=self.padx, pady=self.pady)

    def adidy(self):
        self.window_adidy = tkinter.Toplevel(self.window)
        App = EnregistrementAdidy(self.window_adidy)
        
    def information_personnel(self):
        self.window_personal_information = tkinter.Toplevel(self.window)
        App = EnregistremenPersonnel(self.window_personal_information)

    def effectuer_fifiadianana(self):
        self.window_fifidianana = tkinter.Toplevel(self.window)
        App = Fifidianana(self.window_fifidianana)

    def effectuer_fifiadianana_vevavy(self):
        self.window_fifidiananav = tkinter.Toplevel(self.window)
        App = FifidiananaVavy(self.window_fifidiananav)
    
    def inserer_image_acceuil(self):
        image = Image.open(os.getcwd() + "\\image_acceuil\\image_eglise.png")
        self.canevas_image.update()
        image = image.resize((self.canevas_image.winfo_width(), self.canevas_image.winfo_height()))#, Image.ANTIALIAS
        photo = ImageTk.PhotoImage(image)
        self.canevas_image.create_image(0, 0, anchor=tkinter.NW, image=photo)
        self.canevas_image.image = photo
    
    def effectuer_recherche(self):
        self.window_recherche = tkinter.Toplevel(self.window)
        App = Search (self.window_recherche)

    def fanambadina(self):
        self.window_vady_information = tkinter.Toplevel(self.window)
        App = EnregistremenVady(self.window_vady_information)

    def autre_informations(self):
        self.window_autre_information = tkinter.Toplevel(self.window)
        App = EnregistremenAutre(self.window_autre_information)

    def afficher_IP(self):
        self.window_IP = tkinter.Toplevel(self.window)
        App = AfficherIP(self.window_IP)

class AfficherIP():
    def __init__(self, master):
        self.master = master
        self.master.title("ADDRESS IP")

        self.font = ("Bell MT", 14, "bold")
        self.padx = 2
        self.pady = 2

        self.varAdresseIP = tkinter.StringVar()

        self.frame = tkinter.Frame(self.master)
        self.frame.grid(row=0, column=0)
        self.lblAdresseIP = tkinter.Label(self.frame, text="Adresse IP locale :", font=self.font, fg="white", bg="black")
        self.lblAdresseIP.grid(row=0, column=0, padx=self.padx, pady=self.pady)
        self.txtAdresseIP = tkinter.Label(self.frame, text=self.getAddresseIP(), font=self.font, fg="white", bg="black")
        self.txtAdresseIP.grid(row=0, column=1, padx=self.padx, pady=self.pady)

    def getAddresseIP(self):
        adresse_ip_locale = socket.gethostbyname(socket.gethostname())
        return adresse_ip_locale

class EnregistremenAutre():
    def __init__(self, master):
        self.master = master

        self.font = ("Bell MT", 12, "bold")
        self.padx = 2
        self.pady = 2

        self.select_items = list()
        self.chekboxs = list()
        self.items = list()

        # self.maka_sary= Fakana_sary.Fakana_sary()
        self.batisa = TBatisa.TBatisa()
        self.nahaterahana = TNaterahana.TNahaterahana()
        self.mpandray = TMpandray.TMpandray()
        self.images = TImages.TImages()
        self.membre = TMembres.TMembres()
        self.sampana = TSampana.TSampana()
        self.sampana_membre = TSampana_Membre.TSampana_Membre()
        self.fianarana_diplome = TFianaranaDiplom.TFianaranaDiplom()
        
        self.varRechercheNom = tkinter.StringVar()
        self.varDateNaissance = tkinter.StringVar()
        self.varLieuNaissance = tkinter.StringVar()
        self.varDateBatisa = tkinter.StringVar()
        self.varToeranaBatisa = tkinter.StringVar()
        self.varDatyMpandray = tkinter.StringVar()
        self.varToeranaMpandray = tkinter.StringVar()
        self.varId = tkinter.IntVar()
        self.varNomImage = tkinter.StringVar()
        self.varFianarna = tkinter.StringVar()
        self.varDiplome = tkinter.StringVar()
        self.varIdFianaranaDiplome = tkinter.IntVar()


        self.adidy = TAdidy.TAdidy()
        self.varDatyAdidy = tkinter.StringVar()
        self.varAdidy = tkinter.DoubleVar()
        self.varMembres = tkinter.StringVar()
        self.varDatyAdidy.set(self.getDateJour())

        self.condidah = Tcondidah.Tcondidah()


        self.nisoratra = TNisoratana.TNisoratana()
        self.fanamasinana = TFanamasinana.TFanamasinana()
        self.varId1 = tkinter.IntVar()
        self.varId2 = tkinter.IntVar()
        self.varMembres1 = tkinter.StringVar()
        self.varMembres2 = tkinter.StringVar()
        self.varIdPersonne1 = tkinter.IntVar()
        self.varIdPersonne1 = tkinter.IntVar()
        self.varDatyNisoratana = tkinter.StringVar()
        self.varDatyFanamasinana = tkinter.StringVar()
        self.varToeranaFanamasinana = tkinter.StringVar()


        self.conteneur_Autre_information_personnel = tkinter.Frame(self.master)
        self.conteneur_Autre_information_personnel.grid(row=0, column=1)

        self.frame_recherches = tkinter.LabelFrame(self.conteneur_Autre_information_personnel, text="IDENTIFIANT")
        self.frame_recherches.grid(row=0, column=0, rowspan=5 , sticky=tkinter.NSEW)
        self.frame_recherches.columnconfigure(0, weight=1)
        self.frame_recherches.rowconfigure(0, weight=1)

        # self.cbxMembre = tkinter.Entry(self.conteneur_Adidy, font= self.font, textvariable=self.varMembres, justify=tkinter.CENTER)
        # self.cbxMembre.grid(row=0, column=0, columnspan=3, sticky=tkinter.NSEW, padx=self.padx, pady=self.pady)

        # self.cbxId = tkinter.Entry(self.conteneur_Adidy, font=self.font, textvariable = self.varId, justify=tkinter.CENTER, width=2, state="disabled")
        # self.cbxId.grid(row=0, column = 3, padx=self.padx, pady=self.pady)

        # self.listResultats_adidy = tkinter.Listbox(self.conteneur_Adidy, height=13)
        # self.listResultats_adidy.grid(row=1, column=0, columnspan=3, sticky=tkinter.NSEW, padx=self.padx)

        # self.scrollBar = tkinter.Scrollbar(self.conteneur_Adidy, command=self.listResultats_adidy.yview)
        # self.scrollBar.grid(row=1, column=3, sticky=tkinter.NS)

        # self.listResultats_adidy.configure(yscrollcommand=self.scrollBar.set)
        
        self.cbxBarreRecherhe = tkinter.Entry(self.frame_recherches, font=self.font, textvariable = self.varRechercheNom, justify=tkinter.CENTER)
        self.cbxBarreRecherhe.grid(row=0, column = 0,sticky=tkinter.EW, padx=self.padx, pady=self.pady)

        self.cbxId = tkinter.Entry(self.frame_recherches, font=self.font, textvariable = self.varId, justify=tkinter.CENTER, width=2, state="disabled")
        self.cbxId.grid(row=0, column = 1, padx=self.padx, pady=self.pady)

        self.listResultats = tkinter.Listbox(self.frame_recherches, height=22)
        self.listResultats.grid(row=1, column=0, sticky=tkinter.NSEW, pady=2)

        self.scrollBar = tkinter.Scrollbar(self.frame_recherches, command=self.listResultats.yview)
        self.scrollBar.grid(row=1, column=1,  sticky=tkinter.NS)

        self.listResultats.configure(yscrollcommand=self.scrollBar.set)

        self.frame_nahaterahana = tkinter.LabelFrame(self.conteneur_Autre_information_personnel , text="NAHATERAHANA")
        self.frame_nahaterahana.grid(row =0, column = 1, sticky=tkinter.NSEW)
        self.frame_nahaterahana.columnconfigure(1, weight=1)
        self.frame_nahaterahana.rowconfigure(0, weight=1)
        self.frame_nahaterahana.columnconfigure(0, weight=1)
        self.frame_nahaterahana.rowconfigure(1, weight=1)

        self.frame_batisa = tkinter.LabelFrame(self.conteneur_Autre_information_personnel , text="BATISA")
        self.frame_batisa.grid(row = 1, column = 1, sticky = tkinter.NSEW)
        self.frame_batisa.rowconfigure(0, weight=1)
        self.frame_batisa.columnconfigure(0, weight=1)
        self.frame_batisa.columnconfigure(1, weight=1)
        self.frame_batisa.rowconfigure(1, weight=1)
        self.frame_batisa.rowconfigure(2, weight=1)

        self.frame_Mpandray = tkinter.LabelFrame(self.conteneur_Autre_information_personnel , text="MPANDRAY")
        self.frame_Mpandray.grid(row = 2, column = 1, sticky = tkinter.NSEW)
        self.frame_Mpandray.columnconfigure(1, weight=1)
        self.frame_Mpandray.rowconfigure(0, weight=1)
        self.frame_Mpandray.rowconfigure(1, weight=1)
        self.frame_Mpandray.columnconfigure(0, weight=1)

        self.frame_Images = tkinter.LabelFrame(self.conteneur_Autre_information_personnel , text="PHOTO")
        self.frame_Images.grid(row = 6, column = 0, sticky = tkinter.N + tkinter.EW)
        self.frame_Images.rowconfigure(0, weight=1)
        self.frame_Images.columnconfigure(1, weight=1)

        self.frame_Samapana = tkinter.LabelFrame(self.conteneur_Autre_information_personnel , text="SAMPANA")
        self.frame_Samapana.grid(row = 0, column = 2, rowspan = 3, sticky = tkinter.NSEW)
        self.frame_Samapana.rowconfigure(0, weight=1)
        self.frame_Samapana.columnconfigure(1, weight=1)

        self.frame_Fianarana = tkinter.LabelFrame(self.conteneur_Autre_information_personnel , text="FIANARANA")
        self.frame_Fianarana.grid(row = 3, column = 1, rowspan=4 , sticky = tkinter.NSEW)
        self.frame_Fianarana.columnconfigure(1, weight=1)
        self.frame_Fianarana.rowconfigure(0, weight=1)
        self.frame_Fianarana.columnconfigure(0, weight=1)
        self.frame_Fianarana.rowconfigure(1, weight=1)

        self.conteneur_Adidy = tkinter.LabelFrame(self.conteneur_Autre_information_personnel , text="Adidy")
        self.conteneur_Adidy.grid(row = 3, column = 2, rowspan=4 , sticky = tkinter.NSEW)
        self.conteneur_Adidy.columnconfigure(1, weight=1)
        self.conteneur_Adidy.rowconfigure(0, weight=1)
        self.conteneur_Adidy.columnconfigure(0, weight=1)
        self.conteneur_Adidy.rowconfigure(1, weight=1)

        # self.cbxMembre = tkinter.Entry(self.conteneur_Adidy, font= self.font, textvariable=self.varMembres, justify=tkinter.CENTER)
        # self.cbxMembre.grid(row=0, column=0, columnspan=3, sticky=tkinter.NSEW, padx=self.padx, pady=self.pady)

        # self.cbxId = tkinter.Entry(self.conteneur_Adidy, font=self.font, textvariable = self.varId, justify=tkinter.CENTER, width=2, state="disabled")
        # self.cbxId.grid(row=0, column = 3, padx=self.padx, pady=self.pady)

        # self.listResultats_adidy = tkinter.Listbox(self.conteneur_Adidy, height=13)
        # self.listResultats_adidy.grid(row=1, column=0, columnspan=3, sticky=tkinter.NSEW, padx=self.padx)

        # self.scrollBar = tkinter.Scrollbar(self.conteneur_Adidy, command=self.listResultats_adidy.yview)
        # self.scrollBar.grid(row=1, column=3, sticky=tkinter.NS)

        # self.listResultats_adidy.configure(yscrollcommand=self.scrollBar.set)
        
        self.lblDatyadidy = tkinter.Label(self.conteneur_Adidy, font= self.font, text="Daty", fg="white", background="black")
        self.lblDatyadidy.grid(row=2, column=0, sticky=tkinter.NSEW, pady=self.pady, padx=self.padx)
        self.txtDatyadidy = tkinter.Entry(self.conteneur_Adidy, font= self.font, textvariable=self.varDatyAdidy, justify=tkinter.CENTER)
        self.txtDatyadidy.grid(row=2, column=1, columnspan = 2, sticky=tkinter.NSEW, padx=self.padx, pady=self.pady)

        self.lblAdidy = tkinter.Label(self.conteneur_Adidy, font= self.font, text="Adidy Isambolana ", fg="white", background="black")
        self.lblAdidy.grid(row=3, column=0, sticky=tkinter.NSEW, pady=self.pady, padx=self.padx)
        self.txtAdidy = tkinter.Entry(self.conteneur_Adidy, font= self.font, textvariable=self.varAdidy, justify=tkinter.CENTER)
        self.txtAdidy.grid(row=3, column=1, columnspan = 2, sticky=tkinter.NSEW, padx=self.padx, pady=self.pady)

        self.btn_efface_adidy = tkinter.Button(self.conteneur_Adidy, font= self.font, text="Effacer", fg="white", background="dark blue", command=self.effacer)
        self.btn_efface_adidy.grid(row=4, column=0, sticky=tkinter.EW, pady=self.pady, padx=self.padx)

        self.btn_adidy = tkinter.Button(self.conteneur_Adidy, font= self.font, text="Enregistrer", fg="white", background="dark blue", command=self.energistrer)
        self.btn_adidy.grid(row=4, column=1, sticky=tkinter.EW, pady=self.pady, padx=self.padx)

        self.btn_afficher_adidy = tkinter.Button(self.conteneur_Adidy, font= self.font, text="Afficher Adidy", fg="white", background="dark blue", command=self.afficher_adidy)
        self.btn_afficher_adidy.grid(row=4, column=2, sticky=tkinter.EW, pady=self.pady, padx=self.padx)

        self.btn_recherche_grouper = tkinter.Button(self.conteneur_Adidy, font= self.font, text="Recherche Grouper", fg="white", background="dark blue", command=self.recherche_grouper)
        self.btn_recherche_grouper.grid(row=5, column=0, sticky=tkinter.EW, pady=self.pady, padx=self.padx)

        self.btn_capture = tkinter.Button(self.conteneur_Adidy, font= self.font, text="capture Photo", fg="white", background="#268549", command=self.execute_python_script)
        self.btn_capture.grid(row=5, column=1 , sticky=tkinter.EW, pady=self.pady, padx=self.padx)

        self.btn_ajouter_condidah = tkinter.Button(self.conteneur_Adidy, font= self.font, text="Ajouter au Condidah", fg="white", background="#490049", command=self.energistrer_nouveau_condidah)
        self.btn_ajouter_condidah.grid(row=5, column=2 , sticky=tkinter.EW, pady=self.pady, padx=self.padx)

        # self.cbxMembre.bind("<KeyRelease>", lambda event:self.recherche_options_adidy())
        # self.listResultats_adidy.bind("<<ListboxSelect>>", self.recuprer_selection_adidy)

        self.conteneur_pivady = tkinter.LabelFrame(self.conteneur_Autre_information_personnel , text="Mpivady")
        self.conteneur_pivady.grid(row = 10, column = 0, columnspan = 3 , sticky = tkinter.NSEW)
        self.conteneur_pivady.columnconfigure(1, weight=1)
        self.conteneur_pivady.rowconfigure(0, weight=1)
        self.conteneur_pivady.columnconfigure(0, weight=1)
        self.conteneur_pivady.rowconfigure(1, weight=1)

        self.conteneur_Nisoratana = tkinter.LabelFrame(self.conteneur_pivady, text="Nisoratana")
        self.conteneur_Nisoratana.grid(row = 0, column = 5 )

        self.conteneur_Fanamasinana = tkinter.LabelFrame(self.conteneur_pivady, text="Fanamasinana")
        self.conteneur_Fanamasinana.grid(row = 1, column = 5 , rowspan = 2)

        self.lahy = tkinter.Label(self.conteneur_pivady, font= self.font, text="lahy", fg="white", background="black")
        self.lahy.grid(row=0, column=0, sticky=tkinter.NSEW, pady=self.pady, padx=self.padx)

        self.cbxMembre1 = tkinter.Entry(self.conteneur_pivady, font= self.font, textvariable=self.varMembres1, justify=tkinter.CENTER)
        self.cbxMembre1.grid(row=1, column=0, sticky=tkinter.NSEW, padx=self.padx, pady=self.pady)

        self.listResultats1 = tkinter.Listbox(self.conteneur_pivady, height=5 , width=65)
        self.listResultats1.grid(row=2, column=0, rowspan=2 , sticky=tkinter.NSEW, padx=self.padx)

        self.scrollBar1 = tkinter.Scrollbar(self.conteneur_pivady, command=self.listResultats1.yview)
        self.scrollBar1.grid(row=2, column=1, rowspan=2 , sticky=tkinter.NS)

        self.vavy = tkinter.Label(self.conteneur_pivady, font= self.font, text="vavy", fg="white", background="black")
        self.vavy.grid(row=0, column=2, sticky=tkinter.NSEW, pady=self.pady, padx=self.padx)

        self.cbxMembre2 = tkinter.Entry(self.conteneur_pivady, font= self.font, textvariable=self.varMembres2, justify=tkinter.CENTER)
        self.cbxMembre2.grid(row=1, column=2, sticky=tkinter.NSEW, padx=self.padx, pady=self.pady)

        self.listResultats2 = tkinter.Listbox(self.conteneur_pivady, height=5 , width=65)
        self.listResultats2.grid(row=2, column=2, rowspan=2 , sticky=tkinter.NSEW, padx=self.padx)

        self.scrollBar2 = tkinter.Scrollbar(self.conteneur_pivady, command=self.listResultats2.yview)
        self.scrollBar2.grid(row=2, column=3, rowspan=2 , sticky=tkinter.NS)

        self.listResultats2.configure(yscrollcommand=self.scrollBar2.set)
        self.listResultats1.configure(yscrollcommand=self.scrollBar1.set)


        self.cbxMembre1.bind("<KeyRelease>", lambda event:self.recherche_options1())
        self.cbxMembre2.bind("<KeyRelease>", lambda event:self.recherche_options2())
        self.listResultats1.bind("<<ListboxSelect>>", self.recuprer_selection1)
        self.listResultats2.bind("<<ListboxSelect>>", self.recuprer_selection2)


        self.DatyNisoratana = tkinter.Label(self.conteneur_Nisoratana, font= self.font, text="Daty Nisoratana", fg="white", background="black")
        self.DatyNisoratana.grid(row=0, column=0, sticky=tkinter.NSEW, pady=self.pady, padx=self.padx)
        self.txtDatyNisoratana = tkinter.Entry(self.conteneur_Nisoratana, font= self.font, textvariable=self.varDatyNisoratana, justify=tkinter.CENTER)
        self.txtDatyNisoratana.grid(row=0, column=1, sticky=tkinter.NSEW, padx=self.padx, pady=self.pady)

        # self.btn_efface_Nisoratana = tkinter.Button(self.conteneur_Nisoratana, font= self.font, text="Effacer", fg="white", background="dark blue", command=self.effacer_Nisoratana)
        # self.btn_efface_Nisoratana.grid(row=1, column=0, sticky=tkinter.EW, pady=self.pady, padx=self.padx)

        # self.btn_Nisoratana = tkinter.Button(self.conteneur_Nisoratana, font= self.font, text="Enregistrer", fg="white", background="dark blue", command=self.energistrer_Nisoratana)
        # self.btn_Nisoratana.grid(row=1, column=1, sticky=tkinter.EW, pady=self.pady, padx=self.padx)

        self.DatyFanamasinana = tkinter.Label(self.conteneur_Fanamasinana, font= self.font, text="Daty Fanamasinana", fg="white", background="black")
        self.DatyFanamasinana.grid(row=0, column=0, sticky=tkinter.NSEW, pady=self.pady, padx=self.padx)
        self.txtDatyFanamasinana = tkinter.Entry(self.conteneur_Fanamasinana, font= self.font, textvariable=self.varDatyFanamasinana, justify=tkinter.CENTER)
        self.txtDatyFanamasinana.grid(row=0, column=1, sticky=tkinter.NSEW, padx=self.padx, pady=self.pady)

        self.ToeranaFanamasinana = tkinter.Label(self.conteneur_Fanamasinana, font= self.font, text="Toerana Fanamasinana", fg="white", background="black")
        self.ToeranaFanamasinana.grid(row=1, column=0, sticky=tkinter.NSEW, pady=self.pady, padx=self.padx)
        self.txtToeranaFanamasinana = ttk.Combobox(self.conteneur_Fanamasinana, font= self.font, textvariable=self.varToeranaFanamasinana, justify=tkinter.CENTER)
        self.txtToeranaFanamasinana.grid(row=1, column=1, sticky=tkinter.NSEW, padx=self.padx, pady=self.pady)
        self.txtToeranaFanamasinana['values'] = ["FJKM Ambohijatovo Fitiavana"]

        # self.btn_efface_Fanamasinana = tkinter.Button(self.conteneur_Fanamasinana, font= self.font, text="Effacer", fg="white", background="dark blue", command=self.effacer_Fanamasinana)
        # self.btn_efface_Fanamasinana.grid(row=2, column=0, sticky=tkinter.EW, pady=self.pady, padx=self.padx)

        self.btn_Fanamasinana = tkinter.Button(self.conteneur_Fanamasinana, font= self.font, text="Enregistrer", fg="white", background="dark blue", command=self.enregistrer_Fanambadina)
        self.btn_Fanamasinana.grid(row=2, column=1, sticky=tkinter.EW, pady=self.pady, padx=self.padx)



        self.items = self.sampana.getSampana()
        # print(self.items)
        self.checkbox_vars = [tkinter.IntVar() for _ in range(len(self.items))]

        self.ligne, self.column = 0, 0
        for idx, item in enumerate(self.items):
            #if self.column <4:
            # print("colone inferieur 3 =",idx)
            self.checkbox = tkinter.Checkbutton(self.frame_Samapana, text=item, variable=self.checkbox_vars[idx], onvalue=1, offvalue=0, width=15, bg="deep sky blue")
            self.checkbox.grid(row=self.ligne, column=self.column, padx=self.padx, pady=self.pady)
            self.chekboxs.append(self.checkbox)
            self.column += 1
            if self.column > 2 :
                self.column = 0
                self.ligne += 1

            # self.chekboxs.append(self.checkbox)
            # print("colone superieur 3 =",idx)
            # self.column = 0
            # self.checkbox = tkinter.Checkbutton(self.frame_Samapana, text=item, variable=self.checkbox_vars[idx], onvalue=1, offvalue=0, width=15, bg="deep sky blue")
            # self.checkbox.grid(row=self.ligne, column=self.column, padx=self.padx, pady=self.pady)
            # self.ligne += 1
            # self.chekboxs.append(self.checkbox)

        # self.columns = 4 
        # self.tab_nom_sampana = [element for element in self.items]
        # self.rows = len(self.items) // self.columns
        # for idx in range(self.rows * self.columns):
        #     self.checkbox = tkinter.Checkbutton(self.frame_Samapana, text=self.tab_nom_sampana[idx], variable=self.checkbox_vars[idx], onvalue=1, offvalue=0, width=15, bg="deep sky blue")
        #     self.checkbox.grid(row = idx  // self.columns , column=idx % self.columns )
        #     print(self.checkbox_vars[idx].get())
        #     self.chekboxs.append(self.checkbox)
        
        self.btn_modifier_sampana = tkinter.Button(self.frame_Samapana, font= self.font, text="MODIFIER", fg="white", background="dark blue", command=self.modifier_sampana_membre)
        self.btn_modifier_sampana.grid(row=11, column=0, sticky=tkinter.EW, pady=self.pady, padx=self.padx)
        self.btn_sampana_membre = tkinter.Button(self.frame_Samapana, font= self.font, text="ENREGISTRER", fg="white", background="dark blue", command=self.enregistrer_sampana_membre)
        self.btn_sampana_membre.grid(row=11, column=1, sticky=tkinter.EW, pady=self.pady, padx=self.padx)
        
        self.lblDateNaissance = tkinter.Label(self.frame_nahaterahana, font= self.font, text="Daty Nahaterahana", fg="white", background="black", width=16)
        self.lblDateNaissance.grid(row=0, column=0, sticky=tkinter.NSEW, pady=self.pady, padx=self.padx)
        self.txtDateNaissance = tkinter.Entry(self.frame_nahaterahana, font= self.font, textvariable=self.varDateNaissance, justify=tkinter.CENTER)
        self.txtDateNaissance.grid(row=0, column=1, sticky=tkinter.NSEW, padx=self.padx, pady=self.pady)

        self.lblLieuNaiaasance = tkinter.Label(self.frame_nahaterahana, font= self.font, text="Toerana ", fg="white", background="black")
        self.lblLieuNaiaasance.grid(row=1, column=0, sticky=tkinter.NSEW, pady=self.pady, padx=self.padx)
        self.txtLieuNaiaasance = ttk.Combobox(self.frame_nahaterahana, font= self.font, textvariable=self.varLieuNaissance, justify=tkinter.CENTER)
        self.txtLieuNaiaasance.grid(row=1, column=1, sticky=tkinter.NSEW, padx=self.padx, pady=self.pady)
        self.txtLieuNaiaasance['values'] = ["Befelatanana"]

        # self.btn_modifier_naissace = tkinter.Button(self.frame_nahaterahana, font= self.font, text="MODIFIER", fg="white", background="dark blue", command=self.modifier_nahaterahana)
        # self.btn_modifier_naissace.grid(row=2, column=0, sticky=tkinter.EW, pady=self.pady, padx=self.padx)
        # self.btn_naissace = tkinter.Button(self.frame_nahaterahana, font= self.font, text="ENREGISTRER", fg="white", background="dark blue", command=self.enregistrer_nahaterahana)
        # self.btn_naissace.grid(row=2, column=1, sticky=tkinter.EW, pady=self.pady, padx=self.padx)

        self.lblDatyBatisa = tkinter.Label(self.frame_batisa, font= self.font, text="Daty Batisa ", fg="white", background="black", width=16)
        self.lblDatyBatisa.grid(row=0, column=0, sticky=tkinter.NSEW, pady=self.pady, padx=self.padx)
        self.txtDatyBatisa = tkinter.Entry(self.frame_batisa, font= self.font, textvariable=self.varDateBatisa, justify=tkinter.CENTER)
        self.txtDatyBatisa.grid(row=0, column=1, sticky=tkinter.NSEW, padx=self.padx, pady=self.pady)

        self.lblToeranaBatisa = tkinter.Label(self.frame_batisa, font= self.font, text="Toerana ", fg="white", background="black")
        self.lblToeranaBatisa.grid(row=1, column=0, sticky=tkinter.NSEW, pady=self.pady, padx=self.padx)
        self.txtToeranaBatisa = ttk.Combobox(self.frame_batisa, font= self.font, textvariable=self.varToeranaBatisa, justify=tkinter.CENTER)
        self.txtToeranaBatisa.grid(row=1, column=1, sticky=tkinter.NSEW, padx=self.padx, pady=self.pady)
        self.txtToeranaBatisa['values'] = ["FJKM Ambohijatovo Fitiavana"]

        # self.btn_modifie_batisa = tkinter.Button(self.frame_batisa, font= self.font, text="MODIFIER", fg="white", background="dark blue", command=self.modifier_batisa)
        # self.btn_modifie_batisa.grid(row=2, column=0, sticky=tkinter.EW, pady=self.pady, padx=self.padx)
        # self.btn_batisa = tkinter.Button(self.frame_batisa, font= self.font, text="ENREGISTRER", fg="white", background="dark blue", command=self.enregistrer_batisa)
        # self.btn_batisa.grid(row=2, column=1, sticky=tkinter.EW, pady=self.pady, padx=self.padx)

        self.lblDatyMpandray = tkinter.Label(self.frame_Mpandray, font= self.font, text="Daty Mpandray ", fg="white", background="black", width=16)
        self.lblDatyMpandray.grid(row=0, column=0, sticky=tkinter.NSEW, pady=self.pady, padx=self.padx)
        self.txtDatyMpandray = tkinter.Entry(self.frame_Mpandray, font= self.font, textvariable=self.varDatyMpandray, justify=tkinter.CENTER)
        self.txtDatyMpandray.grid(row=0, column=1, sticky=tkinter.NSEW, padx=self.padx, pady=self.pady)

        self.lblToeranaMpandray = tkinter.Label(self.frame_Mpandray, font= self.font, text="Toerana ", fg="white", background="black")
        self.lblToeranaMpandray.grid(row=1, column=0, sticky=tkinter.NSEW, pady=self.pady, padx=self.padx)
        self.txtToeranaMpandray = ttk.Combobox(self.frame_Mpandray, font= self.font, textvariable=self.varToeranaMpandray, justify=tkinter.CENTER)
        self.txtToeranaMpandray.grid(row=1, column=1, sticky=tkinter.NSEW, padx=self.padx, pady=self.pady)
        self.txtToeranaMpandray['values'] = ["FJKM Ambohijatovo Fitiavana"]

        self.lblIdFianaraDiplome =tkinter.Label(self.frame_Fianarana, text="IdFianaranaDiplom ", font=self.font, bg="black", fg="white")
        self.lblIdFianaraDiplome.grid(row=0, column=0, sticky=tkinter.NSEW, padx=self.padx, pady=self.pady)

        self.cbxIdFianaraDiplome = ttk.Combobox(self.frame_Fianarana, textvariable=self.varIdFianaranaDiplome, font=self.font, justify='center')
        self.cbxIdFianaraDiplome.grid(row=0, column=1, sticky=tkinter.NSEW, padx=self.padx, pady=self.pady)

        self.lblFianarna = tkinter.Label(self.frame_Fianarana, font= self.font, text="Fianrana ", fg="white", background="black", width=16)
        self.lblFianarna.grid(row=1, column=0, sticky=tkinter.NSEW, pady=self.pady, padx=self.padx)
        self.txtFianarna = tkinter.Entry(self.frame_Fianarana, font= self.font, textvariable=self.varFianarna, justify=tkinter.CENTER)
        self.txtFianarna.grid(row=1, column=1, sticky=tkinter.NSEW, padx=self.padx, pady=self.pady)

        self.lblDiplome = tkinter.Label(self.frame_Fianarana, font= self.font, text="Diplome ", fg="white", background="black")
        self.lblDiplome.grid(row=2, column=0, sticky=tkinter.NSEW, pady=self.pady, padx=self.padx)
        self.cbxDiplome = ttk.Combobox(self.frame_Fianarana, font= self.font, textvariable=self.varDiplome, justify=tkinter.CENTER)
        self.cbxDiplome.grid(row=2, column=1, sticky=tkinter.NSEW, padx=self.padx, pady=self.pady)
        self.cbxDiplome['values'] = ["CEPE", "BEPC", "BACC", "DTS", "LICENCE", "Master 1", "Master 2", "DOCTORAT", "CERTIFICAT"]

        self.btn_modifie_Fianarana = tkinter.Button(self.frame_Fianarana, font= self.font, text="MODIFIER", fg="white", background="dark blue", command=self.modifier_fianarana_diplome)
        self.btn_modifie_Fianarana.grid(row=3, column=0, sticky=tkinter.EW, pady=self.pady, padx=self.padx)
        self.btn_fianarana = tkinter.Button(self.frame_Fianarana, font= self.font, text="ENREGISTRER", fg="white", background="dark blue", command=self.enregistrer_fianarana)
        self.btn_fianarana.grid(row=3, column=1, sticky=tkinter.EW, pady=self.pady, padx=self.padx)

        # self.btn_modifie_Mpandray = tkinter.Button(self.frame_Mpandray, font= self.font, text="MODIFIER", fg="white", background="dark blue", command=self.modifier_mpandray)
        # self.btn_modifie_Mpandray.grid(row=2, column=0, sticky=tkinter.EW, pady=self.pady, padx=self.padx)
        # self.btn_Mpandray = tkinter.Button(self.frame_Mpandray, font= self.font, text="ENREGISTRER", fg="white", background="dark blue", command=self.enregistrer_mpandray)
        # self.btn_Mpandray.grid(row=2, column=1, sticky=tkinter.EW, pady=self.pady, padx=self.padx)

        self.btn_modifie_Naissace_batisa_mpandray = tkinter.Button(self.frame_Mpandray, font= self.font, text="MODIFIER", fg="white", background="dark blue", command=self.modifier_autre)
        self.btn_modifie_Naissace_batisa_mpandray.grid(row=2, column=0, sticky=tkinter.EW, pady=self.pady, padx=self.padx)
        self.Naissace_batisa_mpandray = tkinter.Button(self.frame_Mpandray, font= self.font, text="ENREGISTRER", fg="white", background="dark blue", command=self.enregistrer_autre)
        self.Naissace_batisa_mpandray.grid(row=2, column=1, sticky=tkinter.EW, pady=self.pady, padx=self.padx)

        
        self.lblImage= tkinter.Entry(self.frame_Images, font= self.font, textvariable=self.varNomImage, fg="white", background="black", width=18)
        self.lblImage.grid(row=0, column=0, sticky=tkinter.NSEW, pady=self.pady, padx=self.padx)
        self.btn_image = tkinter.Button(self.frame_Images, font= self.font, text="INSERER IMAGE", fg="white", background="dark blue", command=self.enregistrer_image)
        self.btn_image.grid(row=0, column=1, sticky=tkinter.NSEW, pady=self.pady, padx=self.padx)

        self.cbxBarreRecherhe.bind("<KeyRelease>", lambda event:self.recherche_options())
        self.listResultats.bind("<<ListboxSelect>>", self.recuprer_selection)
        self.cbxIdFianaraDiplome.bind("<<ComboboxSelected>>", self.on_cbxIdfianaraDipl_selected)

    def energistrer_nouveau_condidah(self):
        try:
            self.condidah.IdMembre = self.varId.get()
            self.condidah.inserer_dans_table_condidah()
            messagebox.showinfo("Information", message="Enregistré dans table Condidah")
        except ValueError as err:
            messagebox.showerror("ERREUR", message=str(err))
        except mysql.connector.errors.IntegrityError :
            messagebox.showerror("ERREUR", message="existe déjà")
        except TclError :
            messagebox.showerror("ERREUR", message="vous avez entrez une lettre\npar accident")
        finally:
            self.master.focus_set()

    def effacer_nahaterahana(self):
        self.varDateNaissance.set("")
        self.varLieuNaissance.set("")
    
    def modifier_nahaterahana(self):
        # try :
        self.nahaterahana.idPersonne = self.varId.get()
        self.nahaterahana.DateNahaterahana = self.varDateNaissance.get()
        self.nahaterahana.ToeranaNahaterahana = self.varLieuNaissance.get()
        self.nahaterahana.modifier_nahaterahana(self.varId.get())
        #     messagebox.showinfo("INFORMATION", message="modification effectué")
        # except Exception as err:
        #     messagebox.showerror("ERREUR", message=str(err))
        # self.master.focus_set()
        
    def enregistrer_nahaterahana(self):
        
        self.nahaterahana.DateNahaterahana = self.varDateNaissance.get()
        self.nahaterahana.idPersonne = self.varId.get()
        self.nahaterahana.ToeranaNahaterahana = self.varLieuNaissance.get()
        self.nahaterahana.inserer_dans_table_Nahaterahana()
        self.effacer_nahaterahana()      
    
    def effacer_batisa(self):
        self.varDateBatisa.set("")
        self.varToeranaBatisa.set("")
    
    def modifier_batisa(self):
        self.batisa.idPersonne = self.varId.get()
        self.batisa.DateBatisa = self.varDateBatisa.get()
        self.batisa.ToeranaBatisa = self.varToeranaBatisa.get()
        self.batisa.modifier_batisa(self.varId.get())
    
    def enregistrer_batisa(self):
        self.batisa.DateBatisa = self.varDateBatisa.get()
        self.batisa.idPersonne = self.varId.get()
        self.batisa.ToeranaBatisa = self.varToeranaBatisa.get()
        self.batisa.inserer_dans_table_batisa()
        self.effacer_batisa()
    
    def effacer_mpandray(self):
        self.varDatyMpandray.set("")
        self.varToeranaMpandray.set("")

    def modifier_mpandray(self):
        self.mpandray.idPersonne = self.varId.get()
        self.mpandray.DateMpandray = self.varDatyMpandray.get()
        self.mpandray.ToeranaMpandray = self.varToeranaMpandray.get()
        self.mpandray.modifier_mpandray(self.varId.get())
    
    def enregistrer_mpandray(self):
        self.mpandray.DateMpandray = self.varDatyMpandray.get()
        self.mpandray.idPersonne = self.varId.get()
        self.mpandray.ToeranaMpandray = self.varToeranaMpandray.get()
        self.mpandray.inserer_dans_table_Mpandray()
        self.effacer_mpandray()

    def enregistrer_autre(self):
        try :
            self.enregistrer_nahaterahana()
            self.enregistrer_batisa()
            self.enregistrer_mpandray()
            messagebox.showinfo("Information", message="Enregistré")
        except ValueError as err:
            messagebox.showerror("ERREUR", message=str(err))
        except mysql.connector.errors.IntegrityError :
            messagebox.showerror("ERREUR", message="existe déjà")
        finally :
            self.master.focus_set()
    
    def modifier_autre(self):
        try :
            self.modifier_batisa()
            self.modifier_nahaterahana()
            self.modifier_mpandray()
            messagebox.showinfo("INFORMATION", message="modification effectué")
        except ValueError as err:
            messagebox.showerror("ERREUR", message=str(err))
        finally :
            self.master.focus_set()

    def getOptions(self):
        options = self.membre.getContentTable()
        return options

    def getText(self, donnee_tuple):
        reponse = str(donnee_tuple[0]) + "-" + "N : " + str(donnee_tuple[1]) + " " + \
        donnee_tuple[2] + " " + donnee_tuple[3]
        return reponse

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
        idMembre = selection.split("-")[0]
        self.varId.set(idMembre)
        self.varRechercheNom.set(self.membre.getAnarana(idMembre) + " " + self.membre.getFanampiny(idMembre))
        self.varDateNaissance.set(self.nahaterahana.getDaty(idMembre))
        self.varLieuNaissance.set(self.nahaterahana.getToerana(idMembre))
        self.varDateBatisa.set(self.batisa.getDaty(idMembre))
        self.varToeranaBatisa.set(self.batisa.getToerana(idMembre))
        self.varDatyMpandray.set(self.mpandray.getDaty(idMembre))
        self.varToeranaMpandray.set(self.mpandray.getToerana(idMembre))
        self.varNomImage.set(self.images.getNomImage(idMembre))
        self.effacer_fianarana()
        self.cbxIdFianaraDiplome['values'] = self.fianarana_diplome.getIdFianaranaDilome(idMembre)
        self.cocher_les_case()

    def enregistrer_image(self):
        image_path = filedialog.askopenfilename(filetypes=[("Images", "*.jpg;*.jpeg;*.png;*.gif;*.svg;*.bmp;*.JPG;*.JPEG;*.PNG;*.GIF;*.SVG;*.BMP")])
        try :
            if self.varId.get() == 0 :
                messagebox.showerror("ERREUR", message="selectionnez un membre svp")
            elif image_path and self.varId.get() != 0:
                destination_path = os.getcwd() + "\photo_membre"
                shutil.move(image_path, destination_path)
                image_name = os.path.basename(image_path)
                self.varNomImage.set(image_name)
                self.images.NomImage = image_name 
                self.images.IdMembre = self.varId.get()
                self.images.inserer_dans_table_image()
                messagebox.showinfo("Information", message="image enregistrer")
        except :
            messagebox.showerror("ERREUR", message="non enregister, veuillez \nmodifier le nom de l'image")
        finally :
            self.master.focus_set()

    def enregistrer_sampana_membre(self):
        try :
            for IdSampana in self.recurer_selection_sampana():
                self.sampana_membre.IdMembre = self.varId.get()
                self.sampana_membre.IdSampana = IdSampana
                self.sampana_membre.inserer_dans_table_Sampana_Membre()
            self.effacer_selection()
            messagebox.showinfo("INFORMATION", message="Enregistré")
        except ValueError as err :
            messagebox.showerror("ERREUR", message=str(err))
        except mysql.connector.errors.IntegrityError :
            messagebox.showerror("ERREUR", message="sampana existe déjà\nMais vous pouvez le modifier")
        finally :
            self.master.focus_set()
    
    def modifier_sampana_membre(self):
        self.sampana_membre.suprimer_sampana_membre(self.varId.get())
        self.enregistrer_sampana_membre()

    def recurer_selection_sampana(self):
        self.select_items.clear()
        for idx, var in enumerate(self.checkbox_vars):
            if var.get() == 1:
                self.select_items.append(self.sampana.getIdSamapana(self.items[idx]))
        return self.select_items

    def cocher_les_case(self):
        self.effacer_selection()
        Liste_NomSampana = [self.sampana.getNomSampana(IdSampana) for IdSampana in self.sampana_membre.getIdSampana(self.varId.get())]
        for idx, chekbox in enumerate(self.chekboxs):
            if chekbox.cget('text') in Liste_NomSampana:
                self.checkbox_vars[idx].set(1)

    def effacer_selection(self):
        for var in self.checkbox_vars:
            var.set(0)
    
    def enregistrer_fianarana(self):
        try :
            self.fianarana_diplome.IdMembre = self.varId.get()
            self.fianarana_diplome.Fianarana = self.varFianarna.get()
            self.fianarana_diplome.Diplom = self.varDiplome.get()
            self.fianarana_diplome.inserer_dans_table_Fianarana_diplom()
            messagebox.showinfo("INFORMATION", message="Enregistré")
            self.effacer_fianarana()
        except ValueError as err :
            messagebox.showerror("ERREUR", message=str(err))
        except mysql.connector.errors.IntegrityError :
            messagebox.showerror("ERREUR", message="existe déjà")
        finally :
            self.master.focus_set()

    def effacer_fianarana(self):
        self.varDiplome.set("")
        self.varFianarna.set("")
    
    def on_cbxIdfianaraDipl_selected(self, event):
        try :
            self.fianarana_diplome.IdMembre = self.varId.get()
            self.varFianarna.set(self.fianarana_diplome.getFianarana(self.varIdFianaranaDiplome.get(), self.varId.get()))
            self.varDiplome.set(self.fianarana_diplome.getDiplome(self.varIdFianaranaDiplome.get(), self.varId.get()))
        except ValueError as err:
            messagebox.showerror("ERREUR", message=str(err))
    
    def modifier_fianarana_diplome(self):
        try :
            self.fianarana_diplome.IdMembre = self.varId.get()
            self.fianarana_diplome.IdFianaranaDiplom = self.varIdFianaranaDiplome.get()
            self.fianarana_diplome.Fianarana = self.varFianarna.get()
            self.fianarana_diplome.Diplom = self.varDiplome.get()
            self.fianarana_diplome.modifier_fianarana_diplome(self.varIdFianaranaDiplome.get(), self.varId.get())
            messagebox.showinfo("Information", message="Modifié")
        except ValueError as err :
            messagebox.showerror("ERREUR", message=str(err))
        except mysql.connector.errors.IntegrityError :
            messagebox.showerror("ERREUR", message="existe déjà")
        finally :
            self.master.focus_set()


    def effacer(self):
        self.varAdidy.set("")
        self.varDatyAdidy.set("")
    
    def energistrer(self):
        try:
            self.adidy.idPersonne = self.varId.get()
            self.adidy.Daty = self.varDatyAdidy.get()
            self.adidy.Adidy = self.varAdidy.get()
            self.adidy.inserer_dans_table_adidy()
            messagebox.showinfo("Information", message="Enregistré")
        except ValueError as err:
            messagebox.showerror("ERREUR", message=str(err))
        except mysql.connector.errors.IntegrityError :
            messagebox.showerror("ERREUR", message="existe déjà")
        except TclError :
            messagebox.showerror("ERREUR", message="vous avez entrez une lettre\npar accident")
        finally:
            self.master.focus_set()
    
    # def getText(self, donnee_tuple):
    #     reponse = str(donnee_tuple[0]) + "-" + "N : " + str(donnee_tuple[1]) + " " + \
    #     donnee_tuple[2] + " " + donnee_tuple[3]
    #     return reponse

    def recherche_options_adidy(self):
        recherche = self.cbxMembre.get().lower()
        self.listResultats_adidy.delete(0, tkinter.END)
        for option in self.getOptions():
            if recherche in str(option[1]).lower() or recherche in option[2].lower() or recherche in option[3].lower():
                self.listResultats_adidy.insert(tkinter.END, self.getText(option))
    
    def recuprer_selection_adidy(self, *args):
        index = self.listResultats_adidy.curselection()
        if index:
            selection = self.listResultats_adidy.get(index)
        idMembre = selection.split("-")[0]
        donnee_membre = self.membre.getMembre(idMembre)
        self.inserer_donner_recherche(donnee_membre)
    
    def getIdMembre(self, tuple_donnee):
        return tuple_donnee[0]

    def inserer_donner_recherche(self, tuple_donnee):
        nom = self.getNomPrenom(tuple_donnee)
        idmembre = self.getIdMembre(tuple_donnee)
        self.varMembres.set(nom)
        self.varId.set(idmembre)
    
    # def getOptions(self):
    #     options = self.membre.getContentTable()
    #     return options
    
    def getDateJour(self):
        date_actuelle = datetime.date.today()
        date_formater = date_actuelle.strftime("%d-%m-%Y")
        return date_formater
    
    def getNomPrenom(self, tuple_donnee):
        reponse = tuple_donnee[3] + " " + tuple_donnee[4]
        return reponse
    
    def afficher_adidy(self):
        self.window_adidy = tkinter.Toplevel(self.master)
        App = ContenueAdidy(self.window_adidy, self.varId.get())

    def recherche_grouper(self):
        self.window_recherche_grouper = tkinter.Toplevel(self.master)
        App = AdidyRechecheGrouper(self.window_recherche_grouper)

    #----------------capturer photo----------------------
    def capturer_photo(self):
        self.window_caputure = tkinter.Toplevel(self.master)
        App = CapturePhoto(self.window_caputure)

    def enregistrer_Fanambadina(self):
        try :
            self.energistrer_Nisoratana()
            self.energistrer_fanamasinana()
            messagebox.showinfo("Information", message="Enregistré")
        except ValueError as err:
            messagebox.showerror("ERREUR", message=str(err))
        except mysql.connector.errors.IntegrityError :
            messagebox.showerror("ERREUR", message="existe déjà")
        finally :
            self.master.focus_set()

    def energistrer_fanamasinana(self):
        # try:
        self.fanamasinana.idPersonne1 = self.varId1.get()
        self.fanamasinana.idPersonne2 = self.varId2.get()
        self.fanamasinana.DatyFanamasinana = self.varDatyFanamasinana.get()
        self.fanamasinana.ToeranaFanamasinana = self.varToeranaFanamasinana.get()
        self.fanamasinana.inserer_dans_table_Fanamasinana()
        #     messagebox.showinfo("Information", message="Enregistré")
        # except ValueError as err:
        #     messagebox.showerror("ERREUR", message=str(err))
        # except mysql.connector.errors.IntegrityError :
        #     messagebox.showerror("ERREUR", message="existe déjà")
        # except TclError :
        #     messagebox.showerror("ERREUR", message="vous avez entrez une lettre\npar accident")
        # finally:
        #     self.master.focus_set()

    def energistrer_Nisoratana(self):
        # try:
        self.nisoratra.idPersonne1 = self.varId1.get()
        self.nisoratra.idPersonne2 = self.varId2.get()
        self.nisoratra.DatyNisoratana = self.varDatyNisoratana.get()
        self.nisoratra.inserer_dans_table_Nisoratana()
        #     messagebox.showinfo("Information", message="Enregistré")
        # except ValueError as err:
        #     messagebox.showerror("ERREUR", message=str(err))
        # except mysql.connector.errors.IntegrityError :
        #     messagebox.showerror("ERREUR", message="existe déjà")
        # except TclError :
        #     messagebox.showerror("ERREUR", message="vous avez entrez une lettre\npar accident")
        # finally:
        #     self.master.focus_set()

    # def getText(self, donnee_tuple):
    #     reponse = str(donnee_tuple[0]) + "-" + "N : " + str(donnee_tuple[1]) + " " + \
    #     donnee_tuple[2] + " " + donnee_tuple[3]
    #     return reponse

    def recherche_options1(self):
        recherche = self.cbxMembre1.get().lower()
        self.listResultats1.delete(0, tkinter.END)
        for option in self.getOptions():
            if recherche in str(option[1]).lower() or recherche in option[2].lower() or recherche in option[3].lower():
                self.listResultats1.insert(tkinter.END, self.getText(option))

    def recherche_options2(self):
        recherche = self.cbxMembre2.get().lower()
        self.listResultats2.delete(0, tkinter.END)
        for option in self.getOptions():
            if recherche in str(option[1]).lower() or recherche in option[2].lower() or recherche in option[3].lower():
                self.listResultats2.insert(tkinter.END, self.getText(option))
    
    def recuprer_selection1(self, *args):
        index = self.listResultats1.curselection()
        if index:
            selection = self.listResultats1.get(index)
        idMembre = selection.split("-")[0]
        donnee_membre = self.membre.getMembre(idMembre)
        self.inserer_donner_recherche1(donnee_membre)

    def recuprer_selection2(self, *args):
        index = self.listResultats2.curselection()
        if index:
            selection = self.listResultats2.get(index)
        idMembre = selection.split("-")[0]
        donnee_membre = self.membre.getMembre(idMembre)
        self.inserer_donner_recherche2(donnee_membre)

    # def getOptions(self):
    #     options = self.membre.getContentTable()
    #     return options

    def inserer_donner_recherche1(self, tuple_donnee):
        nom = self.getNomPrenom(tuple_donnee)
        idmembre1 = self.getIdMembre(tuple_donnee)
        self.varMembres1.set(nom)
        self.varId1.set(idmembre1)
        donner_fanamasinana = self.fanamasinana.getFanamasinanaLahy(idmembre1)
        donner_nisoratana = self.nisoratra.getNisoratanaLahy(idmembre1)
        self.inserer_Fanamasinana(donner_fanamasinana)
        self.insert_Nisoratana(donner_nisoratana)

    def inserer_donner_recherche2(self, tuple_donnee):
        nom = self.getNomPrenom(tuple_donnee)
        idmembre2 = self.getIdMembre(tuple_donnee)
        self.varMembres2.set(nom)
        self.varId2.set(idmembre2)
        donner_fanamasinana = self.fanamasinana.getFanamasinanaVavy(idmembre2)
        donner_nisoratana = self.nisoratra.getNisoratanaVavy(idmembre2)
        self.inserer_Fanamasinana(donner_fanamasinana)
        self.insert_Nisoratana(donner_nisoratana)
       
    # def getNomPrenom(self, tuple_donnee):
    #     reponse = tuple_donnee[3] + " " + tuple_donnee[4]
    #     return reponse

    def getIdMembre(self, tuple_donnee):
        return tuple_donnee[0]

    def inserer_donner_daty_Fanamasinana(self, tuple_donnee):
        daty_Fanamasinana = self.getDaty(tuple_donnee)
        print(daty_Fanamasinana)
        self.varDatyFanamasinana.set(daty_Fanamasinana)

    def inserer_donner_toerana_Fanamasinana(self, tuple_donnee):
        toerana_Fanamasinana = self.getToerana(tuple_donnee)
        self.varToeranaFanamasinana.set(toerana_Fanamasinana)

    def inserer_donner_daty_nisoratana(self, tuple_donnee):
        daty_Nisoratana = self.getDaty(tuple_donnee)
        self.varDatyNisoratana.set(daty_Nisoratana)
    
    def effacer_Fanamasinana(self):
        self.varDatyFanamasinana.set("")
        self.varToeranaFanamasinana.set("")

    def effacer_Nisoratana(self):
        self.varDatyNisoratana.set("")

    def inserer_Fanamasinana(self, tuple_donnee):
        try:
            self.inserer_donner_daty_Fanamasinana(tuple_donnee)
            self.inserer_donner_toerana_Fanamasinana(tuple_donnee)
        except :
            self.effacer_Fanamasinana()

    def insert_Nisoratana(self , tuple_donnee):
        try:
            self.inserer_donner_daty_nisoratana(tuple_donnee)
        except :
            self.effacer_Nisoratana()

    def getIdMembre1(self, tuple_donnee):
        return tuple_donnee[1]

    def getIdMembre2(self, tuple_donnee):
        return tuple_donnee[2]
    
    def getDaty(self, tuple_donnee):
        return tuple_donnee[3].strftime("%d-%m-%Y")
    
    def getToerana(self, tuple_donnee):
        return tuple_donnee[4]

    def execute_python_script(self):
        # Remplacez 'mon_script.py' par le nom de votre fichier Python à exécuter
        script_name = 'Fakana_sary.py'

        try:
            result = subprocess.run(['python', script_name], capture_output=True, text=True, check=True)
            output = result.stdout
            print("Sortie du script Python:")
            print(output)
        except subprocess.CalledProcessError as e:
            print(f"Erreur lors de l'exécution du script Python : {e}")
        except FileNotFoundError:
            print(f"Fichier '{script_name}' introuvable.")

class ScrollableFrame(tkinter.Frame):
    def __init__(self, master, frame_text="", label_height=1, canvas_width=1080, canvas_height=610, **kwargs):
        tkinter.Frame.__init__(self, master, **kwargs)

        # Ajoutez une étiquette pour afficher le texte
        self.label = tkinter.Label(self, text=frame_text, font=("Helvetica", 12), bg="gray", fg="white", height=label_height )
        self.label.pack(side="top", fill="x", pady=0)

        self.canvas = tkinter.Canvas(self, width=canvas_width, height=canvas_height)
        self.scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = ttk.Frame(self.canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

class Fifidianana():
    def __init__(self, master):
        self.master = master
        self.master.title("Fifidianana")
        # self.master.resizable(False, False)

        self.master.geometry("1300x650")
        self.master.resizable(False, False)
        self.font = ("Bell MT", 12, "bold")
        self.background = "black"
        self.padx = 2
        self.pady = 2

        self.select_items = list()
        self.chekboxs = list()
        self.items = list()

        self.images = TImages.TImages()
        self.var_id_mpifidy_nampidirina_faranay = tkinter.StringVar()
        self.condidah =  TCondidahLandV. TCondidahLandV()
        self.election = TFifidiananaL.TFifidiananaL()
        self.detaillevato = MombaNyVato.MombaNyVato()
        self.Membres = TMembres.TMembres()
        self.var_user_valider = tkinter.StringVar()
        self.id_mpifidy_rechercher = tkinter.StringVar()
        self.citation_text = tkinter.StringVar()
        self.citation_text.set("\n\n\nNe te laisse pas vaincre par le mal, mais triomphe du mal par le bien.\n (Romains 12:21)")

        self.apropo_de_fifidianana = tkinter.LabelFrame(self.master, text="information fifidianana")
        self.apropo_de_fifidianana.grid(row=0, column=0, sticky=tkinter.NSEW)

        self.numero_dernier_mpifidy = tkinter.LabelFrame(self.apropo_de_fifidianana , text="numero ilay taratasy")
        self.numero_dernier_mpifidy.grid(row=0, column=0, sticky=tkinter.NSEW)

        self.fram_information = tkinter.LabelFrame(self.apropo_de_fifidianana , text="Recherche")
        self.fram_information.grid(row=2, column=0, sticky=tkinter.NSEW)

        self.fram_fifidianana_inconu = tkinter.LabelFrame(self.apropo_de_fifidianana , text="VatoFotsy/vatoMaty")
        self.fram_fifidianana_inconu.grid(row=1, column=0, sticky=tkinter.NSEW)

        self.autre_information = tkinter.LabelFrame(self.apropo_de_fifidianana , text="Teny ao anaty baiboly")
        self.autre_information.grid(row=3, column=0, sticky=tkinter.NSEW)

        #self.fram_olona_fidina = ScrollableFrame(self.master, text="Liste Condidah")
        #self.fram_olona_fidina.pack(row=0, column=1, sticky=tkinter.NSEW)

        self.fram_olona_fidina = ScrollableFrame(self.master, frame_text="Liste Condidat")
        self.fram_olona_fidina.grid(row=0, column=1, sticky=tkinter.NE)
        #self.fram_olona_fidina.grid_propagate(False)
        #self.fram_olona_fidina.config(width=500, height=300)

        self.mpifidynumero = tkinter.Label(self.numero_dernier_mpifidy, text="Numero taratasy", font=self.font, background=self.background, foreground="white")
        self.mpifidynumero.grid(row=0, column=0, sticky=tkinter.EW, padx=self.padx, pady=self.pady)
        self.txtmpifidynumero = tkinter.Entry(self.numero_dernier_mpifidy, textvariable=self.var_id_mpifidy_nampidirina_faranay , justify=tkinter.CENTER, width=28)
        self.txtmpifidynumero.grid(row=1, column=0, sticky=tkinter.NSEW, padx=self.padx, pady=self.pady)

        self.numero_chercher = tkinter.Label(self.fram_information, text="Numero à chercher :", font=self.font, background=self.background, foreground="white")
        self.numero_chercher.grid(row=0, column=0, sticky=tkinter.EW, padx=self.padx, pady=self.pady)
        self.txtnumero_chercher = tkinter.Entry(self.fram_information, textvariable=self.var_user_valider, justify=tkinter.CENTER, width=28)
        self.txtnumero_chercher.grid(row=1, column=0, sticky=tkinter.NSEW, padx=self.padx, pady=self.pady)

        self.btn_rechercher = tkinter.Button(self.fram_information, font= self.font, text="Rechercher", fg="white", background="dark blue", command=self.cocher_les_case)
        self.btn_rechercher.grid(row=4, column=0, sticky=tkinter.EW, pady=self.pady, padx=self.padx)

        self.btn_ajout_vato_fotsy = tkinter.Button(self.fram_fifidianana_inconu, font= self.font, text="ENY", fg="white", background="dark blue", command=self.handle_vato_ENY_click)
        self.btn_ajout_vato_fotsy.grid(row=1, column=0,sticky=tkinter.EW, pady=self.pady, padx=self.padx)

        self.btn_ajout_vato_fotsy = tkinter.Button(self.fram_fifidianana_inconu, font= self.font, text="TSIA", fg="white", background="dark blue", command=self.handle_vato_Tsia_click)
        self.btn_ajout_vato_fotsy.grid(row=2, column=0,sticky=tkinter.EW, pady=self.pady, padx=self.padx)

        self.btn_ajout_vato_fotsy = tkinter.Button(self.fram_fifidianana_inconu, font= self.font, text="VATO FOTSY", fg="white", background="dark blue", command=self.handle_vato_fotsy_click)
        self.btn_ajout_vato_fotsy.grid(row=3, column=0,sticky=tkinter.EW, pady=self.pady, padx=self.padx)

        self.btn_ajout_vato_Maty = tkinter.Button(self.fram_fifidianana_inconu, font= self.font, text="VATO MATY", fg="white", background="dark blue", command=self.handle_vato_maty_click)
        self.btn_ajout_vato_Maty.grid(row=4, column=0, sticky=tkinter.EW, pady=self.pady, padx=self.padx)


       # citation_text = "\n\n\nNe te laisse pas vaincre par le mal, mais triomphe du mal par le bien.\n (Romains 12:21)"

        self.teny_ambara = tkinter.Text(self.autre_information, font=self.font, wrap=tkinter.WORD, width=20)
        self.teny_ambara.insert(tkinter.END, self.citation_text.get())

        self.teny_ambara.tag_configure("center", justify="center")

        self.teny_ambara.tag_add("center", "1.0", "end")

        self.teny_ambara.config(state=tkinter.DISABLED)  # Empêcher l'édition du texte
        self.teny_ambara.pack(expand=True, fill="both", padx=self.padx, pady=self.pady)

        self.autre_information.after(6000, self.miser_a_jour_citation)


        self.items = self.condidah.getCondidahL()
        # print(self.items)
        self.checkbox_vars = [tkinter.IntVar() for _ in range(len(self.items))]

        self.ligne, self.column = 0, 0
        #for idx, item in enumerate(self.items):
        chek = 0
        for item in self.condidah.getCondidahInfoL():

            self.canvas_profil = tkinter.Canvas(self.fram_olona_fidina.scrollable_frame, height=130, width=150, background=self.background)
            self.canvas_profil.grid(row=self.ligne , column=self.column , sticky=tkinter.NW)

            photo = self.show_profil(item[4])
            self.canvas_profil.create_image(0, 0, anchor=tkinter.NW, image=photo)
            self.canvas_profil.image = photo
            #if self.column <4:
            # print("colone inferieur 3 =",idx)
            # Nom_de_personne = str(item)+"- "+self.Membres.getAnarana(item) +" "+ self.Membres.getFanampiny(item)
            Nom_de_personne = str(item[1])+"- "+item[2] +" "+ item[3]
            max_caracteres_par_ligne = 17

            # Diviser la chaîne en lignes si elle dépasse la longueur maximale
            lignes = [Nom_de_personne[i:i + max_caracteres_par_ligne] for i in range(0, len(Nom_de_personne), max_caracteres_par_ligne)]

            # Joindre les lignes avec \n
            nom_de_personne_formate = "\n".join(lignes)

            self.checkbox = tkinter.Checkbutton(self.fram_olona_fidina.scrollable_frame, text=nom_de_personne_formate , variable=self.checkbox_vars[chek] , onvalue=1, offvalue=0, width=15, bg="deep sky blue" , compound="top")
            # self.show_profil(self, IdMembre)
            self.checkbox.grid(row=self.ligne + 1, column=self.column, padx=self.padx, pady=self.pady)
            #self.chekboxs.append(self.checkbox)
            #self.chekboxs.append(self.canvas_profil)
            self.chekboxs.append((self.checkbox, self.canvas_profil))
            self.column += 1
            if self.column > 6 :
                self.column = 0
                self.ligne += 2

            chek = chek + 1

        # self.envoier_les_condidah_au_base = tkinter.Button(self.fram_olona_fidina.scrollable_frame, font= self.font, text="Valider", fg="white", background="dark blue", command=self.enregistrer_insert_condidah_selectionner)
        # if(self.column == 0 ):
        #     self.column = 1
        # self.envoier_les_condidah_au_base.grid(row=self.ligne + 2 , column=self.column -1 , sticky=tkinter.EW, pady=self.pady, padx=self.padx)

        # self.modiffier_les_election = tkinter.Button(self.fram_olona_fidina.scrollable_frame, font= self.font, text="Modiffication", fg="white", background="dark blue", command=self.modification_election_numero)
        # self.modiffier_les_election.grid(row=self.ligne + 3 , column=self.column -1 , sticky=tkinter.EW, pady=self.pady, padx=self.padx)
             

    def miser_a_jour_citation(self):

        citations = [
            "\n\n\nMitandrema , ka miarova tena mba tsy ho azon' ny fieremana ianareo; fa ny ain' olona tsy miankina amin'ny habetsahan'ny zavatra ananany (Lioka 12:15)",
            "\n\n\nFa iray no Andriamanitra ,ary iray no Mpanalalana amin'Andriamanitra sy ny olona dia i Kristy Jesosy , Izay olona(1 Timoty 2:5)",
            "\n\n\nKanefa ny fanorenana mafy nataon' Andriamanitra dia miorina tsara sady manana izao tombo-kase izao:'Ny Tompo mahalala ny azy' , ary koa :'aoka ny olona rehetra izay manonona ny anaran' ny Tompo hiala amin'ny ratsy.'(2 Timoty 2:19)",
            "\n\n\nFa ataoko fa ny fahoriana amin' izao andro akehitriny izao dia tsy tokony hoharina amin'ny voninahitra izay haseho amintsika.(Romana 8:18)",
            "\n\n\nMitoria ny teny , mazotoa , na amin'ny fotoana na tsy amin'ny fotoana , mandrese lahatra, mamporisiha , mananara mafy amin'ny fahari-po sy ny fampianarana rehetra(2 Timoty 4:2)",
            "\n\n\nFa izy no nihavian'izao zavatra rehetra izao, ary Izy no mihazona azy sady izy koa no antony; Izy anie no homem-boninahitra mandrakizay Amen.(Romana 11:36)",
            "\n\n\nTandremo mba tsy hisy hamaly ratsy olona; fa miezaha mandrakariva hitady izay tsara, na amin'ny namanareo na amin'ny olona rehetra(1 Tesaloniana 5:15)",
            "\n\n\nFa hilaza fahendrena ny vavako hametsovetso fahalalana ny foko Atongilako hihaino oha-teny ny sofiko (Salamo 49.4,5)",
            "\n\n\nFa voasoratra hoe; Jehovah Andriamanitro no hiankohofanao , ary Izy irery ihany no hotompoinao(Matio 4:10)",
            "\n\n\nMa inona na inona tononinareo amin'ny fivavahana sy angatahinareo, dia minoa fa efa nandray ianareo, dia ho azonareo izany (Marka 11:24)",
            "\n\n\nAry izao no didiny , dia ny hinoantsika ny anaran' i Jesoa Kristy Zanany sy ny hifankatiavatsika araka ny didy nomeny antsika(I Jaona 3:23)",
            # Ajoutez d'autres citations ici
        ]

        nouvelle_citation = random.choice(citations)
        self.citation_text.set(nouvelle_citation)

        self.teny_ambara.config(state=tkinter.NORMAL)
        self.teny_ambara.delete("1.0", tkinter.END)

        # Insérez la nouvelle citation
        self.teny_ambara.insert(tkinter.END, self.citation_text.get())

        # Centrer le texte (si nécessaire)
        self.teny_ambara.tag_configure("center", justify="center")
        self.teny_ambara.tag_add("center", "1.0", "end")

        # Empêcher l'édition du texte
        self.teny_ambara.config(state=tkinter.DISABLED)

        self.autre_information.after(6000, self.miser_a_jour_citation)


    def show_profil(self, Nom_image):
        try:
            image = Image.open(os.getcwd() + "\\photo_membre\\" + Nom_image)
            image = image.resize((150, 130)) # , Image.ANTIALIAS
            photo = ImageTk.PhotoImage(image)
            return photo
        except :
            return ""

    def enregistrer_insert_condidah_selectionner(self):
        try :
            if(self.tester_si_pifidy_existe() == 0):
                for numero_condidah in self.recurer_selection_condidah():
                    self.election._setIdCondidah(numero_condidah)
                    self.election._setIdMpifidy(self.txtmpifidynumero.get())
                    self.election.inserer_dans_table_FifidiananaL()
                    pass
                self.effacer_selection()
                messagebox.showinfo("INFORMATION", message="Enregistré")
                        # Assuming self.txtmpifidynumero is an Entry widget
                current_value = self.txtmpifidynumero.get()
                new_value = str(int(current_value) + 1)
                self.txtmpifidynumero.delete(0, tkinter.END)
                self.txtmpifidynumero.insert(0, new_value)
            else:
                messagebox.showerror("ERREUR", message="Efa misy manana io Numero io")
        except ValueError as err :
            messagebox.showerror("ERREUR", message=str(err))
        except mysql.connector.errors.IntegrityError as e:
            messagebox.showerror("ERREUR", message=f"Erreur d'intégrité : {str(e)}")
        finally :
            self.master.focus_set()


    def tester_si_pifidy_existe(self):
        print(self.election.tester_les_mpifidy_existe(self.txtmpifidynumero.get()))
        return self.election.tester_les_mpifidy_existe(self.txtmpifidynumero.get())
    
    def tester_si_pifidy_existe_dans_vato_manakery(self):
        print(self.election.tester_les_mpifidy_existe_dans_vato_manakery(self.txtmpifidynumero.get()))
        return self.election.tester_les_mpifidy_existe_dans_vato_manakery(self.txtmpifidynumero.get())
    
    def tester_si_pifidy_existe_dans_vato_maty(self):
        print(self.election.tester_les_mpifidy_existe_dans_vato_maty(self.txtmpifidynumero.get()))
        return self.election.tester_les_mpifidy_existe_dans_vato_maty(self.txtmpifidynumero.get())

    def tester_si_pifidy_existe_dans_vato_fotsy(self):
        print(self.election.tester_les_mpifidy_existe_dans_vato_fotsy(self.txtmpifidynumero.get()))
        return self.election.tester_les_mpifidy_existe_dans_vato_fotsy(self.txtmpifidynumero.get())

    def tester_si_le_pifidy_existe_fAjour(self):
        return self.election.tester_les_mpifidy_existe_Ajour(self.txtmpifidynumero.get())


    def recurer_selection_condidah(self):
        self.select_items.clear()
        for idx, var in enumerate(self.checkbox_vars):
            if var.get() == 1:
                self.select_items.append(self.items[idx])
                print("Numero cocher:"+str(self.items[idx]))
        return self.select_items

    def cocher_les_case(self):
        self.effacer_selection()
        print("tonga ato ny afatra")
        Liste_voafidy = [str(idcondidavofidy) for idcondidavofidy in self.election.getIdVoafidy(self.txtnumero_chercher.get())]
        for checkbox, canvas_profil in self.chekboxs:
            text_value = checkbox.cget('text')
            print(text_value.split("-")[0])
            print(Liste_voafidy)
            if text_value.split("-")[0] in Liste_voafidy:
                checkbox.select()

    def modiffication_insertion_election(self):
        try :
            for Numero_condidah in self.recurer_selection_condidah():
                self.election._setIdCondidah(Numero_condidah)
                self.election._setIdMpifidy(self.txtnumero_chercher.get())
                self.election.inserer_dans_table_FifidiananaL()
            self.effacer_selection()
            messagebox.showinfo("INFORMATION", message="Vita Soama tsara ny Modiffication")
        except ValueError as err :
            messagebox.showerror("ERREUR", message=str(err))
        except mysql.connector.errors.IntegrityError as e:
            messagebox.showerror("ERREUR", message=f"Erreur d'intégrité : {str(e)}")
        finally :
            self.master.focus_set()

    def modification_election_numero(self):
        self.election.suprimer_fifidianana_voter(self.txtnumero_chercher.get())
        self.modiffication_insertion_election()

    def effacer_selection(self):
        for var in self.checkbox_vars:
            var.set(0)

    def handle_vato_fotsy_click(self):
        # Your code to handle the click event for "VATO FOTSY"
        try:
            if(self.tester_si_le_pifidy_existe_fAjour()==0 and self.tester_si_pifidy_existe_dans_vato_manakery()==0 and self.tester_si_pifidy_existe_dans_vato_maty()==0 and self.tester_si_pifidy_existe_dans_vato_fotsy()==0):
                current_value = self.txtmpifidynumero.get()
                response = messagebox.askyesno("Confirmation", "Enregistrement VATO MATY VE? \n N°:"+current_value)
                if(response):
                    self.detaillevato._setIdMpifidy(self.txtmpifidynumero.get())
                    self.detaillevato.inserer_dans_table_vatoFotsyL()
                    new_value = str(int(current_value) + 1)
                    messagebox.showinfo("INFORMATION", message="VATO FOTSY :"+current_value)
                    self.txtmpifidynumero.delete(0, tkinter.END)
                    self.txtmpifidynumero.insert(0, new_value)
                else:
                    messagebox.showinfo("INFORMATION", message="Enregistrement annulé.")
            else:
                messagebox.showerror("ERREUR", message="Efa misy manana io Numero io")
        except ValueError as err :
            messagebox.showerror("ERREUR", message="Numero Mpifidy svp!")
        finally :
            self.master.focus_set()
        pass

    def handle_vato_maty_click(self):
        # Your code to handle the click event for "VATO MATY"
        try:
            if(self.tester_si_le_pifidy_existe_fAjour()==0 and self.tester_si_pifidy_existe_dans_vato_manakery()==0 and self.tester_si_pifidy_existe_dans_vato_maty()==0 and self.tester_si_pifidy_existe_dans_vato_fotsy()==0):
                current_value = self.txtmpifidynumero.get()
                response = messagebox.askyesno("Confirmation", "Enregistrement VATO MATY VE? \n N°:"+current_value)
                if(response):
                    self.detaillevato._setIdMpifidy(self.txtmpifidynumero.get())
                    self.detaillevato.inserer_dans_table_vatoMatyL()
                    new_value = str(int(current_value) + 1)
                    messagebox.showinfo("INFORMATION", message="Vato Maty :"+current_value)
                    self.txtmpifidynumero.delete(0, tkinter.END)
                    self.txtmpifidynumero.insert(0, new_value)
                else:
                    messagebox.showinfo("INFORMATION", message="Enregistrement annulé.")
            else:
                messagebox.showerror("ERREUR", message="Efa misy manana io Numero io")
        except ValueError as err :
            messagebox.showerror("ERREUR", message="Numero Mpifidy svp!")
        finally :
            self.master.focus_set()
        pass

    def handle_vato_ENY_click(self):
        # Your code to handle the click event for "VATO MATY"
        try:
            if(self.tester_si_le_pifidy_existe_fAjour()==0 and self.tester_si_pifidy_existe_dans_vato_manakery()==0 and self.tester_si_pifidy_existe_dans_vato_maty()==0 and self.tester_si_pifidy_existe_dans_vato_fotsy()==0):
                current_value = self.txtmpifidynumero.get()
                response = messagebox.askyesno("Confirmation", "Enregistrement ENY VE? \n N°:"+current_value)
                if(response):
                    self.detaillevato._setIdMpifidy(self.txtmpifidynumero.get())
                    self.detaillevato.inserer_dans_table_FifidiananaLAjourEny()
                    self.detaillevato.inserer_dans_table_vatomanakeryL()
                    new_value = str(int(current_value) + 1)
                    messagebox.showinfo("INFORMATION", message="Vato Eny :"+current_value)
                    self.txtmpifidynumero.delete(0, tkinter.END)
                    self.txtmpifidynumero.insert(0, new_value)
                else:
                    messagebox.showinfo("INFORMATION", message="Enregistrement annulé.")
            else:
                messagebox.showerror("ERREUR", message="Efa misy manana io Numero io")

        except ValueError as err :
            messagebox.showerror("ERREUR", message="Numero Mpifidy svp!")
        finally :
            self.master.focus_set()
        pass

    def handle_vato_Tsia_click(self):
        # Your code to handle the click event for "VATO MATY"
        try:
            if(self.tester_si_le_pifidy_existe_fAjour()==0 and self.tester_si_pifidy_existe_dans_vato_manakery()==0 and self.tester_si_pifidy_existe_dans_vato_maty()==0 and self.tester_si_pifidy_existe_dans_vato_fotsy()==0):
                current_value = self.txtmpifidynumero.get()
                response = messagebox.askyesno("Confirmation", "Enregistrement TSIA VE? \n N°:"+current_value)
                if(response):
                    self.detaillevato._setIdMpifidy(self.txtmpifidynumero.get())
                    self.detaillevato.inserer_dans_table_FifidiananaLAjourTsia()
                    self.detaillevato.inserer_dans_table_vatomanakeryL()
                    new_value = str(int(current_value) + 1)
                    messagebox.showinfo("INFORMATION", message="Vato Tsia :"+current_value)
                    self.txtmpifidynumero.delete(0, tkinter.END)
                    self.txtmpifidynumero.insert(0, new_value)
                else:
                    messagebox.showinfo("INFORMATION", message="Enregistrement annulé.")
            else:
                messagebox.showerror("ERREUR", message="Efa misy manana io Numero io")
        except ValueError as err :
            messagebox.showerror("ERREUR", message="Numero Mpifidy svp!")
        finally :
            self.master.focus_set()
        pass


class FifidiananaVavy():
    def __init__(self, master):
        self.master = master
        self.master.title("Fifidianana")
        # self.master.resizable(False, False)

        self.master.geometry("1300x650")
        self.master.resizable(False, False)
        self.font = ("Bell MT", 12, "bold")
        self.background = "black"
        self.padx = 2
        self.pady = 2

        self.select_items = list()
        self.chekboxs = list()
        self.items = list()

        self.images = TImages.TImages()
        self.var_id_mpifidy_nampidirina_faranay = tkinter.StringVar()
        self.condidah =  TCondidahLandV. TCondidahLandV()
        self.election = TFifidiananaV.TFifidiananaV()
        self.detaillevato = MombaNyVato.MombaNyVato()
        self.Membres = TMembres.TMembres()
        self.var_user_valider = tkinter.StringVar()
        self.id_mpifidy_rechercher = tkinter.StringVar()
        self.citation_text = tkinter.StringVar()
        self.citation_text.set("\n\n\nNe te laisse pas vaincre par le mal, mais triomphe du mal par le bien.\n (Romains 12:21)")

        self.apropo_de_fifidianana = tkinter.LabelFrame(self.master, text="information fifidianana")
        self.apropo_de_fifidianana.grid(row=0, column=0, sticky=tkinter.NSEW)

        self.numero_dernier_mpifidy = tkinter.LabelFrame(self.apropo_de_fifidianana , text="numero ilay taratasy")
        self.numero_dernier_mpifidy.grid(row=0, column=0, sticky=tkinter.NSEW)

        self.fram_information = tkinter.LabelFrame(self.apropo_de_fifidianana , text="Recherche")
        self.fram_information.grid(row=2, column=0, sticky=tkinter.NSEW)

        self.fram_fifidianana_inconu = tkinter.LabelFrame(self.apropo_de_fifidianana , text="VatoFotsy/vatoMaty")
        self.fram_fifidianana_inconu.grid(row=1, column=0, sticky=tkinter.NSEW)

        self.autre_information = tkinter.LabelFrame(self.apropo_de_fifidianana , text="Teny ao anaty baiboly")
        self.autre_information.grid(row=3, column=0, sticky=tkinter.NSEW)

        #self.fram_olona_fidina = ScrollableFrame(self.master, text="Liste Condidah")
        #self.fram_olona_fidina.pack(row=0, column=1, sticky=tkinter.NSEW)

        self.fram_olona_fidina = ScrollableFrame(self.master, frame_text="Liste Condidat")
        self.fram_olona_fidina.grid(row=0, column=1, sticky=tkinter.NE)
        #self.fram_olona_fidina.grid_propagate(False)
        #self.fram_olona_fidina.config(width=500, height=300)

        self.mpifidynumero = tkinter.Label(self.numero_dernier_mpifidy, text="Numero taratasy", font=self.font, background=self.background, foreground="white")
        self.mpifidynumero.grid(row=0, column=0, sticky=tkinter.EW, padx=self.padx, pady=self.pady)
        self.txtmpifidynumero = tkinter.Entry(self.numero_dernier_mpifidy, textvariable=self.var_id_mpifidy_nampidirina_faranay , justify=tkinter.CENTER, width=28)
        self.txtmpifidynumero.grid(row=1, column=0, sticky=tkinter.NSEW, padx=self.padx, pady=self.pady)

        self.numero_chercher = tkinter.Label(self.fram_information, text="Numero à chercher :", font=self.font, background=self.background, foreground="white")
        self.numero_chercher.grid(row=0, column=0, sticky=tkinter.EW, padx=self.padx, pady=self.pady)
        self.txtnumero_chercher = tkinter.Entry(self.fram_information, textvariable=self.var_user_valider, justify=tkinter.CENTER, width=28)
        self.txtnumero_chercher.grid(row=1, column=0, sticky=tkinter.NSEW, padx=self.padx, pady=self.pady)

        self.btn_rechercher = tkinter.Button(self.fram_information, font= self.font, text="Rechercher", fg="white", background="dark blue", command=self.cocher_les_case)
        self.btn_rechercher.grid(row=4, column=0, sticky=tkinter.EW, pady=self.pady, padx=self.padx)

        self.btn_ajout_vato_fotsy = tkinter.Button(self.fram_fifidianana_inconu, font= self.font, text="VATO FOTSY", fg="white", background="dark blue", command=self.handle_vato_fotsy_click)
        self.btn_ajout_vato_fotsy.grid(row=1, column=0,sticky=tkinter.EW, pady=self.pady, padx=self.padx)

        self.btn_ajout_vato_Maty = tkinter.Button(self.fram_fifidianana_inconu, font= self.font, text="VATO MATY", fg="white", background="dark blue", command=self.handle_vato_maty_click)
        self.btn_ajout_vato_Maty.grid(row=2, column=0, sticky=tkinter.EW, pady=self.pady, padx=self.padx)

        self.btn_ajout_vato_Maty = tkinter.Button(self.fram_fifidianana_inconu, font= self.font, text="mamafa cocher", fg="white", background="dark blue", command=self.effacer_selection)
        self.btn_ajout_vato_Maty.grid(row=3, column=0, sticky=tkinter.EW, pady=self.pady, padx=self.padx)


       # citation_text = "\n\n\nNe te laisse pas vaincre par le mal, mais triomphe du mal par le bien.\n (Romains 12:21)"

        self.teny_ambara = tkinter.Text(self.autre_information, font=self.font, wrap=tkinter.WORD, width=20)
        self.teny_ambara.insert(tkinter.END, self.citation_text.get())

        self.teny_ambara.tag_configure("center", justify="center")

        self.teny_ambara.tag_add("center", "1.0", "end")

        self.teny_ambara.config(state=tkinter.DISABLED)  # Empêcher l'édition du texte
        self.teny_ambara.pack(expand=True, fill="both", padx=self.padx, pady=self.pady)

        self.autre_information.after(6000, self.miser_a_jour_citation)


        self.items = self.condidah.getCondidahV()
        # print(self.items)
        self.checkbox_vars = [tkinter.IntVar() for _ in range(len(self.items))]

        self.ligne, self.column = 0, 0
        #for idx, item in enumerate(self.items):
        chek = 0
        for item in self.condidah.getCondidahInfoV():

            self.canvas_profil = tkinter.Canvas(self.fram_olona_fidina.scrollable_frame, height=130, width=150, background=self.background)
            self.canvas_profil.grid(row=self.ligne , column=self.column , sticky=tkinter.NW)

            photo = self.show_profil(item[4])
            self.canvas_profil.create_image(0, 0, anchor=tkinter.NW, image=photo)
            self.canvas_profil.image = photo
            #if self.column <4:
            # print("colone inferieur 3 =",idx)
            # Nom_de_personne = str(item)+"- "+self.Membres.getAnarana(item) +" "+ self.Membres.getFanampiny(item)
            Nom_de_personne = str(item[1])+"- "+item[2] +" "+ item[3]
            max_caracteres_par_ligne = 17

            # Diviser la chaîne en lignes si elle dépasse la longueur maximale
            lignes = [Nom_de_personne[i:i + max_caracteres_par_ligne] for i in range(0, len(Nom_de_personne), max_caracteres_par_ligne)]

            # Joindre les lignes avec \n
            nom_de_personne_formate = "\n".join(lignes)

            self.checkbox = tkinter.Checkbutton(self.fram_olona_fidina.scrollable_frame, text=nom_de_personne_formate , variable=self.checkbox_vars[chek] , onvalue=1, offvalue=0, width=15, bg="deep sky blue" , compound="top")
            # self.show_profil(self, IdMembre)
            self.checkbox.grid(row=self.ligne + 1, column=self.column, padx=self.padx, pady=self.pady)
            #self.chekboxs.append(self.checkbox)
            #self.chekboxs.append(self.canvas_profil)
            self.chekboxs.append((self.checkbox, self.canvas_profil))
            self.column += 1
            if self.column > 6 :
                self.column = 0
                self.ligne += 2

            chek = chek + 1

        self.envoier_les_condidah_au_base = tkinter.Button(self.fram_olona_fidina.scrollable_frame, font= self.font, text="Valider", fg="white", background="dark blue", command=self.enregistrer_insert_condidah_selectionner)
        if(self.column == 0 ):
            self.column = 1
        self.envoier_les_condidah_au_base.grid(row=self.ligne + 2 , column=self.column -1 , sticky=tkinter.EW, pady=self.pady, padx=self.padx)

        self.modiffier_les_election = tkinter.Button(self.fram_olona_fidina.scrollable_frame, font= self.font, text="Modiffication", fg="white", background="dark blue", command=self.modification_election_numero)
        self.modiffier_les_election.grid(row=self.ligne + 3 , column=self.column -1 , sticky=tkinter.EW, pady=self.pady, padx=self.padx)
             

    def miser_a_jour_citation(self):

        citations = [
            "\n\n\nMitandrema , ka miarova tena mba tsy ho azon' ny fieremana ianareo; fa ny ain' olona tsy miankina amin'ny habetsahan'ny zavatra ananany (Lioka 12:15)",
            "\n\n\nFa iray no Andriamanitra ,ary iray no Mpanalalana amin'Andriamanitra sy ny olona dia i Kristy Jesosy , Izay olona(1 Timoty 2:5)",
            "\n\n\nKanefa ny fanorenana mafy nataon' Andriamanitra dia miorina tsara sady manana izao tombo-kase izao:'Ny Tompo mahalala ny azy' , ary koa :'aoka ny olona rehetra izay manonona ny anaran' ny Tompo hiala amin'ny ratsy.'(2 Timoty 2:19)",
            "\n\n\nFa ataoko fa ny fahoriana amin' izao andro akehitriny izao dia tsy tokony hoharina amin'ny voninahitra izay haseho amintsika.(Romana 8:18)",
            "\n\n\nMitoria ny teny , mazotoa , na amin'ny fotoana na tsy amin'ny fotoana , mandrese lahatra, mamporisiha , mananara mafy amin'ny fahari-po sy ny fampianarana rehetra(2 Timoty 4:2)",
            "\n\n\nFa izy no nihavian'izao zavatra rehetra izao, ary Izy no mihazona azy sady izy koa no antony; Izy anie no homem-boninahitra mandrakizay Amen.(Romana 11:36)",
            "\n\n\nTandremo mba tsy hisy hamaly ratsy olona; fa miezaha mandrakariva hitady izay tsara, na amin'ny namanareo na amin'ny olona rehetra(1 Tesaloniana 5:15)",
            "\n\n\nFa hilaza fahendrena ny vavako hametsovetso fahalalana ny foko Atongilako hihaino oha-teny ny sofiko (Salamo 49.4,5)",
            "\n\n\nFa voasoratra hoe; Jehovah Andriamanitro no hiankohofanao , ary Izy irery ihany no hotompoinao(Matio 4:10)",
            "\n\n\nMa inona na inona tononinareo amin'ny fivavahana sy angatahinareo, dia minoa fa efa nandray ianareo, dia ho azonareo izany (Marka 11:24)",
            "\n\n\nAry izao no didiny , dia ny hinoantsika ny anaran' i Jesoa Kristy Zanany sy ny hifankatiavatsika araka ny didy nomeny antsika(I Jaona 3:23)",
            # Ajoutez d'autres citations ici
        ]

        nouvelle_citation = random.choice(citations)
        self.citation_text.set(nouvelle_citation)

        self.teny_ambara.config(state=tkinter.NORMAL)
        self.teny_ambara.delete("1.0", tkinter.END)

        # Insérez la nouvelle citation
        self.teny_ambara.insert(tkinter.END, self.citation_text.get())

        # Centrer le texte (si nécessaire)
        self.teny_ambara.tag_configure("center", justify="center")
        self.teny_ambara.tag_add("center", "1.0", "end")

        # Empêcher l'édition du texte
        self.teny_ambara.config(state=tkinter.DISABLED)

        self.autre_information.after(50000, self.miser_a_jour_citation)


    def show_profil(self, Nom_image):
        try:
            image = Image.open(os.getcwd() + "\\photo_membre\\" + Nom_image)
            image = image.resize((150, 130)) # , Image.ANTIALIAS
            photo = ImageTk.PhotoImage(image)
            return photo
        except :
            return ""

    def enregistrer_insert_condidah_selectionner(self):
        try :
            if(self.tester_si_pifidy_existe() == 0 and self.tester_si_pifidy_existe_dans_vato_manakery()==0 and self.tester_si_pifidy_existe_dans_vato_maty()==0 and self.tester_si_pifidy_existe_dans_vato_fotsy()==0):
                for numero_condidah in self.recurer_selection_condidah():
                    self.election._setIdCondidah(numero_condidah)
                    self.election._setIdMpifidy(self.txtmpifidynumero.get())
                    self.election.inserer_dans_table_FifidiananaV()
                    pass
                self.detaillevato._setIdMpifidy(self.txtmpifidynumero.get())
                self.detaillevato.inserer_dans_table_vatomanakeryV()
                self.effacer_selection()
                messagebox.showinfo("INFORMATION", message="Enregistré")
                        # Assuming self.txtmpifidynumero is an Entry widget
                current_value = self.txtmpifidynumero.get()
                new_value = str(int(current_value) + 1)
                self.txtmpifidynumero.delete(0, tkinter.END)
                self.txtmpifidynumero.insert(0, new_value)
            else:
                messagebox.showerror("ERREUR", message="Efa misy manana io Numero io")
        except ValueError as err :
            messagebox.showerror("ERREUR", message=str(err))
        except mysql.connector.errors.IntegrityError as e:
            messagebox.showerror("ERREUR", message=f"Erreur d'intégrité : {str(e)}")
        finally :
            self.master.focus_set()


    def tester_si_pifidy_existe(self):
        print(self.election.tester_les_mpifidy_existe(self.txtmpifidynumero.get()))
        return self.election.tester_les_mpifidy_existe(self.txtmpifidynumero.get())
    
    def tester_si_pifidy_existe_dans_vato_manakery(self):
        print(self.election.tester_les_mpifidy_existe_dans_vato_manakery(self.txtmpifidynumero.get()))
        return self.election.tester_les_mpifidy_existe_dans_vato_manakery(self.txtmpifidynumero.get())
    
    def tester_si_pifidy_existe_dans_vato_maty(self):
        print(self.election.tester_les_mpifidy_existe_dans_vato_maty(self.txtmpifidynumero.get()))
        return self.election.tester_les_mpifidy_existe_dans_vato_maty(self.txtmpifidynumero.get())

    def tester_si_pifidy_existe_dans_vato_fotsy(self):
        print(self.election.tester_les_mpifidy_existe_dans_vato_fotsy(self.txtmpifidynumero.get()))
        return self.election.tester_les_mpifidy_existe_dans_vato_fotsy(self.txtmpifidynumero.get())


    def recurer_selection_condidah(self):
        self.select_items.clear()
        for idx, var in enumerate(self.checkbox_vars):
            if var.get() == 1:
                self.select_items.append(self.items[idx])
                print("Numero cocher:"+str(self.items[idx]))
        return self.select_items

    def cocher_les_case(self):
        self.effacer_selection()
        print("tonga ato ny afatra")
        Liste_voafidy = [str(idcondidavofidy) for idcondidavofidy in self.election.getIdVoafidy(self.txtnumero_chercher.get())]
        for checkbox, canvas_profil in self.chekboxs:
            text_value = checkbox.cget('text')
            print(text_value.split("-")[0])
            print(Liste_voafidy)
            if text_value.split("-")[0] in Liste_voafidy:
                checkbox.select()

    def modiffication_insertion_election(self):
        try :
            for Numero_condidah in self.recurer_selection_condidah():
                self.election._setIdCondidah(Numero_condidah)
                self.election._setIdMpifidy(self.txtnumero_chercher.get())
                self.election.inserer_dans_table_FifidiananaV()
            self.effacer_selection()
            messagebox.showinfo("INFORMATION", message="Vita Soama tsara ny Modiffication")
        except ValueError as err :
            messagebox.showerror("ERREUR", message=str(err))
        except mysql.connector.errors.IntegrityError as e:
            messagebox.showerror("ERREUR", message=f"Erreur d'intégrité : {str(e)}")
        finally :
            self.master.focus_set()

    def modification_election_numero(self):
        for numcondidah in self.election.getlesvoafidy(self.txtnumero_chercher.get()):
            #print("numero moin un"+str(numcondidah[0]))
            self.election.manalavatoazo(numcondidah[0])
        self.election.suprimer_fifidianana_voter(self.txtnumero_chercher.get())
        self.modiffication_insertion_election()

    def effacer_selection(self):
        for var in self.checkbox_vars:
            var.set(0)

    def handle_vato_fotsy_click(self):
        # Your code to handle the click event for "VATO FOTSY"
        try:
            if(self.tester_si_pifidy_existe() == 0 and self.tester_si_pifidy_existe_dans_vato_manakery()==0 and self.tester_si_pifidy_existe_dans_vato_maty()==0 and self.tester_si_pifidy_existe_dans_vato_fotsy()==0):
                current_value = self.txtmpifidynumero.get()
                response = messagebox.askyesno("Confirmation", "Enregistrement VATO FOTSY VE? \n N°:"+current_value)
                if(response):
                    self.detaillevato._setIdMpifidy(self.txtmpifidynumero.get())
                    self.detaillevato.inserer_dans_table_vatoFotsyV()
                    current_value = self.txtmpifidynumero.get()
                    new_value = str(int(current_value) + 1)
                    messagebox.showinfo("INFORMATION", message="VATO FOTSY :"+current_value)
                    self.txtmpifidynumero.delete(0, tkinter.END)
                    self.txtmpifidynumero.insert(0, new_value)
                else:
                    messagebox.showinfo("INFORMATION", message="Enregistrement annulé.")
            else:
                messagebox.showerror("ERREUR", message="Efa misy manana io Numero io")
        except ValueError as err :
            messagebox.showerror("ERREUR", message="Numero Mpifidy svp!")
        finally :
            self.master.focus_set()
        
        pass

    def handle_vato_maty_click(self):
        # Your code to handle the click event for "VATO MATY"
        try:
            if(self.tester_si_pifidy_existe() == 0 and self.tester_si_pifidy_existe_dans_vato_manakery()==0 and self.tester_si_pifidy_existe_dans_vato_maty()==0 and self.tester_si_pifidy_existe_dans_vato_fotsy()==0):
                current_value = self.txtmpifidynumero.get()
                response = messagebox.askyesno("Confirmation", "Enregistrement VATO MATY VE? \n N°:"+current_value)
                if(response):
                    self.detaillevato._setIdMpifidy(self.txtmpifidynumero.get())
                    self.detaillevato.inserer_dans_table_vatoMatyV()
                    current_value = self.txtmpifidynumero.get()
                    new_value = str(int(current_value) + 1)
                    messagebox.showinfo("INFORMATION", message="Vato Maty :"+current_value)
                    self.txtmpifidynumero.delete(0, tkinter.END)
                    self.txtmpifidynumero.insert(0, new_value)
                else:
                    messagebox.showinfo("INFORMATION", message="Enregistrement annulé.")
            else:
                messagebox.showerror("ERREUR", message="Efa misy manana io Numero io")
        except ValueError as err :
            messagebox.showerror("ERREUR", message="Numero Mpifidy svp!")
        finally :
            self.master.focus_set()
        pass

class CapturePhoto():
    def __init__(self, master):
        self.master = master
        
        self.master.title("Capture de photo")

        # Créer un cadre pour afficher la vidéo
        self.frame = ttk.Frame(self.master)
        self.frame.grid(row = 0, column=0)

        self.cap = cv2.VideoCapture(0)
        if not self.cap.isOpened():
            self.master.quit()

        self.panel = ttk.Label(self.frame)
        self.panel.grid(row = 0, column = 0)

        # Bouton de capture
        self.capture_button = ttk.Button(self.master, text="capturer une photo", command=self.capture_photo)
        self.capture_button.grid(row = 1, column = 0)

        # Mettre à jour l'aperçu en temps réel
        self.update_preview()

        # Fermer la webcam
        
        self.cap.release()

    def capture_photo(self):
        ret, frame = self.cap.read()
        if ret:
            cv2.imwrite("photo_capturee.jpg", frame)
            print("Photo enregistrée avec succès.")
    
    def update_preview(self):
        ret, frame = self.cap.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(frame)
            img = ImageTk.PhotoImage(img)
            self.panel.img = img
            self.panel.configure(image=img)
        self.master.after(10, self.update_preview)

class Search():
    def __init__(self, master):
        self.master = master
        self.master.title("RECHERCHE")
        self.master.resizable(False, False)
        
        self.font = ("Bell MT", 12, "bold")
        self.background = "black"
        self.padx = 2
        self.pady = 2



        self.membre = TMembres.TMembres()
        self.nahaterahana = TNaterahana.TNahaterahana()
        self.batisa = TBatisa.TBatisa()
        self.mpandray = TMpandray.TMpandray()
        self.nisoratana = TNisoratana.TNisoratana()
        self.fanamasinana = TFanamasinana.TFanamasinana()
        self.images = TImages.TImages()
        self.fianarana_diplome = TFianaranaDiplom.TFianaranaDiplom()
        self.sampana = TSampana.TSampana()
        self.sampana_membre = TSampana_Membre.TSampana_Membre()

        self.varRecherche = tkinter.StringVar()
        self.varAgeMin = tkinter.StringVar()
        self.varAgeMax = tkinter.StringVar()
        self.varBatisa = tkinter.StringVar()
        self.varMpandray = tkinter.StringVar()
        self.varFanamasinana = tkinter.StringVar()
        self.varCompteur = tkinter.IntVar()

        self.frame_recherche = tkinter.LabelFrame(self.master, text="RECHERCHE")
        self.frame_recherche.grid(row=0, column=0, sticky=tkinter.NSEW)

        self.txtCompteur = tkinter.Entry(self.master, textvariable=self.varCompteur, justify=tkinter.CENTER, width=6)
        self.txtCompteur.grid(row=0, column=1, columnspan = 2, sticky=tkinter.NSEW, padx=self.padx, pady=7)

        self.lblRecherche = tkinter.Label(self.frame_recherche, text="Nom & Fiche Ankohonana :", font=self.font, background=self.background, foreground="white")
        self.lblRecherche.grid(row=0, column=0, sticky=tkinter.EW, padx=self.padx, pady=self.pady)
        self.txtRecherche = tkinter.Entry(self.frame_recherche, textvariable=self.varRecherche, justify=tkinter.CENTER, width=28)
        self.txtRecherche.grid(row=0, column=1, sticky=tkinter.NSEW, padx=self.padx, pady=self.pady)

        self.lblAgeMin = tkinter.Label(self.frame_recherche, text="AgeMin :", font=self.font, background=self.background, foreground="white")
        self.lblAgeMin.grid(row=0, column=2, sticky=tkinter.EW, padx=self.padx, pady=self.pady)
        self.txtAgeMin = tkinter.Entry(self.frame_recherche, textvariable=self.varAgeMin, justify=tkinter.CENTER, width=28)
        self.txtAgeMin.grid(row=0, column=3, sticky=tkinter.NSEW, padx=self.padx, pady=self.pady)

        self.lblAgeMax = tkinter.Label(self.frame_recherche, text="AgeMax :", font=self.font, background=self.background, foreground="white")
        self.lblAgeMax.grid(row=0, column=4, sticky=tkinter.EW, padx=self.padx, pady=self.pady)
        self.txtAgeMax = tkinter.Entry(self.frame_recherche, textvariable=self.varAgeMax, justify=tkinter.CENTER, width=28)
        self.txtAgeMax.grid(row=0, column=5, sticky=tkinter.NSEW, padx=self.padx, pady=self.pady)

        self.lblBatisa = tkinter.Label(self.frame_recherche, text="Batisa :", font=self.font, background=self.background, foreground="white")
        self.lblBatisa.grid(row=1, column=0, sticky=tkinter.EW, padx=self.padx, pady=self.pady)
        self.txtBatisa = tkinter.Entry(self.frame_recherche, textvariable=self.varBatisa, justify=tkinter.CENTER, width=28)
        self.txtBatisa.grid(row=1, column=1, sticky=tkinter.NSEW, padx=self.padx, pady=self.pady)

        self.lblMpandray= tkinter.Label(self.frame_recherche, text="Mpandray :", font=self.font, background=self.background, foreground="white")
        self.lblMpandray.grid(row=1, column=2, sticky=tkinter.EW, padx=self.padx, pady=self.pady)
        self.txtMpandray = tkinter.Entry(self.frame_recherche, textvariable=self.varMpandray, justify=tkinter.CENTER, width=28)
        self.txtMpandray.grid(row=1, column=3, sticky=tkinter.NSEW, padx=self.padx, pady=self.pady)

        self.lblFanamasinana= tkinter.Label(self.frame_recherche, text=" Fanamasinana :", font=self.font, background=self.background, foreground="white")
        self.lblFanamasinana.grid(row=1, column=4, sticky=tkinter.EW, padx=self.padx, pady=self.pady)
        self.txtFanamasinana = tkinter.Entry(self.frame_recherche, textvariable=self.varFanamasinana, justify=tkinter.CENTER, width=28)
        self.txtFanamasinana.grid(row=1, column=5, sticky=tkinter.NSEW, padx=self.padx, pady=self.pady)

        self.style = ttk.Style()
        self.style.configure("Treeview", rowheight=25)
        
        self.tableau = ttk.Treeview(self.master, columns=("Id", "Fiche Ankohonana", "Anarana", "Fanampiny", "Telephone"), show="headings" , height=25)
        self.tableau.heading("Id", text="Id")
        self.tableau.heading("Fiche Ankohonana", text="Fiche Ankohonana")
        self.tableau.heading("Anarana", text="Anarana")
        self.tableau.heading("Fanampiny", text="Fanampiny")
        self.tableau.heading("Telephone", text="Telephone")
        self.tableau.column("Id", width=25)
        self.tableau.column("Fiche Ankohonana", width=100)
        self.tableau.column("Telephone", width=50)
    

        self.tableau.grid(row = 1, column = 0 , sticky = tkinter.NSEW)

        self.scrollbar = tkinter.Scrollbar(self.master, command=self.tableau.yview)
        self.scrollbar.grid(row = 1, column = 1, sticky = tkinter.NS)
        self.tableau.config(yscrollcommand=self.scrollbar.set)


        self.txtRecherche.bind("<KeyRelease>", lambda event:self.recherche_par_nom())
        self.txtAgeMin.bind("<KeyRelease>", lambda event : self.recherche_par_age())
        self.txtAgeMax.bind("<KeyRelease>", lambda event : self.recherche_par_age())
        self.txtBatisa.bind("<KeyRelease>", lambda event : self.recherche_par_vitabatisa())
        self.txtMpandray.bind("<KeyRelease>", lambda event : self.recherche_par_vitampandray())
        self.txtFanamasinana.bind("<KeyRelease>", lambda event : self.recherche_par_vitafanamasinana())
        self.tableau.bind("<Double-1>", self.on_double_click)

    def delete_content(self):
        self.tableau.delete(*self.tableau.get_children())

    def recherche_par_nom(self):
        k = 0
        recherche = self.varRecherche.get().lower()
        self.delete_content()
        for option in self.membre.getContentTable():
            if recherche in str(option[1]).lower() or recherche in option[2].lower() or recherche in option[3].lower():
                self.tableau.insert("", "end", values= option)
                k = k + 1
        self.varCompteur.set(k)

    def recherche_par_age(self):
        self.delete_content()
        options, k = list(), 0
        if (self.varAgeMin.get().strip() != "" and self.varAgeMin.get().isdigit() 
            and (self.varAgeMax.get().strip() != "" and self.varAgeMax.get().isdigit())):
            options = self.nahaterahana.getAgeEntre(int(self.varAgeMin.get()), int(self.varAgeMax.get()))
        elif self.varAgeMax.get().strip() != "" and self.varAgeMax.get().isdigit():
            options = self.nahaterahana.getAgeMax(int(self.varAgeMax.get()))
        elif self.varAgeMin.get().strip() != "" and self.varAgeMin.get().isdigit():
            options = self.nahaterahana.getAgeMin(int(self.varAgeMin.get()))
        if options :
            for option in options :
                self.tableau.insert("", "end", values=option)
                k = k + 1
        self.varCompteur.set(k)

    def recherche_par_vitabatisa(self):
        self.delete_content()
        k = 0
        recherche = self.varBatisa.get()
        for option in self.membre.getMembreBatiser(recherche):
            self.tableau.insert("", "end", values= option)
            k = k + 1
        self.varCompteur.set(k)

    def recherche_par_vitampandray(self):
        self.delete_content()
        k = 0
        recherche = self.varMpandray.get()
        for option in self.membre.getMembreMpandray(recherche):
            self.tableau.insert("", "end", values= option)
            k = k + 1
        self.varCompteur.set(k)

    def recherche_par_vitafanamasinana(self):
        self.delete_content()
        k = 0
        recherche = self.varFanamasinana.get()
        for option in self.membre.getMembreMpivady(recherche):
            self.tableau.insert("", "end", values= option)
            k = k + 1
        self.varCompteur.set(k)
    
    def on_double_click(self, event):
        item = self.tableau.selection()[0] 
        valeur = self.tableau.item(item, "values")
        self.window_details_memebre = tkinter.Toplevel(self.master)
        App = DetailsMembre(self.window_details_memebre, valeur[0])
    
class DetailsMembre():
    def __init__(self, master, IdMembre):
        self.master = master
        self.master.title("DETAILS MEMBRE")

        self.IdMembre = IdMembre

        self.font = ("Bell MT", 12, "bold")
        self.background = "black"
        self.padx = 2
        self.pady = 2
        self.background_canvas = "light blue"

        self.membre = TMembres.TMembres()
        self.nahaterahana = TNaterahana.TNahaterahana()
        self.batisa = TBatisa.TBatisa()
        self.mpandray = TMpandray.TMpandray()
        self.nisoratana = TNisoratana.TNisoratana()
        self.fanamasinana = TFanamasinana.TFanamasinana()
        self.images = TImages.TImages()
        self.fianarana_diplome = TFianaranaDiplom.TFianaranaDiplom()
        self.sampana = TSampana.TSampana()
        self.sampana_membre = TSampana_Membre.TSampana_Membre()

        self.canvas = tkinter.Canvas(self.master, height = 600, width = 980, background = "light blue")
        self.canvas.grid(row = 0, column = 0, sticky= tkinter.NSEW)
        self.scrollbar = tkinter.Scrollbar(self.master, command=self.canvas.yview)
        self.scrollbar.grid(row = 0, column = 1, sticky = tkinter.NS)
        self.canvas.config(yscrollcommand=self.scrollbar.set)
        self.canvas.bind('<Configure>', self.configure_scroll_region)
        self.master.after(1000, self.afficher_membre, self.IdMembre)

    def configure_scroll_region(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox('all'))

       

    def afficher_membre(self, IdMembre):
        self.frame = tkinter.Frame(self.canvas, height=390*2, background=self.background_canvas)
        self.frame.grid(row=0, column=0, sticky=tkinter.NSEW)

        self.frame.columnconfigure(1, weight = 1)
        self.frame.rowconfigure(0, weight = 1)

        self.frame_capital = tkinter.Frame(self.frame, background = self.background_canvas)
        self.frame_capital.grid(row=0, column = 1, sticky = tkinter.NSEW)

        for i in range(4):
            self.frame_capital.rowconfigure(i, weight = 1)
        
        self.frame_capital.columnconfigure(1, weight = 1)

        self.canvas_profil = tkinter.Canvas(self.frame, height=150, width=175, background=self.background)
        self.canvas_profil.grid(row=0, column=0, sticky=tkinter.NW)

        photo = self.show_profil(IdMembre)
        self.canvas_profil.create_image(0, 0, anchor=tkinter.NW, image=photo)
        self.canvas_profil.image = photo

        self.lblFaritra = tkinter.Label(self.frame_capital, text = "Faritra :", fg = "white", font=self.font, background=self.background)
        self.lblFaritra.grid(row=0, column=0, sticky=tkinter.NSEW, padx=self.padx, pady=self.pady)
        self.txtFaritra = tkinter.Label(self.frame_capital, text=self.membre.getFaritra(IdMembre), fg = "white", font=self.font, background=self.background, anchor='w', width=60)
        self.txtFaritra.grid(row=0, column=1, sticky=tkinter.NSEW, padx=self.padx, pady=self.pady)

        self.lblFicheNumero = tkinter.Label(self.frame_capital, text = "Fiche Ankohonana :", fg = "white", font=self.font, background=self.background)
        self.lblFicheNumero.grid(row=1, column=0, sticky=tkinter.NSEW, padx=self.padx, pady=self.pady)
        self.txtFicheNumero = tkinter.Label(self.frame_capital, text = self.membre.getFicheNumero(IdMembre), fg = "white", font=self.font, background=self.background, anchor='w')
        self.txtFicheNumero.grid(row=1, column=1, sticky=tkinter.NSEW, padx=self.padx, pady=self.pady)

        self.lblAnarana = tkinter.Label(self.frame_capital, text = "Anarana :", fg = "white", font=self.font, background=self.background)
        self.lblAnarana.grid(row=2, column=0, sticky=tkinter.NSEW, padx=self.padx, pady=self.pady)
        self.txtAnarana = tkinter.Label(self.frame_capital, text=self.membre.getAnarana(IdMembre), fg = "white", font=self.font, background=self.background, anchor='w')
        self.txtAnarana.grid(row=2, column=1, sticky=tkinter.NSEW, padx=self.padx, pady=self.pady)

        self.lblFanampiny = tkinter.Label(self.frame_capital, text = "Fanampiny :", fg = "white", font=self.font, background=self.background)
        self.lblFanampiny.grid(row=3, column=0, sticky=tkinter.NSEW, padx=self.padx, pady=self.pady)
        self.txtFanampiny = tkinter.Label(self.frame_capital, text=self.membre.getFanampiny(IdMembre) , fg = "white", font=self.font, background=self.background, anchor='w')
        self.txtFanampiny.grid(row=3, column=1, sticky=tkinter.NSEW, padx=self.padx, pady=self.pady)

        self.lblTelephone = tkinter.Label(self.frame_capital, text = "Telephone :", fg = "white", font=self.font, background=self.background)
        self.lblTelephone.grid(row=4, column=0, sticky=tkinter.NSEW, padx=self.padx, pady=self.pady)
        self.txtTelephone = tkinter.Label(self.frame_capital, text=self.membre.getTelephone(IdMembre), fg = "white", font=self.font, background=self.background, anchor='w')
        self.txtTelephone.grid(row=4, column=1, sticky=tkinter.NSEW, padx=self.padx, pady=self.pady)

        #----------------------affichage nahaterahana---------------------
        self.lblDatyNahaterahana = tkinter.Label(self.frame, text = "Daty Nahaterahana :", fg = "white", font=self.font, background=self.background)
        self.lblDatyNahaterahana.grid(row=1, column=0, sticky=tkinter.NSEW, padx=self.padx, pady=self.pady)
        self.txtDatyNahaterahana = tkinter.Label(self.frame, text=self.nahaterahana.getDaty(IdMembre), fg = "white", font=self.font, background=self.background, anchor='w')
        self.txtDatyNahaterahana.grid(row=1, column=1, sticky=tkinter.NSEW, padx=self.padx, pady=self.pady)

        self.lblToeranaNahaterahana = tkinter.Label(self.frame, text = "Toerana Nahaterahana :", fg = "white", font=self.font, background=self.background)
        self.lblToeranaNahaterahana.grid(row=2, column=0, sticky=tkinter.NSEW, padx=self.padx, pady=self.pady)
        self.txtToeranaNahaterahana = tkinter.Label(self.frame, text=self.nahaterahana.getToerana(IdMembre), fg = "white", font=self.font, background=self.background, anchor='w')
        self.txtToeranaNahaterahana.grid(row=2, column=1, sticky=tkinter.NSEW, padx=self.padx, pady=self.pady)

        #---------------------xxxxxxxxx-------------------------------------

        self.lblRay = tkinter.Label(self.frame, text = "Ray :", fg = "white", font=self.font, background=self.background)
        self.lblRay.grid(row=3, column=0, sticky=tkinter.NSEW, padx=self.padx, pady=self.pady)
        self.txtRay = tkinter.Label(self.frame, text=self.membre.getRay(IdMembre), fg = "white", font=self.font, background=self.background, anchor='w')
        self.txtRay.grid(row=3, column=1, sticky=tkinter.NSEW, padx=self.padx, pady=self.pady)

        self.lblReny = tkinter.Label(self.frame, text = "Reny :", fg = "white", font=self.font, background=self.background)
        self.lblReny.grid(row=4, column=0, sticky=tkinter.NSEW, padx=self.padx, pady=self.pady)
        self.txtReny = tkinter.Label(self.frame, text=self.membre.getReny(IdMembre), fg = "white", font=self.font, background=self.background, anchor='w')
        self.txtReny.grid(row=4, column=1, sticky=tkinter.NSEW, padx=self.padx, pady=self.pady)

        self.lblVady = tkinter.Label(self.frame, text = "Vady :", fg = "white", font=self.font, background=self.background)
        self.lblVady.grid(row=5, column=0, sticky=tkinter.NSEW, padx=self.padx, pady=self.pady)
        self.txtVady = tkinter.Label(self.frame, text=self.membre.getVady(IdMembre), fg = "white", font=self.font, background=self.background, anchor='w')
        self.txtVady.grid(row=5, column=1, sticky=tkinter.NSEW, padx=self.padx, pady=self.pady)

        self.lblFanompona = tkinter.Label(self.frame, text = "Fanompona :", fg = "white", font=self.font, background=self.background)
        self.lblFanompona.grid(row=6, column=0, sticky=tkinter.NSEW, padx=self.padx, pady=self.pady)
        self.txtFanompona = tkinter.Label(self.frame, text=self.membre.getFanompona(IdMembre), fg = "white", font=self.font, background=self.background, anchor='w')
        self.txtFanompona.grid(row=6, column=1, sticky=tkinter.NSEW, padx=self.padx, pady=self.pady)

        self.lblAsa = tkinter.Label(self.frame, text = "Asa :", fg = "white", font=self.font, background=self.background)
        self.lblAsa.grid(row=9, column=0, sticky=tkinter.NSEW, padx=self.padx, pady=self.pady)
        self.txtAsa = tkinter.Label(self.frame, text=self.membre.getAsa(IdMembre), fg = "white", font=self.font, background=self.background, anchor='w')
        self.txtAsa.grid(row=9, column=1, sticky=tkinter.NSEW, padx=self.padx, pady=self.pady)

        self.lblTalenta = tkinter.Label(self.frame, text = "Talenta :", fg = "white", font=self.font, background=self.background)
        self.lblTalenta.grid(row=10, column=0, sticky=tkinter.NSEW, padx=self.padx, pady=self.pady)
        self.txtTalenta = tkinter.Label(self.frame, text=self.membre.getTalenta(IdMembre), fg = "white", font=self.font, background=self.background, anchor='w')
        self.txtTalenta.grid(row=10, column=1, sticky=tkinter.NSEW, padx=self.padx, pady=self.pady)

        self.lblAdiresy = tkinter.Label(self.frame, text = "Adiresy :", fg = "white", font=self.font, background=self.background)
        self.lblAdiresy.grid(row=11, column=0, sticky=tkinter.NSEW, padx=self.padx, pady=self.pady)
        self.txtAdiresy = tkinter.Label(self.frame, text=self.membre.getAdiresy(IdMembre), fg = "white", font=self.font, background=self.background, anchor='w')
        self.txtAdiresy.grid(row=11, column=1, sticky=tkinter.NSEW, padx=self.padx, pady=self.pady)

        self.lblEmail = tkinter.Label(self.frame, text = "Email :", fg = "white", font=self.font, background=self.background)
        self.lblEmail.grid(row=12, column=0, sticky=tkinter.NSEW, padx=self.padx, pady=self.pady)
        self.txtEmail = tkinter.Label(self.frame, text=self.membre.getEmail(IdMembre), fg = "white", font=self.font, background=self.background, anchor='w')
        self.txtEmail.grid(row=12, column=1, sticky=tkinter.NSEW, padx=self.padx, pady=self.pady)

        self.lblPseudo = tkinter.Label(self.frame, text = "Pseudo Messenger :", fg = "white", font=self.font, background=self.background)
        self.lblPseudo.grid(row=13, column=0, sticky=tkinter.NSEW, padx=self.padx, pady=self.pady)
        self.txtPseudo = tkinter.Label(self.frame, text=self.membre.getPseudo(IdMembre), fg = "white", font=self.font, background=self.background, anchor='w')
        self.txtPseudo.grid(row=13, column=1, sticky=tkinter.NSEW, padx=self.padx, pady=self.pady)
        
        #-----------------affichage batisa ------------------
       
        self.lblDatyBatisa = tkinter.Label(self.frame, text = "Daty Batisa :", fg = "white", font=self.font, background=self.background)
        self.lblDatyBatisa.grid(row=14, column=0, sticky=tkinter.NSEW, padx=self.padx, pady=self.pady)
        self.txtDatyBatisa = tkinter.Label(self.frame, text=self.batisa.getDaty(IdMembre), fg = "white", font=self.font, background=self.background, anchor='w')
        self.txtDatyBatisa.grid(row=14, column=1, sticky=tkinter.NSEW, padx=self.padx, pady=self.pady)

        self.lblToeranaBatisa = tkinter.Label(self.frame, text = "Toerana Batisa :", fg = "white", font=self.font, background=self.background)
        self.lblToeranaBatisa.grid(row=15, column=0, sticky=tkinter.NSEW, padx=self.padx, pady=self.pady)
        self.txtToeranaBatisa = tkinter.Label(self.frame, text=self.batisa.getToerana(IdMembre), fg = "white", font=self.font, background=self.background, anchor='w')
        self.txtToeranaBatisa.grid(row=15, column=1, sticky=tkinter.NSEW, padx=self.padx, pady=self.pady)

        #----------------affichage mpandray -------------------------
       
        self.lblDatyMpandray = tkinter.Label(self.frame, text = "Daty Mpandray :", fg = "white", font=self.font, background=self.background)
        self.lblDatyMpandray.grid(row=16, column=0, sticky=tkinter.NSEW, padx=self.padx, pady=self.pady)
        self.txtDatyMpandray = tkinter.Label(self.frame, text=self.mpandray.getDaty(IdMembre), fg = "white", font=self.font, background=self.background, anchor='w')
        self.txtDatyMpandray.grid(row=16, column=1, sticky=tkinter.NSEW, padx=self.padx, pady=self.pady)

        self.lblToeranaMpandray = tkinter.Label(self.frame, text = "Toerana Mpandray :", fg = "white", font=self.font, background=self.background)
        self.lblToeranaMpandray.grid(row=17, column=0, sticky=tkinter.NSEW, padx=self.padx, pady=self.pady)
        self.txtToeranaMpandray = tkinter.Label(self.frame, text=self.mpandray.getToerana(IdMembre), fg = "white", font=self.font, background=self.background, anchor='w')
        self.txtToeranaMpandray.grid(row=17, column=1, sticky=tkinter.NSEW, padx=self.padx, pady=self.pady)

        #-----------------------affichage nisoratna --------------------------------------
        self.lblDatyNisoratana = tkinter.Label(self.frame, text = "Daty Nisoratana :", fg = "white", font=self.font, background=self.background)
        self.lblDatyNisoratana.grid(row=18, column=0, sticky=tkinter.NSEW, padx=self.padx, pady=self.pady)
        self.txtDatyNisoratana = tkinter.Label(self.frame, text=self.nisoratana.getDaty(IdMembre), fg = "white", font=self.font, background=self.background, anchor='w')
        self.txtDatyNisoratana.grid(row=18, column=1, sticky=tkinter.NSEW, padx=self.padx, pady=self.pady)

        #----------------------affichage fanamasinana---------------------------------
        self.lblDatyFanamasinana = tkinter.Label(self.frame, text = "Daty Fanamasinana :", fg = "white", font=self.font, background=self.background)
        self.lblDatyFanamasinana.grid(row=19, column=0, sticky=tkinter.NSEW, padx=self.padx, pady=self.pady)
        self.txtDatyFanamasinana = tkinter.Label(self.frame, text=self.fanamasinana.getDaty(IdMembre), fg = "white", font=self.font, background=self.background, anchor='w')
        self.txtDatyFanamasinana.grid(row=19, column=1, sticky=tkinter.NSEW, padx=self.padx, pady=self.pady)

        self.lblToeranaFanamasinana = tkinter.Label(self.frame, text = "Toerana Fanamasinana :", fg = "white", font=self.font, background=self.background)
        self.lblToeranaFanamasinana.grid(row=20, column=0, sticky=tkinter.NSEW, padx=self.padx, pady=self.pady)
        self.txtToeranaFanamasinana = tkinter.Label(self.frame, text=self.fanamasinana.getToerana(IdMembre), fg = "white", font=self.font, background=self.background, anchor='w')
        self.txtToeranaFanamasinana.grid(row=20, column=1, sticky=tkinter.NSEW, padx=self.padx, pady=self.pady)

        self.frame_diplome = tkinter.LabelFrame(self.frame, text="Fianarana - Diplome", background=self.background, fg="white")
        self.frame_diplome.grid(row=21, column=0, columnspan=2, sticky=tkinter.NSEW)
        
        for key, value in enumerate(self.fianarana_diplome.getFinaranaDiplomeMembre(IdMembre)):
            self.label_diplome = tkinter.Label(self.frame_diplome, text=str(value[0]) + " - " + str(value[1]) + "/", background=self.background, fg="white", font=self.font)
            self.label_diplome.grid(row=0, column=key)
        
        self.frame_sampana = tkinter.LabelFrame(self.frame, text="Sampana", background=self.background, fg="white")
        self.frame_sampana.grid(row=22, column=0, columnspan=2, sticky=tkinter.NSEW)
        
        for key, value in enumerate(self.sampana_membre.getIdSampana(IdMembre)):
            self.label_sampana = tkinter.Label(self.frame_sampana, text=self.sampana.getNomSampana(value) + "/", background=self.background, fg="white", font=self.font)
            self.label_sampana.grid(row=0, column=key)

        return self.frame

    def show_profil(self, IdMembre):
        try:
            image = Image.open(os.getcwd() + "\\photo_membre\\" + self.images.getNomImage(IdMembre))
            image = image.resize((175, 150)) # , Image.ANTIALIAS
            photo = ImageTk.PhotoImage(image)
            return photo
        except :
            return ""
       
class Rechercher():
    def __init__(self, master):
        self.master = master
        self.master.title("RECHERCHE")
        self.master.resizable(False, False)
        
        self.font = ("Bell MT", 12, "bold")
        self.background = "black"
        self.padx = 2
        self.pady = 2

        self.background_canvas = "light blue"

        self.membre = TMembres.TMembres()
        self.nahaterahana = TNaterahana.TNahaterahana()
        self.batisa = TBatisa.TBatisa()
        self.mpandray = TMpandray.TMpandray()
        self.nisoratana = TNisoratana.TNisoratana()
        self.fanamasinana = TFanamasinana.TFanamasinana()
        self.images = TImages.TImages()
        self.fianarana_diplome = TFianaranaDiplom.TFianaranaDiplom()
        self.sampana = TSampana.TSampana()
        self.sampana_membre = TSampana_Membre.TSampana_Membre()

        self.varRecherche = tkinter.StringVar()
        self.varAgeMin = tkinter.StringVar()
        self.varAgeMax = tkinter.StringVar()
        self.varBatisa = tkinter.StringVar()
        self.varMpandray = tkinter.StringVar()
        self.varBatiserMpandray = tkinter.StringVar()
        self.varCompteur = tkinter.IntVar()
        
        self.frame_recherche = tkinter.LabelFrame(self.master, text="RECHERCHE")
        self.frame_recherche.grid(row=0, column=0, sticky=tkinter.NSEW)

        self.txtCompteur = tkinter.Entry(self.master, textvariable=self.varCompteur, justify=tkinter.CENTER, width=6)
        self.txtCompteur.grid(row=0, column=1, columnspan = 2, sticky=tkinter.NSEW, padx=self.padx, pady=7)

        self.lblRecherche = tkinter.Label(self.frame_recherche, text="Nom & Fiche Ankohonana :", font=self.font, background=self.background, foreground="white")
        self.lblRecherche.grid(row=0, column=0, sticky=tkinter.EW, padx=self.padx, pady=self.pady)
        self.txtRecherche = tkinter.Entry(self.frame_recherche, textvariable=self.varRecherche, justify=tkinter.CENTER, width=28)
        self.txtRecherche.grid(row=0, column=1, sticky=tkinter.NSEW, padx=self.padx, pady=self.pady)

        self.lblAgeMin = tkinter.Label(self.frame_recherche, text="AgeMin :", font=self.font, background=self.background, foreground="white")
        self.lblAgeMin.grid(row=0, column=2, sticky=tkinter.EW, padx=self.padx, pady=self.pady)
        self.txtAgeMin = tkinter.Entry(self.frame_recherche, textvariable=self.varAgeMin, justify=tkinter.CENTER, width=28)
        self.txtAgeMin.grid(row=0, column=3, sticky=tkinter.NSEW, padx=self.padx, pady=self.pady)

        self.lblAgeMax = tkinter.Label(self.frame_recherche, text="AgeMax :", font=self.font, background=self.background, foreground="white")
        self.lblAgeMax.grid(row=0, column=4, sticky=tkinter.EW, padx=self.padx, pady=self.pady)
        self.txtAgeMax = tkinter.Entry(self.frame_recherche, textvariable=self.varAgeMax, justify=tkinter.CENTER, width=28)
        self.txtAgeMax.grid(row=0, column=5, sticky=tkinter.NSEW, padx=self.padx, pady=self.pady)

        self.lblBatisa = tkinter.Label(self.frame_recherche, text="Batisa :", font=self.font, background=self.background, foreground="white")
        self.lblBatisa.grid(row=1, column=0, sticky=tkinter.EW, padx=self.padx, pady=self.pady)
        self.txtBatisa = tkinter.Entry(self.frame_recherche, textvariable=self.varBatisa, justify=tkinter.CENTER, width=28)
        self.txtBatisa.grid(row=1, column=1, sticky=tkinter.NSEW, padx=self.padx, pady=self.pady)

        self.lblMpandray= tkinter.Label(self.frame_recherche, text="Mpandray :", font=self.font, background=self.background, foreground="white")
        self.lblMpandray.grid(row=1, column=2, sticky=tkinter.EW, padx=self.padx, pady=self.pady)
        self.txtMpandray = tkinter.Entry(self.frame_recherche, textvariable=self.varMpandray, justify=tkinter.CENTER, width=28)
        self.txtMpandray.grid(row=1, column=3, sticky=tkinter.NSEW, padx=self.padx, pady=self.pady)

        self.lblBatiserMpandray= tkinter.Label(self.frame_recherche, text="Batisa & Mpandary :", font=self.font, background=self.background, foreground="white")
        self.lblBatiserMpandray.grid(row=1, column=4, sticky=tkinter.EW, padx=self.padx, pady=self.pady)
        self.txtBatiserMpandray = tkinter.Entry(self.frame_recherche, textvariable=self.varBatiserMpandray, justify=tkinter.CENTER, width=28)
        self.txtBatiserMpandray.grid(row=1, column=5, sticky=tkinter.NSEW, padx=self.padx, pady=self.pady)

        self.canvas = tkinter.Canvas(self.master, height = 525, width = 980, background = "light blue")
        self.canvas.grid(row = 1, column = 0, columnspan = 2, sticky= tkinter.NSEW)
        self.scrollbar = tkinter.Scrollbar(self.master, command=self.canvas.yview)
        self.scrollbar.grid(row = 1, column = 2, sticky = tkinter.NS)
        self.canvas.config(yscrollcommand=self.scrollbar.set)
            
        self.txtRecherche.bind("<KeyRelease>", lambda event:self.recherche_par_nom())
        self.txtBatisa.bind("<KeyRelease>", lambda event:self.recherche_par_vitabatisa())
        self.txtAgeMin.bind("<KeyRelease>", lambda event : self.recherche_par_age())
        self.txtAgeMax.bind("<KeyRelease>", lambda event : self.recherche_par_age())
        self.txtMpandray.bind("<KeyRelease>", lambda event : self.recherche_par_mpandray())
        self.txtBatiserMpandray.bind("<KeyRelease>", lambda event : self.recherche_par_batiser_et_mpandray())
        self.canvas.bind('<Configure>', self.configure_scroll_region)

    def configure_scroll_region(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox('all'))

    def getNombreContenue(self):
        options = self.membre.getContentTable()
        return len(options) + 1

    def recherche_par_nom(self):
        k = 0
        donnee = list()
        self.canvas.delete("all")
        recherche = self.varRecherche.get().lower()
        for option in self.membre.getContentTable():
            if (recherche in str(option[1]).lower() or recherche in option[2].lower() or recherche in option[3].lower()):
                faritra = self.membre.getFaritra(option[0])
                Numero = self.membre.getFicheNumero(option[0])
                Anarana = self.membre.getAnarana(option[0])
                Fanampiny = self.membre.getFanampiny(option[0])
                Vady = self.membre.getVady(option[0])
                Adress = self.membre.getAdiresy(option[0])
                Telephone = self.membre.getTelephone(option[0])

                donnee.append((option[0], faritra, Numero, Anarana + "\n" + Fanampiny, Vady, Adress + "\n" + Telephone))
                self.affichage_membre = self.afficher_membre(option[0])
                self.canvas.create_window(20, k*800, anchor=tkinter.NW, window=self.affichage_membre)
                k = k + 1
        self.varCompteur.set(k)
        self.configure_scroll_region(None)

    def recherche_par_vitabatisa(self):
        k = 0
        self.canvas.delete("all")
        recherche = self.varBatisa.get().lower()
        for option in self.membre.getMembreBatiser():
            if recherche in str(option[1]).lower() or recherche in option[2].lower() or recherche in option[3].lower():
                self.affichage_membre = self.afficher_membre(option[0])
                self.canvas.create_window(20, k*800, anchor=tkinter.NW, window=self.affichage_membre)
                k = k + 1
        self.varCompteur.set(k)
        self.configure_scroll_region(None)
    
    def recherche_par_mpandray(self):
        k = 0
        self.canvas.delete("all")
        recherche = self.varMpandray.get().lower()
        for option in self.membre.getMembreMpandray():
            if recherche in str(option[1]).lower() or recherche in option[2].lower() or recherche in option[3].lower():
                self.affichage_membre = self.afficher_membre(option[0])
                self.canvas.create_window(20, k*800, anchor=tkinter.NW, window=self.affichage_membre)
                k = k + 1
        self.varCompteur.set(k)
        self.configure_scroll_region(None)
    
    def recherche_par_batiser_et_mpandray(self):
        k = 0
        self.canvas.delete("all")
        recherche = self.varBatiserMpandray.get().lower()
        for option in self.membre.getMembreBatiserSyMpandray():
            if recherche in str(option[1]).lower() or recherche in option[2].lower() or recherche in option[3].lower():
                self.affichage_membre = self.afficher_membre(option[0])
                self.canvas.create_window(20, k*800, anchor=tkinter.NW, window=self.affichage_membre)
                k = k + 1
        self.varCompteur.set(k)
        self.configure_scroll_region(None)

    def recherche_par_age(self):
        self.canvas.delete("all")
        options, k = list(), 0
        if (self.varAgeMin.get().strip() != "" and self.varAgeMin.get().isdigit() \
            and (self.varAgeMax.get().strip() != "" and self.varAgeMax.get().isdigit())):
            options = self.nahaterahana.getAgeEntre(int(self.varAgeMin.get()), int(self.varAgeMax.get()))
        elif self.varAgeMax.get().strip() != "" and self.varAgeMax.get().isdigit():
            options = self.nahaterahana.getAgeMax(int(self.varAgeMax.get()))
        elif self.varAgeMin.get().strip() != "" and self.varAgeMin.get().isdigit():
            options = self.nahaterahana.getAgeMin(int(self.varAgeMin.get()))
        if options :
            for option in options :
                self.affichage_membre = self.afficher_membre(option[0])
                self.canvas.create_window(20, k*800, anchor=tkinter.NW, window=self.affichage_membre)
                k = k + 1
        self.varCompteur.set(k)
        self.configure_scroll_region(None)

    #------------------xxxxxxxxx--------------------------------
    
    def afficher_membre(self, IdMembre):
        self.frame = tkinter.Frame(self.canvas, height=390*self.getNombreContenue(), background=self.background_canvas)
        self.frame.grid(row=0, column=0, sticky=tkinter.NSEW)

        self.frame.columnconfigure(1, weight = 1)
        self.frame.rowconfigure(0, weight = 1)

        self.frame_capital = tkinter.Frame(self.frame, background = self.background_canvas)
        self.frame_capital.grid(row=0, column = 1, sticky = tkinter.NSEW)

        for i in range(4):
            self.frame_capital.rowconfigure(i, weight = 1)
        
        self.frame_capital.columnconfigure(1, weight = 1)

        self.canvas_profil = tkinter.Canvas(self.frame, height=150, width=175, background=self.background)
        self.canvas_profil.grid(row=0, column=0, sticky=tkinter.NW)

        photo = self.show_profil(IdMembre)
        self.canvas_profil.create_image(0, 0, anchor=tkinter.NW, image=photo)
        self.canvas_profil.image = photo

        self.lblFaritra = tkinter.Label(self.frame_capital, text = "Faritra :", fg = "white", font=self.font, background=self.background)
        self.lblFaritra.grid(row=0, column=0, sticky=tkinter.NSEW, padx=self.padx, pady=self.pady)
        self.txtFaritra = tkinter.Label(self.frame_capital, text=self.membre.getFaritra(IdMembre), fg = "white", font=self.font, background=self.background, anchor='w', width=60)
        self.txtFaritra.grid(row=0, column=1, sticky=tkinter.NSEW, padx=self.padx, pady=self.pady)

        self.lblFicheNumero = tkinter.Label(self.frame_capital, text = "Fiche Ankohonana :", fg = "white", font=self.font, background=self.background)
        self.lblFicheNumero.grid(row=1, column=0, sticky=tkinter.NSEW, padx=self.padx, pady=self.pady)
        self.txtFicheNumero = tkinter.Label(self.frame_capital, text = self.membre.getFicheNumero(IdMembre), fg = "white", font=self.font, background=self.background, anchor='w')
        self.txtFicheNumero.grid(row=1, column=1, sticky=tkinter.NSEW, padx=self.padx, pady=self.pady)

        self.lblAnarana = tkinter.Label(self.frame_capital, text = "Anarana :", fg = "white", font=self.font, background=self.background)
        self.lblAnarana.grid(row=2, column=0, sticky=tkinter.NSEW, padx=self.padx, pady=self.pady)
        self.txtAnarana = tkinter.Label(self.frame_capital, text=self.membre.getAnarana(IdMembre), fg = "white", font=self.font, background=self.background, anchor='w')
        self.txtAnarana.grid(row=2, column=1, sticky=tkinter.NSEW, padx=self.padx, pady=self.pady)

        self.lblFanampiny = tkinter.Label(self.frame_capital, text = "Fanampiny :", fg = "white", font=self.font, background=self.background)
        self.lblFanampiny.grid(row=3, column=0, sticky=tkinter.NSEW, padx=self.padx, pady=self.pady)
        self.txtFanampiny = tkinter.Label(self.frame_capital, text=self.membre.getFanampiny(IdMembre) , fg = "white", font=self.font, background=self.background, anchor='w')
        self.txtFanampiny.grid(row=3, column=1, sticky=tkinter.NSEW, padx=self.padx, pady=self.pady)

        self.lblTelephone = tkinter.Label(self.frame_capital, text = "Telephone :", fg = "white", font=self.font, background=self.background)
        self.lblTelephone.grid(row=4, column=0, sticky=tkinter.NSEW, padx=self.padx, pady=self.pady)
        self.txtTelephone = tkinter.Label(self.frame_capital, text=self.membre.getTelephone(IdMembre), fg = "white", font=self.font, background=self.background, anchor='w')
        self.txtTelephone.grid(row=4, column=1, sticky=tkinter.NSEW, padx=self.padx, pady=self.pady)

        #----------------------affichage nahaterahana---------------------
        self.lblDatyNahaterahana = tkinter.Label(self.frame, text = "Daty Nahaterahana :", fg = "white", font=self.font, background=self.background)
        self.lblDatyNahaterahana.grid(row=1, column=0, sticky=tkinter.NSEW, padx=self.padx, pady=self.pady)
        self.txtDatyNahaterahana = tkinter.Label(self.frame, text=self.nahaterahana.getDaty(IdMembre), fg = "white", font=self.font, background=self.background, anchor='w')
        self.txtDatyNahaterahana.grid(row=1, column=1, sticky=tkinter.NSEW, padx=self.padx, pady=self.pady)

        self.lblToeranaNahaterahana = tkinter.Label(self.frame, text = "Toerana Nahaterahana :", fg = "white", font=self.font, background=self.background)
        self.lblToeranaNahaterahana.grid(row=2, column=0, sticky=tkinter.NSEW, padx=self.padx, pady=self.pady)
        self.txtToeranaNahaterahana = tkinter.Label(self.frame, text=self.nahaterahana.getToerana(IdMembre), fg = "white", font=self.font, background=self.background, anchor='w')
        self.txtToeranaNahaterahana.grid(row=2, column=1, sticky=tkinter.NSEW, padx=self.padx, pady=self.pady)

        #---------------------xxxxxxxxx-------------------------------------

        self.lblRay = tkinter.Label(self.frame, text = "Ray :", fg = "white", font=self.font, background=self.background)
        self.lblRay.grid(row=3, column=0, sticky=tkinter.NSEW, padx=self.padx, pady=self.pady)
        self.txtRay = tkinter.Label(self.frame, text=self.membre.getRay(IdMembre), fg = "white", font=self.font, background=self.background, anchor='w')
        self.txtRay.grid(row=3, column=1, sticky=tkinter.NSEW, padx=self.padx, pady=self.pady)

        self.lblReny = tkinter.Label(self.frame, text = "Reny :", fg = "white", font=self.font, background=self.background)
        self.lblReny.grid(row=4, column=0, sticky=tkinter.NSEW, padx=self.padx, pady=self.pady)
        self.txtReny = tkinter.Label(self.frame, text=self.membre.getReny(IdMembre), fg = "white", font=self.font, background=self.background, anchor='w')
        self.txtReny.grid(row=4, column=1, sticky=tkinter.NSEW, padx=self.padx, pady=self.pady)

        self.lblVady = tkinter.Label(self.frame, text = "Vady :", fg = "white", font=self.font, background=self.background)
        self.lblVady.grid(row=5, column=0, sticky=tkinter.NSEW, padx=self.padx, pady=self.pady)
        self.txtVady = tkinter.Label(self.frame, text=self.membre.getVady(IdMembre), fg = "white", font=self.font, background=self.background, anchor='w')
        self.txtVady.grid(row=5, column=1, sticky=tkinter.NSEW, padx=self.padx, pady=self.pady)

        self.lblFanompona = tkinter.Label(self.frame, text = "Fanompona :", fg = "white", font=self.font, background=self.background)
        self.lblFanompona.grid(row=6, column=0, sticky=tkinter.NSEW, padx=self.padx, pady=self.pady)
        self.txtFanompona = tkinter.Label(self.frame, text=self.membre.getFanompona(IdMembre), fg = "white", font=self.font, background=self.background, anchor='w')
        self.txtFanompona.grid(row=6, column=1, sticky=tkinter.NSEW, padx=self.padx, pady=self.pady)

        self.lblAsa = tkinter.Label(self.frame, text = "Asa :", fg = "white", font=self.font, background=self.background)
        self.lblAsa.grid(row=9, column=0, sticky=tkinter.NSEW, padx=self.padx, pady=self.pady)
        self.txtAsa = tkinter.Label(self.frame, text=self.membre.getAsa(IdMembre), fg = "white", font=self.font, background=self.background, anchor='w')
        self.txtAsa.grid(row=9, column=1, sticky=tkinter.NSEW, padx=self.padx, pady=self.pady)

        self.lblTalenta = tkinter.Label(self.frame, text = "Talenta :", fg = "white", font=self.font, background=self.background)
        self.lblTalenta.grid(row=10, column=0, sticky=tkinter.NSEW, padx=self.padx, pady=self.pady)
        self.txtTalenta = tkinter.Label(self.frame, text=self.membre.getTalenta(IdMembre), fg = "white", font=self.font, background=self.background, anchor='w')
        self.txtTalenta.grid(row=10, column=1, sticky=tkinter.NSEW, padx=self.padx, pady=self.pady)

        self.lblAdiresy = tkinter.Label(self.frame, text = "Adiresy :", fg = "white", font=self.font, background=self.background)
        self.lblAdiresy.grid(row=11, column=0, sticky=tkinter.NSEW, padx=self.padx, pady=self.pady)
        self.txtAdiresy = tkinter.Label(self.frame, text=self.membre.getAdiresy(IdMembre), fg = "white", font=self.font, background=self.background, anchor='w')
        self.txtAdiresy.grid(row=11, column=1, sticky=tkinter.NSEW, padx=self.padx, pady=self.pady)

        self.lblEmail = tkinter.Label(self.frame, text = "Email :", fg = "white", font=self.font, background=self.background)
        self.lblEmail.grid(row=12, column=0, sticky=tkinter.NSEW, padx=self.padx, pady=self.pady)
        self.txtEmail = tkinter.Label(self.frame, text=self.membre.getEmail(IdMembre), fg = "white", font=self.font, background=self.background, anchor='w')
        self.txtEmail.grid(row=12, column=1, sticky=tkinter.NSEW, padx=self.padx, pady=self.pady)

        self.lblPseudo = tkinter.Label(self.frame, text = "Pseudo Messenger :", fg = "white", font=self.font, background=self.background)
        self.lblPseudo.grid(row=13, column=0, sticky=tkinter.NSEW, padx=self.padx, pady=self.pady)
        self.txtPseudo = tkinter.Label(self.frame, text=self.membre.getPseudo(IdMembre), fg = "white", font=self.font, background=self.background, anchor='w')
        self.txtPseudo.grid(row=13, column=1, sticky=tkinter.NSEW, padx=self.padx, pady=self.pady)
        
        #-----------------affichage batisa ------------------
       
        self.lblDatyBatisa = tkinter.Label(self.frame, text = "Daty Batisa :", fg = "white", font=self.font, background=self.background)
        self.lblDatyBatisa.grid(row=14, column=0, sticky=tkinter.NSEW, padx=self.padx, pady=self.pady)
        self.txtDatyBatisa = tkinter.Label(self.frame, text=self.batisa.getDaty(IdMembre), fg = "white", font=self.font, background=self.background, anchor='w')
        self.txtDatyBatisa.grid(row=14, column=1, sticky=tkinter.NSEW, padx=self.padx, pady=self.pady)

        self.lblToeranaBatisa = tkinter.Label(self.frame, text = "Toerana Batisa :", fg = "white", font=self.font, background=self.background)
        self.lblToeranaBatisa.grid(row=15, column=0, sticky=tkinter.NSEW, padx=self.padx, pady=self.pady)
        self.txtToeranaBatisa = tkinter.Label(self.frame, text=self.batisa.getToerana(IdMembre), fg = "white", font=self.font, background=self.background, anchor='w')
        self.txtToeranaBatisa.grid(row=15, column=1, sticky=tkinter.NSEW, padx=self.padx, pady=self.pady)

        #----------------affichage mpandray -------------------------
       
        self.lblDatyMpandray = tkinter.Label(self.frame, text = "Daty Mpandray :", fg = "white", font=self.font, background=self.background)
        self.lblDatyMpandray.grid(row=16, column=0, sticky=tkinter.NSEW, padx=self.padx, pady=self.pady)
        self.txtDatyMpandray = tkinter.Label(self.frame, text=self.mpandray.getDaty(IdMembre), fg = "white", font=self.font, background=self.background, anchor='w')
        self.txtDatyMpandray.grid(row=16, column=1, sticky=tkinter.NSEW, padx=self.padx, pady=self.pady)

        self.lblToeranaMpandray = tkinter.Label(self.frame, text = "Toerana Mpandray :", fg = "white", font=self.font, background=self.background)
        self.lblToeranaMpandray.grid(row=17, column=0, sticky=tkinter.NSEW, padx=self.padx, pady=self.pady)
        self.txtToeranaMpandray = tkinter.Label(self.frame, text=self.mpandray.getToerana(IdMembre), fg = "white", font=self.font, background=self.background, anchor='w')
        self.txtToeranaMpandray.grid(row=17, column=1, sticky=tkinter.NSEW, padx=self.padx, pady=self.pady)

        #-----------------------affichage nisoratna --------------------------------------
        self.lblDatyNisoratana = tkinter.Label(self.frame, text = "Daty Nisoratana :", fg = "white", font=self.font, background=self.background)
        self.lblDatyNisoratana.grid(row=18, column=0, sticky=tkinter.NSEW, padx=self.padx, pady=self.pady)
        self.txtDatyNisoratana = tkinter.Label(self.frame, text=self.nisoratana.getDaty(IdMembre), fg = "white", font=self.font, background=self.background, anchor='w')
        self.txtDatyNisoratana.grid(row=18, column=1, sticky=tkinter.NSEW, padx=self.padx, pady=self.pady)

        #----------------------affichage fanamasinana---------------------------------
        self.lblDatyFanamasinana = tkinter.Label(self.frame, text = "Daty Fanamasinana :", fg = "white", font=self.font, background=self.background)
        self.lblDatyFanamasinana.grid(row=19, column=0, sticky=tkinter.NSEW, padx=self.padx, pady=self.pady)
        self.txtDatyFanamasinana = tkinter.Label(self.frame, text=self.fanamasinana.getDaty(IdMembre), fg = "white", font=self.font, background=self.background, anchor='w')
        self.txtDatyFanamasinana.grid(row=19, column=1, sticky=tkinter.NSEW, padx=self.padx, pady=self.pady)

        self.lblToeranaFanamasinana = tkinter.Label(self.frame, text = "Toerana Fanamasinana :", fg = "white", font=self.font, background=self.background)
        self.lblToeranaFanamasinana.grid(row=20, column=0, sticky=tkinter.NSEW, padx=self.padx, pady=self.pady)
        self.txtToeranaFanamasinana = tkinter.Label(self.frame, text=self.fanamasinana.getToerana(IdMembre), fg = "white", font=self.font, background=self.background, anchor='w')
        self.txtToeranaFanamasinana.grid(row=20, column=1, sticky=tkinter.NSEW, padx=self.padx, pady=self.pady)

        self.frame_diplome = tkinter.LabelFrame(self.frame, text="Fianarana - Diplome", background=self.background, fg="white")
        self.frame_diplome.grid(row=21, column=0, columnspan=2, sticky=tkinter.NSEW)
        
        for key, value in enumerate(self.fianarana_diplome.getFinaranaDiplomeMembre(IdMembre)):
            self.label_diplome = tkinter.Label(self.frame_diplome, text=str(value[0]) + " - " + str(value[1]) + "/", background=self.background, fg="white", font=self.font)
            self.label_diplome.grid(row=0, column=key)
        
        self.frame_sampana = tkinter.LabelFrame(self.frame, text="Sampana", background=self.background, fg="white")
        self.frame_sampana.grid(row=22, column=0, columnspan=2, sticky=tkinter.NSEW)
        
        for key, value in enumerate(self.sampana_membre.getIdSampana(IdMembre)):
            self.label_sampana = tkinter.Label(self.frame_sampana, text=self.sampana.getNomSampana(value) + "/", background=self.background, fg="white", font=self.font)
            self.label_sampana.grid(row=0, column=key)

        return self.frame
    
    def show_profil(self, IdMembre):
        try:
            image = Image.open(os.getcwd() + "\\photo_membre\\" + self.images.getNomImage(IdMembre))
            image = image.resize((175, 150)) # , Image.ANTIALIAS
            photo = ImageTk.PhotoImage(image)
            return photo
        except :
            return ""
     
class EnregistremenPersonnel():
    def __init__(self, master):
        self.master = master
        self.master.title("INFORMATON PERSONNEL")
        self.master.resizable(False, False)

        self.padx = 5
        self.pady = 5

        self.membre = TMembres.TMembres()
        self.faritra = TFaritra.TFaritra()

        self.font = ("Bell MT", 12, "bold")
        self.background = "black"

        self.varNumeroFiche = tkinter.StringVar()
        self.varNom = tkinter.StringVar()
        self.varPrenom = tkinter.StringVar()
        self.varPere = tkinter.StringVar()
        self.varMere = tkinter.StringVar()
        self.varEpoux = tkinter.StringVar()
        self.varFanompoana = tkinter.StringVar()
        # self.varSampana = tkinter.StringVar()
        # self.varFianarana = tkinter.StringVar()
        self.varAsaAndavanandro = tkinter.StringVar()
        self.varTalenta = tkinter.StringVar()
        self.varAdiresy = tkinter.StringVar()
        self.varTelephone = tkinter.StringVar()
        self.varEmail = tkinter.StringVar()
        self.varPseudo = tkinter.StringVar()
        self.varFaritra = tkinter.StringVar()
        self.varGenre = tkinter.StringVar()
        self.varGenre.set(" ")
        self.varMembres = tkinter.StringVar()
        self.varId = tkinter.IntVar()

        self.conteneur_information_personnel = tkinter.Frame(self.master)
        self.conteneur_information_personnel.grid(row=0, column=0)

        self.frame_utilisateur = tkinter.LabelFrame(self.conteneur_information_personnel)
        self.frame_utilisateur.grid(row=0, column=0, sticky=tkinter.NSEW, padx=self.padx, pady=self.pady)
        
        self.frame_genre = tkinter.LabelFrame(self.frame_utilisateur, text="GENRE", font=self.font)
        self.frame_genre.grid(row=0, column = 0 , sticky=tkinter.NSEW)

        self.frame_recherche = tkinter.LabelFrame(self.frame_utilisateur, text="Recherche", font=self.font)
        self.frame_recherche.grid(row=0, column=1, columnspan = 3, sticky=tkinter.NSEW)

        self.lblFaritra = tkinter.Label(self.frame_genre, font= self.font, text="Faritra ", fg="white", background=self.background)
        self.lblFaritra.grid(row=0, column=0, sticky=tkinter.NSEW, pady=self.pady, padx=self.padx)
        
        self.cbxFaritra = ttk.Combobox(self.frame_genre, textvariable=self.varFaritra, justify=tkinter.CENTER)
        self.cbxFaritra.grid(row=0, column=1, columnspan=3 , sticky=tkinter.NSEW, padx=self.padx, pady=self.pady)
        self.cbxFaritra['values'] = self.faritra.getFaritra()

        self.lblMAsculin = tkinter.Label(self.frame_genre, text="Lahy", font=self.font, bg="black", fg="white")
        self.lblMAsculin.grid(row=1, column=0, sticky=tkinter.NSEW, padx=self.padx, pady=self.pady)

        self.radioMasculin = ttk.Radiobutton(self.frame_genre, value = "M", variable=self.varGenre)
        self.radioMasculin.grid(row=1, column=1, sticky=tkinter.NSEW, padx=self.padx, pady=self.pady)

        self.lblFeminin = tkinter.Label(self.frame_genre, text="Vavy", font=self.font, bg="black", fg="white")
        self.lblFeminin.grid(row=1, column=2, sticky=tkinter.NSEW, padx=self.padx, pady=self.pady)
        
        self.radioFeminin = ttk.Radiobutton(self.frame_genre, value = "F", variable=self.varGenre)
        self.radioFeminin.grid(row=1, column=3, sticky=tkinter.NSEW, padx=self.padx, pady=self.pady)

        self.frame_recherche.columnconfigure(0, weight=1)
        self.frame_recherche.rowconfigure(0, weight=1)

        self.cbxMembre = tkinter.Entry(self.frame_recherche, font= self.font, textvariable=self.varMembres, justify=tkinter.CENTER)
        self.cbxMembre.grid(row=0, column=0 ,sticky=tkinter.NSEW, padx=self.padx, pady=self.pady)

        self.listResultats = tkinter.Listbox(self.frame_recherche, height=3)
        self.listResultats.grid(row=1, column=0, sticky=tkinter.EW, pady=2)

        self.scrollBar = tkinter.Scrollbar(self.frame_recherche, command=self.listResultats.yview)
        self.scrollBar.grid(row=1, column=1, sticky=tkinter.NS)

        self.listResultats.configure(yscrollcommand=self.scrollBar.set)

        self.cbxMembre.bind("<KeyRelease>", lambda event:self.recherche_options())
        self.listResultats.bind("<<ListboxSelect>>", self.recuprer_selection)



        self.lblnumeroFiche = tkinter.Label(self.frame_utilisateur, font= self.font, text="Numéro Ankohonana ", fg="white", background=self.background)
        self.lblnumeroFiche.grid(row=1, column=0, sticky=tkinter.NSEW, pady=self.pady, padx=self.padx)
        self.txtnumeroFiche = tkinter.Entry(self.frame_utilisateur, font= self.font, textvariable=self.varNumeroFiche, justify=tkinter.CENTER)
        self.txtnumeroFiche.grid(row=1, column=1, columnspan=3, sticky=tkinter.NSEW, padx=self.padx, pady=self.pady)

        self.lblAnarana = tkinter.Label(self.frame_utilisateur, font= self.font, text="Anarana", fg="white", background=self.background)
        self.lblAnarana.grid(row=2, column=0, sticky=tkinter.NSEW, pady=self.pady, padx=self.padx)
        self.txtAnarana = tkinter.Entry(self.frame_utilisateur, font= self.font, textvariable=self.varNom, justify=tkinter.CENTER)
        self.txtAnarana.grid(row=2, column=1, columnspan=3, sticky=tkinter.NSEW, padx=self.padx, pady=self.pady)

        self.lblFanampiny = tkinter.Label(self.frame_utilisateur, font= self.font, text="Fanampiny", fg="white", background=self.background)
        self.lblFanampiny.grid(row=3, column=0, sticky=tkinter.NSEW, pady=self.pady, padx=self.padx)
        self.txtFanampiny = tkinter.Entry(self.frame_utilisateur, font= self.font, textvariable=self.varPrenom, justify=tkinter.CENTER)
        self.txtFanampiny.grid(row=3, column=1, columnspan=3, sticky=tkinter.NSEW, padx=self.padx, pady=self.pady)

        self.lblRay = tkinter.Label(self.frame_utilisateur, font= self.font, text="Zanak'i ", fg="white", background=self.background)
        self.lblRay.grid(row=4, column=0, sticky=tkinter.NSEW, pady=self.pady, padx=self.padx)
        self.txtRay = tkinter.Entry(self.frame_utilisateur, font= self.font, textvariable=self.varPere, justify=tkinter.CENTER)
        self.txtRay.grid(row=4, column=1, sticky=tkinter.NSEW, padx=self.padx, pady=self.pady)

        self.lblReny = tkinter.Label(self.frame_utilisateur, font= self.font, text="Sy ", fg="white", background=self.background)
        self.lblReny.grid(row=4, column=2, sticky=tkinter.NSEW, pady=self.pady, padx=self.padx)
        self.txtReny = tkinter.Entry(self.frame_utilisateur, font= self.font, textvariable=self.varMere, justify=tkinter.CENTER)
        self.txtReny.grid(row=4, column=3, sticky=tkinter.NSEW, padx=self.padx, pady=self.pady)

        self.lblVady = tkinter.Label(self.frame_utilisateur, font= self.font, text="Anaran'ny Vady ", fg="white", background=self.background)
        self.lblVady.grid(row=5, column=0, sticky=tkinter.NSEW, pady=self.pady, padx=self.padx)
        self.txtVady = tkinter.Entry(self.frame_utilisateur, font= self.font, textvariable=self.varEpoux, justify=tkinter.CENTER)
        self.txtVady.grid(row=5, column=1, columnspan=3, sticky=tkinter.NSEW, padx=self.padx, pady=self.pady)

        self.lblFanompoana = tkinter.Label(self.frame_utilisateur, font= self.font, text="Fanompoana Manokana ", fg="white", background=self.background)
        self.lblFanompoana.grid(row=6, column=0, sticky=tkinter.NSEW, pady=self.pady, padx=self.padx)
        self.txtFanompoana = tkinter.Entry(self.frame_utilisateur, font= self.font, textvariable=self.varFanompoana, justify=tkinter.CENTER)
        self.txtFanompoana.grid(row=6, column=1, columnspan = 3, sticky=tkinter.NSEW, padx=self.padx, pady=self.pady)

        # self.lblFianarana = tkinter.Label(self.frame_utilisateur, font= self.font, text="Fianarana (diploma)", fg="white", background=self.background)
        # self.lblFianarana.grid(row=7, column=0, sticky=tkinter.NSEW, pady=self.pady, padx=self.padx)
        # self.txtFianarana = tkinter.Entry(self.frame_utilisateur, font= self.font, textvariable=self.varFianarana, justify=tkinter.CENTER)
        # self.txtFianarana.grid(row=7, column=1, columnspan = 3, sticky=tkinter.NSEW, padx=self.padx, pady=self.pady)

        self.lblAsaAndavanandro= tkinter.Label(self.frame_utilisateur, font= self.font, text="Asa Andavanandro/\nToeram-piasana", fg="white", background=self.background)
        self.lblAsaAndavanandro.grid(row=7, column=0, sticky=tkinter.NSEW, pady=self.pady, padx=self.padx)
        self.txtAsaAndavanandro = tkinter.Entry(self.frame_utilisateur, font= self.font, textvariable=self.varAsaAndavanandro, justify=tkinter.CENTER)
        self.txtAsaAndavanandro.grid(row=7, column=1, columnspan = 3, sticky=tkinter.NSEW, padx=self.padx, pady=self.pady)

        self.lblTalenta = tkinter.Label(self.frame_utilisateur, font= self.font, text="Talenta Manokana ", fg="white", background=self.background)
        self.lblTalenta.grid(row=8, column=0, sticky=tkinter.NSEW, pady=self.pady, padx=self.padx)
        self.txtTalenta = tkinter.Entry(self.frame_utilisateur, font= self.font, textvariable=self.varTalenta, justify=tkinter.CENTER)
        self.txtTalenta.grid(row=8, column=1, columnspan=3, sticky=tkinter.NSEW, padx=self.padx, pady=self.pady)

        self.lblAdiresy = tkinter.Label(self.frame_utilisateur, font= self.font, text="Adiresy ", fg="white", background=self.background)
        self.lblAdiresy.grid(row=9, column=0, sticky=tkinter.NSEW, pady=self.pady, padx=self.padx)
        self.txtAdiresy = tkinter.Entry(self.frame_utilisateur, font= self.font, textvariable=self.varAdiresy, justify=tkinter.CENTER)
        self.txtAdiresy.grid(row=9, column=1, columnspan=3, sticky=tkinter.NSEW, padx=self.padx, pady=self.pady)

        self.lblTelephone = tkinter.Label(self.frame_utilisateur, font= self.font, text="Téléphone ", fg="white", background=self.background)
        self.lblTelephone.grid(row=10, column=0, sticky=tkinter.NSEW, pady=self.pady, padx=self.padx)
        self.txtTelephone = tkinter.Entry(self.frame_utilisateur, font= self.font, textvariable=self.varTelephone, justify=tkinter.CENTER)
        self.txtTelephone.grid(row=10, column=1, columnspan=3, sticky=tkinter.NSEW, padx=self.padx, pady=self.pady)

        self.lblEmail = tkinter.Label(self.frame_utilisateur, font= self.font, text="Mailaka ", fg="white", background=self.background)
        self.lblEmail.grid(row=11, column=0, sticky=tkinter.NSEW, pady=self.pady, padx=self.padx)
        self.txtEmail = tkinter.Entry(self.frame_utilisateur, font= self.font, textvariable=self.varEmail, justify=tkinter.CENTER)
        self.txtEmail.grid(row=11, column=1, columnspan=3, sticky=tkinter.NSEW, padx=self.padx, pady=self.pady)

        self.lblPseudo = tkinter.Label(self.frame_utilisateur, font= self.font, text="Pseudo Messenger ", fg="white", background=self.background)
        self.lblPseudo.grid(row=12, column=0, sticky=tkinter.NSEW, pady=self.pady, padx=self.padx)
        self.txtPseudo = tkinter.Entry(self.frame_utilisateur, font= self.font, textvariable=self.varPseudo, justify=tkinter.CENTER)
        self.txtPseudo.grid(row=12, column=1,  columnspan=3, sticky=tkinter.NSEW, padx=self.padx, pady=self.pady)

        self.lblFanamarihana = tkinter.Label(self.frame_utilisateur, font=self.font, text="Fanamarihana", fg="white", bg=self.background )
        self.lblFanamarihana.grid(row=13, column=0, sticky=tkinter.NSEW, pady=self.pady, padx=self.padx)

        self.zoneFanamarihana = tkinter.Text(self.frame_utilisateur, font=self.font, height=3, width=30, bg="light blue")
        self.zoneFanamarihana.grid(row=13, column=1, columnspan=3, sticky=tkinter.EW, pady=self.pady, padx=self.padx)

        self.scrollBar_Zone = tkinter.Scrollbar(self.frame_utilisateur, command=self.zoneFanamarihana.yview)
        self.scrollBar_Zone.grid(row=13, column=4, sticky=tkinter.NS)

        self.zoneFanamarihana.configure(yscrollcommand=self.scrollBar_Zone.set)

        self.btnEffacer = tkinter.Button(self.frame_utilisateur, font= self.font, text="EFFACER", fg="white", background="dark blue", command=self.effacer)
        self.btnEffacer.grid(row=14, column=0, sticky=tkinter.NSEW, pady=self.pady, padx=self.padx)

        self.btnEnregistrer = tkinter.Button(self.frame_utilisateur, font= self.font, text="ENREGISTRER", fg="white", background="dark blue", command=self.enregistrer_membres)
        self.btnEnregistrer.grid(row=14, column=1, sticky=tkinter.NSEW, pady=self.pady, padx=self.padx)

        self.btnModifier = tkinter.Button(self.frame_utilisateur, font= self.font, text="MODIFIER", fg="white", background="dark blue", command=self.modifier_membres)
        self.btnModifier.grid(row=14, column=3, sticky=tkinter.NSEW, pady=self.pady, padx=self.padx)

    def enregistrer_membres(self):
        try:
            self.membre.Faritra = self.varFaritra.get()
            self.membre.FicheNumero = self.varNumeroFiche.get()
            self.membre.Anarana = self.varNom.get()
            self.membre.Fanampiny = self.varPrenom.get()
            self.membre.Genre = self.varGenre.get()
            self.membre.Ray = self.varPere.get()
            self.membre.Reny = self.varMere.get()
            self.membre.Vady = self.varEpoux.get()
            self.membre.Fanompona = self.varFanompoana.get()
            self.membre.Fanamariana = self.zoneFanamarihana.get("1.0", tkinter.END)
            # self.membre.Sampana = self.varSampana.get()
            # self.membre.Fianarana = self.varFianarana.get()
            self.membre.Asa = self.varAsaAndavanandro.get()
            self.membre.Talenta = self.varTalenta.get()
            self.membre.Adiresy = self.varAdiresy.get()
            self.membre.Telephone = self.varTelephone.get()
            self.membre.Email = self.varEmail.get()
            self.membre.Pseudo = self.varPseudo.get()
            self.membre.inserer_dans_table()
            self.effacer_texte()
            messagebox.showinfo("Information", message="Inscription réussi")
        except ValueError as err:
            messagebox.showerror("ERREUR", message=str(err))
        finally:
            self.master.focus_set()

    def modifier_membres(self):
        try :
            self.membre.IdMembre = self.varId.get()
            self.membre.Faritra = self.varFaritra.get()
            self.membre.FicheNumero = self.varNumeroFiche.get()
            self.membre.Anarana = self.varNom.get()
            self.membre.Fanampiny = self.varPrenom.get()
            self.membre.Genre = self.varGenre.get()
            self.membre.Ray = self.varPere.get()
            self.membre.Reny = self.varMere.get()
            self.membre.Vady = self.varEpoux.get()
            self.membre.Fanompona = self.varFanompoana.get()
            self.membre.Asa = self.varAsaAndavanandro.get()
            self.membre.Talenta = self.varTalenta.get()
            self.membre.Adiresy = self.varAdiresy.get()
            self.membre.Telephone = self.varTelephone.get()
            self.membre.Email = self.varEmail.get()
            self.membre.Pseudo = self.varPseudo.get()
            self.membre.Fanamariana = self.zoneFanamarihana.get("1.0", tkinter.END)
            self.membre.modifier_membre(self.varId.get())
            messagebox.showinfo("INFORMATION", message="modification effectué")
        except ValueError as err :
            messagebox.showerror("ERREUR", message=str(err))
        self.master.focus_set()

    def effacer_texte(self):
        self.varFaritra.set("")
        self.varNumeroFiche.set("")
        self.varNom.set("")
        self.varPrenom.set("")
        self.varPere.set("")
        self.varMere.set("")
        self.varEpoux.set("")
        self.varFanompoana.set("")
        self.zoneFanamarihana.delete("1.0", tkinter.END)
        # self.varFianarana.set("")
        self.varAsaAndavanandro.set("")
        self.varTalenta.set("")
        self.varAdiresy.set("")
        self.varTelephone.set("")
        self.varEmail.set("")
        self.varPseudo.set("")
        self.varGenre.set("")
        self.zoneFanamarihana.delete("1.0" , tkinter.END)

    def effacer(self):
        self.effacer_texte()

    def getText(self, donnee_tuple):
        reponse = str(donnee_tuple[0]) + "-" + "N : " + str(donnee_tuple[1]) + " " + \
        donnee_tuple[2] + " " + donnee_tuple[3]
        return reponse

    def recherche_options(self):
        recherche = self.cbxMembre.get().lower()
        self.listResultats.delete(0, tkinter.END)
        for option in self.getOptions():
            if recherche in str(option[1]).lower() or recherche in option[2].lower() or recherche in option[3].lower():
                self.listResultats.insert(tkinter.END, self.getText(option))
    
    def recuprer_selection(self, *args):
        index = self.listResultats.curselection()
        if index:
            selection = self.listResultats.get(index)
        idMembre = selection.split("-")[0]
        donnee_membre = self.membre.getMembre(idMembre)
        self.inserer_donner_recherche(donnee_membre)
        self.varFaritra.set(self.membre.getFaritra(idMembre))
        self.varNumeroFiche.set(self.membre.getFicheNumero(idMembre))
        self.varNom.set(self.membre.getAnarana(idMembre))
        self.varPrenom.set(self.membre.getFanampiny(idMembre))
        self.varGenre.set(self.membre.getGenre(self.varId.get()))
        self.varPere.set(self.membre.getRay(idMembre))
        self.varMere.set(self.membre.getReny(idMembre))
        self.varEpoux.set(self.membre.getVady(idMembre))
        self.varFanompoana.set(self.membre.getFanompona(idMembre))
        self.varAsaAndavanandro.set(self.membre.getAsa(idMembre))
        self.varTalenta.set(self.membre.getTalenta(idMembre))
        self.varAdiresy.set(self.membre.getAdiresy(idMembre))
        self.varTelephone.set(self.membre.getTelephone(idMembre))
        self.varEmail.set(self.membre.getEmail(idMembre))
        self.varPseudo.set(self.membre.getPseudo(idMembre))
        self.zoneFanamarihana.delete("1.0" , tkinter.END)
        try:
            self.zoneFanamarihana.insert(tkinter.END ,self.membre.getFanamarihana(idMembre))
        except: 
            pass
    
    def getIdMembre(self, tuple_donnee):
        return tuple_donnee[0]

    def inserer_donner_recherche(self, tuple_donnee):
        nom = self.getNomPrenom(tuple_donnee)
        idmembre = self.getIdMembre(tuple_donnee)
        self.varMembres.set(nom)
        self.varId.set(idmembre)
    
    def getOptions(self):
        options = self.membre.getContentTable()
        return options
    
    def getDateJour(self):
        date_actuelle = datetime.date.today()
        date_formater = date_actuelle.strftime("%d-%m-%Y")
        return date_formater
    
    def getNomPrenom(self, tuple_donnee):
        reponse = tuple_donnee[3] + " " + tuple_donnee[4]
        return reponse
 
class AdidyRechecheGrouper():
    def __init__(self, master):
        self.master = master
        self.master.title("RECHERCHE GROUPER")
        self.master.resizable(False, False)

        self.font = ("Bell MT", 12, "bold")
        self.padx =  2
        self.pady = 2

        self.varFaritra = tkinter.StringVar()
        self.varFicheNumero = tkinter.StringVar()
        self.varMois = tkinter.StringVar()
        self.varAnner = tkinter.StringVar()
        self.faritra = TFaritra.TFaritra()
        self.membre = TMembres.TMembres()

        self.varAnner.set(datetime.date.today().year)

        self.listes_month = [(1, "Janvier"), (2, "Février"), (3, "Mars"), (4, "Avril"), (5, "Mais"), (6, "Juin"),
                             (7, "Juillet"), (8, "Août"), (9, "Septembre"), (10, "Octobre"), (11, "Novembre"), (12, "Décembre")]

        self.lblFrame_recherche = tkinter.LabelFrame(self.master, text="RECHERCHE")
        self.lblFrame_recherche.grid(row=0, column=0, padx=self.padx, pady=self.pady)

        self.lblFaritra = tkinter.Label(self.lblFrame_recherche, text="Faritra", font=self.font, bg="black", fg="white")
        self.lblFaritra.grid(row=0, column=0, sticky=tkinter.NSEW, padx=self.padx, pady=self.pady)
        self.cbxFaritra = ttk.Combobox(self.lblFrame_recherche, textvariable=self.varFaritra, font=self.font, justify="center")
        self.cbxFaritra.grid(row=0, column=1, sticky=tkinter.NSEW, padx=self.padx, pady=self.pady)

        self.cbxFaritra["values"] = self.faritra.getFaritra()

        self.lblFicheNumero = tkinter.Label(self.lblFrame_recherche, text="Fiche Ankohonana", font=self.font, bg="black", fg="white")
        self.lblFicheNumero.grid(row=0, column=2, sticky=tkinter.NSEW, padx=self.padx, pady=self.pady)
        self.cbxFicheNumero = ttk.Combobox(self.lblFrame_recherche, textvariable=self.varFicheNumero, font=self.font, justify="center")
        self.cbxFicheNumero.grid(row=0, column=3, sticky=tkinter.NSEW, padx=self.padx, pady=self.pady)

        self.cbxFicheNumero['values'] = self.membre.getAllFicheNumero()

        self.lblMois = tkinter.Label(self.lblFrame_recherche, text="Mois", font=self.font, bg="black", fg="white")
        self.lblMois.grid(row=1, column=0, sticky=tkinter.NSEW, padx=self.padx, pady=self.pady)
        self.cbxMois = ttk.Combobox(self.lblFrame_recherche, textvariable=self.varMois, font=self.font, justify="center")
        self.cbxMois.grid(row=1, column=1, sticky=tkinter.NSEW, padx=self.padx, pady=self.pady)
        
        self.cbxMois["values"] = self.getNameMonth()

        self.lblAnner = tkinter.Label(self.lblFrame_recherche, text="Année", font=self.font, bg="black", fg="white")
        self.lblAnner.grid(row=1, column=2, sticky=tkinter.NSEW, padx=self.padx, pady=self.pady)
        self.cbxAnner = tkinter.Entry(self.lblFrame_recherche, textvariable=self.varAnner, font=self.font, justify="center")
        self.cbxAnner.grid(row=1, column=3, sticky=tkinter.NSEW, padx=self.padx, pady=self.pady)

        self.frame_contenue = tkinter.Label(self.master, background="black")
        self.frame_contenue.grid(row=1, column=0, sticky=tkinter.NSEW, padx=self.padx, pady=self.pady)

        self.frame_contenue.rowconfigure(0, weight=1)
        self.frame_contenue.columnconfigure(0, weight=1)

        self.treeview = ttk.Treeview(self.frame_contenue, columns=(1, 2), show='headings', height=17)
        self.treeview.heading(1, text="Non Définie")
        self.treeview.column(1, anchor='center')
        self.treeview.heading(2, text="Montant ")
        self.treeview.column(2, anchor='center')
        self.treeview.grid(row=0, column=0, sticky=tkinter.NSEW, padx=self.padx, pady=self.pady)

        self.scrollBar = ttk.Scrollbar(self.frame_contenue, orient='vertical', command=self.treeview.yview)
        self.scrollBar.grid(row=0, column=1, sticky=tkinter.NS)
        self.treeview.configure(yscrollcommand=self.scrollBar.set)

        self.treeview.tag_configure(0, background="light blue")
        self.treeview.tag_configure(1, background='deep sky blue')

        self.cbxFaritra.bind("<<ComboboxSelected>>", self.recherche_grouper_faritra)
        self.cbxFaritra.bind("<KeyRelease>", lambda event : self.recherche_grouper_faritra_release())
        self.cbxFicheNumero.bind("<<ComboboxSelected>>", self.recherche_grouper_ficheNumero)
        self.cbxFicheNumero.bind("<KeyRelease>", lambda event : self.recherche_grouper_ficheNumero_release())
    
    def getNameMonth(self):
        liste_names = [names[1] for names in self.listes_month]
        return liste_names
    
    def effacer_contenue_treeview(self):
        self.treeview.delete(*self.treeview.get_children())
    
    def getIdMonth(self, NameMonth):
        for month in self.listes_month:
            if month[1] == NameMonth:
                return month[0]
        return 0
    
    def recherche_grouper_faritra(self, event):
        self.effacer_contenue_treeview()
        self.treeview.heading(1, text="Faritra")
        for key, ligne in enumerate(self.membre.getMontantAdidyParFaritra(Month=self.getIdMonth(self.varMois.get()), Year=self.varAnner.get(), Faritra=self.varFaritra.get())):
            self.treeview.insert('', 'end', values=(ligne[0], format(ligne[1], ",")), tags=(key % 2))
    
    def recherche_grouper_faritra_release(self):
        self.effacer_contenue_treeview()
        self.treeview.heading(1, text="Faritra")
        for key, ligne in enumerate(self.membre.getMontantAdidyParFaritra(Month=self.getIdMonth(self.varMois.get()), Year=self.varAnner.get(), Faritra=self.varFaritra.get())):
            self.treeview.insert('', 'end', values=(ligne[0], format(ligne[1], ",")), tags=(key % 2))
    
    def recherche_grouper_ficheNumero(self, event):
        self.effacer_contenue_treeview()
        self.treeview.heading(1, text="Fiche Ankohonana")
        for key, ligne in enumerate(self.membre.getMontantAdidyParAnkohonana(Month=self.getIdMonth(self.varMois.get()), Year=self.varAnner.get(), FicheNumero=self.varFicheNumero.get())):
            self.treeview.insert('', 'end', values=(ligne[0], format(ligne[1], ",")), tags=(key % 2))
    
    def recherche_grouper_ficheNumero_release(self):
        self.effacer_contenue_treeview()
        self.treeview.heading(1, text="Fiche Ankohonana")
        for key, ligne in enumerate(self.membre.getMontantAdidyParAnkohonana(Month=self.getIdMonth(self.varMois.get()), Year=self.varAnner.get(), FicheNumero=self.varFicheNumero.get())):
            self.treeview.insert('', 'end', values=(ligne[0], format(ligne[1], ",")), tags=(key % 2))

class ContenueAdidy():
    def __init__(self, master, IdMembre):
        self.master = master
        self.IdMembre = IdMembre
        self.membre = TMembres.TMembres()
        self.adidy = TAdidy.TAdidy()
        self.master.title("ADIDY : {} {} ".format(self.membre.getAnarana(IdMembre).upper(), self.membre.getFanampiny(IdMembre)))
        self.master.resizable(False, False)
        self.treeview = ttk.Treeview(self.master, columns=(1, 2, 3), show='headings', height=17)
        self.treeview.heading(1, text="IdAdidy")
        self.treeview.column(1, anchor='center')
        self.treeview.heading(2, text="Date ")
        self.treeview.column(2, anchor='center')
        self.treeview.heading(3, text="Montant ")
        self.treeview.column(3, anchor='center')
        self.treeview.grid(row=0, column=0)

        self.scrollBar = ttk.Scrollbar(self.master, orient='vertical', command=self.treeview.yview)
        self.scrollBar.grid(row=0, column=1, sticky=tkinter.NS)
        self.treeview.configure(yscrollcommand=self.scrollBar.set)


        self.treeview.tag_configure(0, background="light blue")
        self.treeview.tag_configure(1, background='deep sky blue')
        self.treeview.tag_configure('totale', background='dark blue', foreground='white')

        self.contenue_afficher = [(value[0], value[2], format(value[3], ",")) for value in self.adidy.getAdidy(self.IdMembre)]
        for key, ligne in enumerate(self.contenue_afficher):
            self.treeview.insert('', 'end', values=ligne, tags=(key % 2))
        self.treeview.insert('', 'end', values=('TOTAL =', '', format(self.adidy.getTotalAdidy(self.IdMembre), ",")), tags='totale')
    
if __name__=="__main__":
    root = tkinter.Tk()
    App = ApplicationClient(root)
    root.mainloop()