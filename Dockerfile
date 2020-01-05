FROM debian
RUN apt update && apt -y install python3 python3-pip ffmpeg imagemagick \
    python3-setuptools \
    --no-install-recommends
ADD requirements.txt /
RUN pip3 install -r requirements.txt
ADD FreeMono.ttf /
ADD bot.py /
CMD python3 /bot.py
