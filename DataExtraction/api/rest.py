import requests
import pandas as pd

url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url)

if response.status_code == 200:
    print("Successful\n")

#coverst json response into pandas dataframe
    data = pd.DataFrame(response.json())
    print("fetched data from API:\n")
    print(data.head())

    extracted_data = data[['name', 'email']]

    print("extracted data: ")
    print(extracted_data)

else:
    print("api request failed", response.status_code) 

data.to_csv("api_users.csv", index=False)
print("\n✔ Data saved to api_users.csv")
