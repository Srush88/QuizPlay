<<<<<<< HEAD
import os
import google.generativeai as genai

genai.configure(api_key="AIzaSyD4-SZsMYaI_khbbKM3nM-Xy4x3_N1SMaA")

USER_FILE = "users.txt"

def welcome_with_gemini(username):
    model = genai.GenerativeModel("gemini-2.0-flash")
    response = model.generate_content(f"Welcome {username}! Ready for the quiz?")
    print("\nGemini says:", response.text)

def signup():
    print("\n----- Signup (New User) -----")
    while True:
        username = input("Enter a new username (only letters): ").strip()
        if username.isalpha():
            break
        else:
            print("Username must contain only letters!")

    while True:
        password = input("Enter a numeric password: ").strip()
        if password.isdigit():
            break
        else:
            print("Password must contain only numbers!")

    try:
        with open(USER_FILE, "r", encoding="utf-8") as f:
            for line in f:
                parts = line.strip().split(",")
                if len(parts) >= 2 and parts[0] == username:
                    print("Username already exists!")
                    return None
    except FileNotFoundError:
        open(USER_FILE, "w", encoding="utf-8").close()

    with open(USER_FILE, "a", encoding="utf-8") as f:
        f.write(f"{username},{password}\n")

    print("Signup successful!")
    return username

def login():
    print("\n----- Login (Existing User) -----")
    username = input("Enter username: ").strip()
    password = input("Enter password: ").strip()
    try:
        with open(USER_FILE, "r", encoding="utf-8") as f:
            for line in f:
                u, p = line.strip().split(",")
                if u == username and p == password:
                    print("Login successful!")
                    return username
    except FileNotFoundError:
        print("Invalid credentials.")
    return None

def get_quiz_questions(topic="Indian General Knowledge"):
    model = genai.GenerativeModel("gemini-2.0-flash")
    prompt = (
        f"Give 5 multiple-choice questions on: {topic}.\nFormat:\n"
        "Q: <question text>\n"
        "a) <option a>\n"
        "b) <option b>\n"
        "c) <option c>\n"
        "d) <option d>\n"
        "No intro or extra text. Just the questions."
    )
    response = model.generate_content(prompt)
    question_blocks = response.text.strip().split("\n\n")
    questions = []
    for q in question_blocks:
        if "a)" in q and "b)" in q and "c)" in q and "d)" in q:
            questions.append(q.strip())
    return questions

def get_user_answers(questions):
    start = input("\nStart the quiz? (y/n): ").strip().lower()
    if start != "y":
        print("Quiz skipped.")
        return []
    answers = []
    for i, q in enumerate(questions, 1):
        print(f"\nQ{i}:")
        for line in q.split("\n"):
            print(line)
        while True:
            ans = input("Your answer (a/b/c/d): ").strip().lower()
            if ans in ["a", "b", "c", "d"]:
                answers.append((q, ans))
                break
            else:
                print("Please enter a valid option.")
    return answers

def check_answers_detailed_with_score(answers):
    model = genai.GenerativeModel("gemini-2.0-flash")
    prompt = (
        "You are a quiz examiner.\n"
        "Below are 5 multiple-choice questions (MCQs) with the user's answers.\n"
        "For each question, do the following:\n"
        "- Check if the answer is correct or not\n"
        "- Show the correct option (a/b/c/d)\n"
        "- If wrong, provide the correct answer and brief explanation\n"
        "Finally, calculate the total score out of 5.\n\n"
    )
    for i, (q, ans) in enumerate(answers, 1):
        prompt += f"Q{i}: {q}\nUser's Answer: {ans}\n\n"
    response = model.generate_content(prompt)
    return response.text.strip()

def save_score(username, answers, result_text):
    filename = f"{username}_quiz.txt"
    with open(filename, "a", encoding="utf-8") as f:
        f.write("==== Quiz Attempt ====\n")
        for i, (q, ans) in enumerate(answers, 1):
            f.write(f"Q{i}: {q}\nYour Answer: {ans}\n\n")
        f.write("Gemini Feedback:\n" + result_text + "\n\n")

