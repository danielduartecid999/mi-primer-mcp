import math
from mcp.server.mcpserver import MCPServer

# 1. Instanciamos el servidor con la clase MCPServer (MCP v2.x)
mcp = MCPServer("MiServidorPython")


# 2. Definimos las herramientas
@mcp.tool()
def calcular_area_circulo(radio: float) -> str:
    """Calcula el área de un círculo dado su radio en metros."""
    if radio < 0:
        return "El radio no puede ser negativo."
    
    area = math.pi * (radio ** 2)
    return f"El área del círculo con radio {radio}m es {area:.2f} m²"


@mcp.tool()
def consultar_estado_equipo(nombre_equipo: str) -> str:
    """Consulta el estado operativo de un equipo o sistema especificado."""
    estados = {
        "bomba_1": "Operativa - Presión normal",
        "servidor": "En línea - Carga 20%",
        "bodega": "Stock actualizado"
    }
    return estados.get(nombre_equipo.lower(), f"El equipo '{nombre_equipo}' no está registrado.")


# 3. Punto de entrada
if __name__ == "__main__":
    mcp.run()