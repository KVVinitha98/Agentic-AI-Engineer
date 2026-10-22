from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama
import os



def main() -> None:
    # print("Hello from langchain-course!")

    information = "A software developer with three years of experience is exploring agentic AI, collaborating with a supportive team, and committed to continuous learning."
    summary_template = """ Take the information {information} and provide a summary. """
    summary_prompt = PromptTemplate(input_variables=["information"], template=summary_template)
    llm = ChatOllama(temperature=0.7,model="gemma3:270m")
    chain = summary_prompt | llm
    response = chain.invoke(input={"information": information})
    print(response.content)





if __name__ == "__main__":
    main()
