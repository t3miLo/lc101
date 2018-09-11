# The code below contains a Chatbot class. A Chatbot is an object that can
# engage in rudimentary conversation with a human. You will be asked to define
# a subclass that inherits from this Chatbot superclass.

# Your job is to make a subclass called BoredChatbot that inherits from Chatbot,
# but acts a little differently, in the following way:
#    A bored chatbot has a short attention span. When the human says something that is
#    longer than 20 characters, it should respond by saying:
#        “zzz... Oh excuse me, I dozed off reading your essay.”

#    If, on the other hand, the human says something with a length of 20 characters or less,
#    then the bored chatbot should respond just like a normal chatbot would.

# Note that we are requiring you to use inheritance. Your new BoredChatbot class must be
# a subclass of the Chatbot class, and your subclass should only implement the things that
# make it distinct. (See the Inheritance chapter for a review of how this works.)


class Chatbot:
    """ An object that can engage in rudimentary conversation with a human. """

    def __init__(self, name):
        self.name = name

    def greeting(self):
        """ Returns the Chatbot's way of introducing itself. """
        return "Hello, my name is " + self.name + ' '

    def response(self, prompt_from_human):
        """ Returns the Chatbot's response to something the human said. """
        return "It is very interesting that you say: '" + prompt_from_human + "' "


class BoredChatbot(Chatbot):

    def __init__(self, name):
        super().__init__(name)

    def response(self, human_message):
        if len(human_message) >= 20:
            return 'Sorry can you repeat yourself I dosed of with your essay!!!'
        else:
            return super().response(human_message)

        # make a chatbot
        # sally = Chatbot("Sally")
        # introduce the chatbot and allow the user to say something
        # human_message = input(sally.greeting())self.name = name
        # respond to the user
        # print(sally.response(human_message))

        # TODO: keep reading! see below


james = BoredChatbot('James')
human_message = input(james.greeting())
print(james.response(human_message))
