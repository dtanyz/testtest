from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django.views.generic import TemplateView
from .models import BFUser, AllABoldface, OpsBriefMinutes, Minutes, Absentee
from django.core import serializers
from .forms import OBMinutesFormSet
from datetime import datetime
from django.contrib.auth import get_user_model

# Create your views here.
class IndexView(TemplateView):
    template_name = "index.html"

def log_out(request):
    return render(request, 'registration/logout.html')

ans = {
    # Egress
    'bf0': 'PARK BRK',
    'bf1': 'SET',
    'bf2': 'EM SWITCHES',
    'bf3': 'STOP',
    'bf4': 'APU',
    'bf5': 'STOP',
    'bf6': 'L & R BATT',
    'bf7': 'OFF',
    'bf8': 'SEAT',
    'bf9': 'SAFE',
    'bf10': 'QRB',
    'bf11': 'OPEN',
    'bf12': 'PSP/OXY/RADIO/CRU-60',
    'bf13': 'DISC',
    'bf14': 'CANOPY',
    'bf15': 'OPEN',
    # APU Fire on Ground
    'bf16': 'APU',
    'bf17': 'STOP',
    'bf18': 'APU FUEL SOV',
    'bf19': 'SHUT',
    'bf20': 'EM SWITCHES',
    'bf21': 'STOP',
    'bf22': 'APU EXTG',
    'bf23': 'DISCH',
    'bf24': 'EGRESS',
    # Eng Fire on Ground
    'bf25': 'EM SWITCHES',
    'bf26': 'STOP',
    'bf27': 'FUEL SOV',
    'bf28': 'SHUT',
    'bf29': 'APU',
    'bf30': 'STOP',
    'bf31': 'ENG EXTG',
    'bf32': 'DISCH',
    'bf33': 'EGRESS',
    # Eng Fire During Take-Off
    'bf34': 'ABORT',
    'bf35': 'ENG FIRE ON GROUND',
    'bf36': 'THROTTLES',
    'bf37': 'MAX',
    'bf38': 'STORES',
    'bf39': 'JETT',
    'bf40': 'ENG FIRE IN FLT',
    # Eng Fire in Flight
    'bf41': 'THROTTLE',
    'bf42': 'IDLE',
    'bf43': 'EM SWITCH',
    'bf44': 'STOP',
    'bf45': 'FUEL SOV',
    'bf46': 'SHUT',
    'bf47': 'ENG EXTG',
    'bf48': 'DISCH',
    'bf49': 'EJECT',
    # Eng Failure During Take-Off
    'bf50': 'ABORT',
    'bf51': 'THROTTLES',
    'bf52': 'MAX',
    'bf53': 'STORES',
    'bf54': 'JETT',
    'bf55': 'MAINT A/C CONFIG',
    # Double Eng Flameout
    'bf56': 'EJECT',
    'bf57': 'GENTLE MAN ONLY',
    'bf58': 'DIVE AT 10-12 DEG FPA',
    'bf59': 'THROTTLES',
    'bf60': 'IDLE',
    'bf61': 'L & R HYD',
    'bf62': 'MONITOR',
    # L & R BLEED
    'bf63': 'B/U OXY',
    'bf64': 'B/U',
    'bf65': 'THROTTLES',
    'bf66': 'IDLE',
    'bf67': 'BLEED KNOB',
    'bf68': 'OFF',
    'bf69': 'L & R BLEED WARN LIGHTS',
    'bf70': 'CHECK OFF',
    'bf71': 'DESC AT OR BELOW 10000FT ASAP',
    # AC DC Fuel Pump Failure
    'bf72': 'AVOID ABRUPT THROTTLES MOVEMENTS',
    'bf73': 'DESC AT OR BELOW 20000FT ASAP',
    # HYD HOT
    'bf74': 'EM SWITCH',
    'bf75': 'STOP',
    # ABORT
    'bf76': 'THROTTLES',
    'bf77': 'IDLE',
    'bf78': 'BRAKES',
    'bf79': 'APPLY',
    # FCS 3RD
    'bf80': 'EJECT',
    'bf81': 'RTB ENV',
    'bf82': 'ATTAIN',
    'bf83': 'A/S',
    'bf84': '<325KCAS/0.75M',
    # LOSS OF CONTROL
    'bf85': 'EJECT',
    'bf86': 'CONTROLS',
    'bf87': 'NEUTRALISE',
    'bf88': 'THROTTLES',
    'bf89': 'IDLE',
    'bf90': 'RUDDER',
    'bf91': 'FULL OPPOSITE TO SPIN',
    'bf92': 'AILERONS',
    'bf93': 'FULL INTO SPIN',
    'bf94': 'CONTROLS',
    'bf95': 'NEUTRALISE',
}


