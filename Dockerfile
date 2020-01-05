FROM debian
RUN apt update && apt -y install python3 python3-pip ffmpeg imagemagick \
    python3-setuptools gsfonts --no-install-recommends
ADD requirements.txt /
RUN pip3 install -r requirements.txt
ADD FreeMono.ttf /
ADD bot.py /
ADD policy.xml /etc/ImageMagick-6/policy.xml
CMD python3 /bot.py
