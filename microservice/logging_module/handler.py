from datetime import datetime, timezone
import logging
import microservice.logging_module.handling_logger


logger = microservice.logging_module.handling_logger.Logger()
time = datetime.now(timezone.utc)
logger.set_stream_handler()
#logger.set_file_handler(f"{LOGS}-{(self.time).strftime('%Y%m%d-%H%M%S')}.log")
logger.set_level(logging.DEBUG)