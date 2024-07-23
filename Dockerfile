FROM ubuntu:20.04

# install cowsay, and move the "default.cow" out of the way so we can overwrite it with "docker.cow"
RUN apt-get update && apt-get install -y cowsay fortune fortunes-debian-hints fortunes-off netcat --no-install-recommends && rm -rf /var/lib/apt/lists/* 

ENV PATH $PATH:/usr/games
COPY wisecow.sh /usr/games

CMD ["bash","/usr/games/wisecow.sh"]
