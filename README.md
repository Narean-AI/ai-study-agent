# 🧠 AI Study Planner Agent (Offline)

A simple offline AI agent built using Python and Ollama.

This project generates structured study plans using a locally running Large Language Model (LLM).

---

## 🚀 Features

- Runs completely offline
- Uses Ollama for local LLM execution
- Generates structured study plans
- Lightweight and beginner-friendly

---

## 🛠 Tech Stack

- Python
- Ollama
- Llama3 / Mistral

---

## 📂 Project Structure

ai-agent/
│
└── main.py

---

## ⚙️ Installation

1. Install Ollama from https://ollama.com

2. Pull the model:

ollama pull llama3

3. Install Python dependency:

pip install ollama

4. Run the project:

python main.py

---

## ▶️ How to Use

After running the program, you will see:

Enter your goal:

Type your study goal.

Example:

Create a 1 week DSA study plan

The AI agent will generate a structured study roadmap in the terminal.

---

## 🧪 Example

Input:
Create a 1 week DSA study plan

Output:
Day 1: Arrays – fundamentals and practice  
Day 2: Strings – manipulation and problems  
Day 3: Recursion basics  
Day 4: Sorting algorithms  
Day 5: Searching techniques  
Day 6: Stack and Queue basics  
Day 7: Revision and problem-solving  

---

## 🧠 How It Works

1. The user enters a goal.  
2. The program sends the prompt to the Llama3 model using Ollama.  
3. The model generates a structured response.  
4. The response is displayed in the terminal.  



