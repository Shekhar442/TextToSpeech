import streamlit as st

def render_sidebar():
    with st.sidebar:
        st.title("Navigation 🧭")
        
        # Page selection
        selected_page = st.radio(
            "Select Page:",
            ["Text to Speech", "Settings"]
        )
        
        st.markdown("---")
        
        # Help section
        with st.expander("How to Use"):
            st.markdown("""
            1. Enter your text
            2. Select language
            3. Adjust speech rate
            4. Click 'Convert to Speech'
            5. Play or download audio
            """)
        
        # About section
        st.markdown("---")
        st.markdown("""
        ### About
        Text to Speech Converter
        
        Made with ❤️ using:
        - Streamlit
        - gTTS
        - Python
        """)
        
    return selected_page