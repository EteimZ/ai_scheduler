# AI Scheduling assitant

A CLI AI scheduling assistant powered by [openai's gpt model](https://platform.openai.com/docs/models). It has the ability of making schedules for the user from just natural language. It is also time aware meaning it has access to the current time this makes it better at properly scheduling for the user.

## Usage

The program only has two external dependencies; [openai](https://platform.openai.com/docs/introduction) and [pydantic](https://docs.pydantic.dev/latest/).

Install them both to get started:

```bash
pip install openai
pip install pydantic
```

Also set your the environemt variable `OPENAI_API_KEY` to your open ai key.

```bash
export OPENAI_API_KEY=sk-XXXXX-YYYYY-ZZZZZZ
```

With that you are good to go. Just run the command below:

```bash
python main.py
```

This will create a REPL. Here's an example conversation between the user and the AI:

```bash
Human: Give me a list of my schedules
AI: You dont have any schedules at the moment.
Human: I will be going fishing tommorow by 12 add it to my schedule
AI: Your fishing trip has been successfully added to your schedule. It is scheduled for tomorrow at 12:00 PM.
```

**Note:** This program is built with python 3.9, ensure you have it or higher. It might also work with python 3.8.

## Technology

The ai model run on `gpt-3.5-turbo`. I didn't use any llm frameworks or library. Rather I made use of open ai [function calls](https://platform.openai.com/docs/guides/function-calling). All the functions used by the model are defined in the `tools.py` file.

For simplicity I didn't make use of a database to store the schedules rather I used a class to be the single source of truth for the model.

## Drawbacks

There are a couple of drawbacks a lot of the times the program will throw an exception because proper error handling wasn't taken into consideration.