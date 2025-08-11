
from imports import *
from lanchain_agent import *
from databse_connection import *
from filter_chat_prompt import *
from main import *
from Visulization import *

conn, cursor, db = connect_to_database(DATABASE_NAME, DATABASE_USERNAME, DATABASE_PASSWORD, DATABASE_URI, PORT)








visulization_flag=False
report_generation_flat=False
flag_report_image=False

def class_filter_1(client, system_promt, user_query, max_tokens=300, temperature=0, seed=1, tools=tools):
    response = client.chat.completions.create(
        model="gpt-4o-mini-2024-07-18",
        messages=[
            {"role": "system", "content":system_promt},
            {"role": "user","content": user_query}
        ],
        max_tokens=max_tokens,
        temperature=temperature,
        seed=seed,
        tools=tools,
    )
    return response

def pre_process_class_filter_1(response):
    response_dict = response.to_dict()
    desired_output = response_dict["choices"][0]["message"]["tool_calls"][0]["function"]["arguments"]
    desired_output = json.loads(desired_output)
    # After we get the responce from main function
    if desired_output['class'].lower()=='greeting':
        back_chat=desired_output['response']  # Response back to User-- GREETING MESSAGE'
        logger.info(f"Greeting message {back_chat}")
        front_end={"message":back_chat, "querry_flag":True}
        return front_end
    if desired_output['class'].lower()=='irrelevant':
        back_chat=desired_output['response']
        logger.info(f"Irrelevant message {back_chat}")
        front_end={"message":back_chat, "querry_flag":True}
        return front_end
    if desired_output['class'].lower()=='data':
        user_querry=desired_output['response']
        logger.info("generating querry")
        #logger.info(f"{back_chat,db,instructions,table_names_to_use,api_keys}")
        back_chat=sql_querry_generator(user_querry,db,instructions,table_names_to_use,api_keys)
        logger.info("lanchain agent worked properly")
        logger.info(f" langchain agent responce {back_chat}")
        if "i don't know" in back_chat.lower() or "i don't" in back_chat.lower() or "don't know" in back_chat.lower():
            message="This question appears to be outside the scope of skills or demand-related insights. Please provide more details or revise your query."
            front_end={"message":message, "querry_flag":True}
            logger.info(f" langchain agent didn't find answer {message}")
            return front_end
        else :
            logger.info(f" Going for CREWS {back_chat}")
            front_end={"message":back_chat, "querry_flag":False}
            return front_end
