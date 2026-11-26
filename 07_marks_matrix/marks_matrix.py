def main():
    try:
        student_count = int(input("Number of students: "))
        subject_count = int(input("Number of subjects: "))
        if student_count <= 0 or subject_count <= 0:
            raise ValueError("Both counts must be greater than zero.")

        marks = []
        for student in range(student_count):
            row = []
            print(f"\\nEnter marks for Student {student + 1}")
            for subject in range(subject_count):
                mark = int(input(f"Subject {subject + 1}: "))
                if mark < 0 or mark > 100:
                    raise ValueError("Marks must be between 0 and 100.")
                row.append(mark)
            marks.append(row)

        totals = []
        print("\\n========== STUDENT RESULTS ==========")
        for index, row in enumerate(marks):
            total = sum(row)
            average = total / subject_count
            totals.append(total)
            print(f"Student {index + 1}: Total = {total}, Average = {average:.2f}")

        print("\\n========== SUBJECT AVERAGES ==========")
        for subject in range(subject_count):
            subject_total = 0
            for student in range(student_count):
                subject_total += marks[student][subject]
            print(f"Subject {subject + 1}: {subject_total / student_count:.2f}")

        top_index = totals.index(max(totals))
        print(f"\\nTop performer: Student {top_index + 1} ({totals[top_index]} marks)")
    except ValueError as error:
        print("Invalid input:", error)


if __name__ == "__main__":
    main()
