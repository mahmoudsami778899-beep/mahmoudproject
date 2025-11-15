
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

#استدعينا ملف الاكسل من الجهاز 
df = pd.read_csv("car_prediction_dataaa.csv")


print("rows of data:")
print(df.head())# عرض أول 5 صفوف 


df = df.dropna()   # حذف أي صف يحتوي على Missing

X = df[['Year', 'Present_Price', 'Kms_Driven']]
y = df['Selling_Price']


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)



model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)*100


print(f"Mean Squared Error: {mse}")
print(f"R-Square: {r2}")




