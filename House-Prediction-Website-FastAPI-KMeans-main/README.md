# 🏡House Category Predictor

This project is about the Website for predicting the 4 different category of house based on the Machine Learning model on a given dataset.

# 📌 Overview

House Category Predictor is a lightweight, interactive web application where users can:
> Enter the sqft of their house

> Location Score (1 being max and 10 min)

> No of BHK

> Price in Crores-₹

> The application uses a FastAPI backend and ML Models created using K-Means ML Algorithm.


# 📦 Dependencies:
> pip install numpy pandas matplotlib seaborn fastapi uvicorn pandas openpyxl jinja2 python-multipart scikit-learn

> In Pycharm, add these packages manually by searching each one by one 


# 📂 File structure

> main.py, pkl models and python notebook in the same directory

> templates folder has index.html

> static folder has images folder, style.css and script.js

> images folder has all the required images


# 👨‍💻 Steps to run the code

> First run the ML notebook code and get the models
>
> scaler model remembers mean and standard deviation of each feature and hence similar scaling as it has done during the training
>
> kmeans model has cluster patterns and learned patterns required for prediction
> 
> Hence short 2 .pkl files because scaler stores how to transform the data, and kmeans stores how to predict.

> Then run the code using command: uvicorn main:app --reload

> Test the predictions with live predicted values

> Predicted values atre normal output values and poster is also added for more visual prediction! 
