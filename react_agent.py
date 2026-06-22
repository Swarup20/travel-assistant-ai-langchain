
# react_agent.py
# ReAct Web Research Agent using LLM (OpenAI) + Tavily Web Search

import os
from tavily import TavilyClient
from openai import OpenAI

# ================= CONFIG =================
OPENAI_API_KEY = "YOUR_OPENAI_API_KEY"
TAVILY_API_KEY = "YOUR_TAVILY_API_KEY"

client = OpenAI(api_key=OPENAI_API_KEY)
tavily = TavilyClient(api_key=TAVILY_API_KEY)

# ==========================================

class ReactResearchAgent:
    def __init__(self, topic):
        self.topic = topic
        self.questions = []
        self.search_results = {}

    def generate_questions(self):
        prompt = f"""Generate 5–6 research questions about the topic: {self.topic}"""
        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[{"role":"user","content":prompt}]
        )
        text = response.choices[0].message.content
        self.questions = [q.strip("- ") for q in text.split("\n") if q.strip()]
        return self.questions

    def search_web(self):
        for q in self.questions:
            results = tavily.search(query=q, max_results=3)
            self.search_results[q] = results
        return self.search_results

    def generate_report(self):
        report = f"# Research Report: {self.topic}\n\n"
        report += "## Introduction\nThis report was generated using a ReAct Agent.\n\n"

        for q, results in self.search_results.items():
            report += f"## {q}\n"
            for r in results["results"]:
                report += f"- {r['title']}: {r['content']}\n"
            report += "\n"

        report += "## Conclusion\nThe agent gathered web-based insights using LLM planning and tool-based execution."
        return report


if __name__ == "__main__":
    topic = input("Enter topic: ")
    agent = ReactResearchAgent(topic)

    print("Generating questions...")
    agent.generate_questions()

    print("Searching web...")
    agent.search_web()

    print("Generating report...")
    final_report = agent.generate_report()
    print(final_report)
