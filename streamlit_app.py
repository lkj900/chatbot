import streamlit as st
from google import genai

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

client = genai.Client(api_key="AIzaSyC3RvcvMieW5IyUk4Aykq6Mu3XHvQt-iVg")

if prompt := st.chat_input("질문을 입력하세요"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").markdown(prompt)

    response = client.models.generate_content(
        model="gemini-2.0-flash", contents=prompt
    )
    print(response.text)

    st.chat_message("assistant").markdown(response.text)
    st.session_state.messages.append({"role": "assistant", "content": response.text})

