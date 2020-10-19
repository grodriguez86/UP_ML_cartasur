#---------------------------------------------------------------------
#
#  LIBRARY
#    cartasur.data_loader
#
#  DESCRIPTION
#    This code is in charge of loading and normalizing the information
#    from the CartaSur datasets provided
#
#---------------------------------------------------------------------
import time
import pandas as pd
from lib.cartasur.constants import *
from lib.cartasur.normalizer import normalize_amount
from lib.cartasur.normalizer import normalize_string_mapping

#  This function serves as a dataset loader
# --------------------------------------------------------------------
def load_dataset(filename):
    print("[i] Loading file {}".format(filename))
    separator = ";"
    encoding = "ISO8859-1"
    return pd.read_csv(filename, sep=separator, encoding=encoding)


#  This function loads
# --------------------------------------------------------------------
def load_merge_all_datasets(dataset_directory, drop_columns=None):
    print("[i] Loading Datasets")
    start = time.time()
    pagos = load_dataset("{}/PAGOS.csv".format(dataset_directory))
    cuotas = load_dataset("{}/CUOTAS.csv".format(dataset_directory))
    clientes = load_dataset("{}/CLIENTES.csv".format(dataset_directory))
    creditos = load_dataset("{}/CREDITOS.csv".format(dataset_directory))
    end = time.time()
    print("Finished in {} secs".format(round(end-start,2)))


    print("[i] Merging Datasets")
    start = time.time()
    temp1 = clientes.merge(creditos, left_on="ID_CLIENTE", right_on="ID_CLIENTE")
    temp2 = temp1.merge(pagos, left_on="ID_CREDITO", right_on="ID_CREDITO")
    everything = temp2.merge(cuotas, left_on="ID_CREDITO", right_on="ID_CREDITO")
    end = time.time()
    print("Finished in {} secs".format(round(end-start, 2)))


    print("[i] Dropping unnecessary columns")
    start = time.time()
    if drop_columns is None:
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
    end = time.time()
    print("Finished in {} secs".format(round(end-start, 2)))


    print("[i] Normalizing MONTO")
    start = time.time()
    normalize_amount(everything, "MONTO", 2500)
    end = time.time()
    print("Finished in {} secs".format(round(end-start, 2)))


    print("[i] Normalizing INGRESO_NETO")
    start = time.time()
    normalize_amount(everything, "INGRESO_NETO", 1000)
    end = time.time()
    print("Finished in {} secs".format(round(end-start, 2)))


    print("[i] Normalizing CLASE_PLAN")
    start = time.time()
    normalize_string_mapping(everything, "CLASE_PLAN", CLASE_PLAN)
    end = time.time()
    print("Finished in {} secs".format(round(end-start, 2)))


    print("[i] Normalizing SEXO")
    start = time.time()
    normalize_string_mapping(everything, "SEXO", SEXO)
    end = time.time()
    print("Finished in {} secs".format(round(end-start, 2)))


    print("[i] Normalizing RECIBO")
    start = time.time()
    normalize_string_mapping(everything, "RECIBO", {'NO':False, 'SI':True})
    end = time.time()
    print("Finished in {} secs".format(round(end-start, 2)))


    print("[i] Normalizing METAL")
    start = time.time()
    normalize_string_mapping(everything, "METAL", METALES)
    end = time.time()
    print("Finished in {} secs".format(round(end-start, 2)))


    print("[i] Normalizing TIPOLABORAL")
    start = time.time()
    normalize_string_mapping(everything, "TIPOLABORAL", TIPO_LABORAL)
    end = time.time()
    print("Finished in {} secs".format(round(end-start, 2)))


    print("[i] Normalizing SUCURSAL_y")
    start = time.time()
    everything["SUCURSAL_y"] = everything["SUCURSAL_y"].str.strip()
    normalize_string_mapping(everything, "SUCURSAL_y", SUCURSAL_Y)
    end = time.time()
    print("Finished in {} secs".format(round(end-start, 2)))

    return everything



