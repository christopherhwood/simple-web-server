# Run with: uvicorn main:app --reload
import os
from typing import List

from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

app = FastAPI()

@app.get("/api/name")
async def get_name():
    return {"name": "John Doe"}

#############################################################################
## KEEP THESE AT THE BOTTOM OF THE FILE. PUT EVERYTHING ELSE ABOVE HERE!!! ##
#############################################################################

# Ensure the 'assets' directory exists
assets_dir = "assets"
if not os.path.exists(assets_dir):
    os.makedirs(assets_dir)
    print(f"Created directory: {assets_dir}")
else:
    print(f"Directory already exists: {assets_dir}")

app.mount("/api/assets", StaticFiles(directory=assets_dir), name="assets")

@app.get("/{full_path:path}")
async def serve_spa(full_path: str):
    file_path = f"../frontend/dist/{full_path}"
    if os.path.isfile(file_path):
        return FileResponse(file_path)
    return FileResponse("../frontend/dist/index.html")

app.mount("/", StaticFiles(directory="../frontend/dist", html=True), name="react")
