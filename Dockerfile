FROM python:3.8 
RUN mkdir /app 
WORKDIR /app 
ADD . /app/ 
RUN pip install -r requirements.txt 
RUN ["python app/load_intent_model.py"]
CMD ["uvicorn" "main:app" "--reload"]
EXPOSE 8000