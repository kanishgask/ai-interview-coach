from analyzer import analyze_code

def main():
    print("🚀 AI Interview Coach")
    
    problem = input("Enter problem description: ")
    code = input("Paste your code: ")

    feedback = analyze_code(problem, code)
    
    print("\n💡 AI Feedback:\n")
    print(feedback)

if __name__ == "__main__":
    main()
