import os
from third_parties.linkedin import scrape_linkedin_profile
from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from dotenv import load_dotenv


information = """ 
david beckhaum.
"""
if __name__ == "__main__":
    # Load environment variables from .env file
    load_dotenv()
  
    print(os.environ["OPENAI_API_KEY"])
    # Access the environment variable
    # api_key = os.environ.get('OPENAI_API_KEY')

    # Check if the API key is available
    # if api_key is None:
    # print("OPENAI_API_KEY is not set")
    # else:
    # print("API key:", api_key)
    summary_template = """
        given the information{information} about a persion that I want you to create:
        1. a short summary
        2.two interesting thing facts about that    
    """
    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )
    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
    chain = LLMChain(llm=llm, prompt=summary_prompt_template)
    
   
#
    linkedin_data=scrape_linkedin_profile(linkedin_profile_url='https://www.linkedin.com/in/mir-akbar-seyedi-9906b658/')
    # print(linkedin_data.json()) 
    print(chain.run(information=linkedin_data))