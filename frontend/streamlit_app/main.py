import os

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

    # TODO: refactor backend call, should not be in line
    # Add button to call /extract API
    if st.button("Extract Medical Info from Transcript"):
        if transcript.strip():
            backend_url = "http://backend:8000/extract"  # Use service name for Docker
            payload = {"transcript": transcript}
            with st.spinner("Extracting medical info..."):
                try:
                    response = requests.post(backend_url, json=payload, timeout=60)
                    if response.status_code == 200:
                        result = response.json()
                        st.session_state.extraction_result = result
                        st.success("Extraction Result:")
                        st.write(result)
                    else:
                        st.error(f"Error: {response.status_code} - {response.text}")
                except requests.exceptions.ConnectionError:
                    st.error("Could not connect to the backend. Make sure the backend service is running.")
                except Exception as e:
                    st.error(f"An error occurred: {str(e)}")
        else:
            st.warning("Please enter or load a transcript before extracting.")

    # New section: Get studies based on extracted info
    st.header("Find Clinical Trials")
    if st.button("Find Studies Based on Extracted Info"):
        extraction_result = st.session_state.get('extraction_result')
        if extraction_result and 'extraction' in extraction_result:
            # Use the first extracted condition for demo
            condition = extraction_result['extraction']['diagnosis']
            if condition:
                studies_url = f"http://backend:8000/studies?condition={condition}&is_recruiting=true&page_size=10"
                with st.spinner(f"Searching studies for: {condition}"):
                    try:
                        studies_response = requests.get(studies_url, timeout=60)
                        if studies_response.status_code == 200:
                            studies_result = studies_response.json()
                            st.session_state.studies_result = studies_result
                            st.success("Matching Studies:")
                            st.write(studies_result)
                        else:
                            st.error(f"Error: {studies_response.status_code} - {studies_response.text}")
                    except Exception as e:
                        st.error(f"Error fetching studies: {str(e)}")
            else:
                st.warning("No medical condition found in extraction result.")
        else:
            st.warning("No extraction result available. Please extract medical info first.")

    # New section: Show studies as table if available
    studies_result = st.session_state.get('studies_result')
    if studies_result and 'studies' in studies_result:
        studies = studies_result['studies']
        rows = []
        for study in studies:
            protocol = study.get('protocolSection', {})
            identification = protocol.get('identificationModule', {})
            nct_id = identification.get('nctId', '')
            brief_title = identification.get('briefTitle', '')
            eligibility = protocol.get('eligibilityModule', {})
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
        st.subheader("Studies Table")
        # Render the Link column as clickable hyperlinks
        st.dataframe(df)

if __name__ == "__main__":
    main()