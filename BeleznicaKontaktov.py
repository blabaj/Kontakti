def main():
    izvajaj = True
    seznam = []
    while(izvajaj == True):
        delaj = raw_input("Ali zelis dodati kontakt? (Da/Ne)").lower()
        if delaj == "da":
            vnosImena = raw_input("Vnesi ime")
            vnosPriimka = raw_input("Vnesi priimek")
            vnosEmaila = raw_input("Vnesi e-posto")
            vnosStevilke = raw_input("Vnesi tel. stevilko")
            vnosNaslova = raw_input("Vnesi naslov")
            oseba = kontakt(vnosImena, vnosPriimka, vnosEmaila, vnosStevilke, vnosNaslova)
            seznam.append(oseba)

        else:
            for oseba in seznam:
                oseba.izpisiPolnoIme()
            izvajaj = False

class kontakt(object):
    def __init__(self, first_name, last_name, email, phone, address ):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.address = address

    def izpisiPolnoIme(self):
        ime = self.first_name
        priimek = self.last_name
        print (ime + " " + priimek)

    def izpisiNaslove(self):
            eposta =  self.email
            tel = self.phone
            naslov = self.address
            print (eposta + " " + tel + " " + naslov)

if __name__ == '__main__':
    main()
