import anthropic

client = anthropic.Anthropic()

msg = client.messages.create(
    model="claude-3-opus-20240229",
    max_tokens=1024,
    messages=[{"role": "user", "content": input("Prompt: ")}]
)

print(msg.content[0].text)