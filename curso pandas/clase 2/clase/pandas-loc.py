import pandas as pd

rewiews = pd.read_csv("../winemag-data-130k-v2.csv", index_col=0)

print('\n dataset ')
rewiews_iloc_n = rewiews.iloc[0]
print(rewiews_iloc_n)
print("---------------------------------------------------------------------------------------------------------------")

rewiews_country = rewiews.iloc[:,0]
print(rewiews_country)

print("---------------------------------------------------------------------------------------------------------------")
print('\n sub-dataset \n select top 3 country form winesmag')
rewiews_country_top3 = rewiews.iloc[:3,0]
print(rewiews_country_top3)

print("---------------------------------------------------------------------------------------------------------------")
print('\n sub-dataset row 2, 3 \n select country form winesmag')
rewiews_country_r2_r3 = rewiews.iloc[1:3,0]
print(rewiews_country_r2_r3)

print("---------------------------------------------------------------------------------------------------------------")
print('\n sub-dataset row 1, 2, 3 \n select country form winesmag')
rewiews_country_r1_r2_r3 = rewiews.iloc[ [0,1,2], 0]
print(rewiews_country_r1_r2_r3)

print("---------------------------------------------------------------------------------------------------------------")
print('\n sub-dataset row 1, 2, 3 \n select country, descripcion form winesmag')
rewiews_country_r1_r2_r3 = rewiews.iloc[ [0,1,2], [0,1] ]
print(rewiews_country_r1_r2_r3)