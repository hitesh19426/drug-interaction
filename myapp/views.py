from django.shortcuts import render
from .models import drugInterectionTable
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
import json

def decode_json(raw_body):
    body_unicode = raw_body.decode("utf-8")
    body = json.loads(body_unicode)
    return body

# Create your views here.
@csrf_exempt
def home(request):
    if request.method == "GET":
        drug_level = drugInterectionTable.objects.all()[0]
        return render(request, "test.html", {
            'entry': drug_level
        })
    elif request.method == "POST":
        data = decode_json(request.body)
        drug_list = data.get('drugs')
        # print("drug_list ", drug_list)

        dic = {
            "data" : []
        }
        for i in range(0, len(drug_list)):
            for j in range(0, len(drug_list)):
                temp = {}
                try:
                    print("----------------------------------------")
                    print(drug_list[i], " ", drug_list[j])

                    interaction = drugInterectionTable.objects.filter(Q(drug1_name = drug_list[i]) & Q(drug2_name = drug_list[j])).get()
                    
                    # print(interaction.values_list())
                    print("interaction.drug1_name", interaction.drug1_name)

                    temp['drug1'] = interaction.drug1_name
                    temp['drug2'] = interaction.drug2_name
                    temp['level'] = interaction.level

                    print("------------------------------------------")
                    dic["data"].append(temp)
                except Exception as e:
                    print(e)
                    pass

        # print(request.POST.get("id"))
        print(dic)
        return JsonResponse(safe=False, data=dic)
