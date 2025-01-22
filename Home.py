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
    Greetings! My name is Yosefi Kroytoro,\n
    and I’m a results-driven DevOps engineer with a talent for turning complex challenges into seamless solutions.\n
    I specialize in automation and integrating complex software components to streamline workflows and enhance efficiency.\n
    Additionally, I excel in monitoring software systems and implementing effective alerting mechanisms to ensure reliability and performance.\n
    I have a B.Sc. in Computer science, Cybersecurity Program, from the open university,\n
    and a degree in Practical Engineering, Electronics and Computers.\n
    Fast learner of new technologies, highly motivated to learn. Have the ability to learn fast and on my own.\n
    Excellent interpersonal skills, diligence, adaptable, innovative, and committed to delivering exceptional results.\n
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
