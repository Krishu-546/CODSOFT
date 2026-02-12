import datetime

def greet():
    print("\n🤖 CodSoft AI Chatbot")
    print("Type 'bye' to exit the chat.\n")

def Chatbot():
    greet()

    while True:
        user_input = input("You: ").lower().strip()

        #greetings
        if user_input in ["hi","hello","hey"]:
            print("Bot: Hello! How can I assist you today? 😊")

        #Asking name
        elif "your name" in user_input:
            print("Bot: I am CodSOft AI Chatbot.")

        #Asking time
        elif "time" in user_input:
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"Bot: Current time is {current_time}")

        #Asking date
        elif "date" in user_input:
            today = datetime.date.today()
            print(f"Bot: Today's date is {today}")

        #How are you
        elif "how are you" in user_input:
            print("Bot: I'm just a program, but I'm doing great! 😊")

        #Help
        elif "help" in user_input:
            print("Bot: You can ask me about time, date, or greetings.")

        #Exit condition
        elif user_input == "bye":
            print("Bot: GoodBye! Have a great day👋")
            break

        #Unknown input
        else:
            print("Bot: Sorry, I didn't understand that. please try again.")

if __name__ == "__main__":
    Chatbot()
