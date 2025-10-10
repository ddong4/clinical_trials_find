import streamlit as st

# Configure the page
st.set_page_config(
    page_title="StudyBridge - Clinical Trial Matching",
    page_icon="🏥"
)


def main():
    st.title("🏥 StudyBridge")
    st.subheader("Connecting Patients with Clinical Trials")
    
    st.header("Patient Interview Transcript")
    transcript = st.file_uploader("Upload a transcript file", type=["txt"])
    transcript_alt = st.text_area("Or paste the transcript here", height=200)

if __name__ == "__main__":
    main()