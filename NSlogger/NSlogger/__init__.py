import logging

def setup_logger(logfile):
    """
    Set up the logger with a specified log file.

    Args:
        logfile (str): The name of the log file.

    Returns:
        logging.Logger: The configured logger instance.
    """
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    # Create a file handler and set the level to DEBUG
    file_handler = logging.FileHandler(logfile)
    file_handler.setLevel(logging.DEBUG)

    # Create a stream handler and set the level to INFO
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.INFO)

    # Create a formatter and add it to the handlers
    formatter = logging.Formatter(
        '[%(asctime)s] [%(levelname)s] %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    file_handler.setFormatter(formatter)
    stream_handler.setFormatter(formatter)

    # Add the handlers to the logger
    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)

    return logger