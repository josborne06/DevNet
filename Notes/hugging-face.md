# 🤗 Hugging Face Cheat Sheet for Engineers

**Hugging Face** makes it easy to use pretrained machine learning models for tasks like text analysis, code generation, log summarization, anomaly detection, and more — all with friendly Python APIs and powerful open-source tools.

---

## 🧰 Core Libraries

| Library       | Description                                                  |
|---------------|--------------------------------------------------------------|
| `transformers`| Pretrained NLP & LLM models (text, audio, vision)            |
| `datasets`    | Thousands of curated ML datasets                             |
| `gradio`      | Build ML web apps and dashboards                             |
| `diffusers`   | Stable Diffusion and other image generation tools            |
| `accelerate`  | Fast, distributed model training on multiple GPUs            |
| `peft`        | Efficient fine-tuning (LoRA, QLoRA, etc)                     |

Install all:
```bash
pip install transformers datasets gradio accelerate peft
```

---

## 🔗 Hugging Face Resources

| Resource             | URL                                                  |
|----------------------|------------------------------------------------------|
| 🔎 Model Hub         | https://huggingface.co/models                        |
| 📚 Datasets          | https://huggingface.co/datasets                      |
| 🎛️ Spaces Gallery    | https://huggingface.co/spaces                        |
| 📖 Transformers Docs | https://huggingface.co/transformers                  |

---

## ⚡ Common Pipelines

```python
from transformers import pipeline

# Text Generation
gen = pipeline("text-generation", model="gpt2")
print(gen("The future of AI is", max_length=50)[0]['generated_text'])

# Summarization
sumr = pipeline("summarization", model="facebook/bart-large-cnn")
print(sumr("Firewall log entry here...", max_length=40)[0]['summary_text'])

# Sentiment Analysis
sentiment = pipeline("sentiment-analysis")
print(sentiment("This firewall rule is annoying."))

# Named Entity Recognition (NER)
ner = pipeline("ner", grouped_entities=True)
print(ner("Blocked 10.1.1.4 due to malware activity in Amsterdam."))

# Question Answering
qa = pipeline("question-answering")
print(qa({
  "question": "Why was the firewall rule triggered?",
  "context": "Access was denied due to a known threat signature match."
}))
```

---

## 🏗️ Useful Models for Network & Security Engineering

| Model Name                                      | Use Case                        | Link                                                   |
|------------------------------------------------|----------------------------------|--------------------------------------------------------|
| `bert-base-uncased`                            | Text classification / NER       | https://huggingface.co/bert-base-uncased              |
| `distilbert-base-uncased-finetuned-sst-2-english` | Sentiment analysis           | https://huggingface.co/distilbert-base-uncased-finetuned-sst-2-english |
| `facebook/bart-large-cnn`                      | Summarization                   | https://huggingface.co/facebook/bart-large-cnn        |
| `tiiuae/falcon-7b`                              | Lightweight GPT-like LLM        | https://huggingface.co/tiiuae/falcon-7b               |
| `mistralai/Mixtral-8x7B-Instruct-v0.1`          | General-purpose assistant       | https://huggingface.co/mistralai/Mixtral-8x7B-Instruct-v0.1 |
| `dslim/bert-base-NER`                          | Entity recognition in logs      | https://huggingface.co/dslim/bert-base-NER            |
| `openai/whisper-base`                          | Speech-to-text (calls, audio)   | https://huggingface.co/openai/whisper-base            |

---

## ⚙️ Manual Model Load Example

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification

model_name = "bert-base-uncased"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)
```

---

## 🧠 Gradio: Quick ML UI

```python
import gradio as gr
from transformers import pipeline

summarizer = pipeline("summarization")

def summarize_text(text):
    return summarizer(text)[0]['summary_text']

gr.Interface(fn=summarize_text, inputs="textbox", outputs="text").launch()
```

---

## 🧪 Tips for Fine-Tuning

- Use `accelerate` for multi-GPU & fast training
- Use `peft` with LoRA for efficient tuning on small hardware
- Monitor training with [Weights & Biases](https://wandb.ai) or TensorBoard
- Start small (100–1k rows) for proof of concept

---

## 🔐 Security & Deployment

- Most models run 100% **locally** (no cloud required)
- Use **private model repos** or deploy with `text-generation-inference`
- For enterprise: [Inference Endpoints](https://huggingface.co/inference-endpoints)

---

## 🛠️ CLI Tools

```bash
huggingface-cli login
huggingface-cli repo create my-model --type model
```

---

## 💬 Community & Support

- Discord: https://discord.gg/huggingface  
- Forums: https://discuss.huggingface.co/  
- GitHub: https://github.com/huggingface  

---

> “Hugging Face brings state-of-the-art AI to your fingertips — perfect for automating workflows, securing networks, and building smart assistants.”
```