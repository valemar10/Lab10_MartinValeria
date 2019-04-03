import urllib
from io import StringIO
from io import BytesIO
import csv
import numpy as np
from datetime import datetime
import matplotlib.pylab as plt
import pandas as pd
import scipy.signal as signal

datos1=pd.read_csv('https://raw.githubusercontent.com/ComputoCienciasUniandes/FISI2029-201910/master/Seccion_2/Fourier/Datos/transacciones2008.txt', sep=";", names=["date", "hora", "valor1", "valor2"])
datos2=pd.read_csv('https://raw.githubusercontent.com/ComputoCienciasUniandes/FISI2029-201910/master/Seccion_2/Fourier/Datos/transacciones2009.txt', sep=";", names=["date", "hora", "valor1", "valor2"])
datos3=pd.read_csv('https://raw.githubusercontent.com/ComputoCienciasUniandes/FISI2029-201910/master/Seccion_2/Fourier/Datos/transacciones2010.txt', sep=";", names=["date", "hora", "valor1", "valor2"])

datos1["new"]=datos1["date"].str[0:-8]+" "+datos1["hora"].str[-8:]
datos2["new"]=datos2["date"].str[0:-8]+" "+datos2["hora"].str[-8:]
datos3["new"]=datos3["date"].str[0:-8]+" "+datos3["hora"].str[-8:]
datos11=datos1.drop(['date', 'hora', 'valor2', 'valor1'], axis=1)
datos22=datos2.drop(['date', 'hora', 'valor2', 'valor1'], axis=1)
datos33=datos2.drop(['date', 'hora', 'valor2', 'valor1'], axis=1)

concatenacion=pd.concat([datos11, datos22, datos33])
print(concatenacion)


concat= open("datos.txt", "a")
concat.write(str(concatenacion))
concat.close()
print(concat)
