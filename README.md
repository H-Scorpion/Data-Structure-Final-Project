# Data-Structure-Final-Project
This project is about schools and students matching algorithm base on students' score and their choice of schools. We will implement the algorithm using different data structures and discuss the math behind them.  
## Generate Testing Data
Just run generateData.py, it will generate the school and student data in json format.
````
python generateData.py --schoolNum 5 --studentNum 20 --choiceNum 3 --output input_3.json
````
Default output file name is 'input_2.josn'
## main
run
````
python main.py --input input_3.json
````
It will take input_3.json as input to do the matching.