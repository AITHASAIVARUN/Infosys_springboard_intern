!pip install langchain

!pip install langchain_community

!pip install langchain.document_loaders

from langchain.document_loaders import UnstructuredURLLoader

urls = [
    'https://www.livemint.com/economy/budget-2024-key-highlights-live-updates-nirmala-sitharaman-infrastructure-defence-income-tax-modi-budget-23-july-11721654502862.html',
    'https://cleartax.in/s/budget-2024-highlights',
    'https://www.hindustantimes.com/budget',
    'https://economictimes.indiatimes.com/news/economy/policy/budget-2024-highlights-india-nirmala-sitharaman-capex-fiscal-deficit-tax-slab-key-announcement-in-union-budget-2024-25/articleshow/111942707.cms?from=md'
]

!pip install unstructured
import unstructured
from unstructured.__version__ import __version__ as __unstructured_version__

loader = UnstructuredURLLoader(urls=urls)
data = loader.load()
data

print(len(data))

!pip install langchain_text_splitter

from langchain.text_splitter import RecursiveCharacterTextSplitter
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000)
docs = text_splitter.split_documents(data)
print(len(docs))

docs[7]

from langchain_community.embeddings import HuggingFaceBgeEmbeddings

embeddings=HuggingFaceBgeEmbeddings()

vector=embeddings.embed_query("Hello how are you")
vector[:5]

!pip install langchain_chroma

from langchain_chroma import Chroma

vectorstore=Chroma.from_documents(documents=docs,embedding=HuggingFaceBgeEmbeddings())

from re import search
retriever =vectorstore.as_retriever(search_type="similarity",search_kwargs={"k":3})
retrieved_docs=retriever.invoke("Budget highlight")

len(retrieved_docs)

print(retrieved_docs[2].page_content)

