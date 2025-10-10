import os

import requests
import streamlit as st

# Configure the page
st.set_page_config(
    page_title="StudyBridge - Clinical Trial Matching",
    page_icon="🏥"
)


def main():
    st.title("🏥 StudyBridge")
    st.subheader("Connecting Patients with Clinical Trials")
    
    # Test section for FastAPI integration
    st.header("🤖 AI Assistant Test")
    
    if st.button("Tell me a medical joke!"):
        try:
            # Call the FastAPI backend
            backend_url = "http://backend:8000/generate"  # Use service name for Docker
            payload = {"prompt": "Tell a medical joke in 30 words!"}
            
            with st.spinner("Generating joke..."):
                response = requests.post(backend_url, json=payload)
                
            if response.status_code == 200:
                result = response.json()
                st.success("🎉 Here's your medical joke:")
                response = result.get("response")
                if not response:
                    st.warning("No response received from Gemini. Please retry.")
                st.write(response)
            else:
                st.error(f"Error: {response.status_code} - {response.text}")
                
        except requests.exceptions.ConnectionError:
            st.error("Could not connect to the backend. Make sure the backend service is running.")
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
    
    st.divider()
    
    st.header("Patient Interview Transcript")
    
    
    # Add Try It Out button
    col1, col2 = st.columns([2, 4])
    with col1:
        if st.button("Try Our Example!"):
            try:
                example_file_path = "streamlit_app/assets/foot_transcript_example.txt"
                if os.path.exists(example_file_path):
                    with open(example_file_path, 'r', encoding='utf-8') as file:
                        st.session_state.transcript_content = file.read()
                else:
                    st.error("Example transcript file not found.")
            except Exception as e:
                st.error(f"Error loading example transcript: {str(e)}")
    
    transcript_content = st.session_state.get('transcript_content', '')
    transcript = st.text_area("Or paste your own transcript here", value=transcript_content, height=300)

if __name__ == "__main__":
    main()