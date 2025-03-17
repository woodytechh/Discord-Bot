import discord
import os
import requests
import json
import random
from keepAlive import keep_alive

intents = discord.Intents.default()
intents.message_content = True 

client = discord.Client(intents=intents)

sad_words = [
    "sad", "depressed", "unhappy", "angry", "miserable", "depressing", 
    "hopeless", "heartbroken", "lonely", "tired", "frustrated", "lost", 
    "overwhelmed", "stressed", "worthless", "empty", "exhausted", 
    "hurt", "broken", "crying", "upset", "disappointed", "gloomy", 
    "down", "melancholy", "devastated", "worried", "anxious", "pessimistic", 
    "helpless", "defeated", "shattered", "suffering", "drained", 
    "numb", "hopeless", "guilt", "regret", "distressed", "alone", 
    "rejected", "ashamed", "insecure", "trapped", "worthless", "self-doubt", 
    "fearful", "tormented", "lost", "stuck", "aching", "suffocating", 
    "burned out", "done", "desperate", "crushed", "unwanted", "despair", 
    "agitated", "disturbed", "weary", "betrayed", "sorrowful", "blue", 
    "low", "moody", "aching", "fragile"
]

starter_encouragements = [
    "This too shall pass.",
    "You are stronger than you think.",
    "Pain is temporary, but growth is forever.",
    "Difficult roads lead to beautiful destinations.",
    "Keep moving forward. Always.",
    "You're not alone in this.",
    "Every storm runs out of rain.",
    "It's okay to not be okay.",
    "Your past does not define your future.",
    "You are enough. Right now. As you are.",
    "Sometimes, we need to fall to learn how to rise.",
    "You are braver than you believe, stronger than you seem.",
    "Life is tough, but so are you.",
    "Even the darkest night will end, and the sun will rise.",
    "One small step at a time. Just keep going.",
    "It’s a bad day, not a bad life.",
    "You matter more than you realize.",
    "Not all storms come to destroy. Some clear the way.",
    "You can rise up from anything.",
    "Keep your face towards the sun, and the shadows will fall behind you.",
    "You are not failing. You are growing.",
    "The struggle you’re in today is building the strength you need tomorrow.",
    "The world needs you, exactly as you are.",
    "It’s not over until you win.",
    "Nothing worth having comes easy.",
    "Even broken crayons can still color.",
    "Your heart and mind are stronger than you think.",
    "You’re already enough. Always have been.",
    "Sometimes, the only way out is through.",
    "What’s coming is better than what’s gone.",
    "You’ve survived every bad day so far. Keep going.",
    "Small progress is still progress.",
    "You are someone’s reason to smile today.",
    "You don’t need to have all the answers right now.",
    "You don’t have to be perfect to be amazing.",
    "Everything you need is already within you.",
    "Courage doesn’t mean you don’t get afraid. It means you don’t let fear stop you.",
    "Don’t let a hard day make you feel like you have a bad life.",
    "Broken people shine the brightest.",
    "You are doing better than you think.",
    "Never let a stumble be the end of your journey.",
    "No rain, no flowers.",
    "Sometimes, things fall apart so better things can fall together.",
    "You're going to be okay. Maybe not today, but someday.",
    "You are worthy of love and happiness.",
    "It's okay to rest. Just don’t quit.",
    "This chapter of your life is not your whole story.",
    "You have survived so much. You will survive this too.",
    "Every flower must grow through dirt.",
    "Do what you can, with what you have, where you are.",
    "When one door closes, another opens.",
    "Even on your worst days, you are still loved.",
    "You are not your mistakes.",
    "Everything happens for a reason, even if you don’t see it yet.",
    "The best view comes after the hardest climb.",
    "Doubt kills more dreams than failure ever will.",
    "You’re one decision away from a completely different life.",
    "Great things take time. Be patient with yourself.",
    "Not all who wander are lost.",
    "You are enough just as you are.",
    "The comeback is always stronger than the setback.",
    "You have more power than you realize.",
    "You’ve got this. One step at a time.",
    "“How you doin’?” – Joey Tribbiani, Friends 😉",
    "Sometimes you have to let go of the picture of what you thought life would be like.",
    "Your mistakes do not define you.",
    "Rest, don’t quit.",
    "Someday, this will just be a story you tell.",
    "It’s not the end of the world. It’s just a bad day.",
    "The best is yet to come.",
    "You don’t have to be perfect to be loved.",
    "Your future self is already proud of you.",
    "Stars can’t shine without darkness.",
    "Every day is a fresh start.",
    "Nothing is permanent, not even pain.",
    "It always seems impossible until it’s done.",
    "You are capable of more than you know.",
    "Don't let yesterday take up too much of today.",
    "Inhale confidence, exhale doubt.",
    "Believe in the magic of new beginnings.",
    "A diamond is just a piece of coal that handled pressure well.",
    "No matter how slow you go, you are still lapping everyone on the couch.",
    "Feel the fear and do it anyway.",
    "One day, you’ll look back and realize you made it through.",
    "Your feelings are valid. But they do not define you.",
    "The sun will rise, and so will you.",
    "Every setback is a setup for a comeback.",
    "A single act of kindness can turn someone’s whole day around.",
    "Sometimes the best thing you can do is just breathe and trust.",
    "You don’t find your worth in people. You find it within yourself.",
    "Some things take time. And that’s okay.",
    "You were given this life because you are strong enough to live it.",
    "Stop being afraid of what could go wrong and start being excited about what could go right.",
    "Your time will come. Just be patient.",
    "Be proud of how far you’ve come.",
    "The universe is not against you; it’s waiting for you.",
    "Rock bottom is a solid foundation to build on.",
    "Even the smallest steps move you forward.",
    "Keep believing. Keep hoping. Keep going."
]

