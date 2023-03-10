# MINeD 2023 Hackathon
## Participating Institutes: Nirma University, SUNY Binghamton
## Track Sponsor: D360
## Team Name: BitBombers

## Live demo: https://drive.google.com/file/d/1ofzxIi4YLNEorX9MOlDN58v0iXYteCOZ/view?usp=sharing

### Problem Statement:
We have made a conversational AI chatbot using Google-assisted NLP engine named Dialogflow to process natural language queries pertaining to different types of diamonds and thereby generating filtering parameters to query out diamonds having these mentioned properties.

### What is Dialogflow?
Dialogflow is a Google assisted NLP engine that essentially works like a chatbot by processing user queries and generating necessary outputs. This processing of user queries is done with the help of Intents and Entities.
#### What is an Intent?

An intent specifies all sorts of variations in which a user might enter a query. Besides this specification, there are methods that run in the backend that map each characteristic variable to a particular identifier known as an Entity.
Below is an image depicting all the different intents that we have created which will process the query based on distinct properties of the diamonds.

![Intent](https://user-images.githubusercontent.com/75877929/222944347-14e3e18f-a453-4162-91b5-fb15d7d77bb8.png)

The intent named as *solve_query* is the intent which consists the user expressions having mixed attributes regarding the diamonds.

#### What is an Entity?
An entity can be regarded analogous to a python dictionary. A dictionary has a key and an associated value with it. Likewise, an entity has a reference variable and all possible synonyms that associate with that particular reference variable. So, whenever a user enters a query, the query has distinct characteristic values that essentially map to these entities and extract out the reference variable that they indicate. 

Below is an image depicting all the different entities that we have used to parse a unique value to its correct reference value.

![Entities](https://user-images.githubusercontent.com/75877929/222944433-9160f968-7130-4192-abb3-d38897eb5573.png)

#### How are Intents and Entities linked to training a Natural Language Processing (NLP) model?
Intents and entities are essentially parameters to an already pre-trained NLP model. When you add a user expression in a particular intent and specify what word maps to which entity, you are essentially passing a training data point to the NLP engine running in the backend. With every expression saved, the model trains itself with the incoming data point and makes prediction for future queries entered by the user. 

Hence, whenever the user would pass a query similar to the query on which the model trained,now the model would be able to identify different parameters present in it and make accurate prediction.

#### Our Approach
The problem statement required us to process as many as 21 different properties related to a diamond accurately. Based on the query entered by the user, the output generated by Dialogflow should be a set of different filtering parameters mentioned in the query and their respective values.

As accuracy was our chief concern, we planned on feeding the NLP engine with as many different user expressions as possible along with the correct entity that they map to. For this purpose, we firstly created all possible entities for the different diamond properties as mentioned in the below dataset file. 

[Dataset Attributes and Mapped Values](https://colab.research.google.com/drive/1LCqzDfJQMhy82R0yYPhWbq8_Szua8XTf?usp=sharing)

The dataset file mentions the characteristic of the diamond and what all possible values are assumed by the characteristic. The creation of custom entities was our first step because it is guaranteed from dataset attributes that every characteristic property has a well defined set of values which will always be matched to a unique element of that characteristic.

One thing to note here is that for the *color* attribute, value can be either entered as a single value or it can be entered as a range. For example, I can mention color as just R or I can mention color as E-U meaning the color can be in range from E to U. For this purpose, besides making an entity for the single color value, we also made a regex expression stating the manner in which the range can be entered. 

After the creation of entities, we made a parent intent by the name of *solve_query* which would inherit all possible variations in the query entered by the user. Every expression entered in this intent is mapped to the correct entity that it refers to. Once the model is correctly trained for that query, it will classify the query correctly for subsequent similar queries no matter the variations in the values present in the query. 

#### Customizing the response from chatbot
- Since our aim is to generate a filter for querying the diamonds, the filter must have exact values to search for in a database.
- Consider the example : "Give me diamond in H to K color range".
    - Here the NLP will process and extract the parameter as "H to K"
    - We need to devise a method which should give paramater as ['H', 'I', 'J', 'K']
- Another example is "Show me diamonds having around 3 ct"
    - Here the parameter extracted will be "approx 3 ct"
    - We format it with our API and give output "carat weight: [2.85, 3.15]"

![Chatbot 01](https://user-images.githubusercontent.com/75877929/222946228-c0ef6d7d-2de9-4325-9d45-77159a7d94a9.png)

- To have such conditional intelligence rendered accurately in our chatbot, we must either train a model in the respective way (which we cannot because it's in hands of Dialogflow) or implement a program.
- We enabled Webhook which is basically an event driven API calling service, so we made an API in Flask which would take these parameters and beautify them and give them back to the chatbot.
- So queries which are not discrete , are continuous and have range specified in the parameters, we need to format them and then give to the chatbot for good readability and future processing purposes.

#### Sample Input and Output Interpretation
Below attached is an image which shows a sample input user diamond query and the necessary response generated by the chatbot thereby having values as per their filtering parameters:

![Chatbot 03](https://user-images.githubusercontent.com/75877929/222946485-1e4c1e71-99e9-43b3-b36a-4f969b43e0a3.jpeg)

The sample user query shows the following input:
*show me round and O oval shaped diamond weighing 1.2-3ct, i-l HS ex fair good none 1.2-3mes1 4mes2 8.9mes3 12 price 2.3 ratio 12 table*

Carefully examining the query gives us with the following properties of the diamond:
- color
- polish type
- fluoroscence
- shape
- cut type
- weight in carats
- symmetry type
- mes1, mes2 and mes3
- price
- ratio
- table 

The chatbot responds with the correct filtering parameters and what values they intend in the query. 
