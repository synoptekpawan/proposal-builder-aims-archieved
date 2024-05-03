import streamlit_authenticator as stauth

hashed_passwords = stauth.Hasher(['test_user']).generate()

print(hashed_passwords)