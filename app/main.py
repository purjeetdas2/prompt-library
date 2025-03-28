from fastapi import FastAPI
from app.api.endpoints import categories, subcategories, prompts
from mangum import Mangum

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Prompt Library APIs"}

# Include routers for your API endpoints
app.include_router(categories.router, prefix="/categories", tags=["categories"])
app.include_router(subcategories.router, prefix="/subcategories", tags=["subcategories"])
app.include_router(prompts.router, prefix="/prompts", tags=["prompts"])

# Create a Mangum handler for AWS Lambda
handler = Mangum(app)
