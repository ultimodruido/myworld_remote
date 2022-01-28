from fastapi import FastAPI
from server_deps import startup, shutdown
from routers import train, config


"""
API
# INFO
/remote_status

# CONFIGURATION
/register/remote/{portname}
/register/train/{name}/{frequency}/
/remove/train/{train_id}

# TRAIN
/train_list
/train/{train_id}/speed/{speed_value}
/train/{train_id}/light
/train/{train_id}/sound/{sound_value}
/train/{train_id}/horn
"""

app = FastAPI()
app.include_router(train.router)
app.include_router(config.router)


@app.get("/")
async def root():
    return {"message": "Maerklin MyWorld universal remote API"}


@app.on_event("startup")
async def startup_event():
    """Grab the uvicorn event loop to add the main_loop function as a task.
    Load previous settings if available"""
    await startup()


@app.on_event("shutdown")
async def shutdown_event():
    """Clean the serial port and save the status settings"""
    await shutdown()
