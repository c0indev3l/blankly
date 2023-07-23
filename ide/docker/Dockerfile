FROM debian:bookworm

ENV DEBIAN_FRONTEND=noninteractive

# Install build dependencies
RUN apt-get update && apt-get install -y build-essential python3 python3-pip python3-dev python3-setuptools python3-pytest && apt-get clean

#COPY ./ide/provisioning/install-debian-packages.sh /root/install-debian-packages.sh
#RUN /root/install-debian-packages.sh && apt-get clean

WORKDIR /usr/src/app
COPY . .
RUN pip3 install -r requirements.txt --break-system-packages
#RUN python3 setup.py install
#COPY ./ide/docker/bin/* /usr/local/bin/
# WORKDIR /usr/local/bin
#RUN chmod 755 ./*


CMD ["/bin/bash", "-c", "pwd; ls -la; python3 -m pytest;"]
