FROM python:3.9.10
LABEL key="0.1"

ENV http_proxy=http://proxy.ecole-navale.fr:8080
ENV https_proxy=http://proxy.ecole-navale.fr

ADD parse_html.py .

RUN apt update
RUN apt upgrade -y

CMD ["python", "-u", "parse_html.py"] 

EXPOSE 80
EXPOSE 443