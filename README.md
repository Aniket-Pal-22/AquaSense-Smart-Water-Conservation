# 💧 AquaSense: Automated Public Tap Management System

AquaSense is a conceptual IoT and AI-driven solution designed to prevent public water wastage from open, dripping, or unattended taps in high-traffic urban and rural spaces. Inspired by concepts explored during the **1M1B & IBM SkillsBuild AI for Sustainability Internship**[cite: 1].

## 🎯 Problem Statement
Public taps frequently suffer from continuous water wastage due to valves left open, slow leaks, and lack of real-time monitoring—leading to significant daily losses of clean water.

## 🌍 UN SDG Alignment
* **SDG 6 (Clean Water and Sanitation):** Improving water-use efficiency and reducing avoidable wastage in shared water points.

## 🛠️ Proposed Architecture & Stack
* **Hardware (Concept):** ESP32 / microcontroller unit, IR/Ultrasonic proximity sensing, solenoid valve control, and flow rate sensing.
* **Simulation & Control Logic:** Python-based simulation of user presence, auto-shutoff timers, and cumulative water savings.
* **AI & Analytics Layer:** Agentic/RAG-inspired query workflows to summarize conservation metrics and check water guidelines.

## 📂 Repository Structure
* [`architecture/system-flow.md`](./architecture/system-flow.md) — End-to-end control and monitoring flow diagram.
* [`simulation/aquasense_sim.py`](./simulation/aquasense_sim.py) — Interactive/scripted simulation of tap triggers and water saved.
* [`ai-analytics/rag_query_logic.py`](./ai-analytics/rag_query_logic.py) — Prototype logic for retrieving conservation guidelines and generating status summaries.
