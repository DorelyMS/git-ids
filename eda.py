
#EDA

#Esta función genera el cuadro de estadísticas descriptivas

#import statistics as stats
import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


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
    def missings(archivo):
        nulos=archivo.isnull().sum()
        return nulos
    def prop_missings(archivo):
        prop=(archivo.isnull().sum()/len(archivo.index))*100
        return prop
    archivonum=selecciona_variables_numericas(archivo).agg(['max','min','mean','std',q25,'median',q75,'skew','kurt','count',uniques,missings,prop_missings])
    return archivonum

def tabla_estadisticos_descriptivos_variables_categoricas(archivo):
    def selecciona_variables_categoricas(archivo):
        lista_variables_categoricas=archivo.select_dtypes(include = 'object').columns.values
        archivo_variables_categoricas = archivo.loc[:, lista_variables_categoricas]
        return archivo_variables_categoricas
    def uniques(archivo):
        uni=archivo.nunique()
        return uni
    def uniques_list(archivo):
        uni=archivo.unique()
        return uni
    def missings(archivo):
        nulos=archivo.isnull().sum()
        return nulos
    def prop_missings(archivo):
        prop=(archivo.isnull().sum()/len(archivo.index))*100
        return prop
    archivocat=selecciona_variables_categoricas(archivo).agg(['count',uniques,uniques_list,missings,prop_missings])
    return archivocat


def grafico_barplot_orden_decreciente(archivo,variable_ejex,variable_ejey,etiqueta_ejex,etiqueta_ejey,titulo):
    result = archivo.groupby([variable_ejex])[variable_ejey].mean().reset_index().sort_values(variable_ejey,ascending=False)
    graf=sns.barplot(x=variable_ejex, y=variable_ejey, data=archivo, order=result[variable_ejex])
    graf.set_xticklabels(graf.get_xticklabels(), rotation=40, ha="right")
    graf.set(xlabel=etiqueta_ejex, ylabel=etiqueta_ejey, title=titulo)

def grafico_barplot_orden_en_barras(archivo,variable_ejex,variable_ejey,lista_orden_barras,etiqueta_ejex,etiqueta_ejey,titulo):
    graf=sns.catplot(x=variable_ejex, y=variable_ejey,order=lista_orden_barras,
                kind="bar",data=archivo)
    graf.set(xlabel=etiqueta_ejex, ylabel=etiqueta_ejey, title=titulo)
    
def grafico_strip(archivo,variable_ejex,variable_ejey,etiqueta_ejex,etiqueta_ejey,titulo):
    graf=sns.catplot(x=variable_ejex, y=variable_ejey,kind="strip", dodge=False, data=archivo, palette="pastel")
    graf.set(xlabel=etiqueta_ejex, ylabel=etiqueta_ejey, title=titulo)
        
def grafico_tipo_uso(archivo,tipo_consumo,etiqueta_ejex,etiqueta_ejey,titulo):
    if tipo_consumo=="total":
        consumos=archivo.melt(id_vars=['nomgeo','alcaldia','colonia','bimestre','indice_des','gid'],value_vars=['consumo_total_dom','consumo_total_mixto','consumo_total_no_dom'],var_name='tipo_consumo', value_name='consumo')
    elif tipo_consumo=="prom":
        consumos=archivo.melt(id_vars=['nomgeo','alcaldia','colonia','bimestre','indice_des','gid'],value_vars=['consumo_prom_dom','consumo_prom_mixto','consumo_prom_no_dom'],var_name='tipo_consumo', value_name='consumo')
    else:
         print("Sólo puedes escoger tipo_consumo=prom/total, por favor vuelve a intentarlo")
    graf = sns.boxplot(x="consumo", y="tipo_consumo", data=consumos, whis=np.inf)
    graf = sns.stripplot(x="consumo", y="tipo_consumo", data=consumos,jitter=True, linewidth=1)
    graf.set(xlabel=etiqueta_ejex, ylabel=etiqueta_ejey, title=titulo)
        