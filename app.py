import streamlit as st
from analyzer import analyze_profile

st.set_page_config(page_title="LinkedIn Profile Analyzer", page_icon="💼")

st.title("💼 LinkedIn Profile Analyzer")
st.write("Analyze your LinkedIn headline and about section for better engagement.")

headline = st.text_input("Enter your LinkedIn Headline")

about = st.text_area("Paste your LinkedIn About Section")

if st.button("Analyze Profile"):
    if headline and about:
        result = analyze_profile(headline, about)

        st.subheader("📊 Profile Score")
        st.success(f"{result['score']} / 100")

        st.subheader("📈 Analysis")

        st.write(f"Headline Length: {result['headline_length']} characters")
        st.write(f"About Length: {result['about_length']} characters")
        st.write(f"Keywords Found: {', '.join(result['keywords'])}")

        st.subheader("💡 Suggestions")

        for suggestion in result["suggestions"]:
            st.write(f"- {suggestion}")
    else:
        st.warning("Please fill both fields.")
