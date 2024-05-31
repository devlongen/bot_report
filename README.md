# Data Extraction and Upload Bot

## Overview
This bot automates the process of extracting data from a PostgreSQL database, transforming the data into an Excel file, and uploading the file to Google Drive. This README provides an overview of the technologies used, the bot's functionality, and its purpose.

## Technologies Used

1. **Python**: Main programming language used for the bot development due to its simplicity and powerful integration capabilities.

2. **Pandas**: Python library for data manipulation and analysis. It is used to convert the SQL query results into a DataFrame and export the data to an Excel file.

3. **Openpyxl**: Python library for working with Excel files. It is used to save the DataFrame data into an Excel file.

4. **Psycopg2**: PostgreSQL adapter for Python. It is used to connect to the database, execute SQL queries, and fetch the results.

5. **Datetime**: Python's standard library for handling dates and times. It is used to generate the current date for naming the Excel file.

6. **OS and Glob**: Python's standard libraries for interacting with the operating system. They are used to search and identify the most recently modified file in the working directory.

7. **Googleapiclient and Google.oauth2**: Google API libraries for interacting with Google Drive. They are used to authenticate with Google Drive and upload the file.

8. **PyDrive**: Library to simplify authentication and interaction with Google Drive. It is used as an alternative for Google Drive authentication and file management.

## How It Works

### 1. Connect to PostgreSQL Database
- The bot establishes a connection to a PostgreSQL database using the `psycopg2` library.
- An SQL query is executed to extract the necessary data.
- The query results are fetched and stored in a list.

### 2. Data Manipulation with Pandas
- The extracted data is converted into a DataFrame using the `pandas` library.
- The DataFrame is then exported to an Excel file using the `openpyxl` library. The file name includes the current date for easy identification and organization.

### 3. Authenticate and Upload to Google Drive
- The bot uses the `googleapiclient` and `google.oauth2` libraries to authenticate with Google Drive using service account credentials.
- The generated Excel file is identified in the working directory and prepared for upload.
- The file is uploaded to Google Drive, and read permissions are set so that anyone with the link can access the file.

### 4. Alternative Authentication with PyDrive
- The bot also has an alternative setup for authentication using `PyDrive`.
- Credentials are loaded from a JSON file, and if unavailable or expired, authentication is prompted via command line.
- The credentials are then saved for future use.

## Purpose and Benefits
This bot was created to automate the Extract, Transform, and Load (ETL) process, saving time and manual effort. It is especially useful in scenarios where data needs to be regularly extracted from a database, formatted, and shared via Google Drive. By automating these tasks, the bot ensures consistency, efficiency, and accuracy, allowing users to focus on more strategic and higher-value activities.

## Credits
Developed by Iago Longen Mendonça.

---
