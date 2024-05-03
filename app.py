import yaml
import streamlit_authenticator as stauth
import streamlit as st
from streamlit_option_menu import option_menu
from src.generate_proposal_3 import generate_proposal
from streamlit_extras.app_logo import add_logo
import base64
from yaml.loader import SafeLoader
with open('config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)


st.set_page_config(
    layout="centered"
)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    #config['preauthorized']
)

st.sidebar.image(r"./synoptek-new-removebg-3.png")

if "name" not in st.session_state:
    st.session_state.name=None

if "authentication_status" not in st.session_state:
    st.session_state.authentication_status=None

if "username" not in st.session_state:
    st.session_state.username=None

# Authentication
name, authentication_status, username = authenticator.login('Login', 'main')

if st.session_state["authentication_status"]:
    st.sidebar.markdown(f'## Hello *{st.session_state["name"]}*')
    # st.sidebar.markdown('### Welcome to Synoptek Professional Proposal Generator !! 🍁"')
    authenticator.logout('Logout', 'sidebar')
    
    # --- APP ---
    with st.sidebar:
        selected = option_menu(
            menu_title="Project AIMS",
            options = ['Proposal Generator'],
            icons = ['gear-fill'],
            orientation="vertical",
            
        )
        
        
    # operation
    if selected == "Proposal Generator":
        generate_proposal()
    else:
        pass

elif st.session_state["authentication_status"] == False:
    st.error('Username/password is incorrect')
elif st.session_state["authentication_status"] == None:
    st.warning('Please enter your username and password')
