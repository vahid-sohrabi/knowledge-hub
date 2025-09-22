from transformers import AutoTokenizer, AutoModelForQuestionAnswering
from app.config.settings import settings


model_name = settings.qa_model_name
local_model_path = settings.qa_model_name

tokenizer = AutoTokenizer.from_pretrained(settings.qa_model_name)
model = AutoModelForQuestionAnswering.from_pretrained(model_name)

tokenizer.save_pretrained(local_model_path)
model.save_pretrained(local_model_path)

print(f"Model saved at {local_model_path}")
