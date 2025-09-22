import os
from model import Kronos, KronosTokenizer, KronosPredictor
os.environ['HF_HOME'] = './base_model' 
# Load from Hugging Face Hub
tokenizer = KronosTokenizer.from_pretrained("NeoQuasar/Kronos-Tokenizer-base")
model = Kronos.from_pretrained("NeoQuasar/Kronos-base")
print(f"Hugging Face cache is set to: {os.environ.get('HF_HOME')}")