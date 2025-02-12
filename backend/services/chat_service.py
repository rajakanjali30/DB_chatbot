def generate_bot_reply(user_message: str) -> str:
    
    responses = {
        "hello": "Hi there! How can I help you?",
        "bye": "Goodbye! Have a great day.",
        "how are you": "I'm just a bot, but I'm doing fine!",
    }

    return responses.get(user_message.lower(), f"Bot received: {user_message}")
