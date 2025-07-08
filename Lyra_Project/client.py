import google.generativeai as genai

# Set your API key
genai.configure(api_key="AIzaSyCfytWNFu-FgbJacY9F9ya0kaJ0-xn3D_M")

# Initialize the model
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    system_instruction="You are Jarvis, a helpful and smart personal assistant like Alexa or Google Assistant. Give answers in simple words and in a bit short"
)

# Send a prompt
response = model.generate_content("Explain how AI works in a few words.")

# Print the response
print(response.text)
