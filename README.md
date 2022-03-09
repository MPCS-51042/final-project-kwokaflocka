------------------------------------------------------------------------------------

The goal of this web application is to create a backend API for a powerful recipe tracker that could be used by any avid cook. In addition to basic features, such as the ability to add or delete various recipies that are customary for such a tracker, this application also advances functionality to add notes, track nutrition information, fetch similar recipies, and return the simplest recipies given certain recipies.

For technical details, this project was built on FastAPI and leverages an object-oriented system based on a RecipeBook and Recipe objects. This allows the application to be very extensible for future features.The project uses the CalorieNinja's API to gather base nutritional information on food items: https://calorieninjas.com/api.

You can populate the initial database with my data from https://docs.google.com/spreadsheets/d/1Eb6jb7U4MfKtMcd6mUWBzg6taVfDT02F/edit?usp=sharing&ouid=103930868228310278871&rtpof=true&sd=true and put the resulting file in my project directory. If you need to permanently store recipes, you should do so within the Google Sheet. Unfortunately, given the time constraint on the project, I was not able to integrate this with a database like MongoDB or write data into the sheet but perhaps you'll see that in version 2!


# Proposals

My ideas for my final project are...

Week 4 – Create a basic web app with a (Recipe +) button that opens a form to create the recipe and some input validation – Some UI design and learn how to incorporate Food Nutrition API (https://esha.com/products/nutrition-database-api/) or (https://developer.edamam.com/food-database-api-docs) or (https://www.calorieking.com/us/en/developers/food-api/)
 
Week 5 – Flesh out Recipe Book object to hold Recipe objects and flesh out a Recipe object and figure out all the functionality you’d want accessible to the Recipe object + implement
 
Recipe Book object:
1. 	Add new Recipe objects
2. 	Delete Recipe objects
3. 	Display all recipes
 
Recipe object:
1. 	Add line to recipe
2. 	Support unit conversion
3. 	Serving size
4. 	Return total calorie count
5. 	Return a fraction of the calorie count
6. 	Allow editing to each individual line (name or calorie count)
 
Week 6 – Finish some more functionality from Week 5, make ability to create user profiles and authentication + sharing/exporting capabilities
 
Week 7 - Figure out ideal database to store the recipes given (MongoDB for sheets?) and add functionality to RecipeBook object to read and populate from Mongo
 
Week 8 – Host on Heroku? AWS? + continue/finish MongoDB

