import streamlit as st
from send_email import send_email

st.title('Contact Me')

with st.form(clear_on_submit=True, key='form'):
    email = st.text_input('Email address')
    raw_message = st.text_area('Message')
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
            st.info('Your message has been sent successfully. We will get in touch with you as soon as possible')
        else:
            st.error('Please provide an email address and a message')
