# OntoChat Extension

This project is an extension of [OntoChat](https://github.com/King-s-Knowledge-Graph-Lab/OntoChat). For more information about OntoChat, please refer to the official GitHub repository.

## About this Extension

This extension adds a new feature, enabling the creation of drafts of ontologies based on a series of competency questions.

## Prerequisites

Before running this project, make sure you have the following tools installed/available:
- [Anaconda](https://www.anaconda.com/products/distribution)
- [Python](https://www.python.org/downloads/)
- You will need an OpenAI API key, which you can obtain by signing up at the [OpenAI website](https://platform.openai.com/signup). 

## Installation Instructions

Follow these steps to set up and run the project:

1. **Download and Install Anaconda**  
   Download Anaconda from [here](https://www.anaconda.com/products/distribution) and follow the installation instructions for your operating system.

2. **Create and Activate a Conda Environment**  
   Open anaconda command prompt and run the following commands:
   ```bash
   conda create --name ontochat-env python=3.9
   conda activate ontochat-env

3. **Install Dependencies**  
   Once the environment is activated, install `pip`:
   
   ```bash
   conda install p
   pip install -r absolute_path_to\requirements.txt

4. **Run Application**
   Open anaconda command prompt, ensure that the newly create conda env is active. You have to put teh absolute path to the python interpreter in your conda env AND the absolute path of app.py:
   
   ```bash
   (ontochat-env) C:\Users\edoar\anaconda\envs\ontochat-env\python "C:\Users\edoar\OneDrive\Desktop\Ontochat\app.py"
   
5. **Web Activation**
   After running the application, you should see a URL displayed in the terminal. Copy and paste the URL into any web browser.
   ```bash
   Running on local URL:  http://127.0.0.1:7860

## Running OntoChat
Remember to substitute your OpenAI API key and the absolute path of the directory of ontochat on your local machine in the *drafting.py* file.
Now you are able to use the OntoChat tool with the new ontology draft creation feature. For any question feel free to contact me on edoardo.saturno@studio.unibo.it



