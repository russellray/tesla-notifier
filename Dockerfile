FROM python

# copy script to container
ADD check_vehicle.py /

# install dependencies
RUN pip install twilio

# run the script
CMD [ "python", "./check_vehicle.py" ]