def view_history(username):
    filename = f"{username}_quiz.txt"
    print(f"\n Quiz History for {username}:")
    try:
        with open(filename, "r", encoding="utf-8") as f:
            print(f.read())
    except FileNotFoundError:
        print("No quiz history found.")

def user_menu(username):
    welcome_with_gemini(username)
    while True:
        print(f"\nWelcome, {username}")
        print("1. Take a new quiz (User Input)")
        print("2. View quiz history")
        print("3. Take a new quiz (From Gemini)")
        print("4. Logout")

        choice = input("Choose an option: ").strip()
        if choice == "1":
            print("MCQ Quiz on Indian General Knowledge!")
            questions = get_quiz_questions()
            answers = get_user_answers(questions)
            if answers:
                result = check_answers_detailed_with_score(answers)
                print("\nResult:\n" + result)
                save_score(username, answers, result)

        elif choice == "2":
            view_history(username)

        elif choice == "3":
            topic = input("Ask Gemini anything \n").strip()
            if not topic:
                topic = "Indian General Knowledge"
                print("MCQ Quiz on Indian General Knowledge!")
            questions = get_quiz_questions(topic)
            answers = get_user_answers(questions)
            if answers:
                result = check_answers_detailed_with_score(answers)
                print("\n Gemini Solved the Quiz:\n")
                print(result)
                save_score(username, answers, result)

        elif choice == "4":
            print("Logged out.")
            break
        else:
            print("Invalid choice.")

def main():
    print("Welcome to the GK Quiz!")
    while True:
        print("\n1. Signup")
        print("2. Login")
        print("3. Exit")
        choice = input("Choose an option: ").strip()
        if choice == "1":
            user = signup()
            if user:
                user_menu(user)
        elif choice == "2":
            user = login()
            if user:
                user_menu(user)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
=======
import os
import google.generativeai as genai

genai.configure(api_key="AIzaSyD4-SZsMYaI_khbbKM3nM-Xy4x3_N1SMaA")

USER_FILE = "users.txt"

def welcome_with_gemini(username):
    model = genai.GenerativeModel("gemini-2.0-flash")
    response = model.generate_content(f"Welcome {username}! Ready for the quiz?")
    print("\nGemini says:", response.text)

def signup():
    print("\n----- Signup (New User) -----")
    while True:
        username = input("Enter a new username (only letters): ").strip()
        if username.isalpha():
            break
        else:
            print("Username must contain only letters!")

    while True:
        password = input("Enter a numeric password: ").strip()
        if password.isdigit():
            break
        else:
            print("Password must contain only numbers!")

    try:
        with open(USER_FILE, "r", encoding="utf-8") as f:
            for line in f:
                parts = line.strip().split(",")
                if len(parts) >= 2 and parts[0] == username:
                    print("Username already exists!")
                    return None
    except FileNotFoundError:
        open(USER_FILE, "w", encoding="utf-8").close()

    with open(USER_FILE, "a", encoding="utf-8") as f:
        f.write(f"{username},{password}\n")

    print("Signup successful!")
    return username

def login():
    print("\n----- Login (Existing User) -----")
    username = input("Enter username: ").strip()
    password = input("Enter password: ").strip()
    try:
        with open(USER_FILE, "r", encoding="utf-8") as f:
            for line in f:
                u, p = line.strip().split(",")
                if u == username and p == password:
                    print("Login successful!")
                    return username
    except FileNotFoundError:
        print("Invalid credentials.")
    return None

