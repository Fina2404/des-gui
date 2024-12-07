import streamlit as st
from Crypto.Cipher import DES
import base64

# Padding function for DES
def pad(text):
    while len(text) % 8 != 0:
        text += ' '
    return text

# Encryption function
def encrypt(plain_text, key):
    des = DES.new(key, DES.MODE_ECB)
    padded_text = pad(plain_text)
    encrypted_text = des.encrypt(padded_text.encode('utf-8'))
    return base64.b64encode(encrypted_text).decode('utf-8')

# Decryption function
def decrypt(encrypted_text, key):
    des = DES.new(key, DES.MODE_ECB)
    decoded_encrypted_text = base64.b64decode(encrypted_text)
    decrypted_text = des.decrypt(decoded_encrypted_text).decode('utf-8')
    return decrypted_text.rstrip()

# Streamlit page configuration
st.set_page_config(page_title="DES Encryption App by Fina Dwi Aulia", page_icon=":lock:")

# Custom style
st.markdown(
    """
    <style>
    .reportview-container {
        background-color: #f5f5f5;
        color: #4A4A4A;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Page title
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>DES Encryption & Auto Decryption</h1>", unsafe_allow_html=True)

# Input for encryption
st.subheader("Encrypt and Automatically Decrypt")
plain_text = st.text_input("Enter text to encrypt")
key_input = st.text_input("Enter a key (8 characters)", type="password")

# Display encryption and decryption result
if key_input:
    if len(key_input) == 8:
        key = key_input.encode('utf-8')
        encrypted_text = encrypt(plain_text, key) if plain_text else None
        decrypted_text = decrypt(encrypted_text, key) if encrypted_text else None
        
        if encrypted_text:
            st.success(f"Encrypted Message: {encrypted_text}")
        if decrypted_text:
            st.success(f"Decrypted Message: {decrypted_text}")
    else:
        st.error("Key must be exactly 8 characters!")
