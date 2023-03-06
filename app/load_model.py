from accelerate import init_empty_weights
from transformers import AutoConfig, AutoModelForCausalLM


checkpoint = "qanastek/XLMRoberta-Alexa-Intents-Classification"
config = AutoConfig.from_pretrained(checkpoint)

with init_empty_weights():
    model = AutoModelForCausalLM.from_config(config)