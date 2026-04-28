from dotenv import load_dotenv
load_dotenv()
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.exceptions import LangChainException, OutputParserException
from langchain_google_genai.chat_models import ChatGoogleGenerativeAIError
import streamlit as st

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")


st.title(" 🤖 Ask Buddy AI QnA Bot")
st.markdown("My QnA Bot With LangChain and Google Gemini")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    role = message["role"]
    content = message["content"]
    st.chat_message(role).markdown(content)


query = st.chat_input("Ask Anything...")

if query:
    st.session_state.messages.append({"role": "user", "content": query})
    st.chat_message("user").markdown(query)
    aiMesage = ""
    try:
        res = llm.invoke(query)
        aiMesage = res.content
    except OutputParserException as e:
        aiMesage = e.error.message
    except LangChainException as e:
        aiMesage = e.error.message
    except ChatGoogleGenerativeAIError as e:
        aiMesage = e
    except Exception as e:
        aiMesage = e

    st.chat_message("ai").markdown(aiMesage)
    st.session_state.messages.append({"role": "ai", "content": aiMesage})