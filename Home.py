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
    Greetings! My name is Yosefi Kroytoro, a results-driven DevOps Engineer passionate about automation, reliability, and seamless software integration. I thrive on solving complex challenges and optimizing workflows to enhance system efficiency and performance.\n
    With expertise in monitoring, alerting, and automation, I ensure robust and scalable infrastructures that keep businesses running smoothly.\n
    I hold a B.Sc. in computer science, cybersecurity program, from the Open University and a Practical Engineering degree in Electronics and Computers. A fast learner with a deep curiosity for emerging technologies, I quickly adapt to new tools and methodologies, continuously expanding my skill set.\n
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
