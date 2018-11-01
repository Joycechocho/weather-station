#!/usr/bin/env bash
# stop script on error
set -e

# Check to see if root CA file exists, download if not
if [ ! -f ./root-CA.crt ]; then
  printf "\nDownloading AWS IoT Root CA certificate from Symantec...\n"
  curl https://www.symantec.com/content/en/us/enterprise/verisign/roots/VeriSign-Class%203-Public-Primary-Certification-Authority-G5.pem > root-CA.crt
fi

# run pub/sub sample app using certificates downloaded in package
printf "\nRunning local server application...\n"
python main.py -e augluwzdcjgie.iot.us-west-2.amazonaws.com -r root-CA.crt -c testSensor.cert.pem -k testSensor.private.key
