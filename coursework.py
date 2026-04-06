import json

# Questions list
Questions = [
    "1. How good is your ability to control room temperature?",
    "2. Is the humidity level in the room comfortable for you?",
    "3. Does the learning environment exhaust you or energize you?",
    "4. Do temperature and humidity affect your concentration?",
    "5. Does your study efficiency increase in a comfortable environment?",
    "6. Does air quality affect your concentration?",
    "7. Does the room temperature bother you while you study?",
    "8. Do you feel uncomfortable when the humidity level is low?",
    "9. Does the learning environment reduce your stress levels?",
    "10. Do you use a humidifier or other tools?",
    "11. Does room temperature and humidity affect your mood?",
    "12. How comfortable is the general learning environment for you?"
]

# Answer options
answers = {
    0: "Very good / Very comfortable",
    1: "Good / Convenient",
    2: "normal",
    3: "Bad / Uncomfortable",
    4: "Very bad / Very uncomfortable"
}

# Collecting answers
results = {}
overall_result = 0

print("The questionnaire is based on a Likert scale (0–4 points).")
print("Answer options:")
for k, v in answers.items():
    print(f"{k} – {v}")
print("\n")

for question in Questions:
    while True:
        try:
            answer = int(input(f"{question}\nYour answer (0–4): "))
            if answer in answers:
                results[question] = answer
                overall_result += answer
                break
            else:
                print("Please enter a number between 0–4 only.")
        except ValueError:
            print("Enter only a number (0–4).")

# Evaluation of the result
if overall_result <= 15:
    situation = "Very comfortable environment"
elif overall_result <= 30:
    situation = "A comfortable environment, but supervision is needed"
elif overall_result <= 45:
    situation = "normal environment"
else:
    situation = "Uncomfortable environment"

# Save in JSON format
data = {
    "Answers": results,
    "overall_result": overall_result,
    "situation": situation
}

with open("results.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print("\nThe survey has been completed")
print(f"Overall Result: {overall_result}")
print(f"Marking: {situation}")
print("Results 'results.json' saved to file.")
