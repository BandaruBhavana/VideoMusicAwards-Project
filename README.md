
VMA’S VOTING WEBSITE – Kirk Cheataa-Laryea, Bhavana Bandaru

Application Login Credentials

With this web application there is the user login and the admin login, 
| Username             | Password | Role        |
|----------------------|----------|-------------|
| curt@gmail.com       | 12345    | Admin       |
| cheatak@clarkson.edu | 12345    | User/Viewer |
| bandarb@clarkson.edu | 12345    | Admin       |
| bhavana@clarkson.edu | 12345    | User/Viewer |


the user/viewer can only view and vote, the admin can add a nominee and delete a nominee(can also place a vote). 

Purpose

The VMA voting website is a platform where users can vote for their favorite music videos. The website allows users to register, login, and vote for their favorite videos in different categories such as Best Hip Hop, Best Pop, and Best Video of the Year. The website also displays the nominees in each category and allows users to view and vote.

Database and Class Description

This VMA voting web application imports modules such as Flask, render_template, request, session, redirect, url_for, escape, send_from_directory, and make_response. It also imports classes for the User, Student, Nominee, and Vote.
This web app creates a Flask application instance and sets the configuration for server-side sessions, including the secret key and session type. It also sets up a route for the home page, which displays the results of the votes and enables or disables voting based on whether a user is signed in or not, It also sets up a route for submitting votes, which gets the database connection, retrieves data from the request, and inserts the vote into the database.It sets up a route for the sign-in page, which handles both GET and POST requests. If the request method is GET, it renders the sign-in template, otherwise, it retrieves the email and password from the request, checks if the email and password match the database records, and if so, sets the session for the user and renders the home page template. Otherwise, it renders the sign-in template with an error message. It sets up a route for the admin page, which is only accessible to users with the admin role. It retrieves the results of the votes and nominee objects and handles POST requests for deleting or adding nominees to the database.
It also sets up a route for managing users, which can handle both GET and POST requests and can insert or update user data into the database.
In the baseobject.py file, there are three classes defined to represent each of these tables. The User class represents the users table, while the Video class represents the videos table. The Vote class represents the votes table. Each class contains attributes that map to the columns in the corresponding table.

Highlighted Custom SELECT Queries

In the nominee class, the getNomineeById function is a custom select query that fetches a single nominee from the database based on their ID. The getNominees function is another custom select query that fetches all nominees from the database. In the vote class, the getVotes function is a custom select query that fetches the number of votes each nominee has received from the database, also in the user class, the checkSignedIn function is a custom select query that fetches a single user from the database based on their email and password also the getUsers function is another custom select query that fetches all users from the database.

SQL Relational Schema

<img width="331" alt="Screenshot 2023-04-27 221748" src="https://user-images.githubusercontent.com/111446938/235038604-a0a62ba6-b095-414b-836e-19ef6c6912d6.png">


