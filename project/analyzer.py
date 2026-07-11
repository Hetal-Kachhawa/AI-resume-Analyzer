import json

from langchain_core.prompts import PromptTemplate
from langchain_mistralai import ChatMistralAI

from config import MISTRAL_API_KEY, MODEL_NAME
from prompts import RESUME_ANALYZER_PROMPT


llm = ChatMistralAI(
    model=MODEL_NAME,
    api_key=MISTRAL_API_KEY,
    temperature=0.2,
)

prompt = PromptTemplate(
    template=RESUME_ANALYZER_PROMPT,
    input_variables=["resume"],
)

chain = prompt | llm


def analyze_resume(resume_text: str):

    response = chain.invoke(
        {
            "resume": resume_text
        }
    )

    content = response.content.strip()

    # Remove markdown code fences if present
    if content.startswith("```"):
        content = content.replace("```json", "")
        content = content.replace("```", "")
        content = content.strip()

    # If model writes text before JSON
    start = content.find("{")
    end = content.rfind("}")

    if start != -1 and end != -1:
        content = content[start:end + 1]

    print("\n========== RAW RESPONSE ==========")
    print(content)
    print("==================================\n")

    return json.loads(content)