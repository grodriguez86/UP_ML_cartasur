#!/usr/bin/env python3
import pandas as pd
from lib.normalizer import normalize_string
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
    'ALUMINIO'  :   1,
    'BRONCE'    :   2,
    'BRONCE_B'  :   3,
    'NUEVO'     :   4,
    'NUEVO_B'   :   5,
    'ORO'       :   6,
    'ORO_B'     :   7,
    'PLATA'     :   8,
    'PLATA_B'   :   9,
    'PLATINO'   :  10,
    'PLATINO_B' :  11,
    'POSREFI'   :  12,
    'POSREFIB'  :  13
}

normalize_amount(selected_columns, "MONTO", 2500)

selected_columns.describe()
