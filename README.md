# 🧠 Market Trend Analysis — Multi-Agent System (ADK)

<div align="center">

![IIT Ropar](https://img.shields.io/badge/IIT%20Ropar-Final%20Semester-blue?style=for-the-badge)
![Framework](https://img.shields.io/badge/Framework-Google%20ADK-00acc1?style=for-the-badge&logo=google)
![Agents](https://img.shields.io/badge/Agents-Sequential%20%2B%20Loop-6a1b9a?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active%2010--Day%20Challenge-orange?style=for-the-badge)

</div>

---

<div align="center">

### 🚀 A modular, **agentic AI system** for real-world **market trend analysis** across **8 domains**

Built with **Google ADK** • **Sequential + Loop** agent patterns • **Free tools/MCPs** only

</div>

---

## 🎓 Academic Project Details

<table>
<tr>
<td><strong>🏫 Institution</strong></td>
<td>Indian Institute of Technology Ropar</td>
</tr>
<tr>
<td><strong>📚 Course</strong></td>
<td>Final Semester Module</td>
</tr>
<tr>
<td><strong>🔧 Project Type</strong></td>
<td>Multi-Agent System Architecture</td>
</tr>
<tr>
<td><strong>⚡ Framework</strong></td>
<td>Google Agent Development Kit (ADK)</td>
</tr>
<tr>
<td><strong>🔄 Pattern</strong></td>
<td><strong>Sequential + Loop</strong> orchestration (simple, robust, maintainable)</td>
</tr>
</table>

> [!NOTE]
> **10-Day AI Challenge**  
> I'm building and documenting this system in **10 days**—end-to-end, domain by domain. Follow daily progress on Medium & LinkedIn (links below).

---

## 🔗 Quick Links

| Platform | Link |
|----------|------|
| 📖 **Live Dev Updates (Medium)** | [https://medium.com/@srinivasvarma764](https://medium.com/@srinivasvarma764) |
| 💼 **Connect (LinkedIn)** | [https://www.linkedin.com/in/srinivas-nampalli/](https://www.linkedin.com/in/srinivas-nampalli/) |
| 🔗 **Repository** | [https://github.com/Srinivas26k/Market-trend/](https://github.com/Srinivas26k/Market-trend/) |

---

## 🌟 What This System Does

<div align="center">

### 🎯 8 Domain Trend Analysis

</div>

<table>
<tr>
<td align="center"><strong>📈</strong><br/>Stock Market</td>
<td align="center"><strong>🛒</strong><br/>E-Commerce</td>
<td align="center"><strong>💼</strong><br/>Jobs</td>
<td align="center"><strong>📱</strong><br/>Social Media</td>
</tr>
<tr>
<td align="center"><strong>✈️</strong><br/>Travel</td>
<td align="center"><strong>💭</strong><br/>Consumer Sentiment</td>
<td align="center"><strong>🔬</strong><br/>Tech Innovation</td>
<td align="center"><strong>🌍</strong><br/>Regional Demand</td>
</tr>
</table>

### 🏗️ Key Features

- **🤖 Agent Orchestration:** Simple **Sequential** + **Loop** pattern per team
- **💰 Free Tools Only:** `yfinance`, `browser-use` MCP, HuggingFace (local), `pandas`, `reportlab`, `streamlit`
- **📊 Interactive Output:** PDF reports + lightweight Streamlit dashboard (on demand)
- **🧩 Modular:** Each domain is a minimal, swappable team (1 sequential agent + 1 loop validator)

---

## 🏗️ Architecture (Mermaid)

> Replace the placeholder below with your diagram if you export it as an image, or keep the Mermaid live.

```mermaid
flowchart TD
    %% --- Styles ---
    classDef user fill:#ffc0cb,stroke:#333,stroke-width:2px;
    classDef orchestrator fill:#add8e6,stroke:#333,stroke-width:4px;
    classDef agent fill:#d3d3d3,stroke:#333,stroke-width:2px;
    classDef loop fill:#fff0b3,stroke:#ffc107,stroke-width:2px,stroke-dasharray:5 5;
    classDef report fill:#f5f5f5,stroke:#616161,stroke-dasharray: 5 5;
    classDef final_output fill:#fffde7,stroke:#fbc02d,stroke-width:2px;

    %% --- User Entry ---
    user([User]) --> greeting_agent(Greeting Agent)
    greeting_agent --> root_orchestrator{Root Orchestrator}

    class user user;
    class greeting_agent agent;
    class root_orchestrator orchestrator;

    %% --- Teams ---
    subgraph stock_team [Stock Market Team]
        market_data[Market Data Agent<br/>Tool: yfinance]:::agent --> validator_stock{Data Validator}:::loop
        validator_stock -- Retry --> market_data
        validator_stock -- OK --> stock_report([Stock Report]):::report
    end

    subgraph ecom_team [E-Commerce Team]
        product_scraper[Product Scraper Agent<br/>Tool: browser-use]:::agent --> validator_ecom{Scrape Validator}:::loop
        validator_ecom -- Retry --> product_scraper
        validator_ecom -- OK --> ecom_report([E-commerce Report]):::report
    end

    subgraph jobs_team [Jobs Team]
        job_scraper[Job Scraper Agent<br/>Tool: browser-use]:::agent --> validator_jobs{Job Validator}:::loop
        validator_jobs -- Retry --> job_scraper
        validator_jobs -- OK --> jobs_report([Jobs Report]):::report
    end

    subgraph social_team [Social Media Team]
        social_scraper[Social Scraper Agent<br/>Tool: browser-use]:::agent --> validator_social{Social Validator}:::loop
        validator_social -- Retry --> social_scraper
        validator_social -- OK --> social_report([Social Report]):::report
    end

    subgraph travel_team [Travel Team]
        travel_scraper[Travel Scraper Agent<br/>Tool: browser-use]:::agent --> validator_travel{Travel Validator}:::loop
        validator_travel -- Retry --> travel_scraper
        validator_travel -- OK --> travel_report([Travel Report]):::report
    end

    subgraph consumer_team [Consumer Sentiment Team]
        review_scraper[Review Scraper Agent<br/>Tools: browser-use + HF]:::agent --> validator_sentiment{Sentiment Validator}:::loop
        validator_sentiment -- Retry --> review_scraper
        validator_sentiment -- OK --> consumer_report([Consumer Report]):::report
    end

    subgraph tech_team [Tech Innovation Team]
        tech_scraper[Tech Scraper Agent<br/>Tool: browser-use]:::agent --> validator_tech{Tech Validator}:::loop
        validator_tech -- Retry --> tech_scraper
        validator_tech -- OK --> tech_report([Tech Report]):::report
    end

    subgraph regional_team [Regional Demand Team]
        regional_scraper[Regional Scraper Agent<br/>Tool: browser-use]:::agent --> validator_regional{Regional Validator}:::loop
        validator_regional -- Retry --> regional_scraper
        validator_regional -- OK --> regional_report([Regional Report]):::report
    end

    %% --- Report Aggregation ---
    stock_report --> report_agent(Report Agent<br/>Tool: LiteLlm):::agent
    ecom_report --> report_agent
    jobs_report --> report_agent
    social_report --> report_agent
    travel_report --> report_agent
    consumer_report --> report_agent
    tech_report --> report_agent
    regional_report --> report_agent

    report_agent --> output_agent(Final Output<br/>Tools: reportlab + Streamlit):::agent
    output_agent --> user

    class output_agent final_output;
```

---

## ✅ Current Status (MVP First)

> [!SUCCESS]
> **Stock Market Team — Implemented** ✅

<div align="center">

| Component | Status | Description |
|-----------|--------|-------------|
| **📊 Sequential** | ✅ | `market_data_agent` → fetch OHLCV via `yfinance`, compute SMA/RSI (`pandas`/`pandas-ta`) |
| **🔄 Loop** | ✅ | `data_validator_agent` → validate NaNs/empties; retry once if invalid |
| **📋 Output** | ✅ | compact JSON + (optional) chart/table for downstream |

</div>

<div align="center">

![Free Tools](https://img.shields.io/badge/Free-Tools-brightgreen?style=flat-square)
![No Auth](https://img.shields.io/badge/No-Auth-blue?style=flat-square)
![Retry Once](https://img.shields.io/badge/Retry-Once-orange?style=flat-square)

</div>

---

## 🧩 Tech Stack

<div align="center">

### Core Technologies

</div>

<table>
<tr>
<td><strong>🤖 Agent Framework</strong></td>
<td>Google <strong>ADK</strong> (Agents, Orchestration)</td>
</tr>
<tr>
<td><strong>🧠 LLM Glue</strong></td>
<td><strong>LiteLlm</strong> via <strong>OpenRouter</strong> (free <code>gpt-oss-20b:free</code>)</td>
</tr>
<tr>
<td><strong>📈 Finance</strong></td>
<td><code>yfinance</code>, <code>pandas</code>, <code>pandas-ta</code></td>
</tr>
<tr>
<td><strong>🌐 Web/MCP</strong></td>
<td><strong>browser-use MCP</strong> + <code>BeautifulSoup</code></td>
</tr>
<tr>
<td><strong>🔤 NLP (optional)</strong></td>
<td>HuggingFace <code>distilbert-base-uncased-finetuned-sst-2-english</code></td>
</tr>
<tr>
<td><strong>📊 Output</strong></td>
<td><code>reportlab</code> (PDF), <code>streamlit</code> (dashboard), <code>matplotlib/plotly</code></td>
</tr>
</table>

> [!TIP]
> All chosen to be **free** and **auth-light/no-auth** wherever possible.

---

## 📁 Repository Structure

```
Market-trend/
├── greeting_agent/
│   ├── __init__.py
│   └── agent.py
├── stock_market_team/
│   ├── subagents/
│   │   ├── stock_data_retrieval/
│   │   │   ├── __init__.py
│   │   │   └── agent.py
│   │   ├── stock_data_analysis/
│   │   │   ├── __init__.py
│   │   │   └── agent.py
│   │   ├── stock_data_validation/
│   │   │   ├── __init__.py
│   │   │   └── agent.py
│   │   └── stock_data_visualization/
│   │       ├── __init__.py
│   │       └── agent.py
│   ├── __init__.py
│   └── agent.py
├── report_agent/
│   └── agent.py
├── output_agent/
│   └── agent.py
├── guide.md
├── README.md
└── requirements.txt
```

---

## ⚙️ Setup

### Prerequisites

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-3776ab?style=for-the-badge&logo=python&logoColor=white)
![OpenRouter](https://img.shields.io/badge/OpenRouter-Optional-ff6b6b?style=for-the-badge)

</div>

- Python **3.8+**
- (Optional) OpenRouter key if you want LLM narrative summaries

### Install

```bash
git clone https://github.com/Srinivas26k/Market-trend.git
cd Market-trend
pip install -r requirements.txt
```

### Environment (optional for LLM)

```bash
# .env
OPENROUTER_API_KEY=your_key_here
```

---

## 🚀 Usage (Stock Team Demo)

```python
# examples/demo_stock.py
from stock_market_team.agent import run_stock_pipeline

result = run_stock_pipeline(
    symbol="INFY.NS",
    period="3mo",
    indicators=["SMA_20","RSI_14"],
    retry=True  # loop agent will refetch once if invalid
)
print(result["summary"])
```

> [!NOTE]
> The **greeting agent** → **root orchestrator** route will be used in the UI flow.
> Programmatic demos let you test sub-teams in isolation.

---

## 🧰 MCP / Tools Configuration

<div align="center">

### Tool Stack Overview

</div>

<table>
<tr>
<td><strong>📈 Stock</strong></td>
<td><code>yfinance</code>, <code>pandas</code>, <code>pandas-ta</code> (no auth)</td>
</tr>
<tr>
<td><strong>🕷️ Scraping</strong></td>
<td><strong>browser-use MCP</strong> + <code>BeautifulSoup</code> (free)</td>
</tr>
<tr>
<td><strong>🔤 NLP (optional)</strong></td>
<td>HuggingFace local models (free)</td>
</tr>
<tr>
<td><strong>📊 Reports</strong></td>
<td><code>reportlab</code> (PDF), <code>streamlit</code> (dashboard)</td>
</tr>
</table>

> [!TIP]
> Keep it simple: 1 **Sequential** agent + 1 **Loop** agent per domain.

---

## 🗺️ 10-Day Roadmap

<div align="center">

### Development Timeline

</div>

- [x] **Day 1–2:** Core scaffolding + **Stock Market Team**
- [ ] **Day 3–4:** **E-Commerce** & **Jobs**
- [ ] **Day 5–6:** **Social** & **Travel**
- [ ] **Day 7–8:** **Consumer Sentiment** & **Tech Innovation**
- [ ] **Day 9–10:** **Regional Demand** + Integration + Polish

---

## 🤝 Contributing

<div align="center">

### Join the Development

</div>

1. ⭐ **Star** & 👀 **Watch** the repo
2. Create a feature branch:
   ```bash
   git checkout -b feature/new-domain-team
   ```
3. Implement: **Sequential + Loop** minimal pair
4. Add tests & docs; open a PR

---

## 📘 Academic Notes & Disclaimer

> [!WARNING]
> This project is developed for academic purposes (IIT Ropar, Final Semester).
> All analyses are **educational** and **not financial advice**.

---

## 🧑‍💻 About the Author

<div align="center">

### Hi, I'm **Srinivas Varma** — building practical, agentic AI systems.

[![Medium](https://img.shields.io/badge/Medium-Follow%20Updates-12100E?style=for-the-badge&logo=medium&logoColor=white)](https://medium.com/@srinivasvarma764)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](#)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-181717?style=for-the-badge&logo=github&logoColor=white)](#)

</div>

> [!NOTE]
> If you like this project, please ⭐ **star** the repo and share feedback!

---

## 📄 License

<div align="center">

![MIT License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

**MIT License** — free for academic and educational use.

</div>
