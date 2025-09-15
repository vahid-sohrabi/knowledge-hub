from transformers import AutoTokenizer, AutoModelForQuestionAnswering

model_name = "deepset/roberta-base-squad2"
local_model_path = "./roberta-base-squad2"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForQuestionAnswering.from_pretrained(model_name)

tokenizer.save_pretrained(local_model_path)
model.save_pretrained(local_model_path)

print(f"Model saved at {local_model_path}")
