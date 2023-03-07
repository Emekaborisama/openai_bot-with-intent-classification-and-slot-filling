FROM python:3.8 
RUN mkdir /app 
WORKDIR /app 
ADD . /app/ 
RUN pip install -r requirements.txt 
RUN app/load_model.py
CMD ["python", "app.py"]
EXPOSE 8000