FROM python:3.8-buster
RUN apt update && apt -y install ffmpeg imagemagick python3-setuptools gsfonts --no-install-recommends && \
    rm -rf /usr/share/doc /usr/share/man /usr/share/perl /usr/share/locale && \
    apt -y remove --purge python2 && apt -y clean && apt -y autoremove
COPY app/requirements.txt /
RUN pip3 install -r /requirements.txt
COPY app /app
WORKDIR /app
CMD python3 /app/bot.py
