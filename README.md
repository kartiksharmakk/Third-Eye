## Android Implementation 
Android app using WebView of Flask WebApp 

https://user-images.githubusercontent.com/77577353/188488867-f4bffe87-4f18-427a-bd33-619d5e4b4da7.mp4

## Web Implementation using Flask 
https://user-images.githubusercontent.com/77577353/188488874-3771d85f-7996-4183-a237-2db90c71c022.mp4

## 💁‍♂️ How to build Web Implementation locally
- Clone The Repo and open `website` directory
- download and extract zip file at (https://drive.google.com/file/d/1-P5NVywbdFcT5XCCxSS1RsDtGiZflblF/view?usp=sharing)
- place features.pkl , image_caption_RNN_LSTM_model.h5 , vgg16_feature_extractor.h5 into `working` folder inside `website` directory
- Install Python requirements `pip install -r requirements.txt`
- Start the server for development `python app.py` or `python3 app.py `

## 💁‍♂️ How to build Android Implementation locally
- Clone The Repo and open Android Studio inside the `android` folder
- Android Studio will sync the gradle
- Make Sure to run the flask WebApp (`python app.py`)
- change variable `URL` in `MainActivity` from "http://192.168.1.2:5000/" to the generated URL and then run the app on Emulator

## Model Details

- We Have used a Combination of pretrained CNN model (VGG-16) With only its feature extraction dense layers while removing the classification layer   
- And We Have used a Custom RNN (LSTM) Model to generate image captions
- This Dataset was used in generation of RNN(LSTM) model for this project(https://www.kaggle.com/datasets/adityajn105/flickr8k) 
- CNN (VGG-16) Model extracts features from images
- RNN (LSTM) Model gives final caption output based on features
- The training jupyter notebook and model files can be downloaded from (https://drive.google.com/file/d/1-P5NVywbdFcT5XCCxSS1RsDtGiZflblF/view?usp=sharing)

## Model 
- Custom RNN(LSTM) Model Visualized
<img src="https://raw.githubusercontent.com/kartiksharmakk/Thrid-Eye/main/image_caption_RNN_LSTM_model.png" width="40%" height="30%"/>

- Pretrained (VGG-16) Model with last 2 layers removed Visualized 
<img src="https://raw.githubusercontent.com/kartiksharmakk/Thrid-Eye/main/vgg16_feature_extractor.png" width="30%" height="25%"/>
