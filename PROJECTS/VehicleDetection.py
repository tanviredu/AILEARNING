import streamlit as st
import easyocr
import numpy as np
import cv2
from PIL import Image

# Load EasyOCR Reader
reader = easyocr.Reader(['en'])

# Streamlit UI
st.set_page_config(page_title="Vehicle Number Plate Extractor")
st.title("Vehicle Number Plate Recognition 🚗")
st.write("Start your webcam, and I will extract number plates in real-time!")

start_button = st.button("Start Webcam")

if start_button:
    cap = cv2.VideoCapture(0)
    st_frame = st.empty()
    detected_plates = set()
    
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        results = reader.readtext(gray)
        
        for (bbox, text, prob) in results:
            if len(text) > 4:
                detected_plates.add(f"{text} (Confidence: {prob:.2f})")
                x_min, y_min = map(int, bbox[0])
                x_max, y_max = map(int, bbox[2])
                cv2.rectangle(frame, (x_min, y_min), (x_max, y_max), (0, 255, 0), 2)
                cv2.putText(frame, text, (x_min, y_min - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
        
        st_frame.image(frame, channels="BGR")
        
    cap.release()
    
    st.subheader("Extracted Number Plates:")
    if detected_plates:
        for plate in detected_plates:
            st.write(f"**Detected Plate:** {plate}")
    else:
        st.write("No number plates detected. Try again.")
