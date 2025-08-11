from imports import *
from filter_chat import *

logger.info("hello")
from input_filter import *
from databse_connection import *
import time
from report_generator import *
from Visulization import *
from amna import *
from s3 import *
from fastapi import FastAPI

app = FastAPI()

logger.info("hello")


@app.get("/")
def read_root():
    """
       --------------------------
       Test our ML-OCR-server
       --------------------------
        """
    # logger.info('This is an info message:  server started is ready')
    return {"message: Hello by System "}


logger.info("hello")





@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_text()
            chat_responce = json.loads(data)
            web_socket_data = input_filter(**chat_responce)
            user_querry = web_socket_data.message
            response = class_filter_1(client, system_promt, user_querry, max_tokens=300, temperature=0, seed=1,
                                      tools=tools)
            response = pre_process_class_filter_1(response)
            if response['querry_flag'] is True:
                logger.info(f" Allowed for repeated Chat chats {response}")
                response_back = json.dumps(response)
                await websocket.send_text(response_back)
            if response['querry_flag'] is False:
                gent_path = "s3://staging-hcms-textract/open/skills-observatory/Visulization_1.png"
                random_number = random.randint(1, 10)
                # Replace the number in the file name with the generated random number
                path_to_save = gent_path.replace("_1.csv", f"_{random_number}.csv")
                response = response['message']
                # user_querry --use this
                logger.info(f" Starting Image Generation {response}")
                result_visulization = analysis_crew.kickoff(inputs={"response": response, "path": path_to_save})
                logger.info(f" Image was generated Now making report")
                result_visulization = result_visulization.json_dict['Visulization']
                logger.info(f" Image tag : {result_visulization}")
                message = "Image was generated Successfully"
                front_end = {"message": message, "querry_flag": False}
                #response_back = json.dumps(front_end)
                #await websocket.send_text(response_back)
                if result_visulization == "1":
                    logger.info(f"Entering for report generation")
                    save_path=path_to_save
                    parts = save_path.split("/")
                    bucket_name = parts[2]  # The third part is the bucket name
                    s3_path = "/".join(parts[3:])  # Join the remaining parts to form the key
                    path_to_save="https://staging-hcms-textract.s3.eu-west-2.amazonaws.com/"+s3_path
                    logger.info(f" Kicking off the report crew")
                    result_report = analysis_crew_i.kickoff(
                        inputs={"response": response, "user_querry": user_querry, "sources": sources,
                                "path": path_to_save, "value": "1"})
                    html_report = result_report.json_dict['Report_HTML']
                    cleaned_text = html_report.replace("\n", " ").strip()
                    front_end = {"message": cleaned_text, "querry_flag": True}  # HOW REPORT
                    response_back = json.dumps(front_end)
                    await websocket.send_text(response_back)

                if result_visulization == "0":
                    # Execute the crew
                    logger.info(f" Image was not generated Now making report")
                    result_report = analysis_crew_x.kickoff(
                        inputs={"response": response, "user_querry": user_querry, "sources": sources, })
                    html_report = result_report.json_dict['Report_HTML']
                    cleaned_text = html_report.replace("\n", " ").strip()
                    front_end = {"message": html_report, "querry_flag": False}  # HOW REPORT
                    response_back = json.dumps(front_end)
                    await websocket.send_text(response_back)

    except Exception as e:
        # Handle and log any error that occurs during the SQLDatabase connection attempt
        logger.error(f"Error: connection error\n{e}")
        await websocket.send_text(f"Error: connection error\n{e}")



