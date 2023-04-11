import requests
import json
import base64
import datetime

# 獲取當前日期和時間
now = datetime.datetime.now()

# 將日期和時間格式化為字符串，並用作新檔案名稱
timestamp = now.strftime("%Y-%m-%d-%H-%M-%S")
file_name = timestamp + ".jpg"

# 設置您的github使用者名稱、儲存庫名稱和分支名稱
USERNAME = "mowuqq"
REPO_NAME = "mytest"
BRANCH_NAME = "main"

# 設置您的access token，用於對GitHub API進行身份驗證
ACCESS_TOKEN = "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"

# 設置您要上傳的圖片的路徑和檔名
x = input("存入的檔案名稱:")
IMAGE_PATH = "D:/SA_TW2/html/pic/" + str(x)
FILE_NAME = file_name

# 設置API的URL和headers
FOLDER_PATH = "test"  # 更改為您的資料夾路徑
url = f"https://api.github.com/repos/{USERNAME}/{REPO_NAME}/contents/{FOLDER_PATH}/{FILE_NAME}"
headers = {
    "Authorization": f"token {ACCESS_TOKEN}",
    "Accept": "application/vnd.github.v3+json",
}

# 讀取圖片並將其轉換為base64格式
with open(IMAGE_PATH, "rb") as image_file:
    encoded_image = base64.b64encode(image_file.read()).decode("utf-8")

# 使用GitHub API上傳圖片
data = {
    "message": "Add image",
    "content": encoded_image,
    "branch": BRANCH_NAME
}
response = requests.put(url, headers=headers, data=json.dumps(data))

# 檢查上傳結果
if response.status_code == 201:
    print("Image uploaded successfully!")
else:
    print("Error uploading image.")
