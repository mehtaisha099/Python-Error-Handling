import logging

logging.basicConfig(
    filename="error.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

try:
    number = 10 / 0
    print(number)

except Exception as e:
    logging.error("An error occurred: %s", e)
    print("Error logged to error.log")