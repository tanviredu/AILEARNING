import os
import time 
import gradio as gr
import groq
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
load_dotenv()
#https://www.suicideinfo.ca/research-roundup-april-2024/

def load_and_parse_content(url):
    #print(url)
    os.listdir(r"C:\Program Files\Google\Chrome\Application")
    options = Options()
    #options.binary_location = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    #print(driver)
    
    driver.get(url)
    #print(url)
    WebDriverWait(driver=driver,timeout=10).until(
        EC.presence_of_element_located((By.TAG_NAME,'body'))
    )
    #print("going to sleep for 2 sec")
    time.sleep(2) ## allow it to load
    soup = BeautifulSoup(driver.page_source,'html.parser')
    title      = soup.title.string if soup.title else "No Title Found"
    #print(title)
    if soup.body :
        #print(soup.body)
        for irr in soup.body(['script','img','style','input']):
            irr.decompose()
        text = soup.body.get_text(separator='\n',strip=True)
        #print(text)
    else:
        text = ""
        #print(text)
        
    links = []
    
    for link in soup.find_all('a'):
        href = link.get('href')
        links.append(href)
    
    
    return f"WEBSITE TITLE : {title}\n\n WEBSITE CONTENT :\n\n {text}\n\n WEBSITE LINKS : {links}"

    
        
SYSTEM_PROMPT = "You are an assistant that analyze website information and make a short summary. ignore the navigation links"

def user_prompt_for(website_data):
    USER_PROMPT    = f"You are looking at a website Data"
    USER_PROMPT   += "The contents of the website is the folowing. please make a short summary \n\n"
    USER_PROMPT   += "If it incudes news and announcement make their summary too"
    USER_PROMPT   += website_data
    return USER_PROMPT

def message_for(webste):
    return [
        {
            "role":"system",
            "content": SYSTEM_PROMPT
        },
        {
            "role":"user",
            "content": user_prompt_for(webste)
        }
    ]
    
def get_summary(url):
    website  = load_and_parse_content(url)
    client   = groq.Groq(api_key=os.environ.get("GROK_API"))
    response = client.chat.completions.create(
        messages=message_for(website),
        model   = "llama-3.3-70b-versatile"
    )
    
    #print(response.choices[0].content)
    return response.choices[0].message.content

demo = gr.Interface(
    fn = get_summary,
    inputs = "text",
    outputs = "text",
    title  = "Website Summarize",
    description= "This app Summarize the website content"
) 

demo.launch()