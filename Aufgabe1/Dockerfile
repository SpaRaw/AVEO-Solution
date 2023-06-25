FROM python:3.10
COPY . .
RUN apt update
RUN apt install unzip
RUN unzip -q Data/ip.zip
RUN pip install --upgrade pip
RUN pip install flask
RUN pip install typing
CMD ["python3", "-m" , "flask", "run", "--host=0.0.0.0"]