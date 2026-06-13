import streamlit as st
from youtube_video_analyzer import analyze_agent

st.set_page_config(
    page_title="Youtube Video Analyzer",
    layout="centered"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');

html, body, [data-testid="stAppViewContainer"] {
    background: #0d0d14;
    font-family: 'Inter', sans-serif;
    color: #e2e8f0;
}
[data-testid="stAppViewContainer"] > .main { background: #0d0d14; }
#MainMenu, footer { visibility: hidden; }

/* Title */
h1 { color: #fff !important; font-weight: 700 !important; }

/* Text input */
[data-testid="stTextInput"] input {
    background: #1a1a2e !important;
    border: 1.5px solid #4f46e5 !important;
    border-radius: 10px !important;
    color: #e2e8f0 !important;
    padding: 0.65rem 1rem !important;
}
[data-testid="stTextInput"] input:focus {
    border-color: #818cf8 !important;
    box-shadow: 0 0 0 3px rgba(129,140,248,0.2) !important;
}

/* Button */
[data-testid="stButton"] > button {
    background: linear-gradient(135deg, #4f46e5, #7c3aed) !important;
    color: #fff !important;
    border: none !important;
    border-radius: 10px !important;
    font-weight: 600 !important;
    padding: 0.6rem 1.6rem !important;
    width: 100% !important;
    transition: opacity 0.2s !important;
}
[data-testid="stButton"] > button:hover { opacity: 0.85 !important; }

/* Spinner text */
[data-testid="stSpinner"] p { color: #a5b4fc !important; }

/* Markdown output area */
[data-testid="stMarkdown"] p, [data-testid="stMarkdown"] li {
    color: #cbd5e1 !important;
    line-height: 1.75 !important;
}
[data-testid="stMarkdown"] h1,
[data-testid="stMarkdown"] h2,
[data-testid="stMarkdown"] h3 { color: #f1f5f9 !important; }
[data-testid="stMarkdown"] code {
    background: rgba(129,140,248,0.15) !important;
    color: #a5b4fc !important;
    border-radius: 5px !important;
    padding: 0.1rem 0.4rem !important;
}

/* ── Background animation ── */

/* Slow-drift gradient backdrop */
@keyframes bgShift {
    0%   { background-position: 0% 50%; }
    50%  { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

[data-testid="stAppViewContainer"]::before {
    content: '';
    position: fixed;
    inset: 0;
    z-index: 0;
    pointer-events: none;
    background: linear-gradient(
        135deg,
        #0d0d14 0%,
        #110d22 30%,
        #0d1530 60%,
        #0d0d14 100%
    );
    background-size: 300% 300%;
    animation: bgShift 18s ease infinite;
}

/* Floating orbs */
@keyframes floatA {
    0%, 100% { transform: translate(0, 0) scale(1); }
    50%       { transform: translate(40px, -50px) scale(1.08); }
}
@keyframes floatB {
    0%, 100% { transform: translate(0, 0) scale(1); }
    50%       { transform: translate(-50px, 30px) scale(1.05); }
}
@keyframes floatC {
    0%, 100% { transform: translate(0, 0) scale(1); }
    50%       { transform: translate(30px, 40px) scale(1.06); }
}

[data-testid="stAppViewContainer"]::after {
    content: '';
    position: fixed;
    inset: 0;
    z-index: 0;
    pointer-events: none;
    /* Orb 1 — top-left indigo */
    background:
        radial-gradient(ellipse 480px 380px at 10% 15%,
            rgba(79, 70, 229, 0.13) 0%, transparent 70%),
        /* Orb 2 — bottom-right violet */
        radial-gradient(ellipse 420px 320px at 90% 85%,
            rgba(124, 58, 237, 0.11) 0%, transparent 70%),
        /* Orb 3 — center-top cyan accent */
        radial-gradient(ellipse 300px 240px at 55% 5%,
            rgba(99, 102, 241, 0.08) 0%, transparent 70%);
    animation: floatA 14s ease-in-out infinite;
}

/* Ensure all Streamlit content layers sit above the background */
[data-testid="stAppViewContainer"] > .main,
[data-testid="stHeader"],
section[data-testid="stSidebar"] {
    position: relative;
    z-index: 1;
    background: transparent !important;
}

/* Keep the output block readable — solid dark card */
[data-testid="stMarkdown"]:has(> p),
[data-testid="stMarkdown"]:has(> h1),
[data-testid="stMarkdown"]:has(> h2),
[data-testid="stMarkdown"]:has(> h3),
[data-testid="stMarkdown"]:has(> ul),
[data-testid="stMarkdown"]:has(> ol) {
    background: rgba(13, 13, 20, 0.72) !important;
    backdrop-filter: blur(6px) !important;
    border-radius: 10px !important;
    padding: 0.6rem 0.9rem !important;
}
</style>

""", unsafe_allow_html=True)

st.title("🎥 AI Youtube Video Analyzer")

@st.cache_resource
def get_agent():
    return analyze_agent()


agent = get_agent()

# input box
video_url = st.text_input("Enter Youtube Video Link") # str
button = st.button("Analyze Video") # True/False

if video_url and button:
    with st.spinner("Analyzing video...."):
        response = agent.run(
            f"Analyze this video: {video_url}"
        )

    st.markdown("Analysis Report of Video:")
    st.markdown(response.content)