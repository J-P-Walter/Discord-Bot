Creating my first Discord Bot

Using tutorial from StartupTechTutorial as a guide, this project is a quick refresher on some OOP for me, as well as introducing some new topics such as websockets, MVC architecture, using a database (mongo), and docker 

There are two branches: main and DockerBranch
Main has my completed bot, should be able to just run it from main.py and it should work. Can run lottery_drawer.py to get lottery numbers as well.
Plans for the future will be to revisit and add documentation/comments for the entire projet

DockerBranch is where I attempted to make the entire bot a container, ran into issues. First, I did not use a virtual environment (not sure why) so my requirements.txt is filled with many modules that are unrelated to the project. Even so, two of the docker containers threw and Exited (1) due to not having modules that were imported. I messed around with the Dockerfile for a bit, but could not find a solution. 
Plans might be to revisit and set up the virtual environment to see if that would fix it, or do another project focused on Docker to learn more about it

