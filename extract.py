#print("Hello Suraj!")
#print("Jenkins is running my Python program.")

#a = 10
#b = 20

#print("Sum =", a + b)
#print("Welcome to automatic trigger")

import pandas as pd
import requests

response = requests.get("'https://jsonplaceholder.typicode.com/users'")
data=response.json()

df=pd.DataFrame(data)
df=df[["id","name","emial"]]
print("transformed user data:")

print(df)