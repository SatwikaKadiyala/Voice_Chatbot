from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline

model_name = "microsoft/DialoGPT-small"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

chatbot = pipeline("text-generation", model="facebook/blenderbot-400M-distill")


def get_response(user_input):
    response = chatbot(user_input, max_length=50, num_return_sequences=1, pad_token_id=tokenizer.eos_token_id)
    return response[0]["generated_text"]

if __name__ == "__main__":
    user_text = "Tell me a joke"
    print("Chatbot Response:", get_response(user_text))
