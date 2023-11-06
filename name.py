import openai

openai.api_key = "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"

completion = openai.Completion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
  ]
)

print(completion.choices[0].message)