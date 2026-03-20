# Python Toolbox 🛠️🐍

A curated collection of personal Python scripts, automation tools, and experiments. This repository serves as my "Swiss Army Knife" for solving daily technical challenges, from web monitoring to blockchain data analysis.

## 📂 Project Structure

### 🌐 Web Automation & Monitoring
Scripts designed to track web changes and automate browser-related tasks.
* **[Web Monitor](./Web-Automation/monitor_rapido.py):** Monitors specific URLs for content changes and sends real-time alerts via **Discord Webhooks**. Uses `difflib` for text comparison and `hashlib` for integrity checks.

### 🔗 Web3 & Blockchain Tools
Utilities for interacting with decentralized networks and analyzing on-chain data.
* **[Solana Token Holders](./Web3-Blockchain/holders.py):** Fetches all wallet addresses for a specific Token Mint using the **Helius RPC API**.
* **[Common Holders Analyzer](./Web3-Blockchain/holders2.py):** A data analysis tool that uses **Pandas** and set theory to find overlapping investors across multiple CSV datasets.

### 📁 File & System Utilities
Automation for local OS tasks.
* *(Upcoming: Bulk renamers, backup managers, and system cleanup tools)*

## 🛠️ Tech Stack
* **Core:** Python 3.10+
* **Data & APIs:** `Pandas`, `Requests`, `JSON`, `CSV`.
* **Security & Network:** `Hashlib`, `Helius RPC`, `Discord API`.
* **Standard Libs:** `Difflib`, `Os`, `Time`, `Re`.

## ⚙️ Safety
1. **Environment Variables:** Most scripts require API Keys or Webhooks. Ensure you set your own keys in the code or use a `.env` file (recommended).
2. **Note on Confidentiality:** All sensitive keys, tokens, and private data have been removed from this public repository.

---
*Developed and maintained by Bautista Galmarini.*
