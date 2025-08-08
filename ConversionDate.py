import datetime, re

class ConversionDate():
    def __init__(self , Test_daty_incorect =""):
        self.Test_daty_incorect=Test_daty_incorect
        pass

    def converteToDate(self, strDate):
        #pattern = r"^(0[1-9]|1[0-9]|2[0-9]|3[01])-(0[1-9]|1[0-9]|1[0-2])-(\d{4})$"
        # if (re.match(pattern, strDate)):
        try :
            date_obj = datetime.datetime.strptime(strDate, "%d-%m-%Y")
            self.Test_daty_incorect="0"
            return date_obj
        except ValueError as err :
            self.Test_daty_incorect="1"
            raise ValueError ("format date incorrect\nEx : 01-06-2022")


        # else :
        #     raise ValueError("format date incorrect\nEx : 01-06-2022")
    """ def tester_daty(self):
        try :
            if(isinstance(self.converteToDate("12-12-2022") , datetime.date )):
                print("FONCTION A ENVOIER UNE DATE VALIDER")
            else:
                print("fonction invalider")
        except ValueError as Ve:
            print("Eurreur attendu:" , Ve) """

    def getDate(self, strDate):
        date = datetime.datetime.strptime(strDate, "%d-%m-%Y")
        return date.date()
        
if __name__=="__main__":
    conv = ConversionDate()
    print(conv.getDate("12-12-2022"))
    print(conv.tester_daty())