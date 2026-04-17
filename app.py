import streamlit as st
from llm_engine import generate_questions
from data_store import save_candidate
from utils.helpers import validate_email, validate_phone
from config import EXIT_KEYWORDS

st.title("TalentScout Hiring Assistant")

if "stage" not in st.session_state:
    st.session_state.stage="start"


if st.session_state.stage=="start":

    st.write("Welcome to TalentScout Hiring Assistant")

    if st.button("Start Interview"):
        st.session_state.stage="info"


elif st.session_state.stage=="info":

    name=st.text_input("Full Name")
    email=st.text_input("Email")
    phone=st.text_input("Phone Number")
    experience=st.number_input("Years of Experience",0,40)
    role=st.text_input("Desired Role")
    location=st.text_input("Current Location")
    tech_stack=st.text_area("Tech Stack")

    if st.button("Submit"):

        if not validate_email(email):
            st.error("Invalid email")

        elif not validate_phone(phone):
            st.error("Invalid phone number")

        else:

            candidate={
                "name":name,
                "email":email,
                "phone":phone,
                "experience":experience,
                "role":role,
                "location":location,
                "tech_stack":tech_stack
            }

            save_candidate(candidate)

            questions=generate_questions(tech_stack)

            st.session_state.questions=questions
            st.session_state.stage="questions"


elif st.session_state.stage == "questions":

    st.subheader("Technical Questions")

    st.write(st.session_state.questions)

    user_input = st.text_input("Type 'exit' or 'finish' to end the interview")

    if user_input and user_input.lower() in EXIT_KEYWORDS:
        st.session_state.stage = "end"
        st.rerun()


elif st.session_state.stage == "end":

    st.success("Thank you for participating. Our recruitment team will contact you.")