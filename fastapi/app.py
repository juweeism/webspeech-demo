from openai import OpenAI
client = OpenAI()


from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": "say 'hello world'"}
    ],
    stream = True
    )
    return completion