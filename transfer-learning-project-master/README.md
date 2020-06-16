# transfer-learning-project

### 1 : YOLOV3 WEIGHTS
Download yolov3 weights file and save it in the folder 'objectDetector/yolo-coco'
- https://pjreddie.com/media/files/yolov3.weights

### 2 : Set the good chrome navigator driver : Download the same driver version that chrome driver on your laptop from https://chromedriver.chromium.org/downloads
#### Default : mac os chrome driver v79
- Change the path ```websearch/chromedriver``` in websearch/scrap.py (LINE 9: ```browser = webdriver.Chrome('websearch/chromedriver', chrome_options=options)``` )
with your driver path

### 3 : Install pipenv : For mac os ```brew install pipenv``` or ```pip install pipenv```

### 4 : Run application :
##### By default product file image to search is set at ```LINE 46``` in ``` main.py```, change the path to a new image to test others.
```pipenv shell```
and then
```python main.py```

### 5 : Open URL ```http://localhost:5000/search``` and wait for response.
