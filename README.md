🚀 AI-Powered WhatsApp Order Automation System

Turn messy WhatsApp chats into structured business insights automatically using AI.

📌 Overview

This project is an end-to-end intelligent automation system that:

📥 Reads WhatsApp chat exports
🖼️ Identifies products from images using AI
🧾 Generates structured orders with IDs & timestamps
📊 Creates Excel reports automatically
🤖 Uses an agent-based architecture for orchestration
💼 Real Business Use Case

Perfect for:

Saree / boutique businesses
Small e-commerce sellers using WhatsApp
D2C brands without formal order systems

👉 Eliminates manual tracking → saves hours daily

🔥 Key Features
🧠 AI Image Matching
Matches customer-shared images with catalog
Uses CLIP-based similarity
Only high-confidence matches are processed
📦 Automated Order Creation
Generates:
Unique Order ID (UUID)
Timestamp
Product & price
Stores images per order
📊 Auto Reporting
Generates:
orders.xlsx
report.xlsx (revenue summary)
🤖 Agent-Based Architecture
Built using CrewAI-style agents
Modular & scalable system design
🔒 Privacy-Friendly
Runs locally using Ollama
No external API dependency required
🏗️ Project Architecture
core/        → Business logic (fast, reliable)
tools/       → Agent tool wrappers
agents/      → AI agents (orchestration layer)
main.py      → Direct pipeline execution
agent_main.py→ Agent-based execution
⚙️ Tech Stack
Python 🐍
Pandas (data processing)
CLIP (image matching)
CrewAI (agent orchestration)
Ollama (phi3) for local LLM
🚀 Installation Guide
1️⃣ Clone the repo
git clone <your-repo-url>
cd agentic-whatsapp-system
2️⃣ Install dependencies
pip install -r requirements.txt
3️⃣ Install Ollama

Download: https://ollama.com

4️⃣ Pull lightweight model
ollama pull phi3
5️⃣ Start Ollama
ollama serve
▶️ How to Run
✅ Option 1: Fast Pipeline (Recommended)
python main.py

✔ Deterministic
✔ Fast
✔ Production-ready

🤖 Option 2: Agent Mode
python agent_main.py

✔ AI-driven orchestration
✔ Demo-friendly

📂 Input Data Format

Place your WhatsApp export here:

data/whatsapp_export/
    ├── chat.txt
    ├── image1.jpg
    ├── image2.jpg
📊 Output
output/
    ├── orders.xlsx
    ├── report.xlsx

data/order_images/
    ├── order_<id>/
🧠 How It Works
Parse WhatsApp chat
Extract order-related messages
Detect attached images
Match images with catalog using AI
Create structured orders
Generate reports
⚡ Performance Optimization
Uses lightweight LLM (phi3)
Minimal LLM dependency (most logic is deterministic)
Optimized for low-resource machines
🔮 Future Enhancements
📄 Invoice PDF generation
📈 Dashboard (Streamlit)
☁️ Cloud deployment
📲 WhatsApp API integration
🧠 Improved AI matching
💡 Why This Project Stands Out
Real-world business problem
End-to-end automation
Combines AI + data engineering
Client-ready architecture
👨‍💻 Author

Built as a real-world AI automation system for small businesses.

⭐ If you like this project

Give it a ⭐ on GitHub — it helps a lot!

🎯 POSITIONING (IMPORTANT)

When you present this project, say:

“This is a hybrid AI system combining deterministic pipelines with lightweight local LLMs to automate unstructured WhatsApp-based commerce.”
