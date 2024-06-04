class Gelenda:
    def __init__(self,FileWithGelenda):
        self.RawFile = FileWithGelenda
        self.TableElementList = []
        self.CoIleMetrowRobic = 10




    def GetHeightAtLenght(self,Where):

        Zakres_gorny = len(self.TableElementList)
        Zakres_dolny = 0

        for j in range(len(self.TableElementList)):
            Srodek = int( (Zakres_gorny+Zakres_dolny)/2)

            OdlegloscSrodka = self.TableElementList[Srodek][1]
            if Where>OdlegloscSrodka:
                Zakres_dolny = Srodek
            else:
                Zakres_gorny = Srodek

            if self.TableElementList[Srodek+1][1] >= Where and self.TableElementList[Srodek][1] <= Where:
                return self.TableElementList[Srodek+1][2]

        return -1

    def Process(self):
        RawSplitted = self.RawFile.split('\n')
        RawSplitted = RawSplitted[1:]
        RawSplitted = RawSplitted[:-1]
        RawSplitted = sorted(RawSplitted, key=lambda x: float(x.split(',')[1]))


        self.TableElementList = []

        WarstwaObiektow = []
        for i in range(1,len(RawSplitted)-1):
            JakaWarstwa = RawSplitted[i].split(',')[0]
            JakaOdleglosc = float(RawSplitted[i].split(',')[1])
            JakaWartosc = float(RawSplitted[i].split(',')[2])
            self.TableElementList.append((JakaWarstwa,JakaOdleglosc,JakaWartosc))


        WarstwaTerenu = []
        NajwiekszaDlugosc = self.TableElementList[-1][1]
        ObecnaDlugosc = 0
        for i in range( int(NajwiekszaDlugosc/self.CoIleMetrowRobic)):
            JakaJestWysokosc = self.GetHeightAtLenght(ObecnaDlugosc)
            ObecnaDlugosc = ObecnaDlugosc + self.CoIleMetrowRobic
            WarstwaTerenu.append(("Grunt",ObecnaDlugosc,JakaJestWysokosc))


        a = 4

