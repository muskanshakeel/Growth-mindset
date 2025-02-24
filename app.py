import streamlit as st
import random
import sqlite3
import datetime
from werkzeug.security import generate_password_hash, check_password_hash

# Author: Muskan Shakeel

# Database setup
def init_db():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users 
                 (id INTEGER PRIMARY KEY, username TEXT UNIQUE, password TEXT, created_at TEXT)''')
    c.execute('''CREATE TABLE IF NOT EXISTS feedback 
                 (id INTEGER PRIMARY KEY, name TEXT, email TEXT, message TEXT, submitted_at TEXT)''')
    c.execute('''CREATE TABLE IF NOT EXISTS journal 
                 (id INTEGER PRIMARY KEY, user TEXT, entry TEXT, date TEXT)''')
    c.execute('''CREATE TABLE IF NOT EXISTS goals 
                 (id INTEGER PRIMARY KEY, user TEXT, goal TEXT, status TEXT, created_at TEXT)''')
    conn.commit()
    conn.close()

# Initialize database
init_db()

# Growth quotes
growth_quotes = [
    "🌟 Success is not final, failure is not fatal: it is the courage to continue that counts. 🌟",
    "💡 Do not be embarrassed by your failures, learn from them and start again. 💡",
    "🔥 Believe you can and you're halfway there. 🔥",
    "🌱 Your mindset determines your success. 🌱"
]



# Sidebar Menu
menu = ["Home", "Login", "Signup", "Dashboard", "Motivational Videos", "Daily Challenges", 
        "Journal",  "Set Goals", "Progress Tracker", 
        "About", "Contact", "Feedback", "Gallery"]
choice = st.sidebar.selectbox("🌟 Menu", menu)
import streamlit as st
import random

# Session state for login
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False
    st.session_state["username"] = ""

if choice == "Home":
    # Adding a heading with style
    st.markdown("<h1 style='text-align: center; color: purple;'>🌸 Glow&Grow 🌸</h1>", unsafe_allow_html=True)
    
    # Welcome message with a little style
    st.markdown("<h3 style='color: #008080;'>🏠 Welcome to Growth Mindset By Muskan Shakeel 🌟</h3>", unsafe_allow_html=True)
    st.write(random.choice(growth_quotes))

    # Section with instructions on how to use the website
    st.markdown("""
        ### 🚀 **How to Use This Website:**
        - **Sign Up/Login** - Create an account to access all features.  
        - **Explore Dashboard** - Set goals, write journals, and track progress.  
        - **Watch Motivational Videos** - Get inspired daily.  
        - **Take Daily Challenges** - Improve your mindset step by step.  
        - **Read Success Stories** - Learn from real-life experiences.  
        - **Engage in Community** - Share feedback and connect with like-minded people.  
    """, unsafe_allow_html=True)
    
    # Adding background color to the instructions section
    st.markdown("""
    <style>
    .stMarkdown>div>p {
        background-color: #f0f8ff;
        padding: 10px;
        border-radius: 8px;
        font-weight: bold;
        font-size: 18px;
        box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Adding a fun animation (balloons effect) for engagement
    st.balloons()

    # Optional: Add a small image to enhance visual appeal
    st.image("https://64.media.tumblr.com/f9b772fc7c6fcae4c1a21a21f9eb6b53/597f9194e0f89e82-64/s500x750/46e16fe3efd43700c5c438c21d33fc52d0afa1e3.gifv", use_container_width=True)

    # Instructions to make it more dynamic
    st.markdown("""
        <h3 style="color: #008080; text-align:center;">✨ Explore, grow, and evolve with each passing day! ✨</h3>
    """, unsafe_allow_html=True)

# Login Page
elif choice == "Login":
    st.subheader("🔑 Login Page")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        c.execute("SELECT password FROM users WHERE username = ?", (username,))
        user = c.fetchone()
        conn.close()
        if user and check_password_hash(user[0], password):
            st.session_state["logged_in"] = True
            st.session_state["username"] = username
            st.success(f"🎉 Welcome back, {username}!")
        else:
            st.error("❌ Invalid username or password.")

# Signup Page
elif choice == "Signup":
    st.subheader("📝 Signup Page")
    username = st.text_input("Choose a username")
    password = st.text_input("Choose a password", type="password")
    if st.button("Signup"):
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        try:
            hashed_password = generate_password_hash(password)
            c.execute("INSERT INTO users (username, password, created_at) VALUES (?, ?, ?)", 
                      (username, hashed_password, str(datetime.datetime.utcnow())))
            conn.commit()
            st.success("🎉 Signup successful! Please log in.")
        except sqlite3.IntegrityError:
            st.error("⚠️ Username already exists!")
        conn.close()

# Dashboard Page
elif choice == "Dashboard":
    st.subheader("📊 Your Dashboard")
    if st.session_state["logged_in"]:
        st.success(f"🎉 Welcome, {st.session_state['username']}! Explore your growth journey.")
        st.image("https://img.freepik.com/free-photo/hands-holding-word-welcome_53876-21131.jpg", caption="Stay Motivated!")
        st.markdown("""
            ### 🚀 Features:
            - 🎯 **Set Goals** and track your progress.
            - 📓 **Write Journal Entries** to reflect on your growth.
            - 🎥 **Watch Motivational Videos** to stay inspired.
            - 🔥 **Take Daily Challenges** to push yourself forward.
            - 🌱 **Engage with the Community** for shared growth.
        """)
        st.markdown("""
            <style>
            @keyframes fadeIn {
                from { opacity: 0; }
                to { opacity: 1; }
            }
            .animated-text {
                animation: fadeIn 2s ease-in-out;
                font-size: 18px;
                font-weight: bold;
                color: #FF5733;
                text-align: center;
            }
            </style>
            <div class='animated-text'>Keep pushing forward! Your journey to growth starts now! 🚀</div>
        """, unsafe_allow_html=True)
    else:
        st.warning("🔐 Please login to access the dashboard.")

# Motivational Videos
elif choice == "Motivational Videos":
    st.subheader("🎥 Motivational Videos")
    video_urls = [
        "https://www.youtube.com/watch?v=ZXsQAXx_ao0",
        "https://www.youtube.com/watch?v=wnHW6o8WMas",
        "https://www.youtube.com/watch?v=mgmVOuLgFB0",
        "https://www.youtube.com/watch?v=fLJsdqxnZb0",
        "https://www.youtube.com/watch?v=26U_seo0a1g"
    ]
    for video in video_urls:
        st.video(video)
# Daily Challenges
elif choice == "Daily Challenges":
    st.subheader("🔥 Today's Challenge")
    challenges = [
        "Write down 3 things you are grateful for.", 
        "Exercise for 30 minutes.", 
        "Read 10 pages of a book.", 
        "Meditate for 10 minutes.",
        "Do a random act of kindness.",
        "Try a new skill for 15 minutes.",
        "Drink 8 glasses of water today.",
        "Avoid social media for an hour.",
        "Write a letter to your future self.",
        "Declutter your workspace or room."
    ]
    challenge_of_the_day = random.choice(challenges)
    st.write(f"🌟 **Challenge:** {challenge_of_the_day}")
    st.markdown("""
        <style>
        @keyframes slideIn {
            from { transform: translateX(-100%); opacity: 0; }
            to { transform: translateX(0); opacity: 1; }
        }
        .challenge-text {
            animation: slideIn 1.5s ease-in-out;
            font-size: 20px;
            font-weight: bold;
            color: #FFA500;
            text-align: center;
        }
        </style>
        <div class='challenge-text'>Take on the challenge and grow stronger every day! 💪</div>
    """, unsafe_allow_html=True)


# Journal Page
elif choice == "Journal":
    st.subheader("📓 Your Personal Journal")
    if st.session_state["logged_in"]:
        entry = st.text_area("Write your journal entry:")
        if st.button("Save Entry"):
            conn = sqlite3.connect('users.db')
            c = conn.cursor()
            c.execute("INSERT INTO journal (user, entry, date) VALUES (?, ?, ?)",
                      (st.session_state["username"], entry, str(datetime.datetime.utcnow())))
            conn.commit()
            conn.close()
            st.success("📝 Journal entry saved!")
    else:
        st.warning("🔐 Please login to write a journal.")

# Set Goals Page
elif choice == "Set Goals":
    st.subheader("🎯 Set Your Goals")
    st.markdown("<style>div.stButton > button {background-color: #FF5733; color: white; font-size: 16px;}</style>", unsafe_allow_html=True)
    if st.session_state["logged_in"]:
        goal = st.text_input("Enter your goal:")
        if st.button("💾 Save Goal"):
            conn = sqlite3.connect('users.db')
            c = conn.cursor()
            c.execute("INSERT INTO goals (user, goal, status, created_at) VALUES (?, ?, ?, ?)",
                      (st.session_state["username"], goal, "In Progress", str(datetime.datetime.utcnow())))
            conn.commit()
            conn.close()
            st.success("🎯 Goal Saved! Keep pushing forward!")
            st.snow()
    else:
        st.warning("🔐 Please login to set goals.")

# Progress Tracker
elif choice == "Progress Tracker":
    st.subheader("📊 Track Your Growth Progress")
    st.markdown("<style>div.stAlert {background-color: #ADD8E6; border-radius: 10px; padding: 10px;}</style>", unsafe_allow_html=True)
    if st.session_state["logged_in"]:
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        c.execute("SELECT goal, status FROM goals WHERE user = ?", (st.session_state["username"],))
        goals = c.fetchall()
        conn.close()
        if goals:
            for goal in goals:
                st.markdown(f"<div style='padding:10px; border-radius:10px; background:#90EE90;'><b>✅ Goal:</b> {goal[0]} | <b>Status:</b> {goal[1]}</div>", unsafe_allow_html=True)
        else:
            st.write("🚀 No goals set yet. Start your journey now!")
    else:
        st.warning("🔐 Please login to track progress.")

# About Page

elif choice == "About":
    st.subheader("📖 **About Growth Mindset Hub**")
    
    st.markdown("""
        <style>
        @keyframes fadeIn {
            0% { opacity: 0; transform: translateY(-10px); }
            100% { opacity: 1; transform: translateY(0); }
        }
        @keyframes glow {
            0% { text-shadow: 0 0 5px #00FF00; }
            50% { text-shadow: 0 0 15px #00FF00; }
            100% { text-shadow: 0 0 5px #00FF00; }
        }
        .glow-text {
            animation: glow 1.5s infinite alternate;
            font-size: 22px;
            font-weight: bold;
            color: #00FF00;
            text-align: center;
        }
        .fadeIn-text {
            animation: fadeIn 1.5s ease-out;
            font-size: 18px;
            text-align: center;
            color: white;
            background: linear-gradient(90deg, #0066FF, #00CCFF);
            padding: 10px;
            border-radius: 10px;
        }
        </style>
        
        <div class='glow-text'>💡 Unlock Your Potential, Achieve More! 🚀</div>
        <br>
        <div class='fadeIn-text'>Growth Mindset Hub is your personal space for self-improvement and motivation. 
        Our platform is built to help you develop a strong mindset, set goals, and stay inspired every day.</div>
        <br>
        <div class='fadeIn-text'>Join a community of achievers who believe in progress over perfection. 
        Start your journey today! 🌱</div>
    """, unsafe_allow_html=True)
# Feedback Page
elif choice == "Feedback":
    st.subheader("📝 **Share Your Feedback**")

    # Input Fields
    name = st.text_input("Name")
    email = st.text_input("Email")
    message = st.text_area("Your Feedback")

    # Button to submit feedback
    if st.button("🚀 Submit Feedback"):
        if name and email and message:  # Ensure fields are not empty
            conn = sqlite3.connect('users.db')
            c = conn.cursor()
            c.execute("INSERT INTO feedback (name, email, message, submitted_at) VALUES (?, ?, ?, ?)",
                      (name, email, message, str(datetime.datetime.utcnow())))
            conn.commit()
            conn.close()

            # Show success message
            st.success("🎉 Thank you for your feedback! Your voice matters. 🌟")

            # Happy Animation (Confetti Effect)
            st.markdown("""
                <style>
                @keyframes confetti {
                    0% { transform: translateY(0); opacity: 1; }
                    100% { transform: translateY(-50px); opacity: 0; }
                }
                .confetti {
                    position: absolute;
                    width: 10px;
                    height: 10px;
                    background: #FFD700;
                    border-radius: 50%;
                    animation: confetti 1s ease-out infinite;
                }
                .confetti:nth-child(2) { left: 20px; background: #FF4500; animation-delay: 0.2s; }
                .confetti:nth-child(3) { left: 50px; background: #00FF00; animation-delay: 0.4s; }
                .confetti:nth-child(4) { left: 80px; background: #0066FF; animation-delay: 0.6s; }
                .confetti:nth-child(5) { left: 110px; background: #FF1493; animation-delay: 0.8s; }
                </style>

                <div style="position: relative; height: 50px;">
                    <div class='confetti'></div>
                    <div class='confetti'></div>
                    <div class='confetti'></div>
                    <div class='confetti'></div>
                    <div class='confetti'></div>
                </div>
                <h3 style="text-align:center; color:#FFA500; animation: bounce 1s infinite;">
                    🎊 Your feedback makes us better! 🎊
                </h3>
            """, unsafe_allow_html=True)

        else:
            st.warning("⚠️ Please fill out all fields before submitting.")

# Contact Page
elif choice == "Contact":
    st.subheader("📞 Contact Us")
    name = st.text_input("Name")
    email = st.text_input("Email")
    message = st.text_area("Your Message")
    if st.button("Submit Message"):
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        c.execute("INSERT INTO feedback (name, email, message, submitted_at) VALUES (?, ?, ?, ?)",
                  (name, email, message, str(datetime.datetime.utcnow())))
        conn.commit()
        conn.close()
        st.success("Thank you for reaching out! We will get back to you soon. 🌟")
    st.write("Email: support@growthmindsethub.com")
    st.write("Follow us on social media for daily motivation!")
    st.markdown("[Instagram](https://instagram.com) | [Twitter](https://twitter.com) | [Facebook](https://facebook.com)")


# Gallery Page
elif choice == "Gallery":
    st.subheader("📸 Motivational Gallery")
    
    st.image("https://cdn.shopify.com/s/files/1/0070/7032/files/churchhill-quote.png?v=1706739710")
    st.image("https://media.istockphoto.com/id/1392896428/photo/inspirational-quote.jpg?s=612x612&w=0&k=20&c=CbqPLlx65768zd6QQpJqo55MZIAhA_o68cS0nLIfjw0=")
    st.image("https://cdn.shopify.com/s/files/1/0070/7032/files/steve-jobs-quote.png?v=1706740164")
    st.image("https://rukminim2.flixcart.com/image/850/1000/k7ry3680/wallpaper/z/a/a/30-45-motivational-quotes-wallpaper-m-106-hk-prints-original-imafccyyqevtwfzz.jpeg?q=90&crop=false")
    st.image("https://cdn-fkmoj.nitrocdn.com/xvpOGZRTxJUhXKufpOYIruQcRqtvAAQX/assets/images/optimized/rev-4e1f421/media.briantracy.com/blog/wp-content/uploads/2024/01/23111601/Quote-10-800x800.png")
    st.image("https://cdn-fkmoj.nitrocdn.com/xvpOGZRTxJUhXKufpOYIruQcRqtvAAQX/assets/images/optimized/rev-4e1f421/media.briantracy.com/blog/wp-content/uploads/2024/01/23111751/Quote-18-800x800.png")
    st.image("https://cdn-fkmoj.nitrocdn.com/xvpOGZRTxJUhXKufpOYIruQcRqtvAAQX/assets/images/optimized/rev-4e1f421/media.briantracy.com/blog/wp-content/uploads/2024/01/23111651/Quote-14-800x800.png")
    