thank_you_words = [
    "thank you", "thanks", "thx", "ty", "tysm", "tq", 
    "thank u", "thankyou", "thank-you", "thanx", "appreciate it", 
    "many thanks", "much obliged", "grateful", "big thanks", "cheers",
    "thank u so much", "thx a lot", "thanks a ton", "thanks a million",
    "thank you very much", "thanks a bunch", "thanks a lot", "deeply grateful", 
    "thank ya", "thankies", "much thanks", "endless thanks", "so thankful", 
    "thank you kindly", "thanks loads", "big appreciation",
    "Thank You", "THANK YOU", "THANKS", "THX", "TY", "TQ", "THANK U", 
    "THANKYOU", "THANK-YOU", "THANX", "APPRECIATE IT", 
    "MANY THANKS", "MUCH OBLIGED", "GRATEFUL", "BIG THANKS", "CHEERS",
    "THANK U SO MUCH", "THX A LOT", "THANKS A TON", "THANKS A MILLION",
    "THANK YOU VERY MUCH", "THANKS A BUNCH", "THANKS A LOT", "DEEPLY GRATEFUL", 
    "THANK YA", "THANKIES", "MUCH THANKS", "ENDLESS THANKS", "SO THANKFUL", 
    "THANK YOU KINDLY", "THANKS LOADS", "BIG APPRECIATION"
]


thank_you_replies = [
    "You're very welcome!",
    "No problem at all!",
    "Anytime! 😊",
    "Glad I could help!",
    "Happy to assist!",
    "No worries!",
    "You got it!",
    "Of course!",
    "Always here for you!",
    "Don't mention it!",
    "My pleasure!",
    "Much love! ❤️",
    "I'm here to help!",
    "It's nothing, really!",
    "That’s what I’m here for!",
    "No need to thank me!",
    "You're awesome too!",
    "Anything for you!",
    "Helping is what I do!",
    "You're the best!",
    "Anytime, anywhere!",
    "Keep being amazing!",
    "A pleasure, as always!",
    "Helping you makes me happy!",
    "You deserve it!",
    "It was my honor!",
    "Anything to make your day better!",
    "Sending positive vibes your way!",
    "Stay awesome!",
    "It was nothing!",
    "The pleasure is all mine!",
    "Just doing my part!",
    "Enjoy, my friend!",
    "No thanks needed!",
    "Right back at ya!",
    "Spread the kindness!",
    "You're worth it!",
    "Keep smiling! 😊",
    "Just spreading some good energy!",
    "Always happy to help!",
    "Your happiness is my reward!",
    "I'm just a message away!",
    "I appreciate YOU too!",
    "No biggie!",
    "All good, mate!",
    "Just keep shining!",
    "You're welcome, rockstar!",
    "Happiness shared is happiness doubled!",
    "It's a joy to help you!",
    "Smiles all around!"
]


def getQuote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return(quote)
    
@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content
    
    if message.content.startswith('$inspire'):
        quote = getQuote()
        await message.channel.send(quote)
        
    if any(word in msg for word in sad_words):
        await message.channel.send(random.choice(starter_encouragements))
        
    if any(word in msg for word in thank_you_words):
        await message.channel.send(random.choice(thank_you_replies))

# keep_alive()
client.run(os.getenv('TOKEN'))