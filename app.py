

from flask import Flask
import sys
from Airline.logging import logging
from Airline.exception import AirlineException
app = Flask(__name__)


@app.route("/",methods=['GET','POST'])
def index():
    try:
        raise Exception("We are testing custom exception")
    except Exception as e:
        Air = AirlineException(e,sys)
        logging.info(Air.error_message)
        logging.info("We are testing logging module")
    return "CI CD pipeline has been established."


if __name__=="__main__":
    app.run(debug=True,port=5000)