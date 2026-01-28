# 🤖 LLM-Powered Chatbot (Flask, Transformers)


## Overview
This is a chatbot application powered by a large language model (BlenderBot) using Hugging Face Transformers. Users can interact with the AI through a web interface and receive real-time, coherent responses.  



## Project Highlights
- Deployed a conversational AI model using Hugging Face Transformers (BlenderBot)  
- Implemented POST-based API communication between frontend and backend  
- Managed model tokenization, inference, and response decoding  
- Built and hosted a web-based chatbot UI using HTML, CSS, and JavaScript  



## Features
-  Real-time text-based conversation  
-  Clean and readable responses  
-  User-friendly web interface  



## Technologies Used
- **Frontend:** HTML, CSS, JavaScript  
- **Backend:** Flask, Python  
- **AI Model:** Hugging Face Transformers (BlenderBot)  



## Screenshot
<img width="1914" height="1018" alt="Screenshot 2026-01-28 142700" src="https://github.com/user-attachments/assets/8bafa804-a27d-4b59-899f-d711cb3140ba" />
  



## Project Structure
LLM_application_chatbot/
├── app.py                  # Flask backend application
├── requirements.txt        # Python dependencies
├── templates/              # HTML templates for Flask
│   └── index.html          # Main frontend page
├── static/                 # Static assets for frontend
│   ├── style.css           # Stylesheet
│   └── script.js           # Frontend JavaScript
├── .gitignore              # Git ignore file to exclude venv, __pycache__, etc.
└── README.md   






## How to Run the Project
Follow these steps to set up and run the LLM-Powered Chatbot locally.

### Clone the Repository
git clone https://github.com/ibm-developer-skills-network/LLM_application_chatbot.git
cd LLM_application_chatbot
# Clone the repository
git clone https://github.com/username/LLM_application_chatbot.git
cd LLM_application_chatbot

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run Flask
export FLASK_APP=app.py
export FLASK_ENV=development
flask run

### Create and Activate a Virtual Environment
Mac / Linux:

python3 -m venv venv
source venv/bin/activate
Windows (PowerShell):

python -m venv venv
venv\Scripts\activate

 ### Install Dependencies

pip install --upgrade pip
pip install -r requirements.txt
### Run the Flask Application
Mac / Linux:

export FLASK_APP=app.py
export FLASK_ENV=development
flask run

Windows (PowerShell):

set FLASK_APP=app.py
set FLASK_ENV=development
flask run

### Open in Browser
Go to: http://127.0.0.1:5000 to see the chatbot interface and start interacting with it.


## License
This project is licensed under the MIT License.
