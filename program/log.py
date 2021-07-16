import logging

def setup(name):
    formatter = logging.Formatter(fmt='%(asctime)s|%(levelname)s|%(name)s-%(threadName)s-%(module)s|%(message)s')

    s_handler = logging.StreamHandler()
    s_handler.setFormatter(formatter)
    f_handler = logging.FileHandler("app.log", mode='a')    
    f_handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(s_handler)
    logger.addHandler(f_handler)
    return logger
