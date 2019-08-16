from django.shortcuts import render, get_object_or_404,render_to_response
from django.http import HttpResponse, Http404
from .models import Enemy, Player, Field, Leveling
from django.template import loader
import random,math

# Create your views here.
def index(request):
    get_field = Field.objects.all()
    template = loader.get_template('plays/index.html')
    context = {
        'get_field' : get_field,
    }
    return HttpResponse(template.render(context,request))
def result(request, field_id):
    try:
        enemy = random.choice(Enemy.objects.filter(appear_field=field_id))
    except:
        raise Http404("This field have no monster")
    template = loader.get_template('plays/result.html')       
    player = Player.objects.filter(id=1).first()
    ehp = enemy.hp
    php = player.hp
    hplist=[]
    #enemyhplist=[]
    #playerhplist=[]
    totalround=0
    while (ehp >0 and php >0):
        ehp-=player.attack
        php-=enemy.attack
        hplist.append([ehp,php])
      
        #enemyhplist.append(ehp)
        #playerhplist.append(php)
        
        totalround+=1
    hpleft=ehp/enemy.hp
    if (php>0):
        winxpcalculate(player.id, enemy.id)
    else:
        losexpcalculate(player.id, enemy.id, hpleft)
    context ={
        'hp':hplist,
        #'ehp':enemyhplist,
        #'php':playerhplist,
        'enemy': enemy,
        'player': player,
        'round':totalround,
    }
    return HttpResponse(template.render(context,request))
    #get_enemy = random.choice(get_enemy)
    
    #return HttpResponse(enemyhplist)

def winxpcalculate(player_id, enemy_id):
    player = Player.objects.get(id=player_id)
    enemy = Enemy.objects.get(id=enemy_id)
    player.xp +=enemy.xp_gain

    player.save()

#def losexpcalculate(player_id, enemy_id, hpleft):
 

