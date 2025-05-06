import streamlit as st

st.title("Gtech Assistant 🤖")

# Display instructions
st.write("Type something below and I'll respond!")

# Text input for user to chat
user_input = st.text_input("Say something:")

# Logic for responses based on user input
if user_input:
    if "hello" in user_input.lower():
        st.write("Hey there! How can I help you today?")
    elif "help" in user_input.lower():
        st.write("I can assist you with the following commands: About, Contact, Joke.")
    elif "about" in user_input.lower():
        st.write("Gtech is your future tech overlords, bringing innovation to your fingertips!")
    elif "contact" in user_input.lower():
        st.write("Contact us at: gtech@email.com 📧")
    elif "joke" in user_input.lower():
        st.write("Why did the developer go broke? Because he used up all his cache! 💸")
    else:
        st.write(f"Sorry, I don't understand '{user_input}'. Try asking for help!")

# Optionally, add a button for more interactive features
if st.button("Give me a joke!"):
    st.write("Why do programmers prefer dark mode? Because the light attracts bugs! 😜")
