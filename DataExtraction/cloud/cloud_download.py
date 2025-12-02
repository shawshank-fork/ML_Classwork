import requests

url = "https://raw.githubusercontent.com/apache/kafka/main/LICENSE"  # Example file

response = requests.get(url)

with open("cloud_file.txt", "wb") as f:
    f.write(response.content)

print(" File downloaded from cloud and saved as cloud_file.txt")
