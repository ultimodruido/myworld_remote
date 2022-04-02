import uvicorn
VERSION = "0.2.2"

if __name__ == "__main__":
    print(f"Starting Maerklin MyWorld universal remote v{VERSION}")
    uvicorn.run("server:app", host="127.0.0.1", port=5000, log_level="info")
