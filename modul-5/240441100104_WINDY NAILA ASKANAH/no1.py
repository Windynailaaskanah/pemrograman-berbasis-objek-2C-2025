from abc import ABC, abstractmethod

class Manusia(ABC):

    @abstractmethod
    def Berbicara(self):
        pass

    @abstractmethod
    def Bekerja(self):
        pass

    @abstractmethod
    def Makan(self):
        pass

class Joko(Manusia):

    def Berbicara(self):
        print("joko sedang berbicara dengan temannya")

    def Bekerja(self):
        print("joko bekerja sebagai programmer")

    def Makan(self): 
        print("joko sedang makan ayam geprek")

class Beni(Manusia):

    def Berbicara(self):
        print("beni sedang berbicara di atas panggung")

    def Bekerja(self):
        print("beni bekerja sebagai seorang pembawa acara")

    def Makan(self): 
        print("beni sedang makan nasi goreng")

class Fani(Manusia):

    def Berbicara(self):
        print("fani sedang berbicara dengan rani")

    def Bekerja(self):
        print("fani bekerja sebagai seorang perawat")

    def Makan(self): 
        print("fani sedang makan ayam penyet")

class Jani(Manusia):

    def Berbicara(self):
        print("jani sedang berbicara dengan rani")

    def Bekerja(self):
        print("jani bekerja sebagai seorang perawat")

    def Makan(self): 
        print("jani sedang makan ayam penyet")       

print("\n===JOKO===")
joko = Joko()
joko.Berbicara()
joko.Bekerja()
joko.Makan()

print("\n===BENI===")
beni = Beni()
beni.Berbicara()
beni.Bekerja()
beni.Makan()

print("\n===FANI===")
fani = Fani()
fani.Berbicara()
fani.Bekerja()
fani.Makan()

print("\n===JANI===")
jani = Jani()
jani.Berbicara()
jani.Bekerja()
jani.Makan()