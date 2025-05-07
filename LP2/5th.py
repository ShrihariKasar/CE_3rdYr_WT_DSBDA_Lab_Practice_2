from rapidfuzz import process

def chatbot():
    responses = {
        "hello": "Hello! How can I assist you today?",
        "hi": "Hi there! What can I help you with?",
        "how are you": "I'm just a bot, but I'm doing great! Thanks!",
        "store hours": "Our store is open from 9 AM to 9 PM, Monday to Saturday.",
        "order status": "Please provide your order ID to track your order.",
        "return policy": "You can return most items within 30 days of purchase.",
        "bye": "Thank you for chatting with us. Have a great day!",
        "thanks": "You're welcome! Is there anything else I can help with?",
        "thank you": "You're welcome! Let me know if you have any more questions."
    }

    print("🛍️ Welcome to ShopBot! Type 'bye' to exit.")
    while True:
        user_input = input("You: ").lower()

        # Match the input to the closest key
        best_match, score, _ = process.extractOne(user_input, responses.keys())

        # Define a minimum confidence score (e.g., 60%)
        response = responses.get(best_match) if score > 60 else "I'm sorry, I didn't understand that clearly. Could you rephrase?"

        print("Bot:", response)

        if best_match == "bye":
            break

chatbot()

# make changes in Qs and ans
# PS C:\Users\Asus\OneDrive\Desktop\LP2> python 5th.py
# 🛍️ Welcome to ShopBot! Type 'bye' to exit.
# You: hello            
# Bot: Hello! How can I assist you today?
# You: order            
# Bot: Please provide your order ID to track your order.
# You: where is my order
# Bot: I'm sorry, I didn't understand that clearly. Could you rephrase?
# You: