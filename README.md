# Ratio Bot

---
A bot created out of excess boredom and a desire to annoy everyone I know on Twitter.

---

## Ratio Bot's Purpose
---
Ratio Bot was created with one primary goal in mind:
  - Automatically ratio a specific person on twitter

As a side effect of this goal, it's also been a fun project to encourage me to learn more about python.  
This project has been a great motivator in learning new things as someone with no direction for programming.

As this is my only project that's seen any sort of deployment, I've intended to keep the code as readable  
and easy to maintain as possible. Whether I've achieved this is certainly debatle, but I attempted to comment  
nearly every section of my code, even where it seems redundant, so I can return after prolonged breaks, getting  
right back on track. (which I have done three times now!)  

With that aside, I've made the decision to release full source code of this bot to practice maintaining a repo  
through git (spoilers: im really bad at this). I have a lot of planned tweaks and fixes coming in the next few  
weeks as well as a collection of new ratios to vary the 'experience' a little more.

---

### Machine Learning?

---

I have a fully trained model for machine learning purposes. However it requires significant personal moderation  
for it to be: (A) funny, and (B) not insensitive (more on that later) so I've decided it is not worth my time  

The model oftentimes says some weird, not funny things that would make some uncomfortable, which is my biggest  
reason for not wanting to utilize this for now. I may implement the model in some limited fashion further down  
the line, but as it currently stands I'm keeping the model in nmy back pocket for later deployment.  

---

## Ratio Bot 1.2.7

---

  - Restructured code for better future proofing
  - Fixed error with tweet writter for SIA purposes
  - Adjusted verbage in backend for personal clarification
  - Cleaned up weather module to be less annoying
    - Cheesy and over the top custom messages are gone
    - Real feel replaced with conditions (who even pays attention to that metric anyway)
    - Short and sweet flavor text dependant on condition implemented instead
  - Sentiment analysis module flavor text adjusted
    - Much more 'socially aware' comment in place of what were essentially insults before
    - "Happiness Percentage" replaced with a common one-word emotional state (neutral, sad, happy)
    - Makes the bot feel more personal and less "in your face"
  - Implemented structure for upcoming feature(s)
  - Connection log to monitor bot downtime
  - Tweets collected are now timestamped for 'book keeping' purposes
  - Sentiment grades are now stored for potential longer peroid averages
  - Ratio Bot now only ratios a percentage of the time rather than 100%

---

### Known Issues

--- 

  - scheduler for both modules frequently attempts duplicate tweet, crashing it's operating thread
  - Tweet writer fails when emoji are used. Switching encoding to UTF-8 works until SIA where it then breaks

---

### Upcoming Features

---

  - Palette Creation
    - Use K-means to generate a color palette based on previous 4 uploaded images
  - More ratios to create more variance
  - @ratiobot remindme (x) (y)
    - pings a user after a specified period of time
 
More features planned as my brain continues to create a weird desire to overload my bot with useless features.  
These are planned to release by mid-November. A stretch featureset will be released later by the end of the Year.
