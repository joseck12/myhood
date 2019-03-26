# MyHood
#### A web application that allows you to be in the loop about everything happening in your neighborhood.
#### By Joseck Ogachi
## Description
This application allows its users to do the following

- Sign in with the application to start using.
- Set up a profile,location and neighbourhood name.
- Find a list of different businesses in my neighbourhood.
- Create Posts that will be visible to members in my neighborhood.
- Change My neighbourhood when I decide to move out to a new one.
## Setup and Installation Requirements
# Installations required
- python version 3.6
-Django version 1.11.5 `pip install django==1.11.5`
- Additionally, you’ll need to make sure you have pip available. You can check this by running:
- `pip --Version`
- Install Pipenv `pip install --user pipenv`
- install virtual env
- `python3.6 -m venv --without-pip virtual`
- `source virtual/bin/activate`
- `curl https://bootstrap.pypa.io/get-pip.py | python`

Inorder to clone , follow the procedure below;
- On GitHub, navigate to the main page of the repository.
- Under the repository name, click Clone or download.
- click the paste button.
- Open Terminal.
- Change the current working directory to your desired location.
- Type git clone, and then paste the URL you copied in Step 2.
- git clone` https://github.com/joseck12/myhood.git`
`Press Enter`.

#install dependancies
- install dependancies that will create an environment for the app to run
`pip3 install -r requirements.txt`
#creating a database
- `psql`
- `CREATE DATABASE hood;`
- connect to the database `\c hoodpro;`
- check if tables have been created `\dt`

#Run migrations
- `python3.6 manage.py migrate`
- `python3.6 manage.py makemigrations hood`

#Running the app
- `python3.6 manage.py runserver`
- Open terminal on ` localhost:8000`

#testing
- `python3.6 manage.py test `

#SPECIFICATIONS
| Behaviour | Input | Output |

| Display Posts| *On the Home Page*| User can view different Posts|
| Posts expand | * On the Home Page*| User can click on an Posts to view more details|
| As An Admin Sign in| * On The Admin Dashboard*| Post Posts,and Businesses|
| As A User   | *On Profile Page| Edit Profile Page|

## Technologies Used
- HTML
- CSS
- Python
- Django
- Postgres
- javascript
- Heroku

## Support and contact details
- jogachi4@gmail.com
- 0726825457

# Known Bugs
- There are no known bugs incase of any reach me on the contact details above.

### License
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE
Copyright (c) {2019} **{By Joseck Ogachi}**

##live link to Heruko
