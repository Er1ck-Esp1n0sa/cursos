import pandas as pd

rewiews = pd.read_csv("../winemag-data-130k-v2.csv", index_col=0)
pd.set_option('display.max_rows', 5)
print(rewiews)
print("---------------------------------------------------------------------------------------------------------------")

print('\n select contry form winesmag/n')
print(rewiews.country)
print("---------------------------------------------------------------------------------------------------------------")

print('\n sub-dataset \n select country form winesmag/n')
rewiews_country = rewiews['country']
print(rewiews.country)
print("---------------------------------------------------------------------------------------------------------------")

print('\n select top 1 country form winesmag/n')
rewiews_country_top_1 = rewiews['country'][1]
print(rewiews_country_top_1)