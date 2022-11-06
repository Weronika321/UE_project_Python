from fastapi.responses import FileResponse, HTMLResponse, StreamingResponse

def html_content(text):
    html = f"""
    <html>
        <body>
            <h1>{text}</h1>
        </body>
    </html>
    """
    return HTMLResponse(content=html, status_code=200)