from django.http import HttpResponse
import json

from django_test.lib import cassandra

def getuser(request, userid):
    #print(cass)
    user = cassandra.get_user_by_userid(userid)
    return HttpResponse(json.dumps(user))

