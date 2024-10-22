import streamlit as st
import pandas as pd
import pickle
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix, classification_report
import numpy as np

# Load the trained model
with open('Customer_Churn_Prediction.pkl', 'rb') as file:
    model = pickle.load(file)

# Sample DataFrame for visualization (replace with your actual DataFrame)
np.random.seed(42)
df = pd.DataFrame({
    'CreditScore': np.random.randint(300, 850, size=1000),
    'Age': np.random.randint(18, 100, size=1000),
    'Tenure': np.random.randint(0, 10, size=1000),
    'Balance': np.random.uniform(0, 200000, size=1000),
    'NumOfProducts': np.random.randint(1, 5, size=1000),
    'HasCrCard': np.random.randint(0, 2, size=1000),
    'IsActiveMember': np.random.randint(0, 2, size=1000),
    'EstimatedSalary': np.random.uniform(0, 150000, size=1000),
    'Geography_Germany': np.random.randint(0, 2, size=1000),
    'Geography_Spain': np.random.randint(0, 2, size=1000),
    'Gender_Male': np.random.randint(0, 2, size=1000),
    'Exited': np.random.randint(0, 2, size=1000)  # Churn label
})

# Title of the app with background color and bold text
st.markdown(
    """
    <style>
    .title {
        background-color: #4CAF50; /* Green background color */
        padding: 10px;
        border-radius: 5px;
        text-align: center;
    }
    .title h1 {
        font-weight: bold; /* Make the title bold */
        color: white; /* Change text color to white for better contrast */
    }
    @media (max-width: 600px) {
        .title {
            font-size: 20px; /* Smaller title size for mobile */
        }
    }
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #4CAF50; /* Green background color */
        color: white; /* White text color */
        text-align: center;
        padding: 10px;
        font-size: 14px;
        font-weight: bold; /* Make text bold */
    }
    .footer p {
        color: black; /* Black text color */
        font-weight: bold; /* Make text bold */
    }
    </style>
    <div class="title">
        <h1>Customer Churn Prediction App</h1>
    </div>
    """,
    unsafe_allow_html=True
)

# Sidebar for navigation
st.sidebar.title('Navigation')
page = st.sidebar.selectbox("Choose a section:", ["Predict Customer Churn", "Model Evaluation", "Feedback", "Contact Us"])

if page == "Predict Customer Churn":
    # User inputs for the features
    col1, col2 = st.columns(2)

    with col1:
        credit_score = st.number_input('Credit Score', min_value=300, max_value=850, value=600)
        tenure = st.slider('Tenure (years)', 0, 10, 2)

    with col2:
        age = st.number_input('Age', min_value=18, max_value=100, value=30)
        estimated_salary = st.number_input('Estimated Salary', min_value=0.0, value=50000.0)

    # One-hot encoding for Geography
    geography = st.selectbox('Geography', ['Germany', 'Spain'])
    geography_germany = 1 if geography == 'Germany' else 0
    geography_spain = 1 if geography == 'Spain' else 0

    # One-hot encoding for Gender
    gender = st.selectbox('Gender', ['Male', 'Female'])
    gender_male = 1 if gender == 'Male' else 0

    # Convert Yes/No for HasCrCard and IsActiveMember to binary
    has_cr_card = st.selectbox('Has Credit Card', ['Yes', 'No'])
    has_cr_card_encoded = 1 if has_cr_card == 'Yes' else 0

    is_active_member = st.selectbox('Is Active Member', ['Yes', 'No'])
    is_active_member_encoded = 1 if is_active_member == 'Yes' else 0

    # Create a DataFrame for the model input in the correct order
    input_data = pd.DataFrame({
        'CreditScore': [credit_score],
        'Age': [age],
        'Tenure': [tenure],
        'Balance': [0.0],  # Placeholder, you can add a balance input if needed
        'NumOfProducts': [1],  # Placeholder, you can add a NumOfProducts input if needed
        'HasCrCard': [has_cr_card_encoded],
        'IsActiveMember': [is_active_member_encoded],
        'EstimatedSalary': [estimated_salary],
        'Geography_Germany': [geography_germany],
        'Geography_Spain': [geography_spain],
        'Gender_Male': [gender_male]
    })

    # Predict the outcome
if st.button('Predict'):
        # Make the prediction using the model
        prediction = model.predict(input_data)

        # Create the message based on the prediction
        if prediction[0] == 1:
            message = '<h3 style="color: red; font-weight: bold;">Customer is likely to churn.</h3>'
        else:
            message = '<h3 style="color: green; font-weight: bold;">Customer is not likely to churn.</h3>'

        # Use st.markdown to display the message with HTML
        st.markdown(message, unsafe_allow_html=True)

elif page == "Model Evaluation":
    st.subheader("Model Evaluation Metrics")

    # Predict on the original dataset for evaluation
    y_true = df['Exited']
    y_pred = model.predict(df.drop('Exited', axis=1))  # Predict on the original dataset
    cm = confusion_matrix(y_true, y_pred)

    st.write("Confusion Matrix:")
    st.write(cm)
    st.write("Classification Report:")
    st.text(classification_report(y_true, y_pred))

    # Display prediction results in bold with color for evaluation
    if st.button('Display Evaluation Predictions'):
        for i in range(5):  # Display the first 5 predictions
            prediction_message = ""
            if y_pred[i] == 1:
                prediction_message = f'<h3 style="color: red; font-weight: bold;">Customer {i+1} is likely to churn.</h3>'
            else:
                prediction_message = f'<h3 style="color: green; font-weight: bold;">Customer {i+1} is not likely to churn.</h3>'

            st.markdown(prediction_message, unsafe_allow_html=True)

elif page == "Feedback":
    # User feedback section
    st.subheader("Feedback")
    feedback = st.text_area("Please provide your feedback:")
    if st.button("Submit Feedback"):
        if feedback:
            # Store feedback in a text file
            with open("feedback.txt", "a") as f:
                f.write(feedback + "\n")  # Append feedback to the file
            st.success("Thank you for your feedback!")
        else:
            st.warning("Please enter your feedback before submitting.")

elif page == "Contact Us":
    st.subheader("Contact Us")
    
    # Contact Form
    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    message = st.text_area("Your Message")

    if st.button("Send Message"):
        if name and email and message:
            # Store the message in a text file
            with open("contact_messages.txt", "a") as f:
                f.write(f"Name: {name}\nEmail: {email}\nMessage: {message}\n\n")  # Append the message to the file
            st.success("Thank you for your message! We will get back to you soon.")
        else:
            st.warning("Please fill in all fields before sending.")

# Footer
st.markdown(
    """
    <style>
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #4CAF50; /* Green background color */
        color: white; /* White text color */
        text-align: center;
        padding: 10px;
        font-size: 14px;
        font-weight: bold; /* Make text bold */
    }
    .footer p {
        color: black; /* Black text color */
        font-weight: bold; /* Make text bold */
    }
    </style>
    <div class="footer">
        <p>© 2024 Matrika Dhamala - Customer Churn Prediction App | <a href="mailto:dhamalamilan4242@example.com" style="color: yellow;">Contact Us</a></p>
    </div>
    """,
    unsafe_allow_html=True
)