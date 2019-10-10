
#EDA

#Esta función genera el cuadro de estadísticas descripticas

def tabla_estadisticos_descriptivos_variables_numericas(archivo):
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
    archivonum=selecciona_variables_numericas(archivo).agg(['max','min','mean','std',q25,'median',q75,'skew','kurt','count',uniques,prop_missings])
    return archivonum

#El siguiente código ya imprime el listado de los 3 más repetidos pero aún no sé cómo guardar todo en un solo dataframe

cols=archivonum.columns.values.tolist()
for num,name in enumerate(cols, start=0):
    print(archivonum.groupby(cols[num])[cols[num]].count().sort_values(ascending=False).head(3))
