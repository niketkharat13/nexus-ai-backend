from fastapi import APIRouter, Depends, status
from app.api.dependencies import get_current_user, permission_check
from app.models.enums import Role
from app.models.user import User
from app.schemas.user import UserResponse

router = APIRouter(prefix="/users", tags=["User"])

@router.post("/me", response_model=UserResponse, status_code=status.HTTP_200_OK)
async def create_user(current_user: User = Depends(get_current_user)):
    return UserResponse.model_validate(current_user)


@router.get("/admin")
async def admin_dashboard(
    current_user=Depends(
        permission_check(Role.ADMIN)
    ),
):
    return {
        "message": "Welcome Admin"
    }