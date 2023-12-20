tools = [
        {
            "type": "function",
            "function": {
                "name": "add_schedule",
                "description": "Create a new schedule for the user.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "title": {
                            "type": "string",
                            "description": "From their description generate a unique title.",
                        },
                        "description": {
                            "type": "string", 
                            "description": "The description of the schedule, e.g I will be going to Lagos tomorrow."     
                        },
                        "datetime": {
                            "type": "string", 
                            "description": "The datetime of the schedule, e.g 2019-06-01 12:22."     
                        },
                    },
                    "required": ["title", "descr", "datetime"],
                },
            },
        },
        {
            "type": "function",
            "function": {
                "name": "update_schedule_time",
                "description": "Update the time of an existing schedule",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "id": {
                            "type": "integer",
                            "description": "A unique integer which represents the schedule.",
                        },
                        "datetime": {
                            "type": "string", 
                            "description": "The new datetime of the schedule, e.g 2019-06-01 12:22."     
                        },
                    },
                    "required": ["id", "datetime"],
                },
            },
        },
        {
            "type": "function",
            "function": {
                "name": "update_schedule_description",
                "description": "Update the description of an existing schedule",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "id": {
                            "type": "integer",
                            "description": "A unique integer which represents the schedule.",
                        },
                        "description": {
                            "type": "string", 
                            "description": "The new description of the schedule."     
                        },
                    },
                    "required": ["id", "description"],
                },
            },
        },
        {
            "type": "function",
            "function": {
                "name": "update_schedule_title",
                "description": "Update the title of an existing schedule",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "id": {
                            "type": "integer",
                            "description": "A unique integer which represents the schedule.",
                        },
                        "title": {
                            "type": "string", 
                            "description": "The new description of the schedule."     
                        },
                    },
                    "required": ["id", "description"],
                },
            },
        },
        {
            "type": "function",
            "function": {
                "name": "list_schedules",
                "description": "This is used to get the current list of schedules",
            },
        }

    ]

