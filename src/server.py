from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from server_deps import startup, shutdown
from routers import train, config


app = FastAPI()
app.include_router(train.router)
app.include_router(config.router)

origins = [
    "http://localhost:*",
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return "Maerklin MyWorld universal remote API"


@app.on_event("startup")
async def startup_event():
    """Grab the uvicorn event loop to add the main_loop function as a task.
    Load previous settings if available"""
    await startup(app)


@app.on_event("shutdown")
async def shutdown_event():
    """Clean the serial port and save the status settings"""
    await shutdown(app)
