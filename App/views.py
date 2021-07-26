from django.shortcuts import render,redirect
from . models import Meeting,Channel
from datetime import datetime
import secrets


# Create your views here.
def index(request):
    app_id="replace_with_app_id"
    if request.method=="POST":
        channel=request.POST.get("channel")
        new=request.POST.get("new")
        if new:
            dir(secrets)
            channel=secrets.token_urlsafe()
            url="agora/?channel="+channel
            save_channel=Channel.objects.create(channel=channel,app_id=app_id)
            save_channel.save()
            meeting = Meeting.objects.create(channel=channel)
            meeting.save()
            return redirect(url)
        if Meeting.objects.filter(channel=channel):
            url="agora/?channel="+channel
            if Channel.objects.filter(app_id=app_id,channel=channel):
                channel_delete=Channel.objects.get(app_id=app_id,channel=channel)
                channel_delete.delete()
                save_channel=Channel.objects.create(channel=channel,app_id=app_id)
                save_channel.save()
            else:
                save_channel=Channel.objects.create(channel=channel,app_id=app_id)
                save_channel.save()
            return redirect(url)
    return render(request,"app1/index.html")

def schedule(request):
    context={}
    try:
        if request.method =="POST":
            channel = request.POST.get("channel_name")
            meeting_title = request.POST.get("meeting_title")
            meeting_subject = request.POST.get("meeting_subject")
            start_time = request.POST.get("start_time")
            end_time = request.POST.get("end_time")
            date = request.POST.get("date")

            if Meeting.objects.filter(channel=channel):
                if datetime.now().time()> Meeting.objects.get(channel=channel).end_time:
                    meeting_old=Meeting.objects.get(channel=channel)
                    meeting_old.delete()
                    meeting = Meeting.objects.create(channel=channel,meeting_title=meeting_title,
                    meeting_subject=meeting_subject,start_time=start_time, end_time=end_time,date=date)
                    meeting.save()
                    filename=meeting_title.replace(" ","")+".txt"
                    with open(filename, 'x') as f:
                        f.write('meeting title: '+meeting_title+"\n channel: "+channel+"\n meeting_subject: "+meeting_subject+"\n time: "+ time+"\n date: "+date)
                    context={"message":"File With meeting details added to directory"}
                else:
                    context={"message":"Channel with the same name already exists"}
            else:
                meeting = Meeting.objects.create(channel=channel,meeting_title=meeting_title,
                meeting_subject=meeting_subject,start_time=start_time, end_time=end_time,date=date)
                meeting.save()
                filename=meeting_title.replace(" ","")+".txt"
                with open(filename, 'x') as f:
                    f.write('meeting title: '+meeting_title+"\n channel: "+channel+"\n meeting_subject: "+meeting_subject+"\n start time: "+ start_time+"\n end time: "+ end_time+"\n date: "+date)
                context={"message":"File With meeting details added to directory"}
    except:
        context={"message":"An error occurred"}
    return render(request,"app1/schedule.html",context)

def success(request):
    return render(request,"app1/success.html")
