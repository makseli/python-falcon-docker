FROM python:alpine

EXPOSE 3499

# Install gunicorn
RUN pip install gunicorn

# Install falcon
RUN pip install falcon

# Add demo app
COPY ./falcon-app /app
WORKDIR /app

CMD ["gunicorn", "-b", "0.0.0.0:3499", "main:app"]
