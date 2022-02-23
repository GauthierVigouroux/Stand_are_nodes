FROM python:3.9.10
LABEL key="0.1"

ADD parse_html.py .

#RUN apt update
#RUN apt upgrade -y

EXPOSE 80
EXPOSE 443

CMD ["python", "-u", "parse_html.py"] 