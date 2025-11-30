import time
from utils.logging_utils import get_logger

logger = get_logger("retry")

def retry_with_backoff(
    func,
    max_retries=3,
    base_delay=1.0,
    backoff_factor=2.0,
    validate_output=None,
    agent=None,
    run_id=None,
):
    attempt = 0
    delay = base_delay

    while attempt <= max_retries:
        try:
            result = func()

            # Optional validation handler
            if validate_output:
                valid, reason = validate_output(result)
                if not valid:
                    logger.warning(
                        f"Validation failed: {reason}",
                        extra={"agent": agent, "run_id": run_id, "attempt": attempt},
                    )
                    raise ValueError(reason)

            if attempt > 0:
                logger.info(
                    f"Success after retry #{attempt}",
                    extra={"agent": agent, "run_id": run_id},
                )

            return result

        except Exception as e:
            if attempt == max_retries:
                logger.error(
                    f"Failed after max retries: {e}",
                    extra={"agent": agent, "run_id": run_id, "attempt": attempt},
                )
                raise

            logger.warning(
                f"Retry {attempt+1} failed, retrying in {delay}s",
                extra={"agent": agent, "run_id": run_id, "attempt": attempt},
            )

            time.sleep(delay)
            attempt += 1
            delay *= backoff_factor
