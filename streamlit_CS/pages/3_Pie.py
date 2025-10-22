import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title
st.title("Pie Chart Viewer")

# Load CSV data
csv_file_path = 'data/pie_demo.csv'

try:
    df = pd.read_csv(csv_file_path)

    st.subheader("Raw Data")
    st.write(df)

    # Let user select columns
    with st.sidebar:
        st.header("Chart Settings")
        label_col = st.selectbox("Select label column", df.columns)
        value_col = st.selectbox("Select value column", df.columns)

    # Validate column data types
    if pd.api.types.is_numeric_dtype(df[value_col]):
        # Create Pie Chart
        fig, ax = plt.subplots()
        ax.pie(df[value_col], labels=df[label_col], autopct='%1.1f%%', startangle=90)
        ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

        st.subheader("Pie Chart")
        st.pyplot(fig)
    else:
        st.error("The selected value column must be numeric.")

except FileNotFoundError:
    st.error(f"CSV file not found at path: {csv_file_path}")
except Exception as e:
    st.error(f"An error occurred: {e}")
