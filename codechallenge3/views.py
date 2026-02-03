from django.shortcuts import render
from .models import CompanyTool

def tool_list(request):
    tools = CompanyTool.objects.all()
    return render(request, "codechallenge3/tools.html", {"tools": tools})