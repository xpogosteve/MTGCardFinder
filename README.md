# MTGCardFinder
## Inspiration
I have been obsessed with Magic: the Gathering for about a year now, but I was finding that when I watched Twitch Streams I didn't know what all of the cards did while I was watching. I figured it would be useful to create a skill for Alexa so that she could do work and tell me.
## What it does
Given a card name, finds relevant information for the card and tells you about it through the Amazon Echo.
Use by saying "Alexa, Start Magic Card Finder", then  "Find [card name]" (currently only contains cards from Amonkhet)
Example Card Names:
Oketra the True
Hazoret the Fervent
Gideon of the Trials
Essence Scatter
## How I built it
Using the Alexa SDK, Python, and AWS, I created a lambda function in python on AWS that connects to a skill hosted on the Alexa Skills Set and grabs card info from an API on magicthegathering.io which I was then able to test with an Amazon Echo.
## Challenges I ran into
Adding images to home card
Having Alexa not sound super clunky when responding
Adding cardnames as json
## Accomplishments that I'm proud of
Working with the Alexa API
Learning more about AWS and how to use it
## What I learned
more python
AWS Lambda Function
Developing Alexa Skills
Working with APIs and External Libraries in AWS
Parsing JSON responses
## What's next for Magic: The Gathering Card Finder
Finishing adding images to home cards
Add more sets to the skill
add pricing info
