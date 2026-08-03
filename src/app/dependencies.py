from app.services.user_service import UserService
def mock_get_user_db():
    return {
        "id": 1,
        "name": "Niket",
        "role": "Admin"
    }

user_service = UserService()

def get_user_service():
    return user_service