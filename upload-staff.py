import csv
import os

# Extracts staff info and creates an md file for each staff member.
#   csv file should be titled "staff.csv" and it shouldn't be in the base folder
#   md files are written into the _staffers folder
#   Update leads if necessary
# NOTE: Once the data from the csv file has been extracted, for sake of privacy, 
#       I would recommend removing the csv from the project (DON'T COMMIT THE CSV)
# NOTE: This script can't automate photo uploads since they require Google Drive authentication.
#       Photos should be named "FirstName_LastInitial.jpg" and stored in assets/images/staff

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
leads = {
    "thomas_g": "Course Director",
    "ramisha_k": "Course Director",
    "edwin_n": "Content",
    "ella_d": "Content",
    "conan_s": "Pedagogy",
    "aileen_w": "Grading",
    "cai_i": "Logistics",
    "andrew_c": "Student Support",
    "brandon_s": "Tutors",
    "sam_c": "Scholars"
}
# Open the CSV file for reading
with open('staff.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    
    # Iterate over each row in the CSV
    for row in reader:
        # Create the full path for the new markdown file
        formatted_name = sanitize_filename(row[name])

        filename = os.path.join(output_directory, f"{formatted_name}.md")
        
        # Open and write to the markdown file
        with open(filename, 'w') as mdfile:
            mdfile.write(f"---\n")
            mdfile.write(f"name: {row[name]}\n")
            mdfile.write(f"email: {row[email]}\n")
            mdfile.write(f"pronouns: {row[pronouns].upper()}\n")
            mdfile.write(f"photo: staff/{formatted_name}.jpg\n")
            if row[website]:
                mdfile.write(f"website:{row[website]}\n")
            mdfile.write(f"bio: {row[bio]}\n")
            mdfile.write(f"role: {row[role]}\n")
            if formatted_name in leads:
                mdfile.write(f"team: {leads[formatted_name]}")
            mdfile.write(f"---\n")