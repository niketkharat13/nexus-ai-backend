from fastapi import APIRouter, Depends, Response
from app.dependencies import mock_get_user_db, get_user_service
from app.services.user_service import UserService
from app.schemas.user import UserCreateRequest, UserResponse, UserUpdateRequest

router = APIRouter(prefix="/users", tags=["User"])


@router.get("/me", response_model=UserResponse)
def profile(user = Depends(mock_get_user_db)):
    return user

@router.post("/", response_model=UserResponse)
def create_user(user: UserCreateRequest, service: UserService = Depends(get_user_service)):
    return service.create_user(user)
    
@router.get("/", response_model=list[UserResponse])
def get_users(service: UserService = Depends(get_user_service), name: str = None, sort_by: str = None, skip: int = 0, limit: int = 10):
    return service.get_users(name, sort_by, skip, limit)

@router.put("/{user_id}", response_model=UserResponse)
def update_user(user_id: int, user: UserUpdateRequest, service: UserService = Depends(get_user_service)):
    return service.update_user(user_id, user)

@router.delete("/{user_id}")
def delete_user(user_id: int, service: UserService = Depends(get_user_service)):
    service.delete_user(user_id)
    return Response(status_code=204)