from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
import json

# 每次启动服务清空被选中的数量
with open('goodsInfo.json', 'r', encoding='utf-8') as f: 
    goods_info = json.loads(f.read())['goodsInfo']
    
for good in goods_info:
    if good['num'] > 0:
        good['num'] = 0
with open('goodsInfo.json', 'w', encoding='utf-8') as f:
    json.dump({'goodsInfo': goods_info}, f, ensure_ascii=False)


def get_goods_info(request):
    with open('goodsInfo.json', 'r', encoding='utf-8') as f: 
        goods_info = json.loads(f.read())
    return JsonResponse(goods_info, status=200)

def get_carts_info(request):
    with open('goodsInfo.json', 'r', encoding='utf-8') as f: 
        goods_info = json.loads(f.read())['goodsInfo']
    return_data = {'goodsInfo': []}
    for good_info in goods_info:
        if good_info['num'] > 0:
            return_data['goodsInfo'].append(good_info)
    return JsonResponse(return_data, status=200)

def add_car(request):
    with open('goodsInfo.json', 'r', encoding='utf-8') as f: 
        goods_info = json.loads(f.read())['goodsInfo']
    
    id = int(json.loads(request.body)['id'])
    for good in goods_info:
        if good['id'] == id:
            good['num'] += 1
            print(f'当前{good["name"]}的数量为：{good["num"]}')
            break
    with open('goodsInfo.json', 'w', encoding='utf-8') as f:
        json.dump({'goodsInfo': goods_info}, f, ensure_ascii=False)
    return JsonResponse({'message': 'Success'})

def reduce(request):
    with open('goodsInfo.json', 'r', encoding='utf-8') as f: 
        goods_info = json.loads(f.read())['goodsInfo']
    
    id = int(json.loads(request.body)['id'])
    for good in goods_info:
        if good['id'] == id:
            good['num'] -= 1
            print(f'当前{good["name"]}的数量为：{good["num"]}')
            break
    with open('goodsInfo.json', 'w', encoding='utf-8') as f:
        json.dump({'goodsInfo': goods_info}, f, ensure_ascii=False)
    return JsonResponse({'message': 'Success'})
