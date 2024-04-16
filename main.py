from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from detect_file import detect_file
import io

app = FastAPI()

@app.get("/")
async def detect(input_file_url: str, output_file_url: str):
    result_image_bytes = detect_file(input_file_url, output_file_url)
    return StreamingResponse(io.BytesIO(result_image_bytes), media_type="image/jpeg")