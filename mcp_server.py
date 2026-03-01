#-MCP SERVER-

from fastmcp import FastMCP
from config import config_dictionary
from modules.tools import load_tools

load_config = config_dictionary()

name = load_config["SERVER_NAME"]
description = load_config["SERVER_DESCRIPTION"]
version = load_config["SERVER_VERSION"]
transport = load_config["SERVER_TRANSPORT"]
host = load_config["SERVER_HOST"]
port = load_config["SERVER_PORT"]
log_level = load_config["SERVER_LOG_LEVEL"]
auth = load_config["SERVER_AUTH"]

###---LOAD SERVER WITH load_configS & TOOLS---
mcp_server = FastMCP(name, description, version, auth)

load_tools(mcp_server)

###---RUN SERVER---
if __name__ == "__main__":
    mcp_server.run(host, port, log_level)