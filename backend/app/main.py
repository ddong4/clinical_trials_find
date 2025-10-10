from fastapi import FastAPI

app = FastAPI(
    title="StudyBridge API",
    description="API for matching patients with clinical trials",
    version="1.0.0",
)

@app.get("/")
async def root():
    return {"message": "Welcome to StudyBridge API"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}
