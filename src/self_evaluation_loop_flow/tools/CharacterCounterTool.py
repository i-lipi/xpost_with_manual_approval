from typing import Type #specify that args_schema will be a type of BaseModel

from crewai_tools import BaseTool #base class for creating custom tools for agents
from pydantic import BaseModel, Field #schema for input, add metadata desc


class CharacterCounterInput(BaseModel):
    """Input schema for CharacterCounterTool."""

    text: str = Field(..., description="The string to count characters in.")
#i/p should be string, ... means required feild

class CharacterCounterTool(BaseTool):
    name: str = "Character Counter Tool"
    description: str = "Counts the number of characters in a given string."
    args_schema: Type[BaseModel] = CharacterCounterInput  #links tool to cci class

    def _run(self, text: str) -> str:
        character_count = len(text)
        return f"The input string has {character_count} characters."
