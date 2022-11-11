from fastapi import APIRouter, UploadFile, BackgroundTasks, HTTPException
from fastapi.responses import FileResponse
import tempfile
import shutil
import os
import cv2
import numpy as np
import mimetypes
from pathlib import Path

picture_invert_router = APIRouter()


def remove_file(path: str):
    os.unlink(path)


@picture_invert_router.post("/picture/invert")
async def picture_invert(background_tasks: BackgroundTasks, file: UploadFile):
    if file.content_type != "image/jpeg":
        raise HTTPException(status_code=406, detail="Not valid mime type")

    Path("tmp").mkdir(parents=True, exist_ok=True)
    tempFileName = "tmp/" + next(tempfile._get_candidate_names()) + ".jpeg"

    with open(tempFileName, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

        image = cv2.imread(tempFileName)
        image = np.invert(image)
        cv2.imwrite(tempFileName, image)

        background_tasks.add_task(remove_file, tempFileName)

    return FileResponse(tempFileName, media_type=mimetypes.guess_type(tempFileName)[0])
