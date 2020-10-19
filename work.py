#!/usr/bin/env python3

#--------------------------------------------------------------------------
#  THIS CODE WAS DEPRECATED
#  the idea with this code was to make some initial investigation
#  now the code is going to be split by algorithms
#--------------------------------------------------------------------------

import pandas as pd
import numpy as np

from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sb
from mpl_toolkits.mplot3d import Axes3D


from lib.normalizer import normalize_string_mapping
from lib.normalizer import normalize_amount


#  Load data
# --------------------------------------------------------------------
separator = ";"
encoding = "ISO8859-1"
pagos = pd.read_csv("./data/PAGOS.csv", sep=separator, encoding=encoding)
cuotas = pd.read_csv("./data/CUOTAS.csv", sep=separator, encoding=encoding)
clientes = pd.read_csv("./data/CLIENTES.csv", sep=separator, encoding=encoding)
creditos = pd.read_csv("./data/CREDITOS.csv", sep=separator, encoding=encoding)


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
    "TIPOLABORAL",
    "SUCURSAL_y",
    "METAL"
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


#  Percentage to use (since the dataset is HUGE), this
#  speed up a little bit the calculation, after we know that's
#  correct, we can go 100%
# --------------------------------------------------------------------
take_this_percentage=5
fraction_of_set=take_this_percentage / 100.0

# Do some kmeans
X = selected_columns.sample(frac=fraction_of_set)
kmeans = KMeans(n_clusters=5).fit(X)
C = kmeans.cluster_centers_


sb.pairplot(
    selected_columns.sample(frac=fraction_of_set),
    hue="METAL",
    size=4,
    vars=["MONTO", "SUCURSAL_y", "TIPOLABORAL"],
    kind="scatter",
    palette="afmhot"
)

# plt.show()    # you can use this here to look at the data


##--------------------------------------------------------------------
## THE FOLLOWING LINES CAN BE IGNORED
##
## I just wrote them down for learning purposes
##--------------------------------------------------------------------
X = np.array(selected_columns.sample(frac=fraction_of_set)[["MONTO", "SUCURSAL_y", "TIPOLABORAL"]])
y = np.array(selected_columns.sample(frac=fraction_of_set)['METAL'])

labels = kmeans.predict(X)
C = kmeans.cluster_centers_


selected_columns.describe()
