from fastapi import FastAPI

app = FastAPI(
    title="FleetFlow Enterprise Platform",
    description="Enterprise Order and Transaction Processing Platform",
    version="1.0.0"
)

@app.get("/")
def root():
    return {
        "message": "FleetFlow API is running",
        "status": "healthy"
    }

@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }