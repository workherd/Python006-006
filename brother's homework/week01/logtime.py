import logging
import os


class mylogging:
    def __init__(self, logfilePath: str):
        logging.basicConfig(filename=logfilePath,
                            format='%(asctime)s %(message)s', filemode='w')
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)

    def log(self, message: str):
        self.logger.info(message)


def test():
    LOGROOT = '/var/log/python'
    try:
        if not os.path.exists(LOGROOT):
            os.makedirs(LOGROOT, exist_ok=True)
    except (PermissionError):
        print(f"Please contact your admin to help you create {LOGROOT}")
        print("and assign the proper permission.")
        return

    mylogger = mylogging(f'{LOGROOT}/log.log')
    mylogger.log("hello, Python")


if __name__ == '__main__':
    test()
