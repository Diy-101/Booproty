import requests

url = "https://readdy.ai/api/search-image?query=High-performance%20engine%20components%20and%20parts%20arranged%20elegantly%2C%20pistons%2C%20valves%20and%20camshafts%20with%20metallic%20finish%2C%20professional%20product%20photography%20on%20white%20background%20with%20soft%20shadows%2C%20automotive%20engineering%20excellence&width=400&height=300&seq=4&orientation=landscape"

response = requests.get(url)

if response.status_code == 200:
    with open("downloaded_image.jpg", "wb") as f:
        f.write(response.content)
    print("Изображение успешно скачано и сохранено.")
else:
    print("Ошибка при загрузке изображения:", response.status_code)