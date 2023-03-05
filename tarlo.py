import requests
import json
import io
import base64
from PIL import Image
import dotenv
import os

dotenv_file = dotenv.find_dotenv()
dotenv.load_dotenv(dotenv_file)

KAKAOBRAIN_HOST_URL = os.environ["KAKAOBRAIN_HOST_URL"]
KAKAO_REST_API_KEY = os.environ["KAKAO_REST_API_KEY"]


def t2i(text, batch_size=1):
    r = requests.post(
        f"{KAKAOBRAIN_HOST_URL}/v1/inference/karlo/t2i",
        json={"prompt": {"text": text, "batch_size": batch_size}},
        headers={
            "Authorization": f"KakaoAK {KAKAO_REST_API_KEY}",
            "Content-Type": "application/json",
        },
    )
    response = json.loads(r.content)
    return response


def stringToImage(base64_string, mode="RGBA"):
    imgdata = base64.b64decode(str(base64_string))
    img = Image.open(io.BytesIO(imgdata)).convert(mode)
    return img
