import csv
import os

CSV_FILE = "students.csv"
TEMPLATE_FILE = "template.html"
OUTPUT_DIR = "docs"

# create main output folder
os.makedirs(OUTPUT_DIR, exist_ok=True)

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

        html = template

        # replace placeholders (name, email, image, github, linkedin)
        for key, value in row.items():
            html = html.replace(f"{{{{{key}}}}}", value)

        file_path = os.path.join(student_dir, "index.html")
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(html)

        print(f"✔ Created page for {name} in folder {student_id}")