def get_quiz_questions(topic="Indian General Knowledge"):
    model = genai.GenerativeModel("gemini-2.0-flash")
    prompt = (
        f"Give 5 multiple-choice questions on: {topic}.\nFormat:\n"
        "Q: <question text>\n"
        "a) <option a>\n"
        "b) <option b>\n"
        "c) <option c>\n"
        "d) <option d>\n"
        "No intro or extra text. Just the questions."
    )
    response = model.generate_content(prompt)
    question_blocks = response.text.strip().split("\n\n")
    questions = []
    for q in question_blocks:
        if "a)" in q and "b)" in q and "c)" in q and "d)" in q:
            questions.append(q.strip())
    return questions

def get_user_answers(questions):
    start = input("\nStart the quiz? (y/n): ").strip().lower()
    if start != "y":
        print("Quiz skipped.")
        return []
    answers = []
    for i, q in enumerate(questions, 1):
        print(f"\nQ{i}:")
        for line in q.split("\n"):
            print(line)
        while True:
            ans = input("Your answer (a/b/c/d): ").strip().lower()
            if ans in ["a", "b", "c", "d"]:
                answers.append((q, ans))
                break
            else:
                print("Please enter a valid option.")
    return answers

def check_answers_detailed_with_score(answers):
    model = genai.GenerativeModel("gemini-2.0-flash")
    prompt = (
        "You are a quiz examiner.\n"
        "Below are 5 multiple-choice questions (MCQs) with the user's answers.\n"
        "For each question, do the following:\n"
        "- Check if the answer is correct or not\n"
        "- Show the correct option (a/b/c/d)\n"
        "- If wrong, provide the correct answer and brief explanation\n"
        "Finally, calculate the total score out of 5.\n\n"
    )
    for i, (q, ans) in enumerate(answers, 1):
        prompt += f"Q{i}: {q}\nUser's Answer: {ans}\n\n"
    response = model.generate_content(prompt)
    return response.text.strip()

def save_score(username, answers, result_text):
    filename = f"{username}_quiz.txt"
    with open(filename, "a", encoding="utf-8") as f:
        f.write("==== Quiz Attempt ====\n")
        for i, (q, ans) in enumerate(answers, 1):
            f.write(f"Q{i}: {q}\nYour Answer: {ans}\n\n")
        f.write("Gemini Feedback:\n" + result_text + "\n\n")

def view_history(username):
    filename = f"{username}_quiz.txt"
    print(f"\n Quiz History for {username}:")
    try:
        with open(filename, "r", encoding="utf-8") as f:
            print(f.read())
    except FileNotFoundError:
        print("No quiz history found.")

def user_menu(username):
    welcome_with_gemini(username)
    while True:
        print(f"\nWelcome, {username}")
        print("1. Take a new quiz (User Input)")
        print("2. View quiz history")
        print("3. Take a new quiz (From Gemini)")
        print("4. Logout")

        choice = input("Choose an option: ").strip()
        if choice == "1":
            print("MCQ Quiz on Indian General Knowledge!")
            questions = get_quiz_questions()
            answers = get_user_answers(questions)
            if answers:
                result = check_answers_detailed_with_score(answers)
                print("\nResult:\n" + result)
                save_score(username, answers, result)

        elif choice == "2":
            view_history(username)

        elif choice == "3":
            topic = input("Ask Gemini anything \n").strip()
            if not topic:
                topic = "Indian General Knowledge"
                print("MCQ Quiz on Indian General Knowledge!")
            questions = get_quiz_questions(topic)
            answers = get_user_answers(questions)
            if answers:
                result = check_answers_detailed_with_score(answers)
                print("\n Gemini Solved the Quiz:\n")
                print(result)
                save_score(username, answers, result)

        elif choice == "4":
            print("Logged out.")
            break
        else:
            print("Invalid choice.")

def main():
    print("Welcome to the GK Quiz!")
    while True:
        print("\n1. Signup")
        print("2. Login")
        print("3. Exit")
        choice = input("Choose an option: ").strip()
        if choice == "1":
            user = signup()
            if user:
                user_menu(user)
        elif choice == "2":
            user = login()
            if user:
                user_menu(user)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
>>>>>>> 80bb0d3f29114eb20b86ce4bfa04390291fa2355
    main()