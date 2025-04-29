import re
from difflib import get_close_matches

# List of common words for spell correction
common_words = ["hello", "how", "are", "you", "your", "name", "is", "I", "am", "fine", "thank", "good", "bye", "thanks", "please", "sorry"]

def correct_spelling(input_text):
    words = input_text.split()
    corrected_words = []
    for word in words:
        # Find the closest match for each word in the common_words list
        corrected_word = get_close_matches(word, common_words, n=1)
        if corrected_word:
            corrected_words.append(corrected_word[0])
        else:
            corrected_words.append(word)
    return ' '.join(corrected_words)

def handle_message(message):
    # Convert to lowercase to make comparison case-insensitive
    message = message.lower()
    
    # Check for specific phrases
    if "hello" in message or "hi" in message:
        return "Hi, how can I assist you today?"
    
    elif "how are you" in message:
        return "I'm doing great, thank you! How can I help you?"
    
    elif "your name" in message or "who are you" in message:
        return f"My name is MatoshriGPT, but you can call me 'Matoshri' for short. What can I do for you, Shrihari Kasar?"
    
    elif "thank you" in message or "thanks" in message:
        return "You're welcome! Let me know if you need anything else."
    
    elif "bye" in message:
        return "Goodbye, Shrihari! Have a great day!"
    
    else:
        return "I'm sorry, I didn't quite understand that. Could you please rephrase?"

def main():
    print("Hello! I'm your assistant chatbot. You can talk to me about anything. Type 'bye' to exit.")
    while True:
        user_message = input("You: ")
        corrected_message = correct_spelling(user_message)
        print(f"Corrected message: {corrected_message}")
        
        response = handle_message(corrected_message)
        print(f"Bot: {response}")
        
        if "bye" in corrected_message:
            break

if __name__ == "__main__":
    main()


# PS C:\Users\Asus\OneDrive\Desktop\LP2> python 5th.py
# Hello! I'm your assistant chatbot. You can talk to me about anything. Type 'bye' to exit.
# You: hello
# Corrected message: hello
# Bot: Hi, how can I assist you today?
# You: hii
# Corrected message: hii
# Bot: Hi, how can I assist you today?
# You: how are you doing
# Corrected message: how are you doing
# Bot: I'm doing great, thank you! How can I help you?
# You: how are you      
# Corrected message: how are you
# Bot: I'm doing great, thank you! How can I help you?
# You: bye
# Corrected message: bye
# Bot: Goodbye, Shrihari! Have a great day!
# PS C:\Users\Asus\OneDrive\Desktop\LP2> 