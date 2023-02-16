import pickle
import numpy as np
from flask import Flask, render_template, request,jsonify
from flask_cors import cross_origin
from structureData import structureData
import json
app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
@cross_origin()
def home():
    sendData = request.data
    if request.data:
      res = structureData(sendData)
      print(res)
      dtree_model = pickle.load(open('dtree.pkl', 'rb'))
      rf_model = pickle.load(open('rf.pkl','rb'))
      xgb_model  = pickle.load(open('xgb.pkl','rb'))
      dtree_res  = dtree_model.predict(np.array([res]))
      rf_res = rf_model.predict(np.array([res]))
      xgb_res = xgb_model.predict(np.array([res]))
      f = open('labels2.json')
      labels = dict(json.load(f))
      print(dtree_res[0])
      print(list(labels.keys())[xgb_res[0]])
      print(rf_res[0])
      suggestedJobRoles = {
        1:dtree_res[0],
        2:list(labels.keys())[xgb_res[0]],
        3:rf_res[0]
      }
      return json.dumps(suggestedJobRoles)
    else:
      return "Welcome to api"



if __name__ == "__main__":
  app.run(debug=False,host='0.0.0.0')