from django.shortcuts import render

def mainPage(request, pk):
    template_name = 'backendSys/mainPage.html'
    admin = request.user.profile.admin.get(admin__user__pk=pk)
    admins = request.user.profile.admin.filter()
    category = request.user.profile.category.filter()               #bbs.models.Category.admin
    permission = admin.permission.filter()
    context = {
        'admin':admin,
        'category':category,
        'permission':permission,
        'admins':admins,
    }
    return render(request, template_name,context)
