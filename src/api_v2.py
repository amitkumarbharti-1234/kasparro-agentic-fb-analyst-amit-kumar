import os
import shutil
from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse

from config import CONFIG
from pipeline_v2 import run_pipeline_v2

app = FastAPI(title="Kasparro FB Analyst V2 API")


@app.post("/run")
async def run_analysis(file: UploadFile = File(...)):
    try:
        # Ensure data directory exists
        os.makedirs("data", exist_ok=True)

        # Save uploaded file as input
        saved_path = os.path.join("data", "uploaded_dataset.csv")
        with open(saved_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        # Point config to the uploaded file
        CONFIG["input_path"] = saved_path

        # Run pipeline
        result = run_pipeline_v2()

        if result["status"] != "success":
            return JSONResponse(
                status_code=500,
                content={"status": "failed", "error": result.get("error", "unknown")}
            )

        return {
            "status": "success",
            "run_id": result["run_id"],
            "hypotheses_path": result["hypotheses_path"],
            "creatives_path": result["creatives_path"]
        }

    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"status": "failed", "error": str(e)}
        )
