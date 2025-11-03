import logging
import os




def get_logger(name: str):
    os.makedirs('reports/logs', exist_ok=True)
    logger = logging.getLogger(name)
    if logger.handlers:

        return logger


    logger.setLevel(logging.INFO)
    fh = logging.FileHandler('reports/logs/test.log')
    fh.setLevel(logging.INFO)
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)


    fmt = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(fmt)
    ch.setFormatter(fmt)


    logger.addHandler(fh)
    logger.addHandler(ch)
    return logger