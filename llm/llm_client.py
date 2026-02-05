import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv(override=True)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

import time
import random

def call_llm(system_prompt, user_prompt, max_retries=3):
    """
    Calls OpenAI API with structured output capability and retry logic
    """
    for attempt in range(max_retries):
        try:
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt},
                ],
                temperature=0
            )
            return response.choices[0].message.content
        except Exception as e:
            # Check if it's a rate limit error (usually 429) or temporary server error (5xx)
            if "429" in str(e) or "500" in str(e) or "503" in str(e):
                if attempt < max_retries - 1:
                    wait_time = (2 ** attempt) + random.uniform(0, 1)
                    print(f"LLM API Error (Attempt {attempt+1}/{max_retries}): {e}. Retrying in {wait_time:.2f}s...")
                    time.sleep(wait_time)
                    continue
            
            # If it's not retriable or we ran out of retries, re-raise
            print(f"LLM API Failed after {attempt+1} attempts: {e}")
            raise e
