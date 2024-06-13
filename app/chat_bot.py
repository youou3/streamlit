import streamlit as st

st.title("Chat Bot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.message = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("What is up?"):
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    # Add user message to chat history
    st.session_state.message.append({"role":"user","content":prompt})

    response = f"Echo: {prompt}"
    with st.chat_message("assistant"):
        st.markdown(response)
    # Add assistant message to chat history
    st.session_state.message.append({"role":"assistant","content":response})


