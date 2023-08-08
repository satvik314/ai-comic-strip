import streamlit as st
import replicate
from langchain.chat_models import ChatOpenAI
from langchain.chains import create_tagging_chain
from dotenv import load_dotenv
import os
load_dotenv()



st.title("🤖📖 Story Generator")
st.write("🚀 Captivating stories using Stable Diffusion and GPT")
prompt = st.text_input("What story would want to read?")
llm = ChatOpenAI(model_name="gpt-3.5-turbo")
if prompt:

    output = replicate.run(
        "stability-ai/sdxl:2b017d9b67edd2ee1401238df49d75da53c523f36e363881e057f5dc3ed3c5b2",
        input={"prompt": prompt, "width": 512, "height": 512}
    )
    story = llm.predict("Generate a story about" + prompt)
    st.image(output)
    st.write(story)