#-TOOLS-

###---MCP TOOLS---
def load_tools(mcp_server):

    @mcp_server.tool()
    def tool_1():
        #what does it do
        pass #need this so doesn't freak out there is no logic in this nested function
        
    @mcp_server.tool()
    def tool_2():
        #what does it do
        pass #need this so doesn't freak out there is no logic in this nested function
        
    @mcp_server.tool()
    def tool_3():
        #what does it do
        pass #need this so doesn't freak out there is no logic in this nested function
