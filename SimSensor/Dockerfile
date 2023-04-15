# This file defines how the simsensor container will be built
# Starting docker image
FROM python:3.12-rc-alpine

# Add the simsensor python file to the root directory of the container
ADD simsensor.py .

# Install paho mqtt libary
RUN pip install paho-mqtt

# Set the default envrioment variables if no other are specified when running (pass these into the container)
# These can be overwritten in the docker compose file
ENV containername=simsensor
ENV broker_address=eclipse-mosquitto
ENV delay=1

# Run the python program
CMD ["python","-u","./simsensor.py"]