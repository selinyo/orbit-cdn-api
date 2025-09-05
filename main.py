from fastapi import FastAPI, UploadFile, File, HTTPException
import uvicorn
import os
from dotenv import load_dotenv

app = FastAPI()
load_dotenv()

@app.get("/")
async def hello():
    return {'Message': 'Hello! this is a wip'}

@app.get("/get-latest-memes")
async def get_latest_memes() -> dict:
    try:
        upload_dir = 'C:/Users/selin/Documents/orbit/cdn-api/uploads'
        all_memes = os.listdir(upload_dir)
        meme_urls = ['https://cdn.orbitntnu.com/memes/'+file_name for file_name in all_memes]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Something went wrong: {e}")
    return {'Message': meme_urls}

@app.post("/post-candidate-meme")
async def upload_meme(file: UploadFile = File(...)):
    upload_dir = 'C:/Users/selin/Documents/orbit/cdn-api/uploads'
    try:
        new_path = os.path.join(upload_dir, file.filename).replace('\\', '/')
        with open(new_path, 'wb') as f:
            while contents := file.file.read(1024*1024):
                f.write(contents)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f'Something went wrong: {e}')
    finally:
        file.file.close()
    return {'Message': f'Successfully uploaded {file.filename}'}

@app.post("/post_winner")
async def upload_winner(file: UploadFile = File(...)):
    upload_dir = 'C:/Users/selin/Documents/orbit/cdn-api/winner'
    new_path = os.path.join(upload_dir, file.filename).replace('\\', '/')

    candidates_dir = 'C:/Users/selin/Documents/orbit/cdn-api/uploads'
    try:
        with open(new_path, 'wb') as f:
            while contents := file.file.read(1024*1024):
                f.write(contents)

        for meme in os.listdir(candidates_dir):
            meme_path =  new_path = os.path.join(upload_dir, meme).replace('\\', '/')
            if os.path.isfile(meme_path):
                os.remove(meme_path)
                print(f'{candidates_dir} was emptied.')

    except Exception as e:
        raise HTTPException(status_code=500, detail=f'Something went wrong: {e}')
    finally:
        file.file.close()
    return {'Message': f'Successfully uploaded the winner {file.filename}'}

        
@app.post("/post-positions")
async def post_positions(file: UploadFile = (...)):
    test_dir = os.getenv('TEST_DIRECTORY')
    new_file = os.path.join(test_dir, file.filename).replace('\\', '/')
    try:
        if os.path.exists(new_file):
            raise HTTPException(status_code=409, detail="File already exists.")
        else:
            with open(new_file, 'wb') as f:
                while contents := file.file.read(1024*1024):
                    f.write(contents)
    except Exception as e:
        print(f'Something went wrong: {e}')
        raise HTTPException(status_code=500, detail=f'Something went wrong: {e}')
    finally:
        file.file.close()
        return {'url': f'https://cdn.orbitntnu.com/positions/{file.filename}'}
    
    

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)