# File: app.py
"""
Streamlit application for data processing demonstration.

This module provides a simple web interface for loading and processing CSV data
using Streamlit framework.
"""

import streamlit as st
import pandas as pd
from modules.data_loader import load_data
from modules.data_processor import process_data


def main():
    """
    Main function that runs the Streamlit application.
    
    This function creates a Streamlit web interface that:
    1. Displays a title for the application
    2. Loads data from a CSV file
    3. Processes the loaded data
    4. Displays the processed data in the web interface
    
    Returns:
        None
    """
    st.title("Streamlit Demo with Repeated Modules")
    
    data = load_data('data/data.csv')
    processed_data = process_data(data)
    
    st.write("Processed Data:")
    st.write(processed_data)


if __name__ == "__main__":
    main()