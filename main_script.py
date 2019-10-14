#!/usr/bin/env python
# coding: utf-8

# In[2]:


import load_data
import clean_data
import transform_data
import eda


# In[3]:


datos=load_data.carga_archivo('consumo-agua.csv')


# In[4]:


load_data.observaciones_variables(datos)


# In[5]:


clean_data.estandariza_variables(datos)


# In[6]:


transform_data.tipo_variables(datos)


# In[7]:


transform_data.separar_variable(datos,'geo_point','latitud','longitud',',')
transform_data.eliminar_variable(datos,'geo_point')
transform_data.eliminar_variable(datos,'geo_shape')
transform_data.cambiar_tipo_variable(datos,'latitud','float64')
transform_data.cambiar_tipo_variable(datos,'longitud','float64')
transform_data.cambiar_tipo_variable(datos,'bimestre','str')
transform_data.cambiar_tipo_variable(datos,'gid','str')
transform_data.cambiar_minusculas_variable(datos,'colonia')
transform_data.cambiar_minusculas_variable(datos,'alcaldia')
transform_data.cambiar_minusculas_variable(datos,'indice_des')
transform_data.quitar_acentos(datos)


# In[8]:


datos.head()


# In[9]:


transform_data.tipo_variables(datos)


# In[10]:


eda.tabla_estadisticos_descriptivos_variables_numericas(datos)


# In[11]:


eda.tabla_estadisticos_descriptivos_variables_categoricas(datos)


# In[12]:


eda.grafico_barplot_orden_decreciente(datos,'alcaldia','consumo_total','Alcaldía','consumo de agua total','Consumo de agua promedio por manzana en cada alcaldía')
    

# In[13]:


eda.tabla_ranking_n(datos,15,"colonia","alcaldia",'consumo_total')


# In[14]:


eda.grafico_barplot_orden_en_barras(datos,'indice_des','consumo_total',['popular','bajo','medio','alto'],'Índice de desarrollo','Consumo de agua total','Consumo de agua promedio por índice de desarrollo')


# In[15]:


eda.grafico_tipo_uso(datos,'total','consumos totales','tipos de uso','Consumos por tipo de uso del inmueble')


# In[16]:


eda.grafico_tipo_uso(datos,'prom','consumos promedio','tipos de uso','Consumos por tipo de uso del inmueble')


# In[17]:


eda.grafico_strip(datos,'bimestre','consumo_total','Bimestre de 2019','Consumo de agua total','Consumo de agua promedio por bimestre')


# In[18]:


eda.matriz_correlacion(datos)