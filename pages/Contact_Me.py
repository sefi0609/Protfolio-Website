import streamlit as st
from send_email import send_email

st.title('Contact Me')

with st.form(clear_on_submit=True, key='form'):
    email = st.text_input('Your email address')
    raw_message = st.text_area('Your message')
    button = st.form_submit_button('Submit')
    # arrange the message
    message = f"""\
Subject: from Portfolio website\n
From: {email}
{raw_message}
"""
    if button:
        # if submit button was pressed check if those fields are not empty
        if email != '' and raw_message != '':
            send_email(message)
            st.info('Your email was sent successfully')
        else:
            st.error('Please supply an email and message')
