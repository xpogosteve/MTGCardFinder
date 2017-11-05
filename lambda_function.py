from mtgsdk import Card
from mtgsdk import Set
from mtgsdk import Type
from mtgsdk import Supertype
from mtgsdk import Subtype
from mtgsdk import Changelog
def build_speechlet_response(title, output, reprompt_text, should_end_session):
        return {
            'outputSpeech': {
                'type': 'PlainText',
                'text': output
            },
            'card': {
                'type': 'Simple',
                'title': title,
                'content': output
            },
            'reprompt': {
                'outputSpeech': {
                    'type': 'PlainText',
                    'text': reprompt_text
                }
            },
            'shouldEndSession': should_end_session
        }
def build_response(session_attributes, speechlet_response):
    return {
        'version': '1.0',
        'sessionAttributes': session_attributes,
        'response': speechlet_response
    }
def get_card(card_request, session):
    session_attributes = {}
    cards = Card.where(name=card_request['intent']['slots']['CardName']['value'])\
                .where(contains='imageUrl').all()
    card = cards[0]
    title = card.name
    output = card.name + " is a " + card.type + " from " + Set.find(card.set).name +",  and it's text reads " + card.text
    reprompt_text = "Please try again"
    return build_response(session_attributes, build_speechlet_response(title,output,reprompt_text,False));
def get_welcome_response():
    session_attributes = {}
    card_title = "Welcome"
    speech_output = "Welcome to the Magic, The Gathering card finder, " \
                    "ask me to tell you about a card"
    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = "Sorry I don't know that card " \
                    "Ask me to tell you about another card."
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))
def on_launch(launch_request, session):
    """ Called when the user launches the skill without specifying what they
    want
    """

    print("on_launch requestId=" + launch_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # Dispatch to your skill's launch
    return get_welcome_response()
def on_session_ended(session_ended_request, session):
    """ Called when the user ends the session.

    Is not called when the skill returns should_end_session=true
    """
    print("on_session_ended requestId=" + session_ended_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # add cleanup logic here
def lambda_handler(event, context):
    if (event['session']['application']['applicationId'] !=
        "amzn1.ask.skill.cc939b29-a4ba-43bb-bf0d-83ddc92758e2"):
        raise ValueError("Invalid Application ID")
    if event['request']['type'] == "LaunchRequest":
        return on_launch(event['request'], event['session'])
    elif event['request']['type'] == "IntentRequest":
        return get_card(event['request'], event['session'])
    elif event['request']['type'] == "SessionEndedRequest":
        return on_session_ended(event['request'], event['session'])
