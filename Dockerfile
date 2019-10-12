FROM debian
RUN apt update && apt -y install python3 python3-pip
ADD bot.py /
