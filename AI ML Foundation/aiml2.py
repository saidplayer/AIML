from transformers import AutoModelForSeq2SeqLM, AutoTokenizer, pipeline


model_name = "google/flan-t5-small"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
generator = pipeline("text2text-generation", model=model, tokenizer=tokenizer)

while True:
    prompt = input("msg: ")
    response = generator(prompt)
    print(response[0]["generated_text"])
