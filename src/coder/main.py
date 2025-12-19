from crewai import CrewOutput

from src.coder.crew import Coder


def run():
    assignment = 'Write a python program to calculate the first 10,000 terms \
    of this series, multiplying the total by 4: 1 - 1/3 + 1/5 - 1/7 + ...'

    inputs = {'assignment':assignment}

    result: CrewOutput = Coder().crew().kickoff(inputs=inputs)
    print(result.raw)

if __name__ == "__main__":
    run()