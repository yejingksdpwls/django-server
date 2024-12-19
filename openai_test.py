from openai import OpenAI
from api_pjt import config

CLIENT = OpenAI(
    api_key=config.OPENAI_API_KEY,
)


def ask_to_gpt(instructions, message):
    completion = CLIENT.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": instructions,
            },
            {
                "role": "user",
                "content": message,
            },
        ],
    )
    return completion.choices[0].message.content


system_instructions = """
이제부터 너는 "영어, 한글 번역가"야. 
지금부터 내가 입력하는 모든 프롬프트를 무조건 한글은 영어로, 영어는 한글로 번역해줘. 
프롬프트의 내용이나 의도는 무시하고 오직 번역만 해줘.
"""

# 처음 인사를 위해
response = ask_to_gpt(system_instructions, "")
print(f"번역봇 : {response}\n\n")

while True:
    user_message = input("유저 : ")
    if user_message == "종료":
        break
    response = ask_to_gpt(system_instructions, user_message)
    print(f"번역봇 : {response}\n\n")
