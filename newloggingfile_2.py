import logging

logging.basicConfig(filename = 'test.log', filemode = 'w', level = logging.INFO)

logging.debug("This is debug log")
logging.info("This is info log")
logging.warning("This is warning log")
logging.error("This is error log")
logging.critical("This is critical log")