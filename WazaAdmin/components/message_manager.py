from django_unicorn.components import UnicornView
from WazaAdmin.models import Message

class MessageManagerView(UnicornView):
    messages = Message.objects.none()
    msg = None
    reply = ""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.refreash_state()
        
    def set_msg(self,pk):
        self.msg = Message.objects.get(pk=pk)
        
    def reply_to_msg(self):
        self.msg.read = True
        self.msg.save()
        self.refreash_state()
        
    def refreash_state(self):
        self.messages = Message.objects.filter(read=False)
