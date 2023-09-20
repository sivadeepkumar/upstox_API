from django.shortcuts import render, redirect
from rest_framework.response import Response
from django.http import JsonResponse
import requests
from upstox_client import *
import pdb
# import urllib.parse
from decouple import config
from django.http import *

# upstox_app/views.py
def upstox_login(request):
    redirect_url = config('UPSTOX_REDIRECT_URI')
    response = "https://api-v2.upstox.com/login/authorization/dialog?client_id={}&redirect_uri={}".format(config('UPSTOX_CLIENT_ID'),config('UPSTOX_REDIRECT_URI'))
    return redirect(response)

   
def get_access_token(request):
    code = request.GET.get('code')
    print(code)
    # URL for obtaining the access token
    token_url = 'https://api-v2.upstox.com/login/authorization/token'

    # Request headers
    headers = {
        'accept': 'application/json',
        'Api-Version': '2.0',
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    # Request data
    data = {
        'code': code,
        'client_id': config('UPSTOX_CLIENT_ID'),
        'client_secret': config("UPSTOX_CLIENT_SECRET"),
        'redirect_uri': config('UPSTOX_REDIRECT_URI'),
        'grant_type': 'authorization_code'
    }

    # Making the POST request
    response = requests.post(token_url, headers=headers, data=data)

    # Print the response
    print(response.json())
    if response.status_code == 200:
        # print('Access Token:',response.json().get('access_token'))
        access_token = response.json().get('access_token')
        print('#########################')
        print(access_token)
        request.session['access_token'] = access_token
        
    else:
        #Request Failed 
        print('Error:' ,response.status_code,response.text)

    # return HttpResponse('given')
    return redirect('get_user_profile')
 


def get_user_profile(request):
    access_token = request.session.get('access_token')
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
    access_token = request.session.get('access_token')
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
    access_token = request.session.get('access_token')
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