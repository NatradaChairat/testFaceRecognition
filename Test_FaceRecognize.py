import cognitive_face as CF
import requests
from io import BytesIO
from PIL import Image, ImageDraw

KEY = '5051ca0f16a34de18bf97cb67d33c1f9'
CF.Key.set(KEY)
BASE_URL = 'https://southeastasia.api.cognitive.microsoft.com/face/v1.0/'  # Replace with your regional Base URL
CF.BaseUrl.set(BASE_URL)

# You can use this example JPG or replace the URL below with your own URL to a JPEG image.
image1 = 'https://raw.githubusercontent.com/Microsoft/Cognitive-Face-Windows/master/Data/detection1.jpg'
image2 = ''

img_url = image1
faces = CF.face.detect(img_url)


print(faces)

def getRectangle(faceDictionary):
    rect = faceDictionary['faceRectangle']
    left = rect['left']
    top = rect['top']
    bottom = left+ rect['height']
    right = top+ rect['width']
    return ((left, top), (bottom, right))

response = requests.get(img_url)
img = Image.open(BytesIO(response.content))

draw = ImageDraw.Draw(img)
for face in faces: draw.rectangle(getRectangle(face), outline='red')

img.show()
