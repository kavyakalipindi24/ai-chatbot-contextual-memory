import streamlit as st

st.set_page_config(page_title="AI Chatbot with Contextual Memory")

st.title("🤖 AI Chatbot with Contextual Memory")

# Initialize memory
if "history" not in st.session_state:
    st.session_state.history = []

user_input = st.text_input("You:")

if user_input:
    if "order" in user_input.lower():
        response = "Sure, please provide your order ID."
    elif user_input.isdigit():
        response = f"Thank you. I am checking the details for order {user_input}."
    else:
        response = "I understand. Please tell me more."

    st.session_state.history.append(("User", user_input))
    st.session_state.history.append(("Bot", response))

# Display conversation
for speaker, message in st.session_state.history:
    st.write(f"*{speaker}:* {message}")
