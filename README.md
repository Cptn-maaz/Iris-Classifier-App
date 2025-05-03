# 🌸 Iris Flower Classifier Web App

This is a simple web application built with **Streamlit** that allows users to classify Iris flowers based on user input features using a machine learning model.

---

## 🚀 Features
- Train and evaluate an ML model on the Iris dataset
- Web interface built using Streamlit
- Predict Iris species from user input
- Visualize model results

---

## 🧠 Tech Stack
- Python 3.10
- Streamlit
- NumPy
- Pandas
- Matplotlib
- Seaborn
- scikit-learn
- Joblib

---
## Project Setup and Deployment Guide
### Step 1: Model Development
Run the provided Jupyter notebook on your preferred platform (Google Colab, Kaggle, or Anaconda). The notebook includes all essential steps for model development:
- Loading the dataset
- Preprocessing
- Model training
- Model evaluation
- Downloading the trained model
  
### Step 2: Project Directory Setup
Create a new folder (e.g., Project) on your local machine.
Copy and paste the following files into this folder:
- Downloaded model file(s)
- streamlit_app.py
- Any associated images or assets

###  Step 3: Virtual Environment Setup (Using Anaconda)
1) Open Anaconda Prompt
2) Navigate to your project directory:
  - cd path\to\your\Project
3) Create a virtual environment with Python 3.10:
  - conda create -n iris_env python=3.10
4) Activate the newly created environment:
  - conda activate iris_env
You can also watch the following video on how to setup a virtual environment for a project
https://www.youtube.com/watch?v=5MDv8R5UGqQ&list=PLxf3-FrL8GzTIQpnY_UyzDX6JK0_Kbe_t&index=32&ab_channel=IrfanMalik

### Step 4: Install Dependencies
Install the required Python packages using pip:
  - pip install streamlit scikit-learn numpy joblib

### Step 5: Running the Streamlit App
1) Open Visual Studio Code (VS Code).
2) Select the iris_env virtual environment.
3) Open the streamlit_app.py file.
4) In the VS Code terminal, run the following command to launch the application:
  - streamlit run streamlit_app.py
