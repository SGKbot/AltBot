FROM debian
RUN apt update && apt -y install python3 python3-pip ffmpeg imagemagick \
    python3-setuptools gsfonts build-essential --no-install-recommends
COPY app/requirements.txt /
RUN pip3 install -r /requirements.txt
COPY app /app
WORKDIR /app
CMD python3 /app/bot.py
