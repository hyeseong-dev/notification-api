from dataclasses import dataclass
from os import path, environ

base_dir = path.dirname(path.dirname(path.dirname(path.abspath(__file__))))

@dataclass
class Config:
    """
    기본 Configuration
    """
    BASE_DIR = base_dir

    DB_POOL_RECYCLE: int = 900
    DB_ECHO: bool = True


@dataclass
class LocalConfig(Config):
    PROJ_RELOAD: bool = True


@dataclass
class ProdConfig(Config):
    PROJ_RELOAD: bool = False

print('실행')
print(LocalConfig())

def conf():
    """
    환경 불러오기
    :return:
    """
    config = dict(prod=ProdConfig(), local=LocalConfig())
    return config.get(environ.get("API_ENV", "local"))
'''

dataclass decorator는 적용되는 클래스의 정보를 딕셔너리로 사용하기 위해서입니다. 
폴더 및 파일 구조 변경시, 해당 파일을 기점으로 각 모듈, 패키지들을 쉽게 참조하기 위함임.

***중요! 객체를 딕셔너리로 사용하기 위해서는 asdict() 함수 이용! ***


참고로 path.abspath(__file__)는 작성된 모듈의 절대경로를 나타내고 path.dirname은 경로의 부모 폴더를 가리킵니다.
'''