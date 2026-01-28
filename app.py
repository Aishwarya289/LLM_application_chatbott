from flask import Flask, request, render_template
from flask_cors import CORS
import json
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

app = Flask(__name__)
CORS(app)

# Load chatbot
model_name = "facebook/blenderbot-400M-distill"
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

conversation_history = []

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/chatbot', methods=['POST'])
def handle_prompt():
    data = request.get_json()
    user_input = data['prompt'].strip()

    # Keep only last 2 turns (clean context)
    history = conversation_history[-2:]
    context = "\n".join(history)

    prompt = f"""
You are a friendly, polite chatbot.
Keep responses short, clear, and relevant.
Do not repeat the user's message.
Do not ask unrelated questions.

Conversation so far:
{context}

User: {user_input}
Bot:
"""

    inputs = tokenizer(
        prompt,
        return_tensors="pt",
        truncation=True,
        max_length=512
    )

    outputs = model.generate(
        **inputs,
        max_length=120,
        temperature=0.6,
        top_p=0.85,
        repetition_penalty=1.3,
        no_repeat_ngram_size=3,
        do_sample=True
    )

    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    response = response.split("Bot:")[-1].strip()

    conversation_history.append(f"User: {user_input}")
    conversation_history.append(f"Bot: {response}")
    conversation_history[:] = conversation_history[-4:]

    return response



if __name__ == '__main__':
    app.run()
