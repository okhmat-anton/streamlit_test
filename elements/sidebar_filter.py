import streamlit as st

class LeftFilters:
    def print_filters(self):
        # Add a slider to the sidebar:
        # add_slider = st.sidebar.slider(
        #     'Select a range of values',
        #     0.0, 100.0, (25.0, 75.0)
        # )

        # Add a selectbox to the sidebar:
        add_selectbox = st.sidebar.selectbox('Period  of data:',(
            'Today',
            'Yesterday',
            'Last month',
            'Previous month',
            'Last Year',
            'Previous Year',
            'All Data',
        ))
        # st.sidebar.write('You selected:', add_selectbox)

        add_multiselect = st.sidebar.multiselect(
            'Country:',
            ['USA', 'Canada', 'Mexico', 'Brasil'],
            [])

        # st.sidebar.write('You selected:', add_multiselect)

        add_multiselect = st.sidebar.multiselect(
            'ISRC:',
            ['123123123123', '123123213123', '12312312312', '123123123123'],
            [])

        add_multiselect = st.sidebar.multiselect(
            'Genre:',
            ['R&B', 'Rock', 'Club', 'Jazz'],
            [])

        add_multiselect = st.sidebar.multiselect(
            'Song:',
            ['Song 1', 'Song 2', 'Song 3', 'Song 4'],
            [])