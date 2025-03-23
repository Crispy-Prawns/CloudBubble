# CloudBubble
---
##CloudBubble is an educational resource platform where individuals can select and filter their preferred media of learning source and the difficulty level they want to learn from. This allows someone with no knowledge to catch up quickly to their peers, or for more underprivelaged students - they can see what the rest of the world are using to imporove their intellect.
---
(after this point, I used chatgpt to help write about the README file because i have no idea what a readme file is)
---
###Features:

1. Filter resources by subject, media and difficulty level

2. 'Chocolate Box of Surprises' - a url below to click so a random fact pops up from a list

3. Every resource is accompanied by their respective link to take you to the resource immediately

---
###Requirements:

1. Python 3.7 or higher must be installed

2. Libraries:
-Streamlit
-Pandas
You can install the necessary libraries using 
-pip install streamlit pandas

3. CSV file - make sure book2.csv is in the same directory as CloudBubble.py

4. Image - make sure Untitled96.png is in the media folder
---
How to run app:
1. Clone this repository
2. Navigate to the folder containing the app script in the terminal and run the following command in the bash:

streamlit run CloudBubble.py

This will open the app in your browser
---
Sidebar Filters:
- Topic: allows you to filter which subject you want
- Type: allows you to filter by the media you want
- Difficulty level: a slider to filter the difficulty level of the subject

Main Content:
-Displays filtered resources with:
--Name of site or video
--Difficulty level
--Topic, media type and link of resource
--logo of resource

Surprise fun_fact:
--clickable url that takes you to an external url that contains academic based facts
---
Troubleshooting
--Ensure all libraries are properly installed, and you are using a Python 3.7 version or better


