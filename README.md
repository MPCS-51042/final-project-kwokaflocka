# Recipe Book API

The goal of this web application is to create a backend API for a powerful recipe tracker that could be used by any avid cook. In addition to basic features, such as the ability to add or delete various recipies that are customary for such a tracker, this application also advances functionality to add notes, track nutrition information, fetch similar recipies, and return the simplest recipies given certain recipies.

The full list of functionalities include: 
1.	Fetching all the recipes
2.	Fetching a specific recipe
3.	Getting the nutritional information for a recipe
4.	Fetching recipes that abide by certain dietary restrictions 
5.	Fetching similar recipe to the one I have in mind
6.	Returning the simplest recipe available given an ingredient
7.	Adding new recipe
8.	Updating existing recipes
9.	Adding cooking notes to my recipes
10.	Deleting recipes
11.	Deleting cooking notes for specific recipes

For technical details, this project was built on FastAPI and leverages an object-oriented system based on a RecipeBook and Recipe objects. This allows the application to be very extensible for future features.The project uses the CalorieNinja's API to gather base nutritional information on food items: https://calorieninjas.com/api.

You can populate the initial database with my data from https://docs.google.com/spreadsheets/d/1Eb6jb7U4MfKtMcd6mUWBzg6taVfDT02F/edit?usp=sharing&ouid=103930868228310278871&rtpof=true&sd=true by puting the resulting file in my project directory. If you need to permanently store recipes, you should do so within the Google Sheet. Unfortunately, given the time constraint on the project, I was not able to integrate this with a database like MongoDB or write data into the sheet but perhaps you'll see that in version 2!
