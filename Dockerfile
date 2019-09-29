FROM python:3
ADD api/ /api
WORKDIR /api
RUN pip install -r requirements.txt
CMD python app.py