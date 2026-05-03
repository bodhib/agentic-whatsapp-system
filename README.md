🤖 AI Agent-Powered WhatsApp Order Automation System

Transform unstructured WhatsApp conversations into fully automated business workflows using intelligent AI agents.

📌 Overview

This project is an Agentic AI system that autonomously:

📥 Understands WhatsApp chat data
🖼️ Identifies products from customer images
🧾 Creates structured orders with metadata
📊 Generates business reports
🤖 Uses multiple AI agents to coordinate the entire workflow
💼 Real Business Impact

Designed for:

Saree & boutique sellers
WhatsApp-based businesses
Small D2C brands

👉 Eliminates manual order tracking
👉 Converts chat → structured data automatically

🔥 Core Capabilities
🤖 Multi-Agent System

The system uses specialized AI agents:

Agent	Responsibility
Ingestion Agent	Loads chat & media
Parsing Agent	Extracts structured order data
Vision Agent	Matches product images
Order Agent	Creates finalized orders
Reporting Agent	Generates reports

👉 Each agent performs a specific role, making the system modular and scalable.

🧠 AI Image Understanding
Matches customer images with product catalog
Uses similarity-based AI matching
Processes only high-confidence matches
📦 Autonomous Order Processing
Generates:
Unique Order ID (UUID)
Timestamp
Product & pricing info
Organizes images per order
📊 Automated Reporting
Creates structured Excel outputs:
Orders data
Revenue summary
🔒 Privacy-First AI
Runs locally using Ollama
No dependency on external APIs
Ensures data privacy and zero recurring cost
🏗️ Architecture
agents/      → AI agents (decision-making layer)
tools/       → Agent tools (execution layer)
core/        → Business logic (processing layer)
agent_main.py→ Agent orchestration entry point
⚙️ Tech Stack
Python 🐍
CrewAI (multi-agent framework)
Pandas (data processing)
CLIP (image matching)
Ollama (phi3) – lightweight local LLM
🚀 Setup Guide
1️⃣ Clone Repository
git clone <your-repo-url>
cd agentic-whatsapp-system
2️⃣ Install Dependencies
pip install -r requirements.txt
3️⃣ Install Ollama

Download from: https://ollama.com

4️⃣ Pull Lightweight Model
ollama pull phi3
5️⃣ Start Ollama Server
ollama serve
▶️ Run the Agent System
python agent_main.py
📂 Input Format
data/whatsapp_export/
    ├── chat.txt
    ├── image1.jpg
    ├── image2.jpg
📊 Output
output/
    ├── orders.xlsx
    ├── report.xlsx

data/order_images/
    ├── order_<order_id>/
🧠 How the Agent System Works
Ingestion Agent loads WhatsApp data
Parsing Agent extracts order details
Vision Agent identifies products from images
Order Agent structures the order data
Reporting Agent generates business insights

👉 Entire workflow is autonomously coordinated by agents

⚡ Performance Design
Lightweight LLM (phi3) for fast execution
Minimal dependency on AI (logic handled in code)
Optimized for local machines
🔮 Future Enhancements
📄 Invoice generation (PDF)
📊 Interactive dashboard (Streamlit)
☁️ Cloud deployment
📲 WhatsApp API integration
🧠 Improved AI matching
💡 Why This Project is Unique
True Agentic AI system (not just scripts)
Real-world business automation
Modular and scalable design
Privacy-first architecture
👨‍💻 Author

Built as a production-style AI automation system for real businesses.

⭐ Support

If you found this useful, consider giving it a ⭐ on GitHub!

🎯 How to Pitch This Project

Use this line:

“This is a multi-agent AI system that converts unstructured WhatsApp conversations into structured business workflows using local AI models.”
