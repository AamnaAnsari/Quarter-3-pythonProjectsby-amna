import streamlit as st

st.set_page_config(page_title="Discord Bot Token UI", layout="centered")
st.title("🤖 Discord Bot Launcher")

token = st.text_input("🔐 Enter Your Discord Bot Token", type="password")

if st.button("💾 Save Token"):
    if token:
        with open("token.txt", "w") as f:
            f.write(token)
        st.success("✅ Token saved successfully! Now run your bot.")
    else:
        st.warning("Please enter a valid token.")
