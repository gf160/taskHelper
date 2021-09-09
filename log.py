import logging

def setLogging(_logName="log"):
    logger = logging.getLogger(_logName)
    logger.setLevel(logging.INFO)

    handler = logging.StreamHandler()

    formatter = logging.Formatter('[%(asctime)s %(name)s:%(lineno)d] %(levelname)-8s %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    file_handler = logging.FileHandler('./log/project.log')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)


    logger.info('logging is ready')
    return logger