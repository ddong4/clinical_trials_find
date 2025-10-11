import os
import time

import pandas as pd
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
    
    st.write(
        """
        Welcome to StudyBridge! This application helps match patients with relevant clinical trials based on their medical information.
        You can input a patient interview transcript, and our AI-powered system will extract key medical details to find suitable trials.
        """
    )
    
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

    # Combined process: Extract Medical Info and Find Studies
    if st.button("🔍 Extract Medical Info & Find Clinical Trials"):
        if transcript.strip():
            # Initialize progress bar
            progress_bar = st.progress(0)
            
            try:
                with st.status("Starting extraction and trial search...", expanded=True) as status:
                    # Step 1: Extract medical information (13 seconds)
                    status.update(label="Extracting medical information from transcript...", state="running")
                    st.write("AI Extraction in progress...")
                    progress_bar.progress(10)
                    backend_url = "http://backend:8000/extract"
                    payload = {"transcript": transcript}
                    import threading
                    response_container = {'response': None, 'error': None}
                    def make_request():
                        try:
                            response_container['response'] = requests.post(backend_url, json=payload, timeout=60)
                        except Exception as e:
                            response_container['error'] = e
                    thread = threading.Thread(target=make_request)
                    thread.start()
                    for i in range(10, 90, 2):
                        if not thread.is_alive():
                            break
                        progress_bar.progress(i)
                        time.sleep(0.3)
                    thread.join()
                    if response_container['error']:
                        status.update(label="❌ Error extracting medical info", state="error")
                        raise response_container['error']
                    response = response_container['response']
                    if response.status_code != 200:
                        status.update(label=f"❌ Error extracting medical info: {response.status_code}", state="error")
                        st.error(f"Error extracting medical info: {response.status_code} - {response.text}")
                        return
                    result = response.json()
                    st.session_state.extraction_result = result
                    progress_bar.progress(90)
                    status.update(label="✅ Medical information extracted!", state="running")
                    # Step 2: Find studies based on extracted info (1 second)
                    if 'extraction' in result:
                        condition = result['extraction']['diagnosis']
                        if condition:
                            status.update(label=f"Finding clinical trials for: {condition}", state="running")
                            st.write(f"Extracted Diagnosis: {condition}")
                            studies_url = f"http://backend:8000/studies?condition={condition}&is_recruiting=true&page_size=10"
                            for i in range(90, 100, 2):
                                progress_bar.progress(i)
                                time.sleep(0.05)
                            studies_response = requests.get(studies_url, timeout=60)
                            if studies_response.status_code == 200:
                                studies_result = studies_response.json()
                                st.session_state.studies_result = studies_result
                                progress_bar.progress(100)
                                status.update(label=f"✅ Found {len(studies_result.get('studies', []))} matching clinical trials for: {condition}", state="complete")
                                st.write(f"Found top {len(studies_result.get('studies', []))} matching studies.")
                            else:
                                progress_bar.progress(100)
                                status.update(label="❌ Error finding studies", state="error")
                                st.error(f"Error finding studies: {studies_response.status_code} - {studies_response.text}")
                        else:
                            progress_bar.progress(100)
                            status.update(label="⚠️ No medical condition found in transcript.", state="error")
                            st.warning("No medical condition found in extraction result.")
                    else:
                        progress_bar.progress(100)
                        status.update(label="⚠️ No extraction data found.", state="error")
                        st.warning("No extraction data found in response.")
            except requests.exceptions.ConnectionError:
                st.error("Could not connect to the backend. Make sure the backend service is running.")
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")
        else:
            st.warning("Please enter or load a transcript before processing.")

    # Results section: Show studies as table if available
    st.header("Clinical Trial Results")
    studies_result = st.session_state.get('studies_result')
    if studies_result and 'studies' in studies_result:
        studies = studies_result['studies']
        rows = []
        for study in studies:
            protocol = study.get('protocolSection', {})
            identification = protocol.get('identificationModule', {})
            nct_id = identification.get('nctId', '')
            brief_title = identification.get('briefTitle', '')
            locations_module = protocol.get('contactsLocationsModule', {})
            locations = locations_module.get('locations', [])
            # Serialize locations as a string of city/country or just count
            if locations:
                loc_str = ', '.join([
                    f"{loc.get('city', '')}, {loc.get('country', '')}" for loc in locations if 'city' in loc and 'country' in loc
                ])
            else:
                loc_str = ''
            link = f"https://clinicaltrials.gov/study/{nct_id}" if nct_id else ''
            rows.append({
                'NCT ID': nct_id,
                'Title': brief_title,
                'Locations': loc_str,
                'Link': link
            })
        df = pd.DataFrame(rows)
        st.subheader("Matching Studies Table")
        # Render the Link column as clickable hyperlinks
        st.table(df)

    st.markdown("---")
    debug = st.session_state.get('debug', False)
    debug_toggle = st.checkbox("Show Debug Info", value=debug, key="debug_toggle")
    st.session_state['debug'] = debug_toggle

    if st.session_state['debug']:
        extraction_result = st.session_state.get('extraction_result')
        if extraction_result:
            st.write("[DEBUG] Extraction Result:")
            st.write(extraction_result)

        studies_result = st.session_state.get('studies_result')
        if studies_result:
            st.write("[DEBUG] Studies Result:")
            st.write(studies_result)

if __name__ == "__main__":
    main()