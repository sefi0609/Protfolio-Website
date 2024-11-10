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

    content = """
    Site Reliability Engineer looking for a DevOps Engineer or SRE positions.
    B.Sc. in Computer science , Cybersecurity Program, from the open university,
    and a degree in Practical Engineering, Electronics and Computers.
    Fast learner of new technologies, highly motivated to learn. Have the ability to learn fast and on my own.
    Excellent interpersonal skills, diligence, ambition, and ability to troubleshoot complex problems.
    """

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
