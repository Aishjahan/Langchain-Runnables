from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel, RunnableSequence

load_dotenv()

model = ChatOpenAI()

prompt1 = PromptTemplate(
    template="Generate a tweet about {topic}", input_variables=["topic"]
)

prompt2 = PromptTemplate(
    template="Generate a Linkedin Post about {topic}", input_variables=["topic"]
)

parser = StrOutputParser()

parallel_chain = RunnableParallel(
    {
        "tweet": RunnableSequence(prompt1, model, parser),
        "linkedin": RunnableSequence(prompt2, model, parser),
    }
)

result = parallel_chain.invoke({"topic": "Machine Learning"})
# result will come in the form of dictionary

print(result)
