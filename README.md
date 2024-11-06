x# CS_474_System_Health_Monitoring_Dashboard

Description: 
The System Health Monitoring Dashboard is a web-based application designed to monitor and display critical system metrics, including CPU usage (user, sys, and idle), memory usage, and load average. The tool will gather real-time data from the host system and present it through an intuitive user interface (UI), providing users with insights into their system’s health and performance.

Technologies to learn: 
• Flask
• JavaScript
• Bash
• Twilio

Tech Stack: 
• Backend: Python with Flask to build the web dashboard.
• Frontend: JavaScript, HTML
• Scripting: Bash scripts for gathering system health data. 
• Database: MySQL for storing data.
• Version Control: Git for repository management. 

External API: 
I will use Flask, and Twilio as an external API to notify users when their system metrics cross defined thresholds. 


Functions: 
• Monitor CPU, memory, disk usage, and load average. 
• Display real-time metrics through a web UI.
• Display charts to show the 
• Send alerts via SMS when specified thresholds are exceeded. 


Implementation Process: 
1.	Run this command:  
for i in {1..20}; do top -l1 | head -n 5 >> top_output.txt; echo "----" >> top_output.txt; sleep 30; done
2.	Using bash, parse, extract the fields you want to use and add them to a text CSV file.
4.	Setup a MySQL database and create a table to store the values of the CSV.
5.	Setup a one-page webpage so you can first press a button and see the contents of the database. 
5.	Create a chart by querying the database and showing it on the webpage.

