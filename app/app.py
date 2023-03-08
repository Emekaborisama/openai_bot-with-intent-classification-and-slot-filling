from app.load_intent_model import predictModel
from app.bot_app import get_response,append_to_chat_log
from fastapi import FastAPI,Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from fastapi_server_session import SessionManager, RedisSessionInterface, Session
import redis

class Message(BaseModel):
    input: str
    output: str = None

app = FastAPI()
model =predictModel()

origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://127.0.0.1:8080"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["POST"],
    allow_headers=["*"],
)



session_manager = SessionManager(
    interface=RedisSessionInterface(redis.from_url("redis://localhost"))
)





async def get_session(session: Session = Depends(session_manager.use_session)):
    return {"value": session["key"]}




@app.post("/conversation_bot")
async def  generate(message: Message,session: Session = Depends(session_manager.use_session)):
    """ get message, run the get_response function, store the current question and answer on redis and use them for the next request. this create a unique session for every user"""
    Message.output =get_response(message.input, chat_log=session["chatlog"], model=model)
    result_res = Message.output
    result_chatlog = append_to_chat_log(chat_log=session["chatlog"],question=message.input, answer=result_res['Chatbot'])
    session['chatlog'] = result_chatlog
    return {"output" : Message.output}




