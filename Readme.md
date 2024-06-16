1st Step - Pintharu-Homes-Backend-Python\ inside this directory Type on terminal to create virtual environment
            
		py -m venv venv   

2nd Step  - After that you go venv/Scripts and type

       		 .\activate     

3rd Step - Back to Pintharu-Homes-Backend-Python\  and type on terminal

		py -m pip install Django
		pip install opencv-python
		pip install matplotlib




4th Step - "Cd Pintharu_Homes" inside this directory and type

		py manage.py runserver 

PostMan Endpoint -  Use PUT Method and "http://127.0.0.1:8000/changecolor/" URL

json file format - {"color":"[212, 40, 155]","image":"Use Base64  encode value of your image"}