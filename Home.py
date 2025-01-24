import streamlit as st
import pandas

st.set_page_config(layout='wide')

# data structure - ['title', 'description', 'url', 'image']
projects = pandas.read_csv('data.csv', sep=';')

col1, empty_col, col2 = st.columns([1.6, 0.2, 1.6], vertical_alignment='center')

with col1:
    st.image('images/photo.jpg')

with col2:
    st.title('Yosefi Kroytoro')

    content = """
    Greetings! My name is Yosefi Kroytoro,
    and I’m a results-driven DevOps engineer with a talent for turning complex challenges into seamless solutions.\n
    I specialize in automation and integrating complex software components to streamline workflows and enhance efficiency.\n
    Additionally, I excel in monitoring software systems and implementing effective alerting mechanisms to ensure reliability and performance.\n
    I have a B.Sc. in Computer science, Cybersecurity Program, from the open university,
    and a degree in Practical Engineering, Electronics and Computers.\n
    Fast learner of new technologies, highly motivated to learn. Have the ability to learn fast and on my own.\n
    Excellent interpersonal skills, diligence, adaptable, innovative, and committed to delivering exceptional results.\n
    """

    st.info(content)

# create two columns
col3, col4 = st.columns(2, border=True)

# half of the project in the right column and half in the left column
with col3:
    for index, row in projects[::2].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image(f'images/{row["image"]}')
        st.link_button('Source Code', row['url'])
        st.write("\n")

with col4:
    for index, row in projects[1::2].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image(f'images/{row["image"]}')
        st.link_button('Source Code', row['url'])
        st.write("\n")
