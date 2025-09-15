from transformers import AutoTokenizer, AutoModelForQuestionAnswering, pipeline

local_model_path = "./roberta-base-squad2"

tokenizer = AutoTokenizer.from_pretrained(local_model_path)
model = AutoModelForQuestionAnswering.from_pretrained(local_model_path)

qa_pipeline = pipeline("question-answering", model=model, tokenizer=tokenizer)

context = """
Python is a high-level programming language used for web development, data science, artificial intelligence, and more.
This language was created by Guido van Rossum and released in 1991.
Python is popular because of its simplicity and code readability.
"""

question = "why Python is useful?"

result = qa_pipeline(question=question, context=context)

if result['score'] < 0.1 or result['answer'].strip() == "":
    print("اطلاعاتش در دسترس من نیست.")
else:
    print("پاسخ احتمالی:", result['answer'])
