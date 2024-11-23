from fastapi import FastAPI
from pydantic import BaseModel
import asyncio
import uvicorn
import signal
from app.agent_logic import run_agent_logic

app = FastAPI()

# Modelo para definir el cuerpo de las solicitudes
class AgentInput(BaseModel):
    message: str
    id: int

@app.post("/run_agent")
async def run_agent(input: AgentInput):
    
    #Ejecuta el agente en segundo plano, liberando el endpoint.
    asyncio.create_task(run_agent_logic(input.message, input.id))

    return ""


if __name__ == "__main__":

    uvicorn.run(app, host="0.0.0.0", port=8000)

    
    