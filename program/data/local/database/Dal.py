import inspect
from program import log
from time import sleep

logger = log.setup(__name__)

def insert(session, item):
    logger.debug(inspect.stack()[0][3])
    
    session.add(item)
    session.flush()
    sleep(0.2)
    return item.id

def select_all(session, class_name):
    logger.debug(inspect.stack()[0][3])

    return session.query(class_name).all()
