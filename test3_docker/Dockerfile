FROM python:3.8
VOLUME ["/pred"]
WORKDIR /pred
COPY model.py /model.py
RUN pip install pandas
RUN pip install numpy
ENTRYPOINT ["python", "/model.py"]
CMD ["internship_hidden_test.csv"]