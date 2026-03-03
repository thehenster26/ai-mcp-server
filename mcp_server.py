#-MCP SERVER-

from fastmcp import FastMCP
from fastmcp.server.auth import StaticTokenVerifier
from config import config_dictionary
from modules.tools import load_tools



###---LOAD CONFIG VARIABLES---
load_config = config_dictionary()

name = load_config["SERVER_NAME"]
description = load_config["SERVER_DESCRIPTION"]
version = load_config["SERVER_VERSION"]
transport = load_config["SERVER_TRANSPORT"]
host = load_config["SERVER_HOST"]
port = load_config["SERVER_PORT"]
log_level = load_config["SERVER_LOG_LEVEL"]

#### authentication
auth_token = load_config["SERVER_AUTH"]
auth = StaticTokenVerifier(tokens={auth_token: {"client_id": "client", "scopes": []}}) if auth_token else None

###---LOAD SERVER WITH CONFIG & TOOLS---
mcp_server = FastMCP(name, description, version=version, auth=auth)

load_tools(mcp_server)

###---RUN SERVER---
if __name__ == "__main__":
    mcp_server.run(transport, host=host, port=port, log_level=log_level)