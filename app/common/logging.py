import logging
import colorlog

# 커스텀 로그 포맷터 생성
class CustomFormatter(colorlog.ColoredFormatter):
    def format(self, record):
        # INFO: 뒤에 공백 추가
        if record.levelname == 'INFO':
            record.levelname = 'INFO: '
        return super().format(record)

# 로거 설정
logger = colorlog.getLogger()
logger.setLevel(logging.INFO)

# 스트림 핸들러 생성 및 포맷터 설정
handler = colorlog.StreamHandler()
handler.setFormatter(CustomFormatter(
    "%(log_color)s%(levelname)-8s%(reset)s%(message)s",
    log_colors={
        'DEBUG': 'cyan',
        'INFO: ': 'blue',  # INFO에 대한 색상 설정
        'WARNING': 'yellow',
        'ERROR': 'red',
        'CRITICAL': 'purple',
    }
))

# 핸들러를 로거에 추가
logger.addHandler(handler)
