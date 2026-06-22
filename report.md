
# ReAct Agent Assignment Report

## How LLM is Used for Reasoning
The Large Language Model (LLM) is used in the **Planning Phase** of the ReAct pattern.
The model receives the topic and generates 5–6 research questions that cover different
aspects of the topic. This step represents the reasoning stage where the model decides
what information should be gathered before acting.

The reasoning step works by prompting the LLM with a structured instruction:
'Generate research questions for the topic'. The model analyzes the semantic meaning
of the topic and produces diverse questions that guide the search process.

## Code and Flow Explanation
1. User enters a topic.
2. The Agent calls the LLM to generate research questions.
3. For each question, the Tavily Web Search tool is used to retrieve results.
4. Results are stored in a dictionary.
5. A structured report is generated including:
   - Title
   - Introduction
   - Sections for each research question
   - Conclusion

This follows the ReAct design pattern:
- Reasoning: LLM generates questions.
- Acting: Web search retrieves information.
- Final Answer: Structured report generation.
