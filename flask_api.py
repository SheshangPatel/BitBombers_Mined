from flask import Flask, request
import flask_cors
import re

app = Flask(__name__)


# @app.route("/webhookcallback", methods = ["POST"])
@app.route("/", methods = ["POST"])
@flask_cors.cross_origin()
def hook():
    print(request.data)

    req = request.get_json(silent=True, force=True)
    result = req.get("queryResult")
    parameters = result.get("parameters")
    print(type(parameters))


    print("Query:::: ", result.get('queryText'))

    for k, v in parameters.items():
        print(k,':', v)

    #bhulna mat color range ko set dalna
    if len(parameters['color_value_range']) > 0:
        tem_colors = parameters['color_value']
        

        for sTem in parameters['color_value_range']:
            tem_colors = color_range_extraction(sTem, tem_colors)

        parameters['color_value'] = tem_colors



    if len(parameters['carat_weight']) > 0:
        tem_cat = []
        for x in parameters['carat_weight']:
            tem_cat.append(func(str(x)))

        parameters['carat_weight'] = tem_cat
    

    if len(parameters['mes1_value']) > 0:
        tem_cat = []
        for x in parameters['mes1_value']:
            tem_cat.append(func(str(x)))

        # tem_cat = func(parameters['mes1_value'])
        parameters['mes1_value'] = tem_cat


    if len(parameters['mes2_value']) > 0:

        tem_cat = []
        for x in parameters['mes2_value']:
            tem_cat.append(func(str(x)))

       
        parameters['mes2_value'] = tem_cat

    if len(parameters['mes3_value']) > 0:
        tem_cat = []
        for x in parameters['mes3_value']:
            tem_cat.append(func(str(x)))

        parameters['mes3_value'] = tem_cat

    if len(parameters['table_value']) > 0:
        tem_cat = []
        for x in parameters['table_value']:
            tem_cat.append(func(str(x)))

        parameters['table_value'] = tem_cat


    if len(parameters['price_cts_value']) > 0:
        tem_cat = []
        for x in parameters['price_cts_value']:
            tem_cat.append(func(str(x)))

        parameters['price_cts_value'] = tem_cat

    if len(parameters['ratio_value']) > 0:
        tem_cat = []
        for x in parameters['ratio_value']:
            tem_cat.append(func(str(x)))


        parameters['ratio_value'] = tem_cat

    if len(parameters['total_value']) > 0:
        
        tem_cat = []
        for x in parameters['total_value']:
            tem_cat.append(func(str(x)))


        parameters['total_value'] = tem_cat
    
    temans = {
       
        "fulfillmentText": " PARAMETER FILTER :" +"  \n" + display_it(parameters) + "  \n"
    }


    return temans


def display_it(parameters):
    
    ans = ""
    for k, v in parameters.items():
        if k != 'color_value_range' and len(v) >= 1:
            # print(f"{k}".ljust(50))
            ans = ans + f"{k}: {v}" + "  \n"

    print("display string:\n", ans)
    return ans

def color_range_extraction(s, t):
    s = s.upper()
    s = s.rstrip()
    s = s.lstrip()
    ansList = t
    if "TO" in s:
        print("To found!")
        tem_list = []

        if "COLOUR" in s :
            tem_list = s.split("COLOUR")

        if "COLOR" in s:
            tem_list = s.split("COLOR")

        # print(tem_list)
        s = tem_list[0]

        tem_list = s.split('TO')
        # print(tem_list)

        for i in range(len(tem_list)):
            tem_list[i] = tem_list[i].lstrip()
            tem_list[i] = tem_list[i].rstrip()

        
        # ansList = []

        for i in range( max(65 , ord(tem_list[0])), min(91 , ord(tem_list[1])+1)):
            # print(i, type(i))
            ansList.append(str(chr(i)))

        # ansList.extend(t)

        ansList = list(set(ansList))

        ansList.sort()
        
        # print(ansList)
        # print(tem_list)

    elif "-" in s:  
        
        for i in range( max(65 , ord(s[0])), min(91 , ord(s[2])+1)):
            # print(i, type(i))
            ansList.append(str(chr(i)))
        



        ansList = list(set(ansList))

        
    
        # print(ansList)

    else :
        ansList.append(s)
        
    ansList.sort()

    # print(ansList)
    return ansList



def func(sentence):
    sentence.lower()
    
    s = sentence

    if('mes1' in sentence): s = sentence.split('mes1')[0]
    if('mes2' in sentence): s = sentence.split('mes2')[0]
    if('mes3' in sentence): s = sentence.split('mes3')[0]

    sentence = s
    # s = sentence
    s = [abs(float(s)) for s in re.findall(r'-?\d+\.?\d*', sentence)]
    if "approx" in sentence or "around" in sentence or "about" in sentence or "approximate" in sentence or "approximately" in sentence :
        ans=[s[0]-0.15,s[len(s)-1]+0.15]
    else:
        ans=s

    print(ans)
    return ans


if __name__ == "__main__":
    app.run()