import requests

for i in range(7276, 7199, -1):
    response = requests.get(
        f'https://cdn.discordapp.xyz/attachments/1098086661847535719/1226012804150984754/IMG_{i}.jpg'
    )
    
    print(response.status_code)

    if response.status_code == 200:
        print("response 200")
        print(f'https://cdn.discordapp.xyz/attachments/1098086661847535719/1226012804150984754/IMG_{i}.jpg')
        break
