import importlib
import json
import logging
import os
import time
from typing import Optional

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

import kociemba

app = FastAPI()
# CORS支持
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler())


@app.post("/v1/cube/solve/{content}")
async def query(content: str, params: Optional[dict] = {}):
    try:
        result = kociemba.solve(content)
        return {
            "code": 1,
            "message": "查询成功",
            "timestamp": int(round(time.time() * 1000)),
            "result": result
        }
    except:
        log.exception("查询异常")
        return {
            "code": 9,
            "message": "查询失败",
            "timestamp": int(round(time.time() * 1000))
        }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8080)
