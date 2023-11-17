import streamlit as st
import pandas as pd
import numpy as np
import lib.db as db
import time

import elements.sidebar_filter as sidebar
import elements.loader_progress_bar as lb
import altair as alt
import elements.country_map as cp

loadBar = lb.LoadBarProgress()
country_map = cp.CountyMap()

st.set_page_config(layout="wide")
# st.set_page_config(

st.markdown("TikTok")
st.sidebar.markdown("TikTok Shorts Filters")

# create filters
filters = sidebar.LeftFilters()
filters.print_filters()


tab1, tab2 = st.tabs(["Creation", "Regions"])

with tab1:
    st.header("Creations")

    loadBar.run_progress()

    with st.container():
        col1, col2, col3 = st.columns(3)
        col1.metric("Creations", "12.7M", "1.2M (10%)")
        col2.metric("Avg. Views Per Creation", "1.621", "-0.32 (-2%)")
        col3.metric("Avg. Shares Per Creation", "7", "+1 (13%)")
    with st.container():
        left_column, right_column = st.columns(2)
        with left_column:
            st.write('Creations')
            chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["Creations", "Views", "Shares"])
            st.line_chart(chart_data)
        with right_column:
            st.write('Top Songs By Creations')
            df = pd.DataFrame(np.random.randn(10, 5), columns=("col %d" % i for i in range(5)))
            st.table(df)

    with st.container():
        left_column2, right_column2 = st.columns(2)
        with left_column2:
            st.write('Top 10 Artists')
            source = pd.DataFrame({"category": ['Artist 1', 'Artist 2', 'Artist 3',
                                                'Artist 4', 'Artist 5', 'Artist 6'], "value": [4, 6, 10, 3, 7, 8]})
            chart = alt.Chart(source).mark_arc(innerRadius=50).encode(
                theta=alt.Theta(field="value", type="quantitative"),
                color=alt.Color(field="category", type="nominal"),
            )
            st.altair_chart(chart, theme=None, use_container_width=True)
        with right_column2:
            st.write('Top Artists By Creations')
            df2 = pd.DataFrame(np.random.randn(10, 5), columns=("col %d" % i for i in range(5)))
            st.table(df2)


with tab2:
    st.header("Ranking")
    loadBar.run_progress()

    with st.container():
        col1, col2, col3 = st.columns(3)
        col1.metric("Creations", "12.7M", "1.2M (10%)")
        col2.metric("Views", "20.12B", "-2B (-2%)")
        col3.metric("Total Shares Per. View", "7", "+1 (13%)")

    with st.container():
        left_column, right_column = st.columns(2)
        with left_column:
            country_map.print_map()
        with right_column:
            st.write('Top Songs By Creations')
            df = pd.DataFrame(np.random.randn(10, 5), columns=("col %d" % i for i in range(5)))
            st.table(df)

    with st.container():
        left_column, right_column = st.columns(2)
        with left_column:
            st.write('Creations')
            chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["Creations", "Views", "Shares"])
            st.line_chart(chart_data)
        with right_column:
            st.write('Top Songs By Creations')
            df = pd.DataFrame(np.random.randn(10, 5), columns=("col %d" % i for i in range(5)))
            st.table(df)


    with st.container():
        left_column, right_column = st.columns(2)
        with left_column:
            st.write('Top Songs By Creations')
            df = pd.DataFrame(np.random.randn(10, 5), columns=("col %d" % i for i in range(5)))
            st.table(df)
        with right_column:
            st.write('Top 10 Artists')
            source = pd.DataFrame({"category": ['Artist 1', 'Artist 2', 'Artist 3',
                                                'Artist 4', 'Artist 5', 'Artist 6'], "value": [4, 6, 10, 3, 7, 8]})
            chart = alt.Chart(source).mark_arc(innerRadius=50).encode(
                theta=alt.Theta(field="value", type="quantitative"),
                color=alt.Color(field="category", type="nominal"),
            )
            st.altair_chart(chart, theme=None, use_container_width=True)

