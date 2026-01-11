# AI Sales Insight Agent (Databricks + LLaMA)

This project demonstrates a **prototype AI agent** that generates business insights from structured sales data.

The objective is to show how **data processing, prompt design, and large language models (LLMs)** can be combined in a clean, modular architecture to support analytical decision-making.

---

## Project Overview

The agent operates in three logical stages:

1. **Data Preparation (Databricks)**
   - Load a real retail sales dataset
   - Clean and standardize columns
   - Aggregate data into business-level summaries

2. **Agent Logic**
   - Convert structured summaries into a reasoning-friendly prompt
   - Define the AI agent’s role as a business analyst

3. **LLM Reasoning (LLaMA)**
   - Send the prompt to a locally hosted LLaMA 3 model
   - Generate natural-language insights such as trends, seasonality, and regional performance

This separation mirrors real-world enterprise systems where data platforms and model inference are decoupled.

---

## Architecture

```
Sales Dataset (CSV)
        ↓
Databricks Notebook
- Data cleaning
- Aggregations
- Summary generation
        ↓
Prompt Builder
        ↓
Local LLaMA 3 (via Ollama)
        ↓
Business Insights (Text)
```

---

## Dataset

- Public **Superstore / Retail Sales dataset**
- Columns used:
  - Order Date
  - Region
  - Category
  - Sales
- Used strictly for analytical and educational purposes

---

## Tech Stack

- Python
- Databricks Community Edition
- Pandas
- LLaMA 3 (local inference via Ollama)
- Prompt Engineering

No paid APIs are required.

---

## Project Structure

```
ai-sales-insight-agent/
│
├── data/
│   └── sales_data.csv
│
├── databricks/
│   └── sales_analysis.ipynb
│
├── llama/
│   └── llama_client.py
│
├── test_llama.py
│
└── README.md
```

---

## How It Works

1. The Databricks notebook:
   - Loads and cleans the sales dataset
   - Aggregates sales by month, region, and category
   - Generates a structured summary dictionary

2. A prompt is built from the summary:
   - Grounds the model in numerical business data
   - Clearly defines the reasoning task

3. The prompt is sent to a locally running LLaMA model:
   - The model reasons over trends and patterns
   - Returns human-readable business insights

---

## Example Questions the Agent Can Answer

- Why did sales decline in certain months?
- Which regions underperformed?
- Are there seasonal patterns in sales?
- Which product categories contribute most to revenue?

---

## Notes

- This is a **prototype-level project**, not a production deployment
- Databricks is used to mirror enterprise data workflows
- The LLM layer is **model-agnostic** and can be replaced with hosted APIs if required
- Focus is on **agent design, data grounding, and reasoning**, not UI or deployment

---

## Learning Outcomes

- Working with real datasets in a managed data platform
- Designing AI agents using structured context instead of raw data
- Integrating local LLMs without paid APIs
- Understanding system boundaries between data, logic, and models
