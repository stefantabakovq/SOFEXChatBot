import json
import os
import shutil
import subprocess
import logging
import time
from dependency_injector.wiring import inject, Provide

from src.Containers.SofexAIContainer import SofexAIContainer
from src.SofexAI.SofexIntelligence import SofexIntelligence
import src.SofexAI


def init():
    cfg_path = "config.json"
    # INIT API DATA
    resource_container = SofexAIContainer()
    resource_container.config.from_json(cfg_path)
    resource_container.wire(packages=[__name__, src.SofexAI])


if __name__ == '__main__':
    init()
    print("Server starting, welcome to SOFEX.")
    print("Loading resources...")
    print("----------------------------------")
    SOFEX = SofexIntelligence()
    SOFEX.create_model()
    answer = SOFEX.generate_answer(message="Hello, your name is SOFEX and I am Stefan. I am your creator."
                                           "Welcome. Introduce yourself.")
    print(answer)

    question = ""
    while True:
        question = input("Ask SOFEX: ")
        answer = SOFEX.generate_answer(message=question)
        print("SOFEX: " + answer)

