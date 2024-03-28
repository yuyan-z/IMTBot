# University Bot
We have developed a chatbot which can be used in the university official website. 
This bot is capable of answering questions about basic university information, querying teacher public informations, and recommending suitable majors based on personal preferences.

# Data
The data comes from the official website of IMT Atlantique collected using a crawler.
- campus.csv : Information about the Brest, Nantes, Rennes campuses
- teacher_info.csv : Profile and contact detail of teachers
- major.csv : Information about majors offered by the university

# Functions
- Answer questions about basic information about the school, such as university overview, university history, university size, campus introduction.  
  ![photo6](https://github.com/yuyan-z/IMTBot/assets/64955334/459019ad-4e9a-4123-aa39-f1c93e9f81a7)
  
- Provide the teacher profile when a user asks for teacher information by memtioning the teacher name.  
  ![photo1](https://github.com/yuyan-z/IMTBot/assets/64955334/d86d7fca-3ed4-4804-9da5-3ce0b77075de)

- Recommends a major based on the interested domain and prefered campus of the user.  
  If the bot hasn't collected complete information for the domain or campus fields, it should prompt the user to provide the missing information until the form is completed.  
  User can use “stop” to quit the loop.  
  ![photo2](https://github.com/yuyan-z/IMTBot/assets/64955334/e2afc602-4813-4a5b-bdfd-de4300b33b06)
  ![photo3](https://github.com/yuyan-z/IMTBot/assets/64955334/be57c2f5-d6eb-4242-8f8b-15ed65925c8d)

- The user requests contact and leaves phone number or email.  
  If the bot hasn't collected at least one of these information, it prompts the user to provide either a phone number or an email address.  
  ![photo4](https://github.com/yuyan-z/IMTBot/assets/64955334/cd40dfb4-c3f3-4517-ac42-fdacb68776fb)
  ![photo5](https://github.com/yuyan-z/IMTBot/assets/64955334/8e7ac544-c312-4670-bb56-f926d3d4d2a0)

# Commands
`rasa train`: Train the model.  
`rasa run actions`: Start an action server  
`rasa shell`: Chat on the shell  
`rasa test nlu --nlu data/nlu.yml --config config.yml`: Evaluate the performance of the model, the results are save in ./results  

To chat on the web:  
`rasa run -m models --enable-api --cors "*"`  
`rasa run actions`  
Open index.html



  




  

