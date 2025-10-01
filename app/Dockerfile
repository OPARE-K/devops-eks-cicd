FROM python:3.11-slim
WORKDIR /app
RUN pip install flask gunicorn
COPY src/ /app/
ENV PORT=8080
CMD ["gunicorn","-b","0.0.0.0:8080","server:app","--workers","2"]
