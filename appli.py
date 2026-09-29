
import streamlit as st
from dotenv import load_dotenv
import os
from google import genai

# -----------------------------
# Load API Key
# -----------------------------
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Penguin AI",
    page_icon="🐧",
    layout="centered"
)

# -----------------------------
# Custom CSS
# -----------------------------
st.markdown("""
<style>

/* =========================
   MAIN BACKGROUND
========================= */

.stApp {
    background:
        linear-gradient(
            180deg,
            #050505 0%,
            #111111 45%,
            #1b1b1b 100%
        );

    min-height: 100vh;
    color: #ffffff;
}

/* =========================
   SNOWFLAKES
========================= */

.snow {
    position: fixed;
    top: -20px;
    color: white;
    font-size: 18px;
    opacity: 0.7;
    pointer-events: none;
    z-index: 1;
}

.snow1 {
    left: 5%;
    animation: snowfall1 9s linear infinite;
}

.snow2 {
    left: 15%;
    font-size: 13px;
    animation: snowfall2 12s linear infinite;
    animation-delay: 2s;
}

.snow3 {
    left: 28%;
    font-size: 22px;
    animation: snowfall1 11s linear infinite;
    animation-delay: 4s;
}

.snow4 {
    left: 42%;
    font-size: 14px;
    animation: snowfall2 10s linear infinite;
    animation-delay: 1s;
}

.snow5 {
    left: 57%;
    font-size: 20px;
    animation: snowfall1 13s linear infinite;
    animation-delay: 3s;
}

.snow6 {
    left: 70%;
    font-size: 15px;
    animation: snowfall2 9s linear infinite;
    animation-delay: 5s;
}

.snow7 {
    left: 82%;
    font-size: 23px;
    animation: snowfall1 12s linear infinite;
    animation-delay: 1s;
}

.snow8 {
    left: 94%;
    font-size: 14px;
    animation: snowfall2 10s linear infinite;
    animation-delay: 6s;
}

@keyframes snowfall1 {

    0% {
        transform: translateY(-30px) rotate(0deg);
        opacity: 0;
    }

    10% {
        opacity: 0.8;
    }

    50% {
        transform: translateY(50vh) translateX(30px) rotate(180deg);
    }

    100% {
        transform: translateY(110vh) translateX(-20px) rotate(360deg);
        opacity: 0;
    }
}

@keyframes snowfall2 {

    0% {
        transform: translateY(-30px) translateX(0);
        opacity: 0;
    }

    10% {
        opacity: 0.8;
    }

    50% {
        transform: translateY(50vh) translateX(-30px);
    }

    100% {
        transform: translateY(110vh) translateX(25px);
        opacity: 0;
    }
}

/* =========================
   MAIN CONTAINER
========================= */

.block-container {
    max-width: 760px;
    padding-top: 2rem;
    padding-bottom: 3rem;

    position: relative;
    z-index: 2;
}

/* =========================
   PENGUIN
========================= */

.penguin {
    text-align: center;

    font-size: 90px;

    margin-top: 10px;
    margin-bottom: 5px;

    animation: penguinFloat 3s ease-in-out infinite;

    filter:
        drop-shadow(
            0 10px 15px rgba(255,255,255,0.08)
        );
}

@keyframes penguinFloat {

    0% {
        transform: translateY(0);
    }

    50% {
        transform: translateY(-8px);
    }

    100% {
        transform: translateY(0);
    }
}

/* =========================
   TITLE
========================= */

.title {
    text-align: center;

    color: #ffffff;

    font-size: 42px;

    font-weight: 800;

    letter-spacing: 3px;

    margin-top: 5px;
    margin-bottom: 5px;

    text-shadow:
        0 3px 10px rgba(255,255,255,0.12);
}

/* =========================
   SUBTITLE
========================= */

.subtitle {
    text-align: center;

    color: #bdbdbd;

    font-size: 15px;

    margin-bottom: 20px;

    font-style: italic;
}

/* =========================
   SNOW LINE
========================= */

.snow-line {

    width: 80%;

    height: 2px;

    margin: 18px auto 25px auto;

    background:
        linear-gradient(
            90deg,
            transparent,
            #ffffff,
            #bdbdbd,
            #ffffff,
            transparent
        );

    opacity: 0.5;
}

/* =========================
   CHAT CARD
========================= */

.chat-card {

    background:
        linear-gradient(
            145deg,
            rgba(28,28,28,0.97),
            rgba(10,10,10,0.98)
        );

    border: 1px solid #383838;

    border-radius: 22px;

    padding: 28px;

    box-shadow:
        0 20px 50px rgba(0,0,0,0.55);

}

/* =========================
   LABELS
========================= */

label {

    color: #eeeeee !important;

    font-weight: 600 !important;

}

/* =========================
   TEXT AREA
========================= */

textarea {

    background-color: #080808 !important;

    color: #ffffff !important;

    border: 1px solid #444444 !important;

    border-radius: 15px !important;

    font-size: 16px !important;

    padding: 15px !important;

}

textarea::placeholder {

    color: #777777 !important;

}

textarea:focus {

    border: 2px solid #ffffff !important;

    box-shadow:
        0 0 15px rgba(255,255,255,0.12) !important;

}

/* =========================
   SELECT BOX
========================= */

div[data-baseweb="select"] > div {

    background-color: #0b0b0b !important;

    border: 1px solid #444444 !important;

    border-radius: 12px !important;

    color: white !important;

}

/* =========================
   BUTTON
========================= */

.stButton > button {

    width: 100%;

    border-radius: 15px;

    border: 1px solid #ffffff;

    padding: 13px;

    background:
        linear-gradient(
            90deg,
            #111111,
            #303030,
            #111111
        );

    color: white;

    font-size: 16px;

    font-weight: 700;

    letter-spacing: 1px;

    transition: 0.3s;

}

.stButton > button:hover {

    transform: translateY(-3px);

    background:
        linear-gradient(
            90deg,
            #ffffff,
            #dddddd,
            #ffffff
        );

    color: #111111;

    box-shadow:
        0 8px 25px rgba(255,255,255,0.15);

}

/* =========================
   RESPONSE TITLE
========================= */

.response-title {

    color: #ffffff;

    font-size: 18px;

    font-weight: 700;

    margin-top: 20px;

}

/* =========================
   RESPONSE BOX
========================= */

.gemini-response {

    background:
        linear-gradient(
            145deg,
            #151515,
            #090909
        );

    border: 1px solid #3d3d3d;

    border-left: 5px solid #ffffff;

    padding: 22px;

    border-radius: 15px;

    margin-top: 12px;

    color: #eeeeee;

    font-size: 16px;

    line-height: 1.8;

    box-shadow:
        0 10px 25px rgba(0,0,0,0.35);

}

/* =========================
   FOOTER
========================= */

.footer {

    text-align: center;

    color: #777777;

    font-size: 12px;

    margin-top: 30px;

}

</style>
""", unsafe_allow_html=True)


