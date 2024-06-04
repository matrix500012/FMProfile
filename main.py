from Gelenda import Gelenda

LokalizacjaPlikuWejsciowego = "\\\\enprom.pl\\Teams\\UAV\\Share\\ma\\22_02_Test\\KLAUDIUSOWE_SPRAWY\\03_06_2024\\profil_DISTANCE_ELEV.csv"




PlikZWysokosciami = open(LokalizacjaPlikuWejsciowego).read()
Gelendy = Gelenda(PlikZWysokosciami)
Gelendy.Process()
a = 4