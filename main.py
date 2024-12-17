from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.message.endpoints import app as message_router
import uvicorn

app = FastAPI()
app.router.redirect_slashes = False
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# 메시지 라우터 추가
app.include_router(message_router)


@app.get("/")
def read_root():
    return {"message": "Welcome to the Message API"}


if __name__ == "__main__":
    uvicorn.run(
        app="main:app",
        host="0.0.0.0",
        port=80,
        reload=True,
        workers=1,
        timeout_keep_alive=600,
    )