# -----------------------------
# Snowflakes
# -----------------------------

st.markdown(
    '<div class="snow snow1">❄</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="snow snow2">❅</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="snow snow3">❄</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="snow snow4">❅</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="snow snow5">❄</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="snow snow6">❅</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="snow snow7">❄</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="snow snow8">❅</div>',
    unsafe_allow_html=True
)


# -----------------------------
# Header
# -----------------------------

st.markdown(
    '<div class="penguin">🐧</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="title">PENGUIN AI</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'A tiny penguin is ready to answer your questions ❄️'
    '</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="snow-line"></div>',
    unsafe_allow_html=True
)


# -----------------------------
# Chat Card
# -----------------------------

st.markdown(
    '<div class="chat-card">',
    unsafe_allow_html=True
)


# -----------------------------
# Prompt
# -----------------------------

prompt = st.text_area(
    "🐧 Ask your penguin...",
    placeholder="What would you like to know?",
    height=150
)


# -----------------------------
# Mood
# -----------------------------

mood = st.selectbox(
    "❄️ Choose your penguin mood",
    [
        "🐧 Happy Penguin",
        "☕ Cozy Penguin",
        "❄️ Snowy Penguin",
        "🌙 Sleepy Penguin",
        "🤍 Friendly Penguin"
    ]
)


# -----------------------------
# Generate Response
# -----------------------------

if st.button("🐧 ASK THE PENGUIN"):

    if prompt:

        with st.spinner("🐧 The penguin is thinking..."):

            response = client.models.generate_content(
                model="gemini-3.5-flash-lite",
                contents=prompt
            )

        st.markdown(
            """
            <div class="response-title">
                🐧 Penguin says...
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            f'<div class="gemini-response">{response.text}</div>',
            unsafe_allow_html=True
        )

    else:

        st.warning(
            "🐧 The penguin is waiting for your question!"
        )


# -----------------------------
# Current Mood
# -----------------------------

st.markdown(
    f"""
    <div style="
        text-align:center;
        color:#777777;
        font-size:12px;
        margin-top:15px;
    ">
        🐧 Current mood: {mood}
    </div>
    """,
    unsafe_allow_html=True
)


# -----------------------------
# Close Card
# -----------------------------

st.markdown(
    '</div>',
    unsafe_allow_html=True
)


# -----------------------------
# Footer
# -----------------------------

st.markdown(
    '<div class="footer">'
    '🐧 Made with ❄️ and Gemini AI'
    '</div>',
    unsafe_allow_html=True
)

