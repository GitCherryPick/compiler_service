from fastapi import FastAPI
from pydantic import BaseModel
from RestrictedPython import compile_restricted

app = FastAPI()

class CodeRequest(BaseModel):
    code: str

@app.post("/run")
def run_code(request: CodeRequest):
    code = request.code

    # Código base restringido para ejecución
    safe_globals = {"__builtins__": {}}
    safe_locals = {}

    try:
        bytecode = compile_restricted(code, "<string>", "exec")
        exec(bytecode, safe_globals, safe_locals)

        # Devolver el valor de 'result' si existe
        output = safe_locals.get("result", "No output")

        return {"output": output}

    except Exception as e:
        return {"error": str(e)}

@app.get("/hi")
def read_root():
    return {"message": "Compiler service is running!"}
