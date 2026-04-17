from groq import Groq
import time
from config import GROQ_API_KEY
from prompts import SYSTEM_PROMPT, TECH_QUESTION_PROMPT

client = Groq(api_key=GROQ_API_KEY)


def generate_questions(tech_stack):

    prompt = TECH_QUESTION_PROMPT.format(tech_stack=tech_stack)

    for attempt in range(3):  # retry logic
        try:
            response = client.chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.5,
                max_tokens=250   # 🔥 LIMIT TOKENS (VERY IMPORTANT)
            )

            questions = response.choices[0].message.content

            return f"### QUESTIONS FOR TECH STACK: {tech_stack.upper()}\n\n{questions}"

        except Exception as e:

            if "429" in str(e) or "rate_limit" in str(e):
                print("Rate limit hit, retrying...")
                time.sleep(8)  # wait before retry
            else:
                raise e

    return "⚠️ Rate limit exceeded. Please try again after a few seconds."