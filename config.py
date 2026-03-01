#-CONFIG-

from dotenv import load_dotenv
import os

load_dotenv()

###---SERVER CONFIGURATION---
def config_dictionary():
    return {
        "SERVER_NAME" : "AI MCP SERVER",
        "SERVER_DESCRIPTION" : "Model Context Protocol (MCP) server providing system tools and capabilities to AI assistants. Supports both local and remote access.",
        "SERVER_VERSION" : "2026.02.28.01",
        "SERVER_TRANSPORT" : "sse",
        "SERVER_HOST" : "127.0.0.1",
        "SERVER_PORT" : "2642",
        "SERVER_LOG_LEVEL" : "",
        "SERVER_AUTH" : os.environ.get("TOKEN"),
    }