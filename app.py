import streamlit as st

st.set_page_config(page_title="🌟Growth Mindset Project")
st.title("Growth Mindset challenge: Web App with Streamlit")

st.header("🚀Welcome to Your Growth Journey")
st.write("This app is designed to help you cultivate a growth mindset through daily challenges, self-reflection, and progress tracking.Let's embark on this journey together! 🎯")

#quote section
st.header("today's Growth Mindset Qoute")
st.write("🎯 You are capable of amazing things if you believe in yourself.")

st.header(" 📌 What's your challenge Today?")
user_input = st.text_input("Describe a challenge you are facing.")

#condition
if user_input:
    st.success(f"you are facing: {user_input}. Keep pushing forward towards your goal!")
else:
    st.warning("Tell us about your challenge to get started!.")
    
    #reflexing
    st.header("Reflect on your learning")
    reflection = st.text_area("Write your relections here:")
    
    if reflection:
        st.success("Great insight! Your reflection: {reflection}")
    else:
        st.info("Write something about your learning experience! Share your difficulties")
        
        #achievements
        st.header("🏆 Celebrate your Achievements")  

# User Input for Achievements  
achievements = st.text_area("Learned something new 📖:")

if achievements:
    st.success("🎉 Keep it up! Your achievements are recorded.")
else:
    st.info("Write down what you've accomplished today, no matter how small! 🤝")
    
    #footer
    st.write("---")
    st.write("🌟 **Keep Growing, Keep Learning!** 🚀")
    st.write("© 2025 Growth Mindset Challenge. All rights reserved.")