import csv

courses = []
with open("fundamentals/manipulating_files/dados/courses.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        courses.append({"language": row["language"], "category": row["category"]})
        
print("\n")
print(courses)