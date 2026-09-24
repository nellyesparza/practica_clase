import sys
from pathlib import Path

# Garantiza que la raíz del proyecto esté en sys.path
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from mcp.server.fastmcp import FastMCP
from app.mcp.tools import gastos

mcp = FastMCP("gastos-server")
gastos.register(mcp)