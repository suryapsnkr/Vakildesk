import pandas as pd
import re

# Function to validate email format
def is_valid_email(email):
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None

# Read the CSV file
input_file = 'user_data.csv'  # Replace with your input CSV file name
output_file = 'cleaned_user_data.csv'  # Output CSV file name

try:
    # Load the data into a DataFrame
    df = pd.read_csv(input_file)

    # Remove duplicates based on 'user_id'
    df = df.drop_duplicates(subset='user_id')

    # Filter out rows with invalid email formats
    df = df[df['email'].apply(is_valid_email)]

    # Write the cleaned data to a new CSV file
    df.to_csv(output_file, index=False)

    print(f"Cleaned data has been written to {output_file}")

except Exception as e:
    print(f"An error occurred: {e}")
