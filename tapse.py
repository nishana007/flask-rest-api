# -*- coding: utf-8 -*-
"""
Created on Thu May 21 15:34:55 2020

@author: NAVEENA
"""


from flask import Flask,flash,render_template,request,jsonify
from flask_restful import Api,Resource

app=Flask(__name__)
app.secret_key = "super secret key"
api=Api(app)

Data=[{"emp_id":1,"name":"abeer","age":27},
      {"emp_id":2,"name":"mishti","age":24},
      {"emp_id":3,"name":"kunal","age":28},
      {"emp_id":4,"name":"kuhu","age":22},
      {"emp_id":5,"name":"nidhi","age":37},
      {"emp_id":6,"name":"ketki","age":22}
      ]


class Employee(Resource):
    

    def get(self):
        return jsonify({'records':Data})
            
             
    def post(self):
        
      try:
         record={}
         req=request.get_json()
         record['emp_id']=req['emp_id']
         record['name']=req['name']
         record['age']=req['age']
         Data.append(record)

         return {"msg":"Data was succesfully added"}
     
      except:
         return {"msg":"There was an issue adding your data"},200
       
       
        
        

class EmployeeById(Resource):
    
     def get(self,empid):
        
        for x in Data:
            for key,value in x.items():
                if value == int(empid):
                     return jsonify({'records':x})
                    
        else:
             return {"msg":"No record was found!"}
        
        
     
     def put(self,empid):
        
      try:
         for x in Data:
            for key,value in x.items():
                if value == int(empid):
                     req=request.get_json()
                     x['emp_id']=req['emp_id']
                     x['name']=req['name']
                     x['age']=req['age']
                     Data.append(x)
                     return {"msg":"Data was succesfully updated"}
                 
        else:
               return {"msg":"No matching record was found!"}
      except:
          
            return {"msg":"There was a problem updating that record"},200
        
        
        
        
     def delete(self,empid):
        
        try:
            for x in Data:
              for key,value in x.items():
                if value == int(empid):
                    Data.remove(x)
                    return {"msg":"Data was succesfully deleted"}
            else:
                 return {"msg":"No matching record was found!"}
             
        except:
            return {"msg":"There was a problem deleting that record"},200
           
        
        

api.add_resource(Employee,"/records")
api.add_resource(EmployeeById,"/records/<string:empid>")

if __name__== '__main__':
    
    app.run(debug=True)
    