import pandas as pd
from sklearn.tree import DecisionTreeRegressor

melbourne_file_path = 'melb_data.csv'

print("--------------------------------------------------------------------------")
home_data = pd.read_csv(melbourne_file_path) 
print("Selecting Data for Modeling")
print(home_data.columns)
print("--------------------------------------------------------------------------")

# elimina los campos nulos 
melbourne_data = home_data.dropna(axis=0)

# crea un data set con la columna de Price
y = melbourne_data.Price
print("Prediction Target")
print(y)
print("--------------------------------------------------------------------------")

# crea un array con las columnas seleccionadas
melbourne_features = ['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude']
# se dclara el aray
X = melbourne_data[melbourne_features]
print("Features")
print("y head")
print(y.head())
print("x head")
print(X.head())
print("--------------------------------------------------------------------------")


# Define model. Specify a number for random_state to ensure same results each run
melbourne_model = DecisionTreeRegressor(random_state=1)

# Fit model
melbourne_model.fit(X, y)