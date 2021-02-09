from fastapi import APIRouter, Depends

from ..controllers.auth import login, login_required, logout, register
from .models.auth import LoginRequest, LoginResponse, RegisterRequest, RegisterResponse, ValidateResponse

router = APIRouter()


@router.post('/login', status_code=200, response_model=LoginResponse)
def router_login(body: LoginRequest):
    token, user = login(**body.dict())
    return {'token': token, 'user': user}


@router.post('/logout', status_code=200)
def router_logout(auth: str = Depends(login_required)):
    token, _ = auth
    logout(token)
    return {}


@router.post('/register', status_code=201, response_model=RegisterResponse)
def router_register(body: RegisterRequest):
    register(**body.dict())
    token, user = login(**body.dict())
    return {'token': token, 'user': user}


@router.post('/validate', status_code=200, response_model=ValidateResponse)
def router_validate(auth: str = Depends(login_required)):
    token, user = auth
    return {'user': user, 'token': token}