def new_view(request):
    current_user = request.user
    user_id = current_user.id

    def check_boldface(Boldface, range_start, range_end, user_id):
        this_bf = Boldface.objects.get(bf_user=user_id)
        is_correct = True

        for i in range(range_start, range_end):
            if request.POST[f'bf{i}'].upper() == ans[f'bf{i}']:
                setattr(this_bf, f"bf{i}", request.POST[f'bf{i}'].upper())
            else:
                setattr(this_bf, f"bf{i}", "")
                is_correct = False
        if is_correct:
            this_bf.is_complete = True
        else:
            this_bf.is_complete = False

        this_bf.save()

    if request.method == "POST":
        check_boldface(AllABoldface, 0, 34, user_id=user_id)
        boldface_a = AllABoldface.objects.get(bf_user=user_id)

        bf_user = BFUser.objects.get(id=user_id)
        bf_user.update_score()

        is_post_method = 1

    else:
        boldface_a = AllABoldface.objects.get(bf_user=user_id)
        bf_user = BFUser.objects.get(id=user_id)

        is_post_method = 0
        
    boldface_a_data = serializers.serialize('json', [AllABoldface.objects.get(bf_user=user_id)])

    context = {
        'boldface_a': boldface_a,
        'bf_user': bf_user,
        'boldface_a_data': boldface_a_data,
        'is_post_method': is_post_method,
    }

    return render(request, 'test_form.html', context=context)


def gonogo_board(request):
    all_users = BFUser.objects.all()

    for user in all_users:
        print(user)

    context = {
        'all_users': all_users,
    }

    return render(request, 'first_app_go_nogo.html', context=context)


### Ops Brief Minutes

def opsbrief_minutes_create(request):
    ob_minutes = OpsBriefMinutes()

    User = get_user_model()
    users = User.objects.all()

    all_users = BFUser.objects.all()

    if request.method == "POST":
        speakers = request.POST.getlist('speaker')
        messages = request.POST.getlist('write_up')
        absentees = request.POST.getlist('absentees')
        speakers_and_messages = list(zip(speakers, messages))

        date_str = request.POST['datepicker']
        real_date = datetime.strptime(date_str, '%d-%m-%Y')
        ob_minutes.date = real_date
        ob_minutes.minutes_taker = request.POST['minutes_taker']
        ob_minutes.duty_instructor = request.POST['duty_instructor']
        ob_minutes.save()

        for speaker_and_message in speakers_and_messages:
            if speaker_and_message != ("", ""):
                new_minutes = Minutes(minutes_for=ob_minutes, who_talked= speaker_and_message[0], write_up=speaker_and_message[1])
                new_minutes.save()

        for absentee in absentees:
            absent_user = BFUser.objects.get(callsign=absentee)
            new_absentee = Absentee(minutes=ob_minutes, absent_user=absent_user)
            new_absentee.save()

        print(request.POST)

        return HttpResponseRedirect(reverse('opsbrief_minutes_create'))

    context = {
        'all_users': all_users,
    }

    return render(request, 'opsbrief_minutes_create.html', context=context)


def opsbrief_minutes_overview(request):
    all_minutes = OpsBriefMinutes.objects.filter(vetted=True).order_by('-date')

    absent_user = BFUser.objects.get(user=request.user)
    minutes_not_signed = Absentee.objects.filter(absent_user=absent_user)

    context = {
        'all_minutes': all_minutes,
        'minutes_not_signed': minutes_not_signed,
    }

    return render(request, 'opsbrief_minutes_overview.html', context=context)


def opsbrief_minutes_detailview(request, minutes_id):
    minutes = OpsBriefMinutes.objects.get(id=minutes_id)
    write_ups = Minutes.objects.filter(minutes_for=minutes)
    absent_user = BFUser.objects.get(user=request.user)

    was_absent = Absentee.objects.filter(minutes=minutes, absent_user=absent_user)
    

    if was_absent:
        absent = True
    else:
        absent = False

    context = {
        'minutes': minutes,
        'write_ups': write_ups,
        'absent': absent,
    }

    if request.method == "POST":
        was_absent[0].delete()

        absent_ever = Absentee.objects.filter(absent_user=absent_user)
        if absent_ever:
            absent_user.opsbrief_signed = False
            absent_user.save()
        else:
            absent_user.opsbrief_signed = True
            absent_user.save()

        return HttpResponseRedirect(reverse('opsbrief_minutes_detailview', args=(minutes_id,)))

    return render(request, 'opsbrief_minutes_detail.html', context=context)


def vet_minutes_view(request):
    user = BFUser.objects.get(user=request.user)
    minutes_to_vet = OpsBriefMinutes.objects.filter(vetted=False, duty_instructor=user)
    all_users = BFUser.objects.all()

    context = {
        'minutes_to_vet': minutes_to_vet,
    }

    return render(request, 'vet_minutes_overview.html', context=context)


def vet_minutes_detailview(request, minutes_id):
    minutes = OpsBriefMinutes.objects.get(id=minutes_id)
    write_ups = Minutes.objects.filter(minutes_for=minutes)
    absentees = Absentee.objects.filter(minutes=minutes)

    if request.method == "POST":
        speakers = request.POST.getlist('speaker')
        messages = request.POST.getlist('write_up')
        speakers_and_messages = list(zip(speakers, messages))

        for write_up in write_ups:
            write_up.delete()

        for speaker_and_message in speakers_and_messages:
            if speaker_and_message != ("", ""):
                new_minutes = Minutes(minutes_for=minutes, who_talked= speaker_and_message[0], write_up=speaker_and_message[1])
                new_minutes.save()

        minutes.vetted = True
        minutes.save()

        return HttpResponseRedirect(reverse('allopsbrief_minutes'))

    context = {
        'minutes': minutes,
        'write_ups': write_ups,
        'absentees': absentees,
    }

    return render(request, 'vet_minutes_detailview.html', context=context)