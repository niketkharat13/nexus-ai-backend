from fastapi import APIRouter, Depends

router = APIRouter()

def mock_get_user_db():
    return {
        "id": 1,
        "name": "Niket",
        "role": "Admin"
    }

@router.get("/users/me", tags=["User"])
def profile(user = Depends(mock_get_user_db)):
    return user
    
