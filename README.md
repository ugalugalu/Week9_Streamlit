**Problem Statement**
Fraud in telecommunications is a significant problem that costs the industry billions of dollars
annually. Fraudsters use various techniques to exploit telecom infrastructure weaknesses,
including hacking into phone systems, stealing identities, and exploiting vulnerabilities in billing
systems. The challenge for telecom companies is to detect and prevent fraud in real-time before
it causes significant financial damage.
This project seeks to create a real-time data visualization dashboard that monitors Reddit for
mentions of telecoms fraud and other related keywords, such as "telecoms scam", "phone
fraud", "billing fraud", and "identity theft". You will extract useful information from the posts, such
as the post text, user name, subreddit, and date/time, and use this information to analyze the
data for patterns and trends related to telecom fraud.

**Fraud Detection**
The algorithm employed is a simple search of the fraud keywords against the post title and body. If any keyword is matched, the post is 
added into a list that will be loaded as a dataframe for visualization in streamlit.

Below is a screen shot of dashboard deployed locally and when the same is deployed on google cloud!

[Uploading Screenshot 2023-05-14 at 16.09.47.png…]()

![image](https://github.com/ugalugalu/Week9_Streamlit/assets/54645939/9af6f658-bd07-495a-a9f8-a4c1c64e7022)

