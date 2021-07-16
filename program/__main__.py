#!/usr/bin/env python3
from program import app #can run the app with "python -m myapp"
from program import log


logger = log.setup(__name__)


if __name__ == '__main__':    
    logger.debug("App started...")
    app.run()
    logger.debug("App ended...")
