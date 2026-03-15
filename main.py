from fastapi import FastAPI
from fastapi.responses import StreamingResponse, FileResponse
import qrcode
import io

app = FastAPI()

@app.get("/")
def home():
    return FileResponse("index.html", media_type="text/html")

@app.get("/qr")
def generate_qr(url: str):
    qr = qrcode.QRCode()
    qr.add_data(url)
    img = qr.make_image()

    buffer = io.BytesIO()  # create a bytes buffer to hold the image data
    img.save(buffer, format="PNG")  # save the image to the buffer in PNG format
    buffer.seek(0)

    return StreamingResponse(buffer, media_type="image/png")