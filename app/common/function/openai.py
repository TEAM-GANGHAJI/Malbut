# from fastapi import APIRouter, HTTPException, Depends
# from pydantic import BaseModel
# from typing import List, Optional
# import openai
# import os
# from dotenv import load_dotenv

# # Load environment variables
# load_dotenv()

# # Configure OpenAI API
# openai.api_key = os.getenv("OPENAI_API_KEY")

# async def get_ai_response(messages: List[Message]) -> str:
#     try:
#         response = openai.ChatCompletion.create(
#             model="gpt-3.5-turbo",
#             messages=[
#                 {"role": "system", "content": "You are an English teacher. The user's English level is beginner. Respond according to the user's English level. You must answer only in English."},
#                 *[{"role": msg.role, "content": msg.content} for msg in messages]
#             ],
#             temperature=0.7,
#             max_tokens=150
#         )
#         return response.choices[0].message['content']
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=f"GPT API 호출 중 오류 발생: {str(e)}")