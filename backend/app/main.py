from fastapi import FastAPI

app = FastAPI()

@app.get("/")

def home():
    return {"message": " AI customer automation API"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}
