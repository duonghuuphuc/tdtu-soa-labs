# Exercise 1

def calculate_final_score(assignment_score: float, midterm_score: float, final_score: float) -> float:
    output = assignment_score * 0.2 + midterm_score * 0.3 + final_score * 0.5
    return output

def get_result(score: float) -> str:
    if score >= 0.5:
        return "Pass"
    return "Fail"

def main():
    assignment_score = 8.0
    midterm_score = 7.0
    final_exam_score = 6.0

    score = calculate_final_score(assignment_score, midterm_score, final_exam_score)
    result = get_result(score)

    print(f"Final Score: {score:.2f}")
    print(f"Result: {result}")

    return

if __name__ == "__main__":
    main()