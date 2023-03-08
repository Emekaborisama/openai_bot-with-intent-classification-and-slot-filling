from transformers import AutoTokenizer, AutoModelForSequenceClassification, TextClassificationPipeline
model_path='./app/intent_classifier'
model_name = 'qanastek/XLMRoberta-Alexa-Intents-Classification'


class SaveModel():
    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForSequenceClassification.from_pretrained(model_name)
        self.classifier = TextClassificationPipeline(model=self.model, tokenizer=self.tokenizer)
        
        
    def save_initialize_model(self):
        self.classifier.save_pretrained(model_path)
        return self.classifier
    

    
    
class predictModel():
    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained(model_path)
        self.model = AutoModelForSequenceClassification.from_pretrained(model_path)
        self.classifier = TextClassificationPipeline(model=self.model, tokenizer=self.tokenizer)
    
    def predict(self, message):
        return self.classifier(message)

if __name__ == '__main__':
    model =SaveModel()
    model.save_initialize_model()





















