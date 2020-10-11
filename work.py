#!/usr/bin/env python3
import pandas as pd
import numpy as np

from sklearn.cluster import KMeans

from lib.normalizer import normalize_string_mapping
from lib.normalizer import normalize_amount


#  Load data
# --------------------------------------------------------------------
separator = ";"
encoding = "ISO8859-1"
pagos = pd.read_csv("/Users/felix/Dropbox/universidad/2020/2do_cuatrimestre/machine_learning/UP_ML_cartasur/data/PAGOS.csv", sep=separator, encoding=encoding)
cuotas = pd.read_csv("/Users/felix/Dropbox/universidad/2020/2do_cuatrimestre/machine_learning/UP_ML_cartasur/data/CUOTAS.csv", sep=separator, encoding=encoding)
clientes = pd.read_csv("/Users/felix/Dropbox/universidad/2020/2do_cuatrimestre/machine_learning/UP_ML_cartasur/data/CLIENTES.csv", sep=separator, encoding=encoding)
creditos = pd.read_csv("/Users/felix/Dropbox/universidad/2020/2do_cuatrimestre/machine_learning/UP_ML_cartasur/data/CREDITOS.csv", sep=separator, encoding=encoding)


#  Merge some data
# --------------------------------------------------------------------
everything = clientes.merge(creditos, left_on="ID_CLIENTE", right_on="ID_CLIENTE")
everything = everything.merge(pagos, left_on="ID_CREDITO", right_on="ID_CREDITO")
everything = everything.merge(cuotas, left_on="ID_CREDITO", right_on="ID_CREDITO")


# 1st. Remove columns with NaN
#      (My guess is that there should be a simpler way to do this)
# --------------------------------------------------------------------
drop_columns = [
    "TDOC_x",
    "NROC",
    "FECHA_ALTA_LABORAL",
    "SUCURSAL_x",
    "TDOC_y",
    "NDOC",
    "Unnamed: 5"
]
everything = everything.drop(labels=drop_columns, axis=1)



desired_columns = [
    "MONTO",
    "METAL",
    "TIPOLABORAL",
    "SUCURSAL_y"
]
selected_columns = everything[desired_columns]

metales = {
    'ALUMINIO'  :   1, 'BRONCE'    :   2, 'BRONCE_B'  :   3, 'NUEVO'     :   4,
    'NUEVO_B'   :   5, 'ORO'       :   6, 'ORO_B'     :   7, 'PLATA'     :   8,
    'PLATA_B'   :   9, 'PLATINO'   :  10, 'PLATINO_B' :  11, 'POSREFI'   :  12,
    'POSREFIB'  :  13
}

tipo_laboral = {
    'Cooperativista'      : 1, 'Empleada Domestica'  : 2,
    'JUBILADO'            : 3, 'MONOTRIBUTISTA'      : 4,
    'NODEFINIDA'          : 5, 'PUBLICA'             : 6,
    'Pension Graciable'   : 7, 'Plan Social'         : 8,
    'Privada'             : 9, 'SIN RECIBO'          : 10
}

sucursal_y = {
    'Alejandro Korn'   : 1, 'Avellaneda'       : 2, 'Brandsen'         : 3,
    'Burzaco'          : 4, 'CallCenter'       : 5, 'Casa Central'     : 6,
    'Caseros'          : 7, 'Cañuelas'         : 8, 'Chascomús'        : 9,
    'Ezeiza'           : 10, 'Florencio Varela' : 11, 'Flores'           : 12,
    'Glew'             : 13, 'La Plata'         : 14, 'Laferrere'        : 15,
    'Lanús'            : 16, 'Liniers'          : 17, 'Lomas'            : 18,
    'Los Polvorines'   : 19, 'Monte Grande'     : 20, 'Moreno'           : 21,
    'Morón'            : 22, 'Once'             : 23, 'Pompeya'          : 24,
    'Merlo'            : 25, 'Quilmes'          : 26, 'Rafael Castillo'  : 27,
    'San José'         : 28, 'San Justo'        : 29, 'San Miguel'       : 30,
    'Solano'           : 31, 'Sucursal Web'     : 32
}

normalize_amount(selected_columns, "MONTO", 2500)
normalize_string_mapping(selected_columns, "METAL", metales)
normalize_string_mapping(selected_columns, "TIPOLABORAL", tipo_laboral)

# Remove trailing spaces for "SUCURSAL_y" (some have trailing spaces)
selected_columns["SUCURSAL_y"] = selected_columns["SUCURSAL_y"].str.strip()
normalize_string_mapping(selected_columns, "SUCURSAL_y", sucursal_y)


selected_columns.describe()
