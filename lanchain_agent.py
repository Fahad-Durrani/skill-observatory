from imports import *
from databse_connection import *
instructions = [
    "Use only the following tables: supply_data_flat, demand_jobs_data_flat.",
    "Do not use any columns outside the table schema.",
    "If querry is not Executed, only return **i don't know .",
    "Never return Table schema at ouput"
    "Always execute so we get count, so data should be easily shown as barchar or pie chart. Don't include any such text in output"
    "Exclude any Nan Value or Terms in rown or tables"
]


table_names_to_use = ["supply_data_flat", "demand_jobs_data_flat"]

def sql_querry_generator(querry,db,instructions,table_names_to_use,api_keys):
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0,openai_api_key=api_keys)
    agent_executor = create_sql_agent(llm,db=db, agent_type="openai-tools", verbose=False,table_schemas=table_names_to_use)
    #sql_result=agent_executor.invoke  ({"input": f"Only use the following tables to answer: supply_data_flat, demand_jobs_data_flat{querry}"})
    sql_result = agent_executor.invoke({"input": f"{' '.join(instructions)} SQL Query: {querry}"})
    db_responce=sql_result['output']
    return db_responce

