import os
import google.generativeai as genai

# 1) Configure your Gemini API key
genai.configure(api_key="AIzaSyBiGqFNepCP6BKMUmut40g9NTDhZVdfSFc")  # ← replace with your real key

# 2) Choose the free-tier model
model = genai.GenerativeModel("gemini-1.5-flash")

def generate_and_save_script():
    # 3) Ask user for a topic
    topic = input("Enter the script topic: ").strip()
    if not topic:
        print("No topic entered. Exiting.")
        return

    # 4) Build a prompt to ask Gemini for a “script”
    prompt = (
        f"Please write a detailed script on the topic: \"{topic}\".\n"
        "Structure it into scenes or sections, include character names/dialogue, and make it coherent as a standalone script."
    )

    # 5) Start a fresh chat (empty history)
    chat = model.start_chat(history=[])

    # 6) Send the prompt and receive the response
    response = chat.send_message(prompt)

    # 7) Extract the generated script text
    script_text = response.text.strip()
    if not script_text:
        print("Gemini returned an empty response. Try again.")
        return

    # 8) Decide on a filename
    #    Replace spaces with underscores, remove any problematic characters
    safe_topic = "".join(c if c.isalnum() or c in (" ", "_") else "_" for c in topic).strip()
    safe_topic = safe_topic.replace(" ", "_")
    filename = f"{safe_topic}_script.txt"

    # 9) Save to disk (UTF-8)
    with open(filename, "w", encoding="utf-8") as f:
        f.write(script_text)

    print(f"\n✅ Script successfully saved to: {os.path.abspath(filename)}")

if __name__ == "__main__":
    generate_and_save_script()
