import os
from dotenv import load_dotenv
from pathlib import Path
import logging
from main.brain_components.front_end_agents.user_interface_agent import UIAgent
from main.brain_components.back_end_agents.back_end_agent import BackendAgent

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def main():
    """
    Main function to run the application.
    This is the entry point.
    """
    load_environment()
    print("Hello and welcome to Python Website Builder!")
    # print("Testing the UI agent.")
    # ui_agent = UIAgent()
    # ui_agent.agent_trials()
    print("Testing the backend agent")
    backend_agent= BackendAgent()
    backend_agent.agent_trials()


def load_environment():
    """
    Load environment variables from the .env file.
    """
    env_path = Path('config') / '.env'
    if env_path.exists():
        load_dotenv(dotenv_path=env_path)
        logger.info("Environment variables loaded from .env file.")
    else:
        logger.warning(".env file not found. Make sure to create one if environment variables are needed.")


if __name__ == '__main__':
    main()
