from fastapi import FastAPI

app = FastAPI()
@app.get("/hi")
def read_root():
    return {"message": "Compiler service is running!"}
