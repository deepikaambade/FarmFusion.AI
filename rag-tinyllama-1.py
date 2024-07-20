# Importing libraries
from langchain_community.llms import Ollama
from langchain_community.embeddings import OllamaEmbeddings
from langchain_core.output_parsers import StrOutputParser
from langchain_community.document_loaders import PyPDFLoader
from langchain.prompts import PromptTemplate
from langchain_community.vectorstores import DocArrayInMemorySearch
from operator import itemgetter

# Model and embeddings selection
MODEL = 'tinyllama'
model = Ollama(model=MODEL)
embeddings = OllamaEmbeddings(model=MODEL)

parser = StrOutputParser()
# chain = model | parser

# ASking for input file path
file_to_read = input("C:\Users\deepi\Downloads\output.pdf")

# Loading and splitting the file
# loader = PyPDFLoader("doc1.pdf")
loader = PyPDFLoader(file_to_read)
pages = loader.load_and_split()

# Prompt Template making
template = """
Answer the Q based on the context given below.
If you don't know the answer, say "I don't know"

Context: {context}

Question: {question}

"""

# Defining the prompt
prompt = PromptTemplate.from_template(template)

# chain = prompt | model | parser

# Creating the vector store search
vectorstore = DocArrayInMemorySearch.from_documents(pages, embedding=embeddings)
retriever = vectorstore.as_retriever()

# Complete chain structure
chain = (
    {
        "context" : itemgetter("question") | retriever,
        "question" : itemgetter("question")
    }
    | prompt
    | model
    | parser
)

# Asking the questions
for x in range(1000):
    print ("You may ask " + str(1000-x) + " questions about the document. To quit, type 'bye'. ")
    q1 = input("What is your question regarding the document? \n --> ")
    print ("\n")
    if (q1 == 'bye'):
        break
    a1 = chain.invoke({"question": q1})
    print (a1)
    print ("\n")
# q1 = input("What is your question regarding the document?")
# chain.invoke({"question": "What are LLMs?"})
# a1 = chain.invoke({"question": q1})
# print (a1)
