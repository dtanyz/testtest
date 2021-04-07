from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import SafetyAlertMsg, SafetyAlertMsgImages
from first_app.models import BFUser

# Create your views here.

def safety_sam(request):
    user = BFUser.objects.get(user=request.user)
    sam_signed = user.sam_signed

    msg_obj = SafetyAlertMsg.objects.all().latest('sam_date')

    images = SafetyAlertMsgImages.objects.filter(alert_msg=msg_obj)

    num_of_slides = ""

    for i in range(len(images)):
        num_of_slides += str(i)

    if request.method == "POST":
        user.sam_signed = True

        user.save()

        return HttpResponseRedirect(reverse('sam'))

    context = {
        'images': images,
        'num_of_slides': num_of_slides,
        'sam_signed': sam_signed,
    }

    return render(request, 'safety_sam.html', context=context)