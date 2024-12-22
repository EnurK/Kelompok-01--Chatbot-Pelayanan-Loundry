import streamlit as st
import joblib

# --- Konfigurasi Halaman ---
st.set_page_config(page_title="Chatbot Laundry", page_icon="🧺", layout="centered")

# --- Load Model and Vectorizer ---
@st.cache_resource
def load_models():
    model = joblib.load("chatbot_model.pkl")
    return model

model = load_models()

# Tampilan Streamlit
st.title("💬 Chatbot Layanan Laundry")
st.markdown("Selamat datang di layanan chatbot laundry kami. Tanya apa saja tentang layanan kami!")

# Kotak obrolan
if 'messages' not in st.session_state:
    st.session_state['messages'] = []

# Fungsi untuk menguji chatbot
def test_chatbot(user_input):
    prediction = model.predict([user_input])
    return prediction[0]
# Input pengguna
with st.form("user_input_form"):
    user_input = st.text_input("Masukkan pesan Anda:", placeholder="Ketik sesuatu...")
    submitted = st.form_submit_button("Kirim")

if submitted and user_input:
    # Simpan pesan pengguna
    st.session_state['messages'].append({"user": user_input})
    
    # Dapatkan respons chatbot
    bot_response = test_chatbot(user_input)
    st.session_state['messages'].append({"bot": bot_response})

# Tampilkan obrolan
st.write("---")
st.markdown("### Obrolan")
for message in st.session_state['messages']:
    if "user" in message:
        st.markdown(
            f"<div style='text-align: right; color: blue;'>👤 *Anda*: {message['user']}</div>", 
            unsafe_allow_html=True
        )
    if "bot" in message:
        st.markdown(
            f"<div style='text-align: left; color: green;'>🤖 *Chatbot*: {message['bot']}</div>", 
            unsafe_allow_html=True
        )

# Bagian footer
st.write("---")
st.markdown("Dikembangkan oleh *Chatbot Laundry Services*")
