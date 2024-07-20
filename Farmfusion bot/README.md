Agricultural Crop Chatbot

[Access the chatbot here] https://farmfusionai-9670.chipp.ai

   Overview

This project implements an NLP-powered chatbot specialized in agricultural crop information. The chatbot is trained on custom data and is capable of answering a wide range of queries about crops, including crop mixing, crop rotation, benefits, seasons, and places of growth.

   Features

- Answers queries about various crops
- Provides information on crop mixing and rotation
- Offers details on crop benefits, optimal growing seasons, and suitable locations
- Built using a low-code/no-code approach with Chipp.AI

   Data Sources

The chatbot's knowledge base is derived from two primary data files:

1. `crop_details.csv`: Contains general information about various crops
2. `crop_needs.csv`: Specifies the requirements and conditions for different crops

These files were merged into a single dataset, `mergedcsv.csv`, which forms the foundation of the chatbot's knowledge.

   Technology Stack

- NLP (Natural Language Processing) for understanding and processing user queries
- Chipp.AI: A low-code/no-code platform used for building and deploying the chatbot
- CSV data processing for creating the merged dataset

   Setup and Deployment

1. Data Preparation:
   - Merge `crop_details.csv` and `crop_needs.csv` into `mergedcsv.csv`
   - Ensure the merged file contains all necessary information without duplications

2. Chipp.AI Configuration:
   - Upload `mergedcsv.csv` to Chipp.AI platform
   - Configure the NLP model settings according to the data structure
   - Set up intents and entities based on the crop information

3. Chatbot Training:
   - Train the model using the Chipp.AI interface
   - Test and refine responses for accuracy

4. Deployment:
   - Deploy the chatbot using Chipp.AI's deployment options
   - Obtain the access link for users

   Usage

Users can interact with the chatbot by:
1. Accessing the provided link
2. Typing in questions related to crops
3. Receiving informative responses about crop details, mixing, rotation, benefits, seasons, and growth locations

Example queries:
- "What are the best conditions for growing wheat?"
- "Tell me best mixed crop suggestions for cotton?"
- "What are the benefits of crop rotation in Maize?"
- "Which crops grow well in Rabi season in Nanded, Maharashtra?"

   Maintenance and Updates

To keep the chatbot up-to-date:
1. Regularly update the source CSV files with new crop information
2. Re-merge the files and update the `mergedcsv.csv` in Chipp.AI
3. Retrain the model to incorporate new data
4. Test the chatbot with various queries to ensure accuracy

   Contributing

Contributions to improve the chatbot's knowledge base or functionality are welcome. Please submit pull requests or open issues for any enhancements.

   License

GPL 2.0
