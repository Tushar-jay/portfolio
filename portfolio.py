import streamlit as st
from PIL import Image
import requests
from streamlit_lottie import st_lottie
import time

st.set_page_config(page_title="Tushar Dasgupta | Portfolio", page_icon="🚀", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200: return None
    return r.json()

lottie_coder = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_u4yrau.json")

# Typing Header
st.markdown("""
    <style>
    .typing {
        font-size: 45px;
        font-weight: bold;
        color: #004080;
        white-space: nowrap;
        overflow: hidden;
        border-right: 4px solid #004080;
        animation: typing 3s steps(40, end), blink-caret .75s step-end infinite;
    }
    @keyframes typing {
      from { width: 0 }
      to { width: 100% }
    }
    @keyframes blink-caret {
      from, to { border-color: transparent }
      50% { border-color: #004080; }
    }
    </style>
    <p class='typing'>Hi, I'm Tushar — I turn data into decisions.</p>
""", unsafe_allow_html=True)

tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["🏠 About", "📁 Projects", "🧠 Skills", "📜 Certs", "💬 Testimonials", "📬 Contact"])

# Tab 1 - About
with tab1:
    col1, col2 = st.columns([1, 2])
    with col1:
        st_lottie(lottie_coder, height=280)
    with col2:
        st.subheader("Data Analyst | ML Engineer | BI Developer")
        st.markdown("""
        I'm a results-driven Data Analyst with experience in real-time analytics, time-series modeling, and interactive dashboards.

        I build intelligent systems that predict, classify, and narrate the data story.
        """)
        st.markdown("📍 Kolkata, India | 📧 tushardasgupta4@gmail.com")
        st.markdown("[🔗 GitHub](https://github.com/Tushar-jay) | [🔗 LinkedIn](https://linkedin.com/in/tushar-dasgupta-756519226/)")

        try:
            with open("Tushar Dasgupta_Resume.pdf", "rb") as f:
                st.download_button("📄 Download Resume", f, file_name="Tushar Dasgupta_Resume.pdf")
        except FileNotFoundError:
            st.error("⚠️ Resume not found. Please place 'Tushar Dasgupta_Resume.pdf' in the same folder.")

        st.image("https://ghchart.rshah.org/Tushar-jay", caption="GitHub Contributions")

# Tab 2 - Projects
with tab2:
    st.markdown("## 📁 Highlight Projects")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("### 🔹 DeepStock AI")
        st.markdown("- LSTM-based stock forecasting")
        st.markdown("[GitHub](https://github.com/Tushar-jay/stock-prediction)")
    with col2:
        st.markdown("### 🔹 MotionIQ")
        st.markdown("- Real-time activity recognition with ML models")
        st.markdown("[GitHub](https://github.com/Tushar-jay/human-activity-recognition)")
    with col3:
        st.markdown("### 🔹 SmartFlow BI")
        st.markdown("- Revenue & client dashboard in Power BI")
        st.markdown("[GitHub](https://github.com/Tushar-jay/SmartFlow-BI-Revenue-Trends-Client-Insights)")

# Tab 3 - Skills
with tab3:
    st.markdown("## 🧠 Skills")
    skills = {
        "Languages & Tools": ["Python", "SQL", "Git"],
        "Libraries": ["pandas", "NumPy", "scikit-learn"],
        "Modeling": ["LSTM", "Random Forest", "MLP", "KNN"],
        "Visualization": ["Power BI", "Seaborn", "Matplotlib"],
        "Cloud & DB": ["Azure ML (exploratory)", "PostgreSQL"],
        "Soft Skills": ["Leadership", "Teamwork", "Storytelling", "Creative Thinking"]
    }
    for section, items in skills.items():
        st.markdown(f"#### 🔸 {section}")
        st.markdown(" | ".join([f"`{item}`" for item in items]))

# Tab 4 - Certifications
with tab4:
    st.markdown("## 📜 Certifications")
    st.success("• Python for Data Science and Machine Learning (Udemy)")
    st.success("• Complete SQL Masterclass (Udemy)")

# Tab 5 - Testimonials
with tab5:
    st.markdown("## 💬 Testimonials")
    quotes = [
        "“Tushar was incredibly resourceful during our data project. His forecasting improved accuracy by 18%.“ – Team Lead",
        "“Excellent dashboard builder. Our insights report became 10x easier to digest.“ – Business Analyst",
        "“Rare blend of data skills and storytelling. Highly recommended.“ – Peer Reviewer"
    ]
    for q in quotes:
        st.success(q)
        time.sleep(1.2)

# Tab 6 - Contact
with tab6:
    st.markdown("## 📬 Contact Me")
    with st.form("contact_form"):
        name = st.text_input("Name")
        email = st.text_input("Email")
        message = st.text_area("Message")
        submitted = st.form_submit_button("Send")
        if submitted:
            st.success("✅ Message Sent! (Pretend API)")

st.markdown("---")
st.caption("⚡ Built with ❤️ using Streamlit | © 2025 Tushar Dasgupta")
