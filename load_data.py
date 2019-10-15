#Este módulo carga la información del archivo indicado, en este caso del consumo de agua en la Ciudad de México, el cual es un csv separado por punto y comas e imprime el número de observaciones y variables.

import pandas as pd

def carga_archivo(archivo):
    return pd.read_csv(archivo,sep=';')


def observaciones_variables(archivo):
    print('Número de observaciones:',archivo.shape[0],',', 'Número de variables:',archivo.shape[1],'\n') #numero       de observaciones y variables.
    
    
    
