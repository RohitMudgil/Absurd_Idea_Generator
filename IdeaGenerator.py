import pathlib
import textwrap
import os
import markdown

import google.generativeai as genai

from dotenv import load_dotenv

def getResponseFromGemini( promptValues):
    initialize()
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(generate_prompt(promptValues))
    return markdown.markdown(response.text)

def initialize():
    load_dotenv()
    GOOGLE_API_KEY = os.getenv('GEMINI_API_KEY')
    # print("hello", GOOGLE_API_KEY)
    genai.configure(api_key=GOOGLE_API_KEY)

def generate_prompt(promptValues):
    prompt = "Hi Gemini, I have " + promptValues[2] + " days to make a project in the " + promptValues[0] + "  field of using the " + promptValues[1] +" tech stack: Give me the most interestingly weird idea you can think of."
    return prompt
