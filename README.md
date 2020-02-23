##  TITLE
 NEIGHBOURHOOD

## AUTHOR
 Built By Faith Gakori

## PROJECT DESCRIPTION
 An Application that enables users to view their neighbourhoods. User can update, create and view their hood.
    

## SCREENSHOTS
![Screenshot](images/s1.png)
![Screenshot](images/s2.png)
![Screenshot](images/s3.png)

## USER STORIES

* Sign in with the application to start using.
* Set up a profile about me and a general location      and my neighborhood name.
* Find a list of different businesses in my            neighborhood.
* Find Contact Information for the health department    and Police authorities near my neighborhood. 
* Create Posts that will be visible to everyone in      my neighborhood.
* Change My neighborhood when I decide to move out.
   Only view details of a single neighborhood.

## SetUp / Installation Requirements
  Clone the repo by running:
*   git clone https://github.com/Gakori/Hood.git

 Navigate to the project directory;
*   cd Hood

 Create a virtual environment and activate it
*   python3 -m venv virtual
*   source virtual/bin/activate

  Create a database
  using postgress, type the following commands;
*   $psql

Then run the command to create a new database
*   #create database gram

 Install dependencies
*   pip install -r requirements.txt

 Create database migrations
*   python3 manage.py makemigrations gram
*   python3 manage.py migrate

 Run the app
*   python3 manage.py runserver

## TECHNOLOGIES USED
* Django==2.1
* Python
* Bootstrap
* Html
* Css
* Postgres

## CONTACT INFORMATION
 For email reach us through faithgakori506@gmail.com

## LICENCE
MIT License

Copyright (c) 2020 Faith Gakori

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.