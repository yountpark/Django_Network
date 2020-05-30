from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from .models import Candidate

now = timezone.now()
cnt = 0

#게임 대기 화면
def index(request):
    candidates = Candidate.objects.all()
    context = {'candidates':candidates}
        #context에 모든 후보 정보를 저장
    return render(request, 'elections/index2.html', context)
        #context안에 있는 후보 정보를 index2.html로 전달

#게임 화면
def game(request):
    candidates = Candidate.objects.all()
    context = {'candidates':candidates}

    # 득표수 초기화
    for i in candidates:
        i.votes = 0
        i.life = True
        i.save()
    return render(request, 'elections/index.html', context)

# 투표 버튼 누를때 마다 이벤트 발생
def polls(request):
    global cnt
    cnt = cnt + 1

    # poll = Poll.objects.get(pk = poll_id)#Poll객체를 구분하는 녀석은 poll_id이므로 PK지정
    selection = request.POST['choice']
    candi = Candidate.objects.get(pk = selection)
    
    candi.votes += 1 #투표수 증가
    candi.save()

    #다시 첫 화면으로 돌아옴
    candidates = Candidate.objects.all()
    context = {'candidates':candidates}
        #context에 모든 어린이 정보를 저장

    if cnt%5 == 0:
        max = 0
        who = 'name'
        for i in candidates:
            if max < i.votes:
                max = i.votes
                who = i.name
                #print(who.name)
        for i in candidates:
            if(who == i.name):
                i.life = False
                i.save()
    
    
    return render(request, 'elections/index.html', context)
    # return을 하지 않으면 화면이 바뀌지 않고, 득표수만 증가한다
    # return HttpResponse("finish")


