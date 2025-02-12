def generate_bot_reply(user_message: str) -> str:
    """
    Simple chatbot response logic (Replace with AI/NLP logic if needed)
    """
    responses = {
        "hello": "Hi there! How can I help you?",
        "bye": "Goodbye! Have a great day.",
        "how are you": "I'm just a bot, but I'm doing fine!",
    }

    # Return predefined response or a default message
    return responses.get(user_message.lower(), f"Bot received: {user_message}")
