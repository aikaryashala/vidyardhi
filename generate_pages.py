import csv
import os
import shutil

CSV_FILE = "students.csv"
TEMPLATE_FILE = "template.html"
TEMPLATE_CSS = "template.css"
OUTPUT_DIR = "docs"
CSS_OUTPUT_DIR = os.path.join(OUTPUT_DIR, "assets", "css")

# create main output folder
os.makedirs(OUTPUT_DIR, exist_ok=True)

# create css directory and copy template.css
os.makedirs(CSS_OUTPUT_DIR, exist_ok=True)
shutil.copy(TEMPLATE_CSS, os.path.join(CSS_OUTPUT_DIR, "styles.css"))
print(f"✔ Copied {TEMPLATE_CSS} to {os.path.join(CSS_OUTPUT_DIR, 'styles.css')}")

# read template
with open(TEMPLATE_FILE, "r", encoding="utf-8") as f:
    template = f.read()

with open(CSV_FILE, newline="", encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        student_id = row["student_id"].strip()
        name = row["name"].strip()

        # ✅ folder name = student_id
        student_dir = os.path.join(OUTPUT_DIR, student_id)
        os.makedirs(student_dir, exist_ok=True)

        # construct projects URL from github URL
        github_url = row["github"].strip()
        github_username = github_url.split("/")[-1]
        row["projects"] = f"http://aikaryashala.com/projects-{github_username}/"

        html = template

        # replace placeholders (name, email, image, github, linkedin, projects)
        for key, value in row.items():
            html = html.replace(f"{{{{{key}}}}}", value)

        file_path = os.path.join(student_dir, "index.html")
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(html)

        print(f"✔ Created page for {name} in folder {student_id}")
