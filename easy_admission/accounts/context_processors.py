from .models import UserAccountTypes

def model_context(request):
    if request.user.is_authenticated:
        current_user = request.user
        
        # Check if the current user is a superuser
        if current_user.is_superuser:
            account_type = 'superuser'
        else:
            user_account_types = UserAccountTypes.objects.filter(user=current_user).first()
            account_type = user_account_types.account_type if user_account_types else 'No Account Type'
        
        return {'account_type': account_type}
    else:
        return {}
