import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics

from lib.cartasur.data_loader import load_merge_all_datasets

iris = load_merge_all_datasets("./data/")

desired_columns = [
    "MONTO",
    "INGRESO_NETO",
    "TIPOLABORAL",
    "CLASE_PLAN",
    "RECIBO",
    "SEXO",
    "SUCURSAL_y",
    "METAL"
]
selected_columns = iris[desired_columns]

# sexo -> add
# recibo -> add
# clase_plan -> add
# provincia_per -> add

data_subset = selected_columns.sample(frac=0.10)

data = pd.DataFrame(
    {
        'monto': data_subset["MONTO"],
        'ingreso_neto': data_subset["INGRESO_NETO"],
        'tipo_laboral': data_subset["TIPOLABORAL"],
        'sexo': data_subset["SEXO"],
        'recibo': data_subset["RECIBO"],
        'clase_plan': data_subset["CLASE_PLAN"],
        'sucursal': data_subset["SUCURSAL_y"],
        'metal': data_subset["METAL"]
    }
)

X = data[
    [
        'monto',
        'ingreso_neto',
        'tipo_laboral',
        'clase_plan',
        'sexo',
        'recibo',
        'sucursal'
    ]
]
y = data['metal']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

clf = RandomForestClassifier(n_estimators=100)

clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)
print("Accuracy:", metrics.accuracy_score(y_test, y_pred))
