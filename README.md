# Data-Structure-Final-Project
## Exam Matching Algorithm 
This project is about schools and students matching algorithm based on students' score and their choices of schools. We will implement the algorithm using different data structures and discuss the math behind them.
## To run our code
---
## main.py
This progam implements the matching algorithm.  
It takes input Data of the schools and the students and write the matching result in an output file
### input
file format: json  
location: ./inputData
```json
{
    "schoolList": ["school1","school2","school3","school4""school5"],
    "acceptQuota":[school1quota,school2quota], // int
    "schoolweighted":[
        [subj1,subj2,subj3,subj4,subj5],  
        //weighting of each subject for school1
        [subj1,subj2,subj3,subj4,subj5]  
        //weighting of each subject for school2
    ],
    "overquota": [
        [2, 3, 4, 0, 1],  
        //超額比序先比科目2，再比科目3，依此類推
        [0, 1, 2, 3, 4],  
        //超額比序先比科目0，再比科目1，依此類推 
        [0, 3, 4, 5, 1]],  
        //超額比序先比科目0，再比科目3，依此類推 
    "studentList": ["1", "2", "3", "4", "5"], //list for each student
    "score":[  
        [54, 67, 44, 56, 100],  
        //student 1 get 54 in subject 1, 67 in subject 2, and so on.
        [34, 28, 63, 25, 83],
        [83, 2, 11, 33, 47],
        [63, 44, 13, 7, 84],
        [89, 82, 34, 48, 28]],
    "choice": [
        ["4", "2", "1", "3", "5"],  
        //for student 1 school 4 is his/her first choice, followed by school 2, and so on.
        ["3", "4", "1", "5", "2"], 
        ["2", "1", "4", "5", "3"], 
        ["3", "1", "4", "2", "5"], 
        ["4", "1", "5", "3", "2"]]}
}
```  
To run run
````
python main.py --input input_1.json --output output_1.txt
````
It will take input_1.json in inputData as input to do the matching, then write the result in output_1.txt in the directory "outputData"

## Generate Testing Data
Just run generateData.py, it will generate the school and student data in json format.
````
python generateData.py --schoolNum 5 --studentNum 20 --choiceNum 3 --output input_1.json
````
Default output file name is 'input_1.json'


---
## Contributors
- b08901018 黃士賢 H-Scorpion 
- b08901069 黃政勛 YellowJason 