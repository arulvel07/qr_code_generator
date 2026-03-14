# QR Code Generator API

A simple backend API built using **FastAPI** that generates a QR code from a given URL.

The API accepts a URL as a query parameter and returns a **PNG image** containing the QR code for that URL.

---

## Features

- Generate QR codes from URLs
- FastAPI backend
- Returns QR code as PNG image
- Simple and lightweight API

---

## Technologies Used

- Python
- FastAPI
- Uvicorn
- qrcode library


---

## Running the Server

Start the FastAPI server with: `uvicorn main:app`

The server will start at: <http://127.0.0.1:8000>

---

## API Endpoints

### Home Endpoint

Returns a welcome message.

`{
"message": "Welcome to QR code generator API. Use /qr?url=your_url to generate QR code."
}`

### QR Code Endpoint

Generates a QR code for a given URL and returns it as a **PNG image**.

**Endpoint**

`GET /qr`

**Query Parameter**

| Parameter | Type | Description |
|-----------|------|-------------|
| url | string | The URL that will be encoded into the QR code |

**Example Request**
<http://127.0.0.1:8000/qr?url=https://google.com>

**Response**

- Content-Type: `image/png`
- Returns a PNG image containing the generated QR code.

When you open the above link in a browser, the server generates a QR code encoding `https://google.com` and streams the image directly to the browser.
