import google.generativeai as genai

# Paste your Gemini API key here
genai.configure(api_key="AIzaSyBiGqFNepCP6BKMUmut40g9NTDhZVdfSFc")

# Use Gemini 1.5 Flash model (faster and free tier eligible)
model = genai.GenerativeModel("gemini-1.5-flash")

# Start a chat session
chat = model.start_chat(history=[])

print("💬 Gemini Chatbot (type 'exit' to quit)")

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        break

    response = chat.send_message(user_input)
    print("Bot:", response.text)

