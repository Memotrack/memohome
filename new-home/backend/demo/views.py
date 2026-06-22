from django.http import JsonResponse
import json
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def demo_request(request):
    # Allow CORS preflight OPTIONS request
    if request.method == 'OPTIONS':
        response = JsonResponse({'detail': 'CORS preflight OK'})
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "POST, OPTIONS"
        response["Access-Control-Allow-Headers"] = "Content-Type, Accept"
        return response

    if request.method != 'POST':
        response = JsonResponse({'error': 'Method not allowed'}, status=405)
        response["Access-Control-Allow-Origin"] = "*"
        return response
    try:
        data = json.loads(request.body)
        name = data.get('name', '').strip()
        institution = data.get('institution', '').strip()
        email = data.get('email', '').strip()

        if not all([name, institution, email]):
            response = JsonResponse({'error': 'Missing fields'}, status=400)
            response["Access-Control-Allow-Origin"] = "*"
            return response

        send_mail(
            subject=f'Demo Request — {institution}',
            message=f'Name: {name}\nInstitution: {institution}\nEmail: {email}',
            from_email='mohanadharshini2404@gmail.com',
            recipient_list=['mohanadharshini2404@gmail.com'],
        )
        response = JsonResponse({'success': True})
        response["Access-Control-Allow-Origin"] = "*"
        return response
    except Exception as e:
        response = JsonResponse({'error': str(e)}, status=500)
        response["Access-Control-Allow-Origin"] = "*"
        return response