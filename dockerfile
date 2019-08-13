FROM ubuntu:18.04
RUN apt-get update
RUN cd ./home && mkdir pythonfile && cd pythonfile && touch helloworld.py 
COPY /app/main.py /
CMD ["python", "./main.py"]
