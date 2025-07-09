import os
from dotenv import load_dotenv
# Loading the GROK api key from the env file
load_dotenv()
api = os.getenv("API")

def translate_text(text: str, target_lang: str) -> str:
    try:
        from langchain_groq import ChatGroq
        from langchain_core.messages import HumanMessage
        llm = ChatGroq(api_key=api, model_name="llama3-70b-8192")

        # Spliting  by paragraphs or sentences
        chunks = text.split(". ")

        translated_chunks = []
        for chunk in chunks:
            prompt = f"""You are a professional translator.
            Translate the following text into {target_lang}.
            Return only the translated text in {target_lang} script, with no explanation.

            Text:
            {text}
            """
            message = [HumanMessage(content=prompt)]
            response = llm.invoke(message)
            translated_chunks.append(response.content.strip())

        return " ".join(translated_chunks)

    except Exception as e:
        return f"Translation failed: {str(e)}"