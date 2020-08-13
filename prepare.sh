#!/bin/bash

# curl -SL https://chromedriver.storage.googleapis.com/2.43/chromedriver_linux64.zip > chromedriver.zip
rm -rf lib/chromedriver
curl -SL https://chromedriver.storage.googleapis.com/2.25/chromedriver_linux64.zip > chromedriver.zip
unzip chromedriver.zip
mv chromedriver lib/
rm -rf chromedriver.zip

# rm -rf lib/headless-chrome
# curl -SL https://github.com/adieuadieu/serverless-chrome/releases/download/v1.0.0-55/stable-headless-chromium-amazonlinux-2017-03.zip > headless-chromium.zip
# unzip headless-chromium.zip

# mv headless-chromium lib/
# rm -rf chromedriver.zip headless-chromium.zip
