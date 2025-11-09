#-------------------------------------------------------------
# Name       : Priyanshu
# Course     : Programming for Problem-Solving using Python
# Assignment : Mini Project – GradeBook Analyzer
# Date       : 05-Nov-2025
#-------------------------------------------------------------
"""
Description:
This GradeBook Analyzer helps teachers quickly record and analyze
student performance. It allows manual entry of names and marks,
computes statistics (average, median, max, min), assigns grades,
identifies pass/fail students, and displays all results neatly in a
tabular form with a looped menu interface.
"""

import statistics

#-------------------------------------------------------------
# Task 1: Project Setup and Initialization
#-------------------------------------------------------------
def welcome():
    print("=" * 60)
    print("          🎓 Welcome to GradeBook Analyzer 🎓")
    print("=" * 60)
    print("A simple Python program to record and analyze student marks to save time and work of professors and teachers\n")

#-------------------------------------------------------------
# Task 3: Statistical Analysis Functions
#-------------------------------------------------------------
def calculate_average(marks_dict):
    return sum(marks_dict.values()) / len(marks_dict)

def calculate_median(marks_dict):
    return statistics.median(marks_dict.values())

def find_max_score(marks_dict):
    max_name = max(marks_dict, key=marks_dict.get)
    return max_name, marks_dict[max_name]

def find_min_score(marks_dict):
    min_name = min(marks_dict, key=marks_dict.get)
    return min_name, marks_dict[min_name]

#-------------------------------------------------------------
# Task 4: Grade Assignment and Distribution
#-------------------------------------------------------------
def assign_grades(marks_dict):
    grades = {}
    for name, mark in marks_dict.items():
        if mark >= 90:
            grades[name] = "A"
        elif mark >= 80:
            grades[name] = "B"
        elif mark >= 70:
            grades[name] = "C"
        elif mark >= 60:
            grades[name] = "D"
        else:
            grades[name] = "F"
    return grades

def grade_distribution(grades_dict):
    dist = {"A":0, "B":0, "C":0, "D":0, "F":0}
    for g in grades_dict.values():
        dist[g] += 1
    return dist

#-------------------------------------------------------------
# Task 5: Pass/Fail Filter with List Comprehension
#-------------------------------------------------------------
def pass_fail_lists(marks_dict):
    passed_students = [name for name, m in marks_dict.items() if m >= 40]
    failed_students = [name for name, m in marks_dict.items() if m < 40]
    return passed_students, failed_students

#-------------------------------------------------------------
# Task 6: Results Table and Display
#-------------------------------------------------------------
def display_results(marks_dict, grades_dict):
    print("\n{:<12} {:<10} {:<6}".format("Name", "Marks", "Grade"))
    print("-" * 30)
    for name in marks_dict:
        print("{:<12} {:<10} {:<6}".format(name, marks_dict[name], grades_dict[name]))
    print("-" * 30)

#-------------------------------------------------------------
# Main Program – User Loop and Execution
#-------------------------------------------------------------
def main():
    welcome()

    while True:
        print("\n📋 MENU")
        print("1. Enter student data and analyze")
        print("2. Exit program")
        choice = input("Enter your choice (1/2): ")

        if choice == "2":
            print("\nThank you for using GradeBook Analyzer. Goodbye! 👋")
            break

        elif choice == "1":
            marks = {}
            n = int(input("\nHow many students are in the class? "))

            # Task 2: Manual Input
            for i in range(n):
                name = input(f"Enter name of student {i+1}: ")
                mark = float(input(f"Enter marks for {name}: "))
                marks[name] = mark

            # Task 3: Statistics
            avg = calculate_average(marks)
            median = calculate_median(marks)
            top_name, top_score = find_max_score(marks)
            low_name, low_score = find_min_score(marks)

            print("\n📊 STATISTICAL ANALYSIS")
            print(f"Average Marks : {avg:.2f}")
            print(f"Median Marks  : {median:.2f}")
            print(f"Highest Score : {top_name} ({top_score})")
            print(f"Lowest Score  : {low_name} ({low_score})")

            # Task 4: Grades
            grades = assign_grades(marks)
            dist = grade_distribution(grades)

            print("\n🎯 GRADE DISTRIBUTION")
            for g, count in dist.items():
                print(f"Grade {g}: {count} student(s)")

            # Task 5: Pass/Fail
            passed, failed = pass_fail_lists(marks)
            print("\n✅ Passed Students:", passed, f"({len(passed)})")
            print("❌ Failed Students:", failed, f"({len(failed)})")

            # Task 6: Display Table
            print("\n🧾 RESULT TABLE")
            display_results(marks, grades)

            again = input("\nDo you want to analyze another class? (y/n): ")
            if again.lower() != 'y':
                print("\nThank you for using GradeBook Analyzer.  👋")
                break
        else:
            print("Invalid choice! Please select 1 or 2.")

#-------------------------------------------------------------
# Run Program
#-------------------------------------------------------------
if __name__ == "__main__":
    main()
