# Agentic Coder

An AI-powered Python code generator using [CrewAI](https://crewai.com). This agent receives coding assignments, plans the solution, writes Python code, executes it safely in Docker, and provides the output.

## What It Does

The agent acts as a Python developer that:
1. Receives a coding assignment
2. Plans how to solve it
3. Writes clean, efficient Python code
4. Executes the code safely in a Docker container
5. Saves the code and output to a file

## Requirements

- Python >=3.10, <3.14
- Docker (must be running for code execution)
- OpenAI API key

## Installation

1. Install dependencies:
```bash
crewai install
```

2. Create a `.env` file and add your OpenAI API key:
```
OPENAI_API_KEY=your_api_key_here
```

## Usage

Run the agent from the project root:

```bash
crewai run
```

Or run directly with Python:

```bash
python -m src.coder.main
```

The agent will process the assignment defined in `src/coder/main.py` and save the results to `output/code_and_output.txt`.

## Configuration

- **Agents**: Modify `src/coder/config/agents.yaml` to change agent behavior
- **Tasks**: Modify `src/coder/config/tasks.yaml` to change task definitions
- **Assignment**: Edit the `assignment` variable in `src/coder/main.py` to change what the agent will code

## How It Works

The agent uses CrewAI's framework with:
- Safe code execution via Docker containers
- 5-minute timeout for complex tasks
- Automatic retry on failures (up to 3 attempts)
- GPT-4o-mini for cost-effective code generation
