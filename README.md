# TalentScout AI Hiring Assistant 🤖

An AI-powered chatbot that helps recruiters perform **initial candidate screening** by collecting candidate details and generating **technical interview questions based on the candidate's tech stack using LLMs**.

---

## Live Demo

Streamlit App:  
https://talentscout-ai-recruiter.streamlit.app/

GitHub Repository:  
https://github.com/Akk8113/talentscout-hiring-assistant

---

## Features

### Candidate Information Collection
The chatbot collects the following details:

- Full Name  
- Email Address  
- Phone Number  
- Years of Experience  
- Desired Role  
- Current Location  
- Tech Stack  

---

### Tech Stack Based Question Generation

Candidates can enter technologies like:

```
Python, SQL, Machine Learning
React, Node.js, MongoDB
Docker, Kubernetes, AWS
```

The chatbot generates **3–5 technical questions per technology**.

---

### LLM Powered Question Generation

Example:

Tech Stack Input:

```
Python, Django
```

Generated Questions:

```
Python
• Explain Python decorators
• What are generators in Python?

Django
• What is Django ORM?
• Explain Django middleware
```

---

## Tech Stack

Programming Language  
- Python

Framework  
- Streamlit

LLM  
- Groq API  
- LLaMA Model

Libraries  
- streamlit  
- groq  
- python-dotenv  

---

## Project Structure

```
talentscout-hiring-assistant
│
├── app.py
├── llm_engine.py
├── config.py
├── prompts.py
├── data_store.py
├── requirements.txt
├── README.md
│
└── utils
    └── helpers.py
```

---

## Installation

Clone the repository

```
git clone https://github.com/yourusername/talentscout-hiring-assistant.git
```

Move to project directory

```
cd talentscout-hiring-assistant
```

Create virtual environment

```
python -m venv venv
```

Activate environment (Windows)

```
venv\Scripts\activate
```

Install dependencies

```
pip install -r requirements.txt
```

---

## Run the Application

```
streamlit run app.py
```

---

## Deployment

The project can be deployed on **Streamlit Community Cloud**.

Steps:

1. Push project to GitHub
2. Connect repository to Streamlit Cloud
3. Select `app.py` as the main file
4. Add secret key:

```
GROQ_API_KEY = "your_api_key"
```

---

## Prompt Design

The system uses two prompts:

**System Prompt**

Defines chatbot behavior as a technical interviewer.

**Technical Question Prompt**

```
Generate 3–5 technical interview questions for {tech_stack}.
```

---

## Data Privacy

- Candidate data is stored locally
- No personal data is shared externally
- API keys are stored using environment variables

---

## Challenges Faced

**API Quota Issues**

Solution: Switched to Groq API for faster LLM inference.

**Handling Multiple Tech Stacks**

Solution: Split the tech stack and generate questions per technology.

---

## Future Improvements

- AI-based candidate answer evaluation
- Interview scoring system
- Multilingual support
- UI improvements

---

## Author

Arpit Kakaiya  
B.Tech Computer Engineering  
AI & Data Science Enthusiast

