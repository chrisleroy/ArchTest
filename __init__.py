# Importing IntentBuilder
from adapt.intent import IntentBuilder
# Importing MycroftSkill class
from mycroft.skills.core import MycroftSkill

# Creating HelloWorldSKill extending MycroftSkill
class ArchTest(MycroftSkill):
    
    def __init__(self):
        super(ArchTest, self).__init__("ArchTest")

    def initialize(self):
        # Creating GreetingsIntent requiring Greetings vocab
        greetings = IntentBuilder("GreetingsIntent")
                           .require("greetings").build()
        # Associating a callback with the Intent
        self.register_intent(greetings, self.handle_greetings)
        
    def handle_greetings(self):
        # Sending a command to mycroft, speak Greetings Dialog
        self.speak_dialog("greetings")
        
    def stop(self):
        pass


def create_skill():
    return ArchTest()
