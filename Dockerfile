
FROM ubuntu:22.04 as ubuntul
ENV DEBIAN_FRONTEND=noninteractive
RUN apt update \
  && apt install -y python3.11 python3-pip python3-dev build-essential build-essential tzdata \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 install --upgrade pip



#layering --
FROM ubuntul as app
LABEL app="skill_observatory"
# operation working directory
WORKDIR /root/skill_observatory
RUN pip3 install --upgrade pip
COPY requirements.txt /root/skill_observatory
RUN pip3 install -r /root/skill_observatory/requirements.txt
RUN echo "Asia/Dubai" > /etc/timezone && \
    ln -sf /usr/share/zoneinfo/Asia/Dubai /etc/localtime && \
    dpkg-reconfigure -f noninteractive tzdata

ENV PYTHONPATH="${PYTHONPATH}:/root/skill_observatory/:/root/skill_observatory/skill_observatory"

