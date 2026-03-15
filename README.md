# QR Code Generator

A simple web application that generates QR codes from user input using **FastAPI** and a basic **HTML frontend**.

Users can enter a URL or text in the webpage. The HTML form sends the input to the FastAPI backend, which generates and returns a QR code image.

---

## Features

* Generate QR codes from URLs or text
* Simple HTML user interface
* FastAPI backend
* QR code returned as PNG image
* Lightweight and easy to run

---

## Technologies Used

* Python
* FastAPI
* Uvicorn
* qrcode library
* HTML

---

## Project Structure

```
project/
│
├── main.py        # FastAPI backend
├── index.html     # Frontend HTML page
└── README.md
```

---

## Running the Application

Start the FastAPI server:

```
uvicorn main:app
```

The server will run at:

```
http://127.0.0.1:8000
```

Open the `index.html` file in your browser.

---

## Frontend (HTML Form)

The HTML page contains a simple form where the user enters a URL or text.
The form sends a **GET request** to the FastAPI backend.

Example HTML form:

```html
<form action="http://127.0.0.1:8000/qr" method="get">
    <input type="text" name="url" placeholder="Enter URL or text here">
    <button type="submit">Generate QR Code</button>
</form>
```

When the form is submitted, the browser sends a request like:

```
http://127.0.0.1:8000/qr?url=https://google.com
```

---

## API Endpoint

### Generate QR Code

**Endpoint**

```
GET /qr
```

**Query Parameter**

| Parameter | Type   | Description                          |
| --------- | ------ | ------------------------------------ |
| url       | string | URL or text to encode in the QR code |

**Example Request**

```
http://127.0.0.1:8000/qr?url=https://google.com
```

**Response**

* Content-Type: `image/png`
* Returns a PNG image containing the generated QR code.

The browser directly displays the QR code image returned by the server.

---

## How It Works

1. User enters a URL or text in the HTML input field.
2. The HTML form sends a **GET request** to the FastAPI endpoint.
3. FastAPI receives the query parameter `url`.
4. The server generates a QR code using the **qrcode library**.
5. The QR code image is returned as a **PNG stream**.
6. The browser displays the generated QR code.
