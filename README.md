# BBS(for developer)
develop with Django

## ACCOUNT FRO ADMIN SITE
account - password
- normal user - (has no permission to enter the admin site)   
test_user - stubbs..
- super user    
yx2 - stubbs..  
- admin     
test_user

## DJANGO PACKAGE
download all require package:
>  pip install -r requirements.txt

## IMPORTANT
- CSRF verification     

> return render_to_response('login.html')    

>>这种跳转没有把request对象传出去，导致很多request里面的变量无法引用，包括csrf，所以登陆的时候无法验证csrf。request里面包含了绝大部分的信息，包括用户的信息，之前用户权限的问题就是因为request没有传到首页，导致template里面的user变量无法引用（已经更改）。如遇到其他奇奇怪怪的问题，请把页面跳转的方式改一下，具体可以参考文档。    

>template_name = 'login.html'    
context = {}    
return render(request,template_name,context)    