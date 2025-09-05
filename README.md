# orbit-cdn-api
A simple API for OrbitNTNU's CDN. The CDN contains images and other media files. Built with Python, FastAPI and Uvicorn.
allowed media files: jpg, png, gif, mp4

this api offers the following endpoints:
- /get-latest-memes : get all file names of the newly submitted memes
- /get-winner-memes : get all file names of the winner memes
- /get-positions : get all file names of position images
- /get-profile-imgs : get all file names of profile pictures
- /post-candidate-meme : put a meme in the CDN
- /post-winner : put the winner meme in the CDN
- /post-positions : put position images in the CDN
- /post-profileimg : put profile images in the CDN

how to run it:
make sure to be in the "/cdn-api" directory and run the docker container+image:
```
docker compose up --build
```

example on how to use the API (in Python):
```
import requests
cat_gif = "C:/Users/selin/Screenshots/cat-dancing.gif"
post_url = "http://0.0.0.0:8000/post-winner"

with open(cat_gif, 'rb') as f:
    cat_data = f.read()
    f.close()

files_data = {'file': ('cat-dancing.gif', cat_data, 'image/gif')}
response1 = requests.post(post_url, files=files_data)
print(response1)
```
This API is meant to run on OrbitNTNU's server.
