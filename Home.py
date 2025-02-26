import streamlit as st
from src.logo_title import logo_title

# Page configuration
# st.set_page_config(page_title="Student Performance Dashboard", layout="wide")

st.set_page_config(layout="wide")
logo_title("Student Performance Dashboard")
# st.title("📊 Student Performance Dashboard")
st.markdown(
    """
    Welcome to the **Student Performance Dashboard**! 
    This intuitive and interactive multi-page application is designed to give you a 360-degree view of student performance. Dive into historical data, explore predictive analytics, and uncover meaningful trends—all in one place.

    ### Explore the Dashboard:
    
    - **Historical Data Analysis**: Unearth actionable insights through our detailed analysis. This page focuses on key performance metrics, temporal trends, and the distribution of students across performance categories like Advanced, Intermediate, and Basic.

    - **Prediction Data Analysis**: Delve into the world of predictions. This page compares predicted performance with historical and actual results, providing a forward-looking perspective on student outcomes.

    ### Key Features:
    - **Interactive Filters**: Tailor your analysis by applying custom filters for subjects, years, and months.
    - **Dynamic Insights**: Discover trends, averages, and distributions in an easy-to-understand format.
    - **Comprehensive Overview**: Navigate seamlessly between raw data, trends, and predictions to uncover the complete story.

    Use the sidebar to navigate through the pages and personalize your analysis to your needs. Whether you're an educator, analyst, or student, this dashboard is your ultimate companion for performance evaluation and improvement.
    """
)


