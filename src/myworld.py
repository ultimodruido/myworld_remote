import uvicorn
import argparse


VERSION = "1.0"


if __name__ == "__main__":
    # parse CLI arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--port", help="set the port for the server (default 5000)", type=int)
    args = parser.parse_args()

    # define server port number
    server_port = 5000
    if args.port:
        server_port = args.port

    print(f"Starting Maerklin MyWorld universal remote v{VERSION}")
    uvicorn.run("server:app", host="0.0.0.0", port=server_port, log_level="info")
