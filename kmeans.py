import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import pairwise_distances_argmin_min
from lib.cartasur.data_loader import load_merge_all_datasets

everything = load_merge_all_datasets("./data/")

desired_columns = ["MONTO", "TIPOLABORAL", "SUCURSAL_y", "METAL"]
selected_columns = everything[desired_columns]

data_subset = selected_columns.sample(frac=0.05)
kmeans = KMeans(n_clusters=5).fit(data_subset)

print("[i] Cluster Centers")
print(kmeans.cluster_centers_)

print("[i] Distributions")
ps = pd.Series(kmeans.labels_)
print(ps.value_counts())
