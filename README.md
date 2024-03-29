# Ratio Bot

A bot created out of excess boredom and a desire to annoy everyone I know on Twitter.

---

## Ratio Bot's Purpose

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

I have a fully trained model for machine learning purposes ready to get, trained off of over 50,000 tweets collected  
from the people of Cogswell. However it requires significant personal moderation  for it to be:  

 (A) funny   
 (B) not insensitive   
 
so I've decided it is not worth my time in it's current state to move forward with.

The model oftentimes says some weird, not funny things that would make some uncomfortable, which is my biggest  
reason for not wanting to utilize this for now. I may implement the model in some limited fashion further down  
the line, but as it currently stands I'm keeping the model in my back pocket for later deployment.  

---

## Ratio Bot 1.2.11

  - Refactored code to be less redundant + more organized
  - Some new ratios added for more variety
  - On occassion ratiobot would ratio a harmless bystander. This should now be fixed.
  - Ratiobot began an endless ratio loop on himself until RNG decided to end it. This has now been fixed.
  - Staged an organizational change to prepare for the 1.3 update.

---

### Known Issues

--- 

  - Scheduler for tweets occasionally attempts double tweeting. at least it doesn't crash every time now, but it's annoying to see an error raised on occasion.
  - Not an issue inherently, but sentiment analysis hovers around 50% consistently.
    - This is to be expected, I'm tracking sentiment of all tweets over an extended period of time on literally every subject
    - Because of this, I plan on making the analysis a little more volatile, perhapss within a 45-55% range
    - More testing needs done on this before implementation

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

---

### Dependencies

---

Dependencies are listed in requirements.txt and are as follows:

  - nltk==3.7
  - requrests==2.27.1
  - schedule==1.1.0
  - tweepy==4.6.0