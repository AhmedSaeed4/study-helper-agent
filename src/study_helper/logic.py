import os
import asyncio
from dotenv import load_dotenv
from pydantic import BaseModel
from agents import (
    Agent, OpenAIChatCompletionsModel, RunConfig, AsyncOpenAI, Runner, 
    )

from dataclasses  import dataclass

load_dotenv()
API_KEY = os.environ["GEMINI_API_KEY"]
if not API_KEY:
    raise ValueError("GEMINI_API_KEY not found ")





client = AsyncOpenAI(
    api_key=API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)


model = OpenAIChatCompletionsModel(
    model="gemini-2.5-flash",
    openai_client=client)


config = RunConfig(
    model=model,
    model_provider=client,

)



class StudyAssistant:
    def __init__(self):
  
        self.agent = Agent(
            name="Study Assistant",
            instructions="You are a helpful study assistant. Process the provided document and task to generate a relevant response.",
        )

    def process_task(self, task_instruction: str, pdf_content: str) -> str:
        prompt = f"""DOCUMENT:
{pdf_content}

TASK:
{task_instruction}"""
        
  
        try:
            result = Runner.run_sync(
                starting_agent=self.agent,
                input=prompt, run_config=config 
            )
           
            if result.final_output and result.final_output:
                return result.final_output
            elif isinstance(result.final_output, str):
                return result.final_output
            else:
                return "Agent did not produce a readable text response."
        except Exception as e:
            return f"Error during agent processing: {e}"