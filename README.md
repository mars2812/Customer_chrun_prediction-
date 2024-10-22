**Customer Churn Prediction App**
This project is a web-based application built using Python and Streamlit to predict customer churn (i.e., whether a customer is likely to leave a service or business). The app allows users to input various customer features and returns a prediction of whether the customer will churn based on a machine learning model. Additionally, the app includes sections for model evaluation, feedback collection, and contact information

**Features**
1. Predict Customer Churn
•	Users can input customer details such as Credit Score, Age, Tenure, Estimated Salary, Geography, Gender, Credit Card Status, and Active Membership.
•	The app predicts whether a customer will churn using a pre-trained machine learning model.
•	Results are displayed with color-coded messages (green for no churn, red for likely churn).
2. Model Evaluation
•	Users can view the confusion matrix and classification report to understand the model's performance.
•	The app displays evaluation metrics on the original dataset used to train the model.
•	Users can also view individual predictions with color-coded results.
3. Feedback Collection
•	Users can provide feedback on the app, which is saved for further analysis and improvements.
4. Contact Us
•	Users can send messages, which are stored in a file for follow-up.

**Technologies Used**

•	Python: Core language used for data manipulation and building the app.
•	Streamlit: Framework for building the web interface and deploying the app.
•	Scikit-learn: Machine learning library used to build the churn prediction model.
•	Matplotlib & Seaborn: Used for visualizing evaluation metrics.
•	Pandas: Data manipulation and input handling.
•	Pickle: Used to load the pre-trained machine learning model.


**How It Works**

Input Fields
•	Credit Score: An integer between 300 and 850.
•	Age: An integer between 18 and 100.
•	Tenure: A number between 0 and 10 representing how many years the customer has been with the company.
•	Estimated Salary: A floating point number representing the estimated salary of the customer.
•	Geography: One of Germany or Spain (one-hot encoded).
•	Gender: Male or Female (one-hot encoded).
•	Has Credit Card: Whether the customer has a credit card (Yes/No).
•	Is Active Member: Whether the customer is an active member (Yes/No).

**Model Prediction**

•	The input data is passed through the pre-trained machine learning model, and a prediction is made.
•	If the model predicts 1, the customer is likely to churn. If 0, the customer is not likely to churn.
•	The result is displayed in a color-coded message (green for no churn, red for likely churn).

**Model Evaluation**

•	Displays the confusion matrix and classification report to evaluate the model's performance on the dataset.
•	Allows users to see the first 5 predictions and their respective results.

**Feedback & Contact**

•	Users can submit feedback or contact details, which are stored locally in text files.

**Installatio**

1.	Clone the repository:
        git clone https://github.com/yourusername/Customer-Churn-Prediction-App.git
2.	Navigate to the project directory:
       cd Customer-Churn-Prediction-App
3.	Install the required dependencies:
       pip install -r requirements.txt
4.	Run the app:
       streamlit run app.py


**Dataset**

The dataset used for training the model includes various customer features such as credit score, age, tenure, and others, with the target variable being whether the customer exited (churned) or not.
•	Input Features:
o	CreditScore, Age, Tenure, Balance, NumOfProducts, HasCrCard, IsActiveMember, EstimatedSalary, Geography_Germany, Geography_Spain, Gender_Male.
•	Target Variable:
o	Exited: 1 for churn, 0 for no churn.

**Model**

The model used for this project is a machine learning classification model trained using Scikit-learn. It is serialized using pickle and loaded in the app for prediction purposes.
Files
•	app.py: The main file that contains the Streamlit code for the web app.
•	Customer_Churn_Prediction.pkl: The pre-trained machine learning model serialized using pickle.
•	requirements.txt: The file containing all necessary libraries and dependencies.
•	feedback.txt: Stores user feedback.
•	contact_messages.txt: Stores user messages from the 'Contact Us' section.

**Future Enhancements**

•	Adding more customer features for input.
•	Improving model performance by tuning hyperparameters or using advanced algorithms.
•	Deploying the app on a cloud platform like Heroku or AWS.

**Screenshots**

1. Prediction Page
   
![Screenshot 2024-10-22 221152](https://github.com/user-attachments/assets/de97b326-40c7-418b-bf71-e6c10e9b60f5)


2. Model Evaluation
   
![Screenshot 2024-10-22 221209](https://github.com/user-attachments/assets/c5a72d5a-164d-4f46-96da-cbda95d468a3)


3. Feedback Section

![Screenshot 2024-10-22 221222](https://github.com/user-attachments/assets/e9492d70-786b-495b-85f4-3b788d64882a)

4. Contact Us

![Screenshot 2024-10-22 221235](https://github.com/user-attachments/assets/70fea60d-8bcb-4407-ac45-9a6762b64201)




**License**

This project is licensed under the MIT License.
Contact
If you have any questions or suggestions, feel free to contact me:
•	Email: dhamalamilan4242@example.com



