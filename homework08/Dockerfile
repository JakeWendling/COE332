FROM python:3.8.10

RUN pip install matplotlib==3.7.1
RUN pip install redis==4.5.1
RUN pip install Flask==2.2.2
RUN pip install requests==2.22.0

COPY gene_api.py /gene_api.py

CMD ["python", "gene_api.py"]