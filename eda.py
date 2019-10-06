
#EDA

#Se crea cuadro de principales estadísticas de las variables numéricas

def selecciona_variables_numericas(archivo):
    lista_variables_numericas=archivo.select_dtypes(include = 'number').columns.values
    archivo_variables_numericas = archivo.loc[:, lista_variables_numericas]
    return archivo_variables_numericas

def q25(archivo):
    qal25=archivo.quantile(.25)
    return qal25

def q75(archivo):
    qal75=archivo.quantile(.75)
    return qal75

def uniques(archivo):
    uni=archivo.nunique()
    return uni

def prop_missings(archivo):
    prop=nulos=(archivo.isnull().sum()/len(archivo.index))*100
    return prop

#Falta crear funciones para obtener top3 valores más repetidos

archivonum=selecciona_variables_numericas(archivo)
archivonum.agg(['max','min','mean','std',q25,'median',q75,'skew','kurt','count',uniques,prop_missings])