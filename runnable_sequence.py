from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence

load_dotenv()

model = ChatOpenAI()

prompt1 = PromptTemplate(
    template="Tell me a joke on {topic}", input_variables=["topic"]
)

prompt2 = PromptTemplate(
    template="Explain the following joke - {text}", input_variables=["text"]
)

parser = StrOutputParser()

chain = RunnableSequence(prompt1, model, parser, prompt2, model, parser)

result = chain.invoke({"topic": "Government"})

print(result)
