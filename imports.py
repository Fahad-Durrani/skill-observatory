from langchain_community.utilities import SQLDatabase
from pydantic import BaseModel
import psycopg2
from langsmith.wrappers import wrap_openai
from langsmith import traceable
from langsmith import Client
import io
from langchain_community.utilities import SQLDatabase
from sqlalchemy import create_engine
from sqlalchemy.exc import SAWarning
import random
import warnings
# Suppress SAWarning warnings
warnings.filterwarnings('ignore', category=DeprecationWarning)
warnings.filterwarnings('ignore', category=SAWarning)
warnings.filterwarnings("ignore", category=DeprecationWarning, module="langchain")
import os
#from langchain_community.chat_models import ChatOpenAI
from langchain.chains import create_sql_query_chain
from operator import itemgetter
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence
from langchain_community.tools.sql_database.tool import QuerySQLDataBaseTool
from langchain_community.agent_toolkits import create_sql_agent
from langchain_openai import OpenAI
from langchain_openai import ChatOpenAI

import openai
from openai import OpenAI

import logging
import logging as logger
from utils.uLogger import logger
#from fastapi import FastAPI, WebSocket, WebSocketDisconnect
#from app.models.reg_models import WebSocketData
import json
#---
from crewai import Agent, Task, Crew #-----------------
from crewai_tools import tool #------------------------
#---
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
import asyncio

import numpy as np


from dotenv import load_dotenv
load_dotenv('all.env')

DATABASE_URI = os.getenv('DATABASE_URI')
DATABASE_USERNAME = os.getenv('DATABASE_USERNAME')
DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD')
DATABASE_NAME = os.getenv('DATABASE_NAME')
PORT = os.getenv('PORT')

openai_api_key=os.getenv('openai_api_key')
os.environ["OPENAI_API_KEY"]=openai_api_key
api_keys=os.getenv('api_key')

# if api_key is None:
#     raise ValueError("OPENAI_API_KEY environment variable is not set.")
client = OpenAI(api_key=api_keys)

#openai.api_key = api_key

# Create the client (if using OpenAI client)
#client = openai
