# Importing IntentBuilder
from adapt.intent import IntentBuilder
# Importing MycroftSkill class
from mycroft.skills.core import MycroftSkill

# Creating HelloWorldSKill extending MycroftSkill
class ArchTest(MycroftSkill):
    
    def __init__(self):
        super(ArchTest, self).__init__("ArchTest")

    def initialize(self):
         my_setting = self.settings.get('my_setting')
         
 @intent_handler(IntentBuilder('GreetingsIntent').require('Greetings'))
    def handle_Greetings_Intent(self, message):
        """ This is an Adapt intent handler, it is triggered by a keyword."""
        self.speak_dialog("Greetings")
        
    def stop(self):
        pass


def create_skill():
    return ArchTest()
