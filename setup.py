from setuptools import setup, find_packages

setup(
    name="Multilingual-AI-Assistant",
    version="0.0.1",
    author="Kunal Koshta",
    email="harshkosh200407@gmail.com",
    packages=find_packages(),
    install_requires=["SpeechRecognition","pipwin","pyaudio","gTTS","google-generativeai","python-dotenv","streamlit"]
)