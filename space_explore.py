
import streamlit as st
import pandas as pd

# --------------------------------
# PAGE CONFIGURATION
# --------------------------------
st.set_page_config(
    page_title="Space Explorer Adventure 🚀",
    page_icon="🚀",
    layout="wide"
)

# --------------------------------
# SPACE THEME CSS
# --------------------------------
st.markdown("""
<style>
/* Main background */
.stApp {
    background: linear-gradient(
        135deg,
        #05051a,
        #101038,
        #1b1045,
        #080820
    );
    color: white;
}

/* Main headings */
h1, h2, h3 {
    color: #b9a5ff !important;
    text-shadow: 0px 0px 15px #815cff;
}

/* Paragraph text */
p, label, .stMarkdown {
    color: #e6e6ff;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background: linear-gradient(
        180deg,
        #100b30,
        #21104b,
        #080820
    );
    border-right: 2px solid #7655ff;
}

/* Buttons */
.stButton > button {
    background: linear-gradient(90deg, #713cff, #00cfff);
    color: white;
    border: none;
    border-radius: 12px;
    padding: 10px 25px;
    font-weight: bold;
    box-shadow: 0px 0px 15px #7655ff;
    transition: 0.3s;
}

.stButton > button:hover {
    transform: scale(1.05);
    box-shadow: 0px 0px 25px #00cfff;
    color: white;
}

/* Input fields */
.stTextInput input {
    background-color: #171735;
    color: white;
    border: 1px solid #7655ff;
}

div[data-baseweb="select"] {
    background-color: #171735;
}

/* Radio buttons */
.stRadio {
    background-color: rgba(100, 70, 180, 0.12);
    padding: 12px;
    border-radius: 10px;
}

/* Data table */
[data-testid="stTable"] {
    background-color: #171735;
}

/* Horizontal divider */
hr {
    border-color: #7655ff;
}

/* Info boxes */
.stAlert {
    border-radius: 12px;
}
</style>
""", unsafe_allow_html=True)


# --------------------------------
# APP TITLE
# --------------------------------
st.title("🚀 SPACE EXPLORER ADVENTURE")
st.caption("✨ Discover the Universe | Explore the Unknown | Beyond the Stars")
st.markdown("---")


# --------------------------------
# SIDEBAR NAVIGATION
# --------------------------------
st.sidebar.title("🌌 SPACE STATION")
st.sidebar.markdown("### 🛸 Navigation")

choice = st.sidebar.radio(
    "Choose your destination:",
    ["Home", "Space Quiz", "Mission Planner"]
)

st.sidebar.markdown("---")
st.sidebar.info("🌠 Your journey through the universe begins here!")


# --------------------------------
# HOME SECTION
# --------------------------------
if choice == "Home":

    st.header("🌌 Welcome to Space Explorer Adventure!")

    st.markdown("""
    ### 👨‍🚀 Greetings, Space Explorer!

    Welcome aboard your interstellar adventure!

    Prepare yourself to travel beyond Earth and discover
    the mysteries of the universe.

    ---

    ### 🪐 Your Space Missions

    🚀 **Space Quiz**  
    Test your knowledge about planets, galaxies and astronauts.

    🛰️ **Mission Planner**  
    Create your own spacecraft and schedule your space mission.

    🌟 **Explore the Unknown**  
    Discover the wonders of the universe!

    ---
    """)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("🌍 Home Planet", "Earth")

    with col2:
        st.metric("🪐 Solar System", "8 Planets")

    with col3:
        st.metric("🌌 Destination", "Universe")

    st.success("🚀 Mission Control is ready. Let's explore space!")


# --------------------------------
# SPACE QUIZ SECTION
# --------------------------------
elif choice == "Space Quiz":

    st.header("🧑‍🚀 Test Your Space Knowledge")
    st.write("🌟 Answer these questions and prove you're a space expert!")

    st.markdown("---")

    q1 = st.radio(
        "🪐 Q1: What is the largest planet in our solar system?",
        ["Earth", "Jupiter", "Mars"],
        key="q1"
    )

    q2 = st.radio(
        "👨‍🚀 Q2: Who was the first human to travel into space?",
        ["Neil Armstrong", "Buzz Aldrin", "Yuri Gagarin"],
        key="q2"
    )

    q3 = st.radio(
        "🌌 Q3: What galaxy do we live in?",
        ["Milky Way Galaxy", "Andromeda Galaxy", "Whirlpool Galaxy"],
        key="q3"
    )

    st.markdown("---")

    if st.button("🚀 Submit Quiz"):

        score = 0

        score += 1 if q1 == "Jupiter" else 0
        score += 1 if q2 == "Yuri Gagarin" else 0
        score += 1 if q3 == "Milky Way Galaxy" else 0

        st.success(f"🎉 Your Space Quiz Score: {score}/3")

        if score == 3:
            st.balloons()
            st.success("🌟 Excellent! You're a Space Genius!")

        elif score == 2:
            st.info("🪐 Great work! You're almost a Space Expert!")

        else:
            st.warning("🚀 Keep exploring! You'll become a Space Expert!")

        results = pd.DataFrame({
            "Question": ["Q1", "Q2", "Q3"],
            "Your Answer": [q1, q2, q3],
            "Correct Answer": [
                "Jupiter",
                "Yuri Gagarin",
                "Milky Way Galaxy"
            ]
        })

        st.subheader("📊 Your Mission Results")
        st.table(results)


# --------------------------------
# MISSION PLANNER SECTION
# --------------------------------
elif choice == "Mission Planner":

    st.header("🛰️ Plan Your Space Mission")

    st.write("🌠 Customize your spacecraft and prepare for launch!")

    st.markdown("---")

    spacecraft = st.text_input(
        "🚀 Name your spacecraft:",
        "Star Explorer"
    )

    launch_date = st.date_input(
        "📅 Select your mission launch date:"
    )

    launch_time = st.time_input(
        "⏰ Select your mission launch time:"
    )

    spaceship_type = st.selectbox(
        "🛸 Choose your spaceship type:",
        ["Rocket", "Shuttle", "Space Station"]
    )

    category = st.selectbox(
        "🌟 Choose your mission inspiration:",
        ["Exploration", "Discovery", "Adventure"]
    )

    quotes = {
        "Exploration": "To explore the universe is to explore ourselves.",
        "Discovery": "Discovery is seeing what everybody else has seen, and thinking what nobody else has thought.",
        "Adventure": "Space is an adventure worth taking."
    }

    st.info(f"✨ Motivational Quote: '{quotes[category]}'")

    st.markdown("---")

    if st.button("🚀 Launch Mission Plan"):

        if spacecraft.strip():

            st.success(
                f"🌌 Mission '{spacecraft}' scheduled for "
                f"{launch_date} at {launch_time} "
                f"with a {spaceship_type}!"
            )

            st.balloons()

            st.subheader("🛰️ Mission Summary")

            st.write(f"🚀 **Spacecraft:** {spacecraft}")
            st.write(f"📅 **Launch Date:** {launch_date}")
            st.write(f"⏰ **Launch Time:** {launch_time}")
            st.write(f"🛸 **Spaceship:** {spaceship_type}")
            st.write(f"🌟 **Mission Type:** {category}")

        else:
            st.error("⚠️ Please enter a spacecraft name!")


# --------------------------------
# FOOTER
# --------------------------------
st.markdown("---")

st.markdown(
    "<center>🌌 Made with ❤️ for Space Explorers | "
    "Keep Looking Beyond the Stars 🚀</center>",
    unsafe_allow_html=True
)
