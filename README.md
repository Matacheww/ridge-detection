# Automating Ridge Detection

This project is an extension of my MSci Physics research project - 'Mapping Polygonal Ridges Across the Martian Mid-Latitudes' - in which I analysed user-generated data from Zooniverse.org to determine locations of ridge formations on Mars.  This project will build upon the analysis I conducted to create a machine-learning approach to detecting these ridge formations.

### Context
#### Zooniverse.org

Zooniverse is a citizen science website, allowing users to participate in active research projects. Projects commonly provide brief training to familiarise the users in simple tasks they are given to complete. 'Planet Four: Ridges' was a project created on Zooniverse by the Planet Four team, a group of planetary scientists from various academic institutions and labs including NASA's Jet Propulsion Laboratory (JPL). This project asked users to classify images of the Martain landscape by the types of ridges present. The response options were:

- None of the Above Ridge Types Are Present in the Image
- Polygonal Ridges
- Meridiani-type Ridges

Users' responses were then stored and later analysed by myself for my fourth year MSci project. The user data I worked with was from the second iteration of the 'Planet Four: Ridges' project.

### Goal of this project

The aim of this project is to use Fourier Transforms of ridge images to identify common features. These features can then be used for automated detection of ridges.

### Method

User-generated data has been aquired previously, including a full list of subject image IDs for the images stored on Zooniverse. Therefore, we start analysis by:
- Scrape Zooniverse to retrieve image (webscraper.ipynb)
- Perform Fourier Transform of the image and store the result in DB (transform_images.ipynb)

These steps are completed using each Image ID.

*Further steps to continue analysis to follow*