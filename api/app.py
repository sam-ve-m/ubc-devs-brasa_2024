import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from decouple import config

from api.routes import users, auth, intranet
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users.router, tags=["Users"])
app.include_router(auth.router, tags=["Auth"])
app.include_router(intranet.router, tags=["Intranet Triggers"])


if __name__ == "__main__":
    uvicorn.run(
        app,
        port=int(config("API_PORT", 8000))
    )
