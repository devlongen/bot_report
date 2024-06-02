# Import necessary libraries
import pandas as pd            # Library for data manipulation in dataframes
import openpyxl                # Library for working with Excel files
import psycopg2                # Library for connecting to and manipulating PostgreSQL databases
from datetime import datetime  # Library for working with dates and times
import os                      # Library for interacting with the operating system
import glob                    # Library for finding files with specified patterns
from googleapiclient.discovery import build   # Library for interacting with Google APIs
from google.oauth2.service_account import Credentials   # Library for authentication with Google service accounts
from googleapiclient.http import MediaFileUpload  # Library for uploading files to Google Drive

# Connect to PostgreSQL database
conn = psycopg2.connect(
    # Connection parameters should be specified here, such as dbname, user, password, host, port
)

cur = conn.cursor()  # Create a cursor to execute SQL commands
print("Connection established")

# SQL query (the desired query should be specified here)
query = """
    -- The SQL query should be inserted here
"""

cur.execute(query)  # Execute the SQL query
result = cur.fetchall()  # Fetch the query results
print("Query executed and fetched")

cur.close()  # Close the cursor
conn.close()  # Close the database connection
print("Database connection and cursor closed")

# Convert query results to a Pandas DataFrame
df = pd.DataFrame(result, columns=['name', 'contract_id', 'invoice_id', 'amount'])
print("File formatted for upload to drive")

# Get current date for naming the file
current_date = datetime.now()

# Save the DataFrame to an Excel file
df.to_excel(f'bot/BOT REPORT ({current_date.day:02d}.{current_date.month:02d}.{current_date.year}).xlsx', engine='openpyxl', header=True, index=False)
print("Exact date added to the file and converted to Excel.")

# Authenticate with Google Drive using the service account
credentials = Credentials.from_service_account_file(r'')
drive = build('drive', 'v3', credentials=credentials)
print("Credentials accepted")

# Identify the most recently modified file in the current folder
file_path = glob.glob("*")  # Search for all files in the current folder
latest_file = max(file_path, key=os.path.getatime)  # Select the most recently accessed/modified file
print("Fetching latest file")

# Prepare to upload the file to Google Drive
file_name = os.path.basename(latest_file)  # Get the file name
folder_id = ''  # ID of the Google Drive folder where the file will be stored (should be specified)
file_metadata = {'name': file_name, 'id': folder_id}  # File metadata for Google Drive
media = MediaFileUpload(latest_file, resumable=True)  # Prepare the file for upload

# Upload the file to Google Drive
file_drive = drive.files().create(body=file_metadata, media_body=media, fields='id').execute()
print("Check if uploaded to production")

# Grant read permission to anyone with the link
drive.permissions().create(fileId=file_drive['id'], body={'type': 'anyone', 'role': 'reader'}).execute()

# Credits to Iago Longen Mendonça, developer of this bot
print("Credits to Iago Longen Mendonça, developer of this bot")
