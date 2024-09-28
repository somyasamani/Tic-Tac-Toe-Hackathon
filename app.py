from flask import Flask, request, render_template
import pandas as pd
import os

app = Flask(__name__)

# Define the path to the Excel file
FILE_PATH = r'C:\Users\somya\OneDrive\Desktop\Hackathon\registration.xlsx'

@app.route('/')
def registration_form():
    return render_template('registration.html')

@app.route('/register', methods=['POST'])
@app.route('/register', methods=['POST'])
def register():
    # Extract form data
    data = {
        'Name': request.form['name'],
        'Email': request.form['email'],
        'Phone': request.form['phone'],
        'Address': request.form['address'],
        'State': request.form['state'],  # Ensure this matches the form field
        'Date of Registration': request.form['dor'],
        'Registration No': request.form['regno']
    }

    # Print the form data for debugging purposes
    print("Form Data Received:", data)

    # Convert data to DataFrame
    df = pd.DataFrame([data])  # Make sure to wrap data in a list

    try:
        # Check if file exists
        if os.path.exists(FILE_PATH):
            print(f"File {FILE_PATH} exists. Appending data.")
            df_existing = pd.read_excel(FILE_PATH)
            df_combined = pd.concat([df_existing, df], ignore_index=True)
            df_combined.to_excel(FILE_PATH, index=False)
            print("Data appended successfully.")
        else:
            print(f"File {FILE_PATH} does not exist. Creating a new file.")
            df.to_excel(FILE_PATH, index=False)
            print("New Excel file created successfully.")

        print("Excel file updated successfully.")
    except Exception as e:
        print(f"Error occurred while writing to Excel: {e}")

    return "Registration successful!"

