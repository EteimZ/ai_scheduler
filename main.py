from openai import OpenAI
import json

from datetime import datetime
from tools import tools

from schedule import ScheduleDB, Schedule

client = OpenAI()

# Schedule database
scheduleDB = ScheduleDB()

system_msg = """
            You are a smart AI assistant who job is to manage the user's schedule.
            At every point of the conversation you have access to the current time.
            Use this time to smartly make schedules for the user.

            For example:

            user: Sent a schedule with my doctor in an hour.
            current_time: 2023-12-10 10:00:00
            assistant: Your schedule has been made with you doctor has been made succesfuly at 2023-12-10 11:00:00 
            """

messages = [{"role": "system", "content": system_msg}]

def main():
    while (prompt := input("Human: ")) != "exit":

        messages.extend([{"role": "system", "content": f"current_time: {datetime.now()}"}, 
                        {"role": "user", "content": prompt}])
            
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages,
            tools=tools,
            tool_choice="auto",
        )

        response_message = completion.choices[0].message
        tool_calls = response_message.tool_calls

        # Check if the model wanted to called a function
        if tool_calls:
            # Add the function call
            messages.append(response_message)  
            
            # Iterate through every function call
            for tool_call in tool_calls:
                function_name = tool_call.function.name
                if function_name == "add_schedule":
                    function_args = json.loads(tool_call.function.arguments)
                    schedule = Schedule(**function_args)
                    scheduleDB.add(schedule)
                    function_response =  json.dumps({"add_schedule": schedule.model_dump_json(), "id": scheduleDB.id})
            
                elif function_name == "update_schedule_time":
                    function_args = json.loads(tool_call.function.arguments)
                    scheduleDB.update_datetime(id=function_args.get("id"), date_time=function_args.get("datetime")) 
                    function_response =  json.dumps({"updated_schedule": scheduleDB[int(function_args.get('id'))]})

                elif function_name == "update_schedule_description":
                    function_args = json.loads(tool_call.function.arguments)
                    scheduleDB.update_description(id=function_args.get("id"), descr=function_args.get("description")) 
                    function_response =  json.dumps({"updated_schedule": scheduleDB[int(function_args.get('id'))]})
                
                elif function_name == "update_schedule_title":
                    function_args = json.loads(tool_call.function.arguments)
                    scheduleDB.update_title(id=function_args.get("id"), title=function_args.get("title")) 
                    function_response =  json.dumps({"updated_schedule": scheduleDB[int(function_args.get('id'))]})

                elif function_name == "list_schedules":
                    function_response = json.dumps(scheduleDB.list())

                else:
                    function_response = json.dumps({"message": "Function does not exist."})

                # Add the function response
                messages.append(
                    {
                        "tool_call_id": tool_call.id,
                        "role": "tool",
                        "name": function_name,
                        "content": function_response,
                    }
                )  
                
                # Pass the function resposne to the llm
                completion = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=messages,
                )
        else:
            messages.append(response_message)

        print("AI:", completion.choices[0].message.content)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Program canceled")