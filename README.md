# Data-Structure-Final-Project
## Exam Matching Algorithm 
This project is about schools and students matching algorithm based on students' score and their choices of schools. We will implement the algorithm using different data structures and discuss the math behind them.
## Matching Flow Chart
![iamge](https://github.com/H-Scorpion/Data-Structure-Final-Project/blob/main/images/flow%20chart.png)

## Implementation & Matching Result


## Different Data Structure
1. Min Heap: O(k\*n\*log(n))
2. Ordered List: O(k*n<sup>2</sup>)

## Project Structure
### ./dataStructure
The directory stores the data structures implemented in our project, including min heap and ordered list.  
We can choose to implement different data structure in line 9 in Student.py
### ./inputData
The directory stores the input data for matching. An example input data "input_1.json" is provided
### ./matchingPackage
This is the package for matching. It contians Student, School and Match three classes
### ./outputData
The directory stores the ouput data, which includes the matching result(in matchingResult) and runtime data(in runtimeData)
### main.py
Implement the matching algorithm
### generateData.py
Generate matching Data for matching
### calRuntime.py
Calculate matching runtime and record it in a file.
### plot.py
Plot the relationship between runtime and student number as well as data structures.  
The data for plotting is generated by calRuntime.py  
The module requires matplotlib.pyplot


---
## To Run Our Code

## main.py
This progam implements the matching algorithm.  
It takes input Data of the schools and the students and write the matching result in an output file

run 
````
python main.py --input input_1.json --output output_1.txt
````
It will take input_1.json in inputData as input to do the matching, then write the result in output_1.txt in the directory "outputData"

### input
file format: json  
location: ./inputData
```json
{
    "schoolList": ["school1","school2","school3","school4","school5"],
    "acceptQuota":[20, 50, 30, 40, 10],  
    "//": "school 1 accepts 20 students, and so on",  

    "schoolweighted":[
        [[3, 0, 2, 3, 3], [0, 1, 0, 0, 3], [2, 1, 1, 1, 0], [2, 2, 3, 3, 2], [0, 2, 3, 3, 0]], 
    ],
    "//schoolweighted":"weighting of each subject for schools, ranging from 0 to 3",  

    "overquota": [
        [2, 3, 4, 0, 1],  
        [0, 1, 2, 3, 4],  
        [0, 3, 4, 5, 1]],  
    "//":"school 1:超額比序先比科目2，再比科目3，依此類推",
    "//":"school 2:超額比序先比科目0，再比科目1，依此類推",  
      
    "studentList": ["1", "2", "3", "4", "5"],
    "//":"list for each student",  

    "score":[  
        [54, 67, 44, 56, 100],          
        [34, 28, 63, 25, 83],
        [83, 2, 11, 33, 47],
        [63, 44, 13, 7, 84],
        [89, 82, 34, 48, 28]],
    "//":"student 1 get 54 in subject 1, 67 in subject 2, and so on.",  

    "choice": [
        ["4", "2", "1", "3", "5"],  
        ["3", "4", "1", "5", "2"], 
        ["2", "1", "4", "5", "3"], 
        ["3", "1", "4", "2", "5"], 
        ["4", "1", "5", "3", "2"]],
    "//":"for student 1 school 4 is his/her first choice, followed by school 2, and so on."
}
```
PS:Length of school data should match, and so does student data  
Here we omit some of the data for simplicity
  


## Generate Testing Data
Just run generateData.py, it will generate the school and student data in json format.  
The location of generated data is in ./inputData
````
python generateData.py --schoolNum 8 --studentNum 20 --choiceNum 3 --output input_2.json --weighted 1
````
weighted: 1: weighted; 0: not weighted  
Default output file name is 'input_1.json'

## Calculate Runtime
run
````
python calRuntime.py
````
It will generate an output runtime data in outputData/runtimeData  
We can modify the output file name in line 5 in calRuntime.py 

## Plot
run
````
python plot.py
````
It will plot the  relationship between runtime and student number as well as data structures.  
The default data for plotting is runtimeHeap.txt and runtimeList.txt in ./outputData/runtimeData generated by calRuntime.py  
Note: This program requires matplotlib.pyplot

---
## Contributors
- b08901018 黃士賢 H-Scorpion 
- b08901069 黃政勛 YellowJason 
