from groq import Groq
from config import GROQ_API_KEY
from prompts import SYSTEM_PROMPT, TECH_QUESTION_PROMPT

client = Groq(api_key=GROQ_API_KEY)

def generate_questions(tech_stack):

    prompt = TECH_QUESTION_PROMPT.format(tech_stack=tech_stack)

    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7
        )

        return response.choices[0].message.content

    except Exception as e:
        print("Groq API Error:", e)
        return "⚠️ Could not generate questions."