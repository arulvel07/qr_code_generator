from fastapi import FastAPI
from fastapi.responses import StreamingResponse
import qrcode
import io

app=FastAPI()
@app.get("/")
def home():
    return {"message":"Welcome to QR code generator API. Use /qr?url=your_url to generate QR code."}

@app.get("/qr")
def generate_qr(url: str):
    qr = qrcode.QRCode()
    qr.add_data(url)
    img = qr.make_image()

    buffer = io.BytesIO() #create a bytes buffer to hold the image data
    img.save(buffer, format="PNG") #save the image to the buffer in PNG format
    buffer.seek(0)

    return StreamingResponse(buffer, media_type="image/png")