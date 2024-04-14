import streamlit as st
from openai import OpenAI
import os
import time
key= st.text_input("enter key")
# Setting up OpenAI client
os.environ["OPENAI_API_KEY"] =key
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

# Retrieving assistant
assistant = client.beta.assistants.retrieve("asst_TuCwfc1MqzmAFbQb0ss9V95D")
st.write("Assistant Located")
user_input = st.text_input("Enter your values")
# Creating a thread
thread = client.beta.threads.create()
st.write("Thread Created")


# Sending initial message
message = client.beta.threads.messages.create(
    thread_id=thread.id,
    role="user",
    content=user_input
)
st.write("Thread Ready")

# Starting the assistant
run = client.beta.threads.runs.create(
    thread_id=thread.id,
    assistant_id=assistant.id
)
st.write("Assistant Loaded")
st.write("Run Started - Please Wait")

# Checking for completion
while True:
    time.sleep(10)

    run_status = client.beta.threads.runs.retrieve(
        thread_id=thread.id,
        run_id=run.id
    )

    if run_status.status == "completed":
        st.write("Run is Completed")
        messages = client.beta.threads.messages.list(
            thread_id=thread.id
        )
        st.write(messages.data[1].content[0].text.value)
        break
    else:
        st.write("Run is in progress - Please Wait")
        continue
