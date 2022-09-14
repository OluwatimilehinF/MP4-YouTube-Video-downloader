from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from youtube import youtube_mp4


app = FastAPI(title='YouTube vides to mp4 file',
              description='Converting your YouTube videos to offline mp4 files')

@app.get("/", response_class=PlainTextResponse)
def home():
    return "Welcome! API is working perfectly well. Use /docs to proceed to convert your YouTube videos to offline mp4 files."


@app.post("/youtube to mp4")
async def YouTube_MP4(url_link: str):

    try:
        youtube_mp4(url_link)
        return "Download successful! Check your local device for the downloaded mp4 file"

    except Exception as e:
        return "Invalid link. Please check and try again"


