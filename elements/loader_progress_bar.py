import streamlit as st
import time


class LoadBarProgress:
    def run_progress(self):
        with st.container():
            load_text = st.empty()
            load_text.text('Starting a long computation...')

            # Add a placeholder
            latest_iteration = st.empty()
            bar = st.progress(0)

            for i in range(100):
                # Update the progress bar with each iteration.
                latest_iteration.text(f'Iteration {i + 1}')
                bar.progress(i + 1)
                # time.sleep(0.01)

            bar.empty()
            latest_iteration.empty()
            load_text.empty()
