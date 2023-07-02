import openai

openai.api_key = "SOME_API_KEY"

conversation = ""

i=1

while (i!=0):
    question = input("Humano: ")
    conversation += "\nHumano: " + question + "\nAI:"
    response = openai.Completion.create(
        engine = "ada",
        prompt = conversation,
        temperature=0.9,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.6,
        stop=["\n", " Humano:", " AI:"]
    )

    answer = response.choices[0].text.strip()
    conversation += answer
    print ("AI: " + answer + "\n")