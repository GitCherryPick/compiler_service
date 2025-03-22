from fastapi import FastAPI
import docker

app = FastAPI()
client = docker.from_env()

@app.get("/hi")
def read_root():
    return {"message": "Compiler service is running!"}

@app.post("/run")
def run_code(code: str):
    try:
        container = client.containers.run(
            "python:3.10",
            command=f"python -c {code!r}",
            remove=True,
            mem_limit="256m",
            cpus=0.5
        )
        return {"output": container}
    except Exception as e:
        return {"error": str(e)}