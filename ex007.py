# BMI Calculator Application with Database

import mysql.connector

# Connect to the database
db = mysql.connector.connect(
    host="localhost",
    user="your_username",
    password="your_password",
    database="bmi_database"
)

cursor = db.cursor()

# Create table if it doesn't exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS bmi_records (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    weight FLOAT,
    height FLOAT,
    bmi FLOAT,
    date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

def calculate_bmi(weight, height):
    return weight / (height ** 2)

def save_bmi_record(name, weight, height, bmi):
    cursor.execute("INSERT INTO bmi_records (name, weight, height, bmi) VALUES (%s, %s, %s, %s)",
                   (name, weight, height, bmi))
    db.commit()

def main():
    name = input("Enter your name: ")
    weight = float(input("Enter your weight in kg: "))
    height = float(input("Enter your height in meters: "))
    
    bmi = calculate_bmi(weight, height)
    print(f"{name}, your BMI is: {bmi:.2f}")
    
    save_bmi_record(name, weight, height, bmi)
    print("Your BMI record has been saved.")

if _name_ == "_main_":
    main()

# Close the database connection
cursor.close()
db.close()
