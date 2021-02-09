import uvicorn

from .settings import api

if __name__ == '__main__':
    uvicorn.run('api:app', host=api.API_HOST, port=api.API_PORT, debug=api.API_DEBUG, reload=api.API_RELOAD, access_log=api.API_LOG)
