from fastapi import FastAPI,HTTPException
#we are creating instance for fastapi
app=FastAPI()

@app.get("/")
def root():
    return {"Select Operation": " /add, /subtract, /multiply, or /divide endpoints."}

@app.get("/add")
def add(x:float,y:float):
    return{"operation":"addition","x":x,"y":y,"result":x+y}


@app.get("/subtract")
def subtract(x: float, y: float):
    return {"operation": "subtraction", "x": x, "y": y,"result": x-y}

@app.get("/multiply")
def multiply(x: float, y: float):
    return {"operation": "multiplication", "x": x, "y": y, "result": x * y}

@app.get("/divide")
def divide(x: float, y: float):
    if y == 0:
        raise HTTPException(status_code=400, detail="Division by zero is not allowed")
    return {"operation": "division", "x": x, "y": y, "result": x/ y}