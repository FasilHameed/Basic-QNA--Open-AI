from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os 
import streamlit as st 
import time

# Load environment variables from .env file
load_dotenv()

# Function to get OpenAI response
def get_openai_response(question):
    llm = ChatOpenAI(
        openai_api_key=os.environ['OPENAI_API_KEY'],
        model_name='gpt-3.5-turbo',
        temperature=0.5
    )
    # Simulate a delay to demonstrate the loading animation
    time.sleep(2)
    response = llm.invoke(question)
    return response

# Set Streamlit page configuration
st.set_page_config(page_title='QnA App', page_icon=':robot_face:', layout='wide')

# Header
st.title('QnA Chat Bot')

# Text input for user question
input_text = st.text_input("Ask a question:", key="input")

# Button to submit question
submit_button = st.button('Ask')

# Display response
if submit_button:
    if input_text:
        # Display loading spinner animation while fetching the response
        with st.spinner('Searching for answer...'):
            response = get_openai_response(input_text)
            # Display response once fetched
            st.subheader('The Response for your Query is:')
            st.write(response)
    else:
        st.error('Please enter a question before submitting.')

# Sidebar footer with author information
st.sidebar.markdown("---")
st.sidebar.markdown("Author: Fasil Hameed")
st.sidebar.markdown("Contact Email: faisalhameed763@gmail.com")
st.sidebar.markdown("Phone Number: 7006862681")
