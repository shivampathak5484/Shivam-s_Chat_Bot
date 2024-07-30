import streamlit as st
from groq import Groq

# Initialize the Groq client
client = Groq(
    api_key="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",
)

def get_chat_completion(user_input):
    # Generate chat completion
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": user_input,
            }
        ],
        model="llama3-70b-8192",
    )
    
    return chat_completion.choices[0].message.content

# Streamlit app layout
st.title("Shivam's Chat bot")

# Input text box
user_input = st.text_input("Enter your message:")

# Submit button
if st.button("Submit"):
    # Get chat completion based on user input
    response = get_chat_completion(user_input)
    
    # Display the response
    st.write(f"Response: {response}")

### streamlit run streamlit_app.py