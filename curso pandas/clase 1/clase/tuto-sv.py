import pandas as pd

wine_reviews = pd.read_csv("../winemag-data-130k-v2.csv")

print("--------------------------------------------------------")
print(wine_reviews)
print("--------------------------------------------------------")
print(wine_reviews.shape)
print("--------------------------------------------------------")
print(wine_reviews.shape[0])
print("--------------------------------------------------------")
print(wine_reviews.shape[1])
print('\n------------------------head------------------------\n')
print(wine_reviews.head())