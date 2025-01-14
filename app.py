import streamlit as st
from src.helper import voice_input, load_llm_model, text_to_speech

def main():
    st.title("Multilingual AI Assistant 🤖")
    
    if st.button("Ask me anything"):
        with st.spinner("Listening..."):
            text = voice_input()
            ans = load_llm_model(text)
            text_to_speech(ans)
            
            audio_file = open("speech.mp3",'rb')
            audio_byte = audio_file.read()
            
            st.text_area(label = "Response:- ",value = ans, height=350)
            st.audio(audio_byte)
            st.download_button(label="Download Audio",
                               data = audio_byte,
                               file_name = "speech.mp3",
                               mime = "audio/mp3")
            
if __name__ == "__main__":
    main()