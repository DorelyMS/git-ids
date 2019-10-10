

import load_data
import clean_data
import transform_data
import eda

#funciones del módulo load_data.py
datos=load_data.carga_archivo('consumo-agua.csv')
load_data.observaciones_variables(datos)

#función del módulo clean_data.py
clean_data.estandariza_variables(datos)

#funciones del módulo transform_data.py
transform_data.tipo_variables(datos)
transform_data.separar_variable(datos,'geo_point','latitud','longitud',',')
transform_data.eliminar_variable(datos,'geo_point')
transform_data.eliminar_variable(datos,'geo_shape')
transform_data.cambiar_tipo_variable(datos,'latitud','float64')
transform_data.cambiar_tipo_variable(datos,'longitud','float64')
transform_data.cambiar_minusculas_variable(datos,'colonia')
transform_data.cambiar_minusculas_variable(datos,'alcaldia')
transform_data.cambiar_minusculas_variable(datos,'indice_des')
transform_data.quitar_acentos(datos)
datos.head()
transform_data.tipo_variables(datos)


#funciones del módulo eda.py