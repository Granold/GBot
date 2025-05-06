import streamlit as st

st.title("Gtech Assistant 🤖")

command = st.text_input("Type a command (like !help, !about, !contact):")

if command == "!help":
    st.info("Available commands: !help, !about, !contact, !joke")
elif command == "!about":
    st.success("This site is made by Gtech, your future tech overlords 😎")
elif command == "!contact":
    st.warning("Contact us at: gtech@email.com")
elif command == "!joke":
    st.balloons()
    st.write("Why did the developer go broke? Because he used up all his cache 💸")
elif command:
    st.error("Unknown command. Type !help for options.")
