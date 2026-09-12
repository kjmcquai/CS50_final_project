# Duck Migration Explorer

#### Video Demo: https://youtu.be/-RUnMvbjInA

#### Description:
Duck Migration Explorer is a Python-based educational program that allows users to explore the migration patterns of various duck
species native to North America. The basic functionality of the project is to enable users to input a duck species along with a
month and receive detailed information about whether the species migrates during that time, the typical migration months and routes
it follows, and the biological reasons driving these migrations. Additionally, the program generates a visual map that plots the migration route on a world map, providing a clearer understanding of these patterns.

The data for this project is stored in a CSV file, which contains the information about different duck species, including their
migration status, active migration months, migration routes, and reasons for migrating. This approach was chosen to simplify
updating and expanding the dataset without requiring changes to the code itself, making the program scalable and adaptable to new
information.

The blank map of the world is stored in a png file that can be called by my project program to allow it to plot the points of each specific duck species based on their migration routes.

The requirements.txt file contains the two libraries that need to be installed through the pip install method in order to allow users to easily identify and install them.

The test_project.py folder contains tests to verify that core functions like data loading, migration status checking, route formatting, and map generation behave as expected, increasing the program’s reliability and maintainability.

The user interface is designed to be flexible and user-friendly. It accepts species names with or without the word "duck" and allows
month inputs in full or abbreviated forms. The program validates the inputs, prompting users to re-enter if the data is not
recognized. This ensures that users can interact with the application smoothly and without confusion.

One of the features of the Duck Migration Explorer is its ability to generate a migration map image using the matplotlib and Pillow
libraries. The map overlays the species’ migration route on a world map background, plotting key stop locations as red dots
connected by a dashed line. This visual helps users better visualize the geographical scale and directionality of the migrations.

Throughout the development of this project, several important design decisions were made. Using a CSV file for data storage
maintains separation of data and logic, which is a best practice in software design. Input normalization for species and months
improves usability and accessibility. The choice to include a visual map provides an engaging and educational tool beyond simple
text output.

In summary, Duck Migration Explorer combines biological knowledge with programming skills to create a practical, user-friendly tool
that educates users about duck migration patterns. It showcases data handling, input validation, visualization, and testing which
are all important skills learned from this course!
