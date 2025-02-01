import streamlit as st
import pandas as pd
import ollama

convo = []


def stream_response(prompt):
    convo.append({'role': 'user', 'content': prompt})
    response = ''
    stream = ollama.chat(model='llama3.1:8b', messages=convo, stream=True)
    for chunk in stream:
        response += chunk['message']['content']
        print(chunk['message']['content'], end='', flush=True)
    convo.append({'role': 'assistant', 'content': response})
    return response


# Streamlit UI
st.title("Automated Essay Scoring and Feedback System")

st.header("Submit Your Essay")

# Essay input
essay_text = st.text_area("Enter your essay here", height=300)

# Optional user information for personalized feedback
user_level = st.selectbox("Select your academic level", ["High School", "Undergraduate", "Graduate"])

if st.button("Submit"):
    # Generate prompt for scoring and feedback
    prompt = f"Essay: {essay_text}\nAcademic Level: {user_level}\nPlease provide a score and detailed feedback."
    response = stream_response(prompt=prompt)

    # Display the response
    st.write("**Score and Feedback:**")
    st.write(response)

    # Visualize strengths and weaknesses (mockup)
    strengths = {"Grammar": 85, "Coherence": 90, "Organization": 80, "Content Relevance": 75}

