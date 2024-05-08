from .models import UserAccountTypes
from django.contrib.auth.models import User

def model_context(request):
    if request.user.is_authenticated:
        
        current_user = request.user
        
        user_account_types = UserAccountTypes.objects.filter(user=current_user).first()
        
        return {'account_type': user_account_types.account_type}
    else:
        return {}
