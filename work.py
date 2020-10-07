#!/usr/bin/env python3

import pandas as pd

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


