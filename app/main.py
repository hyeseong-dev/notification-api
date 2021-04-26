import uvicorn
from fastapi import FastAPI

from app.common.config import conf


def create_app():
    '''
    앱 함수실행
    :return
    '''

    c = conf()
    app = FastAPI()

    # DB initializing

    # Redis initializing

    # Define middle

    # Define router

    return app

app = create_app()

if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=8000, reload=conf().PROJ_RELOAD)

'''
서버 배포 할 경우에는 reload=conf().PROJ_RELOAD를 사용해서 환경에 따라서 디버깅을 True or False하게 됨.
현재는 conf().PROJ_RELO값을 True 그 자체로 값을 할당함.

추후 Docker 빌드 할 경우 다르게 적용할 예정
배포 환경은 Elastic Beanstalk 과 Travis CI를 통해 환경설정이 추가 될 예정

# 보조 설명 
__name__ == '__main__' 은 실행되는 파일이 main.py와 같이 해당 모듈일 때 해당 조건이 실행됨.
'''