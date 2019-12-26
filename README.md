# AlexaInterview
This project was created alongside with Nabid Farvez, Vincent Huynh, and Jolin Tran

# Inspiration
As rising 2nd year students, we know the grind to find those first summer internships. What better way than to have Alexa act as a helping hand that provides tips on stuttering, recommendations to coding challenges to relevant topics (@leetcode), and additional options for relevant jobs.

# What it does
Right as you're about to pick up the phone to answer for your phone interview, you trigger the Alexa skill, "Hey Alexa, it's interview time." Alexa proceeds to listen to your end of the interview, recording and parsing your speech to text, and conducting some natural language processing on it. Some of that processing includes checking for sentiments (making sure you're speaking positively and avoiding those negative or self-deprecating phrasing), counting "filler" words like "um", and listening for topics that were involved (i.e. linked lists) to suggest practice challenges specific to those mentioned to make sure you get them the second time around. The hope was to have visual analytics from each interview so you could track your progress with time (i.e. less filler words or more positive sentiment).

# How we built it
Well, we were working on it. It's in the development phase still. Ultimately, we were going to use Alexa and AWS services to activate the trigger, using google-speech-to-text API to parse the audio, then using google-natural-language-processing API to conduct analysis of the text. From there, we can use labels to web scrape the internet for similar internships/jobs to return to you but also scrape the web such as for coding challenges or additional learning resources that relate to topics mentioned during your interview.

# Challenges we ran into
We had some trouble setting up the authentication for the various APIs. We also couldn't find a dataset of interview transcripts to feed to the NLP's training models as well as setting up Alexa. Ok, we had a lot of trouble. But the idea's there.

# Accomplishments that we're proud of
We sort of understand how API's work with authentication tokens, having never used them. We are proud of the conception of the idea and where we could possibly lead it in the future when we #gitgud

# What we learned
Skills learned: how to web scrape, use various API's with authentication tokens, working collaboratively in teams using git.

# What's next for Hey Alexa, Interview Time
Perhaps in the future, when we've gotten #gud, we'll tackle the issue again and make it fully functional.
