import csv
import os

# Extracts staff info and creates an md file for each staff member. 
# NOTE: Once the data from the csv file has been extracted, for sake of privacy, 
#       I would recommend removing the csv from the project (DON'T COMMIT THE CSV)
# NOTE: This script can't automate photo uploads since they require Google Drive authentication.
# Also, lead roles need to be added manually.

# Formats filenames as "FirstName_LastInitial.md"
def sanitize_filename(full_name):
    name_parts = full_name.split()
    first_name = name_parts[0]
    last_initial = name_parts[-1][0] if len(name_parts) > 1 else ''
    formatted_name = f"{first_name}_{last_initial}".lower()
    return formatted_name

# Specify the directory where you want to save the files
output_directory = './_staffers/'

# Ensure the directory exists, if not, create it
os.makedirs(output_directory, exist_ok=True)

# Column names are long. We could probably redefine them, but we'll just assign them to variables here
name = "What is your preferred first name and last name for the website?"
email = "Email Address"
pronouns = "What (if any) pronouns do you want listed on the website?"
website = " What link/homepage do you want listed on the course website (if any)?"
bio = "Staff Bio"
role = "What's your role on staff?"

# Open the CSV file for reading
with open('staff.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    
    # Iterate over each row in the CSV
    for row in reader:
        # Create the full path for the new markdown file
        filename = os.path.join(output_directory, f"{sanitize_filename(row[name])}.md")
        
        # Open and write to the markdown file
        with open(filename, 'w') as mdfile:
            mdfile.write(f"---\n")
            mdfile.write(f"name: {row[name]}\n")
            mdfile.write(f"email: {row[email]}\n")
            mdfile.write(f"pronouns: {row[pronouns].upper()}\n")
            mdfile.write(f"photo:\n")
            if row[website]:
                mdfile.write(f"website:{row[website]}\n")
            mdfile.write(f"bio: {row[bio]}\n")
            mdfile.write(f"role: {row[role]}\n")
            mdfile.write(f"---\n")