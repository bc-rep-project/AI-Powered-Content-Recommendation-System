import os
from fastapi import FastAPI

app = FastAPI()

# Your existing FastAPI routes and logic here...

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port) 