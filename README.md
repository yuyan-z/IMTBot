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
  ![photo6](https://github.com/yuyan-z/IMTBot/assets/64955334/d53cc51f-6a8a-4d6b-9e67-0c8de094224b)

- Provide the teacher profile when a user asks for teacher information by memtioning the teacher name.  
  ![photo1](https://github.com/yuyan-z/IMTBot/assets/64955334/c44fe6de-de7f-4f9f-8ee0-68f46259fae1)


- Recommends a major based on the interested domain and prefered campus of the user.  
  If the bot hasn't collected complete information for the domain or campus fields, it should prompt the user to provide the missing information until the form is completed.  
  User can use “stop” to quit the loop.  
  ![photo2](https://github.com/yuyan-z/IMTBot/assets/64955334/ea0251fc-0b6a-4247-9390-c17ac5a2d54f)

  ![photo3](https://github.com/yuyan-z/IMTBot/assets/64955334/900a8d43-985e-44fc-8daf-388c380ab5c6)


- The user requests contact and leaves phone number or email.  
  If the bot hasn't collected at least one of these information, it prompts the user to provide either a phone number or an email address.  
  ![photo4](https://github.com/yuyan-z/IMTBot/assets/64955334/5977a42e-5aa2-4600-8a1c-1a8903cf7155)
  
  ![photo5](https://github.com/yuyan-z/IMTBot/assets/64955334/e4346d9d-9d42-401e-8ec5-db7d6158ade2)


# Commands
`rasa train`: Train the model.  
`rasa run actions`: Start an action server  
`rasa shell`: Chat on the shell  
`rasa test nlu --nlu data/nlu.yml --config config.yml`: Evaluate the performance of the model, the results are save in ./results  

To chat on the web:  
`rasa run -m models --enable-api --cors "*"`  
`rasa run actions`  
Open index.html



  




  

