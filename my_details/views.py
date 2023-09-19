# from django.shortcuts import render
# from django.http import JsonResponse
# import requests
# from upstox_client import *

# # Create your views here.
# access_token = 'eyJ0eXAiOiJKV1QiLCJrZXlfaWQiOiJza192MS4wIiwiYWxnIjoiSFMyNTYifQ.eyJzdWIiOiIzOTQ5NjMiLCJqdGkiOiI2NTA4N2IxNThiYzM5NjIyNTMzMTljOGMiLCJpc011bHRpQ2xpZW50IjpmYWxzZSwiaXNBY3RpdmUiOnRydWUsInNjb3BlIjpbImludGVyYWN0aXZlIiwiaGlzdG9yaWNhbCJdLCJpYXQiOjE2OTUwNTQ2MTMsImlzcyI6InVkYXBpLWdhdGV3YXktc2VydmljZSIsImV4cCI6MTY5NTA3NDQwMH0.HliDFDrSMa84N8DaG2NoDl8wFwly0yG4mXHGQM9uLH0'


# # upstox_app/views.py


# def get_user_profile(request):
#     api_endpoint = 'https://api-v2.upstox.com/user/profile'
#     headers = {
#         'accept': 'application/json',
#         'Api-Version': '2.0',
#         'Authorization': f'Bearer {access_token}'
#     }
#     response = requests.get(api_endpoint, headers=headers)

#     if response.status_code == 200:
#         user_profile_data = response.json()
#         user_profile = user_profile_data['data']
#         return JsonResponse({'user_profile': user_profile})
#     else:
#         return JsonResponse({'error': f"Error: {response.status_code} - {response.text}"}, status=500)


# def get_orders(request):
#     api_endpoint = 'https://api-v2.upstox.com/order/retrieve-all'
#     headers = {
#         'accept': 'application/json',
#         'Api-Version': '2.0',
#         'Authorization': f'Bearer {access_token}'
#     }
#     response = requests.get(api_endpoint, headers=headers)

#     if response.status_code == 200:
#         orders_data = response.json()
#         orders = orders_data['data']
#         return JsonResponse({'orders': orders})
#     else:
#         return JsonResponse({'error': f"Error: {response.status_code} - {response.text}"}, status=500)




# def each_order(request,id):
#     api_endpoint = f'https://api-v2.upstox.com/order/history?tag={id}'
#     headers = {
#         'accept': 'application/json',
#         'Api-Version': '2.0',
#         'Authorization': f'Bearer {access_token}'
#     }
#     response = requests.get(api_endpoint, headers=headers)

#     if response.status_code == 200:
#         orders_data = response.json()
#         orders = orders_data['data']
#         return JsonResponse({'orders': orders})
#     else:
#         return JsonResponse({'error': f"Error: {response.status_code} - {response.text}"}, status=500)





from django.shortcuts import render, redirect
from rest_framework.response import Response

from django.http import JsonResponse
import requests
from upstox_client import *
import pdb
import os
import urllib.parse

# Create your views here.
access_token = 'eyJ0eXAiOiJKV1QiLCJrZXlfaWQiOiJza192MS4wIiwiYWxnIjoiSFMyNTYifQ.eyJzdWIiOiIzOTQ5NjMiLCJqdGkiOiI2NTA4N2IxNThiYzM5NjIyNTMzMTljOGMiLCJpc011bHRpQ2xpZW50IjpmYWxzZSwiaXNBY3RpdmUiOnRydWUsInNjb3BlIjpbImludGVyYWN0aXZlIiwiaGlzdG9yaWNhbCJdLCJpYXQiOjE2OTUwNTQ2MTMsImlzcyI6InVkYXBpLWdhdGV3YXktc2VydmljZSIsImV4cCI6MTY5NTA3NDQwMH0.HliDFDrSMa84N8DaG2NoDl8wFwly0yG4mXHGQM9uLH0'
redirect_url = urllib.parse.quote(f"{os.environ.get('UPSTOX_REDIRECT_URI')}",safe="")
client_id = os.environ.get("UPSTOX_CLIENT_ID")
# upstox_app/views.py
def upstox_login(request):
    response = requests.get(f'https://api-v2.upstox.com/login/authorization/dialog?response_type=code&client_id={os.environ.get("UPSTOX_CLIENT_ID")}&redirect_uri={os.environ.get("UPSTOX_REDIRECT_URI")}')
    # r = requests.get("https://api-v2.upstox.com/login/authorization/dialog?response_type=code&client_id={}&redirect_uri={}".format(client_id,urllib.parse.quote(f"{os.environ.get('UPSTOX_REDIRECT_URI')}",safe="")))
    pdb.set_trace()
    redirect_url = response.url
    return redirect(redirect_url)

def get_access_token(code):
    data = {
        "client_id": os.environ.get("UPSTOX_CLIENT_ID"),
        "client_secret": os.environ.get("UPSTOX_CLIENT_SECRET"),
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": os.environ.get('UPSTOX_REDIRECT_URI')
    }

    url = "https://discord.com/api/oauth2/token"
    response = requests.post(url, data=data)

    return response.json()["access_token"]
0
def upstox(request):
  pdb.set_trace()

def get_user_profile(request):
    api_endpoint = 'https://api-v2.upstox.com/user/profile'
    headers = {
        'accept': 'application/json',
        'Api-Version': '2.0',
        'Authorization': f'Bearer {access_token}'
    }
    response = requests.get(api_endpoint, headers=headers)

    if response.status_code == 200:
        user_profile_data = response.json()
        user_profile = user_profile_data['data']
        return JsonResponse({'user_profile': user_profile})
    else:
        return JsonResponse({'error': f"Error: {response.status_code} - {response.text}"}, status=500)


def get_orders(request):
    api_endpoint = 'https://api-v2.upstox.com/order/retrieve-all'
    headers = {
        'accept': 'application/json',
        'Api-Version': '2.0',
        'Authorization': f'Bearer {access_token}'
    }
    response = requests.get(api_endpoint, headers=headers)

    if response.status_code == 200:
        orders_data = response.json()
        orders = orders_data['data']
        return JsonResponse({'orders': orders})
    else:
        return JsonResponse({'error': f"Error: {response.status_code} - {response.text}"}, status=500)




def each_order(request,id):
    api_endpoint = f'https://api-v2.upstox.com/order/history?tag={id}'
    headers = {
        'accept': 'application/json',
        'Api-Version': '2.0',
        'Authorization': f'Bearer {access_token}'
    }
    response = requests.get(api_endpoint, headers=headers)

    if response.status_code == 200:
        orders_data = response.json()
        orders = orders_data['data']
        return JsonResponse({'orders': orders})
    else:
        return JsonResponse({'error': f"Error: {response.status_code} - {response.text}"}, status=500)