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
    everything = clientes.merge(creditos, left_on="ID_CLIENTE", right_on="ID_CLIENTE")
    everything = everything.merge(pagos, left_on="ID_CREDITO", right_on="ID_CREDITO")
    everything = everything.merge(cuotas, left_on="ID_CREDITO", right_on="ID_CREDITO")
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




# desired_columns = [
#     "MONTO",
#     "TIPOLABORAL",
#     "SUCURSAL_y",
#     "METAL"
# ]
# selected_columns = everything[desired_columns]


# normalize_amount(selected_columns, "MONTO", 2500)
# normalize_string_mapping(selected_columns, "METAL", metales)
# normalize_string_mapping(selected_columns, "TIPOLABORAL", tipo_laboral)

# # Remove trailing spaces for "SUCURSAL_y" (some have trailing spaces)
# selected_columns["SUCURSAL_y"] = selected_columns["SUCURSAL_y"].str.strip()
# normalize_string_mapping(selected_columns, "SUCURSAL_y", sucursal_y)


# #  Percentage to use (since the dataset is HUGE), this
# #  speed up a little bit the calculation, after we know that's
# #  correct, we can go 100%
# # --------------------------------------------------------------------
# take_this_percentage=5
# fraction_of_set=take_this_percentage / 100.0

# # Do some kmeans
# X = selected_columns.sample(frac=fraction_of_set)
# kmeans = KMeans(n_clusters=5).fit(X)
# C = kmeans.cluster_centers_


# sb.pairplot(
#     selected_columns.sample(frac=fraction_of_set),
#     hue="METAL",
#     size=4,
#     vars=["MONTO", "SUCURSAL_y", "TIPOLABORAL"],
#     kind="scatter",
#     palette="afmhot"
# )

# # plt.show()    # you can use this here to look at the data


# ##--------------------------------------------------------------------
# ## THE FOLLOWING LINES CAN BE IGNORED
# ##
# ## I just wrote them down for learning purposes
# ##--------------------------------------------------------------------
# X = np.array(selected_columns.sample(frac=fraction_of_set)[["MONTO", "SUCURSAL_y", "TIPOLABORAL"]])
# y = np.array(selected_columns.sample(frac=fraction_of_set)['METAL'])

# labels = kmeans.predict(X)
# C = kmeans.cluster_centers_


# selected_columns.describe()
