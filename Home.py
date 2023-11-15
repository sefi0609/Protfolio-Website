import streamlit as st
import pandas

st.set_page_config(layout='wide')

# data structure - ['title', 'description', 'url', 'image']
projects = pandas.read_csv('data.csv', sep=';')

col1, empty_col1, col2 = st.columns([1.5, 0.5, 1.5])

with col1:
    st.image('images/photo.jpg', width=400)

with col2:
    st.title('Yosefi Kroytoro')

    content = """I'm a computer science student at the open university, looking for a full time position.
        I'm working in a software company as a NOC operator, working with complex systems. 
        Acting as the first line of defence, collecting data, 
        responding to production issues and cyber attacks.
        In addition I provide technical support to company employees and our users.  
        I have a high self-learning ability as a student at the open university,
        can learn new technologies and program Languages on my own.
        Below you can find some of the apps I have built,
        Using GUIs, Web Frameworks, APIs, Threads, Data Bases, encryptions, Sockets and Binary Data.
        Feel free to contact me via contact page."""

    st.info(content)

# create two columns
col3, empty_col2, col4 = st.columns([1.5, 0.5, 1.5])

# half of the project in the right column and half in the left column
with col3:
    for index, row in projects[::2].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image(f'images/{row["image"]}')
        st.link_button('Source Code', row['url'])

with col4:
    for index, row in projects[1::2].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image(f'images/{row["image"]}')
        st.link_button('Source Code', row['url'])
