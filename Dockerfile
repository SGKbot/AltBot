FROM debian
RUN apt update && apt -y install python3 python3-pip
ADD requirements.txt /
RUN pip3 install -r requirements.txt
ADD bot.py /
CMD python3 /bot.py
