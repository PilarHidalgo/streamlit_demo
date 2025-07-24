import streamlit as st
import pandas as pd
from modules.data_loader import load_data
from modules.data_processor import process_data


def main():

    st.title("Streamlit Demo with Repeated Modules")
    
    data = load_data('data/data.csv')
    processed_data = process_data(data)
    
    st.write("Processed Data:")
    st.write(processed_data)


if __name__ == "__main__":
    main()