**AI-Powered WhatsApp Order Automation System**

An end-to-end AI-assisted automation platform that converts raw WhatsApp business exports into structured sales orders using:

🤖 Agentic AI orchestration
🖼️ CLIP-based image matching
📊 Automated reporting & analytics
📁 WhatsApp export parsing
🧠 Smart embedding caching
🌐 Streamlit dashboard

Designed for saree businesses, fashion sellers, wholesalers, and catalog-driven commerce workflows.

🚀 Features
✅ WhatsApp Export Automation

Process complete WhatsApp exports containing:
- chat.txt
- customer images

The system automatically:
- parses chats
- extracts image references
- processes customer order requests

✅ AI Agent Workflow

Built using:
- CrewAI
- Google Gemini

A lightweight orchestration agent coordinates:
- order parsing
- image matching
- reporting workflow
- 
✅ CLIP-Based Product Matching

Uses:
- OpenAI CLIP
to intelligently match:
- customer-uploaded saree images with catalog product images

Supports:
- visually similar products
- color variations
- real-world WhatsApp order screenshots

✅ Smart Embedding Cache

Catalog embeddings are cached locally to:
- reduce repeated processing
- improve performance
- minimize AI compute overhead

✅ Streamlit Dashboard

Interactive UI for:
- uploading WhatsApp exports
- running automation workflows
- downloading reports

Built with:
- Streamlit
- 
✅ Automated Reporting

Generates:
- orders.xlsx
- sales reports
- analytics-ready structured data

🏗️ Architecture
Streamlit Dashboard
        ↓
AI Automation Agent
        ↓
Tool-Based Workflow
        ↓
Deterministic Python Services
        ↓
CLIP Image Matching
        ↓
Excel Reports & Analytics

📂 Project Structure
agentic-whatsapp-system/
│
├── agents/
│   └── agents.py
│
├── tools/
│   └── order_tools.py
│
├── core/
│   ├── parser_service.py
│   ├── vision_service.py
│   ├── order_service.py
│   ├── reporting_service.py
│   ├── media_handler.py
│   └── workspace_manager.py
│
├── data/
│   ├── catalog/
│   ├── images/
│   └── whatsapp_export/
│
├── cache/
│   └── catalog_embeddings.pkl
│
├── output/
│   ├── orders.xlsx
│   └── report.xlsx
│
├── app.py
├── agent_main.py
├── requirements.txt
└── .env

⚡ Installation

1️⃣ Clone Repository
git clone <your_repo_url>
cd agentic-whatsapp-system

2️⃣ Create Virtual Environment
Windows
python -m venv venv
venv\Scripts\activate

Linux / Mac
python3 -m venv venv
source venv/bin/activate

3️⃣ Install Dependencies
pip install -r requirements.txt

🔑 Environment Variables

Create a .env file:
GOOGLE_API_KEY=your_gemini_api_key

Get Gemini API Key from:
- Google AI Studio

🖼️ Catalog Setup

Place catalog product images inside:
data/catalog/

Example:
data/catalog/
    ├── saree_001.jpg
    ├── saree_002.jpg
    ├── saree_003.jpg

📄 Catalog CSV Format

Example:
image,product_name,price
saree_001.jpg,Red Banarasi Saree,2500
saree_002.jpg,Blue Silk Saree,3200

🚀 Running from Console

Place WhatsApp export files inside:
data/whatsapp_export/

Example:
data/whatsapp_export/
    ├── chat.txt
    ├── IMG-20260401-WA001.jpg
    ├── IMG-20260401-WA002.jpg

Run:

python agent_main.py
🌐 Running Streamlit Dashboard

Start dashboard:
streamlit run app.py

Then:
- Upload WhatsApp export ZIP
- Click Process Orders
- Download generated reports

🧠 How AI Workflow Works
Step 1 — WhatsApp Parsing

The system:
- reads chat.txt
- extracts image references
- structures order data

Step 2 — Image Processing

- Customer images are:
- automatically moved
- encoded using CLIP embeddings

Step 3 — Product Matching

The system compares:
- customer image embeddings with catalog embeddings to identify the closest product.

Step 4 — Order Generation

Structured orders are generated with:
- order IDs
- matched products
- confidence scores

Step 5 — Reporting

Excel reports are automatically generated.

📊 Generated Outputs
Orders File
output/orders.xlsx

Contains:
- order ID
- matched product
- confidence score
- timestamps

Analytics Report
output/report.xlsx

Contains:
- sales summary
- analytics-ready data

⚡ Performance Optimizations
✅ Embedding Cache

Catalog embeddings are cached locally:
cache/catalog_embeddings.pkl to avoid repeated CLIP encoding.

✅ Lightweight AI Orchestration

Only ONE lightweight AI agent is used.

Business logic remains:
- deterministic
- fast
- low-cost

🛠️ Tech Stack
Component	        Technology
AI Orchestration	CrewAI
LLM	Google          Gemini
Computer Vision	    OpenAI CLIP
UI Dashboard	    Streamlit
Data Processing	    Pandas
Reporting	        OpenPyXL
ML Framework	    PyTorch

🎯 Real-World Use Cases
- Saree businesses
- Fashion wholesalers
-WhatsApp commerce automation
- Catalog order management
- AI-assisted retail workflows

🚀 Future Enhancements
- WhatsApp Business API integration
- Real-time dashboard analytics
- Google Sheets sync
- Auto daily scheduling
- Customer reply automation
- Cloud deployment
- Multi-user support

📸 Demo Workflow
Export WhatsApp Chat
        ↓
Zip Export Folder
        ↓
Upload to Dashboard
        ↓
AI Agent Processes Orders
        ↓
Download Excel Reports

🤝 Contributing

Pull requests are welcome.

For major changes:
- open an issue first
- discuss proposed improvements

📜 License

MIT License

⭐ If You Like This Project

Please consider:
- starring the repository
- sharing feedback
- contributing improvements