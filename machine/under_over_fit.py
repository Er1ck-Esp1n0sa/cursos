#----------------------------------under_over_fit.py ( part 1 )----------------------------------

from sklearn.metrics import mean_absolute_error
from sklearn.tree import DecisionTreeRegressor

def get_mae(max_leaf_nodes, train_X, val_X, train_y, val_y):
    model = DecisionTreeRegressor(max_leaf_nodes=max_leaf_nodes, random_state=0)
    model.fit(train_X, train_y)
    preds_val = model.predict(val_X)
    mae = mean_absolute_error(val_y, preds_val)
    return(mae)

#----------------------------------under_over_fit.py ( part 2 )----------------------------------

# Data Loading Code Runs At This Point
import pandas as pd
    # Load data
melbourne_file_path = 'melb_data.csv'
melbourne_data = pd.read_csv(melbourne_file_path) 
# Filter rows with missing values
filtered_melbourne_data = melbourne_data.dropna(axis=0)
# Choose target and features
y = filtered_melbourne_data.Price
melbourne_features = ['Rooms', 'Bathroom', 'Landsize', 'BuildingArea', 
                        'YearBuilt', 'Lattitude', 'Longtitude']
X = filtered_melbourne_data[melbourne_features]

from sklearn.model_selection import train_test_split
# split data into training and validation data, for both features and target
train_X, val_X, train_y, val_y = train_test_split(X, y,random_state = 0)

#----------------------------------under_over_fit.py ( part 3 )----------------------------------

# compare MAE with differing values of max_leaf_nodes
#for max_leaf_nodes in [5, 50, 500, 5000]:
#for max_leaf_nodes in [450, 460, 470, 480, 490, 500, 510, 520]:
for max_leaf_nodes in [450, 452, 454, 456, 458, 460, 462, 464]:
    my_mae = get_mae(max_leaf_nodes, train_X, val_X, train_y, val_y)
    print("Max leaf nodes: %d  \t\t Mean Absolute Error:  %d" %(max_leaf_nodes, my_mae))