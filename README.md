# MINeD 2023 Hackathon
## Participating Institutes: Nirma University, SUNY Binghamton
## Track Sponsor: D360
## Team Name: BitBombers

### Problem Statement:
We have made a conversational AI chatbot using Google-assisted NLP engine named Dialogflow to process natural language queries pertaining to different types of diamonds and thereby generating filtering parameters to segregate different diamond properties.

### What is Dialogflow?
Dialogflow is a Google assisted NLP engine that essentially works like a chatbot by processing user queries and generating necessary outputs. This processing of user queries is done with the help of Intents and Entities.
#### What is an Intent?
An intent specifies all sorts of variations in which a user might enter a query. Besides this specification, there are methods that run in the backend that map each characteristic variable to a particular identifier known as an Entity.
#### What is an Entity?
An entity can be regarded analogous to a python dictionary. A dictionary has a key and an associated value with it. Likewise, an entity has a reference variable and all possible synonyms that associate with that particular reference variable. So, whenever a user enters a query, the query has distinct characteristic values that essentially map to these entities and extract out the reference variable that they indicate. 

#### How are Intents and Entities linked to training a Natural Language Processing (NLP) model?
Intents and entities are essentially parameters to an already pre-trained NLP model. When you add a user expression in a particular intent and specify what word maps to which entity, you are essentially passing a training data point to the NLP engine running in the backend. With every expression saved, the model trains itself with the incoming data point and makes prediction for future queries entered by the user. Hence, whenever the user would pass a query similar to the query on which the model trained,now the model would be able to identify different parameters present in it and make accurate prediction.
