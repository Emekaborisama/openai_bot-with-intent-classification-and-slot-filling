from transformers import AutoTokenizer, AutoModelForSequenceClassification, TextClassificationPipeline


def initialize_model():
    model_name = 'qanastek/XLMRoberta-Alexa-Intents-Classification'
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSequenceClassification.from_pretrained(model_name)
    classifier = TextClassificationPipeline(model=model, tokenizer=tokenizer)
    return classifier




