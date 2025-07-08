# 🧠 GPT-style Character-Level Language Model

Welcome to a from-scratch implementation of a **GPT-style Transformer** trained on the Tiny Shakespeare dataset.  
This project is built using only PyTorch, with no external dependencies like Hugging Face, to help you understand the core components of Transformer models.

> 🔗 [Live Repo](https://github.com/Sai3570-je/GPT-style-character-level-language-model)

---

## 📚 Project Highlights

- Transformer architecture (multi-head self-attention, feedforward, layer norm)
- Character-level tokenization
- Trains on raw Shakespearean text
- Generates coherent text with Shakespearean style
- Fully written in PyTorch for complete transparency

---

## 📁 Dataset

The model is trained on the [Tiny Shakespeare dataset](https://raw.githubusercontent.com/karpathy/char-rnn/master/data/tinyshakespeare/input.txt).  
Save it in the root folder as:

2. Install PyTorch:
bash
Copy
Edit
pip install torch
🚀 Run the Model
🏋️‍♂️ Train:
bash
Copy
Edit
python main.py
✍️ Generate Text:
After training finishes, it will generate 500 characters of Shakespeare-style output automatically.

Or manually:

python
Copy
Edit
context = torch.zeros((1, 1), dtype=torch.long, device=device)
print(decode(model.generate(context, max_new_tokens=500)[0].tolist()))
🧠 Sample Output
vbnet
Copy
Edit
KING RICHARD:
Why, uncle, what's the matter?  
God give you joy of him!  
And will you hence, before I die?

GLOUCESTER:  
Nay, good my lord, be not afraid...  
📌 To-Do
 Add checkpoint saving/loading

 Add temperature sampling and top-k decoding

 Try training on other text datasets

🧠 Credits & Inspiration
Andrej Karpathy's nanoGPT

PyTorch for model building

Tiny Shakespeare Dataset

📄 License
This project is released under the MIT License.

