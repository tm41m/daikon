#!/bin/bash

sudo useradd -m -d /home/circleci -s /bin/bash circleci;
sudo ufw allow http;
sudo mkdir /home/circleci/.ssh;
sudo touch /home/circleci/.ssh/authorized_keys;
sudo echo "$DAIKON_SSH_KEY" > /home/circleci/.ssh/authorized_keys;

touch ~/.ssh/config;
echo "Host github.com" >> ~/.ssh/config;
echo "  StrictHostKeyChecking no" >> ~/.ssh/config;
chmod 600 ~/.ssh/config;

cp ~/.ssh/config /home/circleci/.ssh;
chown circleci /home/circleci/.ssh/config;

cd $DAIKON_DIR && git clone git@github.com:tm41m/daikon.git && git checkout -b $DAIKON_ENV && git branch -u origin/$DAIKON_ENV;
chown -R circleci /home/circleci/daikon;

sudo usermod -aG docker circleci;
docker image pull tm41m/daikon:0.1;
