from dotenv import load_dotenv

load_dotenv() #this will load all the .env variables

import streamlit as st
import os
from PIL import Image
import google.generativeai as genai
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


##function to load gemini pro
model=genai.GenerativeModel('models/gemini-2.5-pro')

def get_gemini_response(input,image,prompt):
    response=model.generate_content([input,image[0],prompt])
    return response.text


def input_image_setup(uploaded_file):
    if upload_file is not None:
        byte_data=upload_file.getvalue()
        image_parts=[
            {
                "mime_type":uploaded_file.type,
                "data":byte_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")

st.set_page_config(page_title="MultiLangauge Invoice Extractor")
st.header("MultiLangauge Invoice Extractor")
user_input=st.text_input("Enter The Prompt:",key='input')
upload_file=st.file_uploader("Upload the Image here ",type=["jpeg",'jpg','png'])
image=""

if upload_file is not None:
    image=Image.open(upload_file)
    st.image(image,caption="uploaded image",use_container_width=True)


submit=st.button("tell me about this invoce:")
input_prompt="""
    You are an expert in understanding the inovice that can be in any langauges.
    You will help the industry expert/users to know what in the invoice.
    For that i will provide you an image about that invoice.
"""


if submit:
    image_data=input_image_setup(upload_file)
    response=get_gemini_response(input_prompt,image_data,user_input)
    st.subheader("Response is:")
    st.write(response)