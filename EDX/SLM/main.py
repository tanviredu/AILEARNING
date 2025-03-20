import os
import json
import groq
import Website
import gradio as gr
from dotenv import load_dotenv
load_dotenv()

SYSTEM_PROMPT = "You are an assistan that analyze the contents of a website and provides a short summary.Ignore the navigation link"

def user_prompt_for(website_data):
    USER_PROMPT  = f"you are looking at a website titled{website_data.title} "
    USER_PROMPT += "The contents of this website is as follows. please provide a short summary of the website"
    USER_PROMPT += "If it includes news and any announcement, summarize it too\n\n"
    USER_PROMPT += website_data.text
    return USER_PROMPT

def messages_for(website):
    return[
        {
            "role":"system",
            "content":SYSTEM_PROMPT
        },
        {
            "role":"user",
            "content":user_prompt_for(website)
        }
    ]

def get_summary(url):
    website  = Website.Website(url)
    client   = groq.Groq(api_key=os.environ.get("GROQ_API_KEY"))
    response = client.chat.completions.create(
        messages=messages_for(website),
        model="llama-3.3-70b-versatile"
    )

    return response.choices[0].message.content



demo = gr.Interface(
    fn = get_summary,
    inputs = "text",
    outputs= "text",
    title="Website summarize",
    description="This tool Summarize website."
)

demo.launch()



