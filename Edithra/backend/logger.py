# Logger Configuration
import logging

logging.basicConfig(
    filename="Edithra/logs/app.log",
    filemode="a",
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

logger = logging.getLogger(__name__)

def log_event(event_type, message):
    """Logs an event to the system."""
    if event_type == "info":
        logger.info(message)
    elif event_type == "warning":
        logger.warning(message)
    elif event_type == "error":
        logger.error(message)




