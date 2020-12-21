class Module:
    def __init__(self,name,code,students,weights):
        self.name=name 
        self.code=code
        self.students=students
        self.weights=weights #number of assessments is the same as length on the weights
    
    def average_score_all(self): 
        sum_of_scores=0                                        
        for student in self.students:                         
            for score in student.scores:                          
                sum_of_scores=+score
        return sum_of_scores/len(self.weights)/len(self.students)        


    def average_score_spec(self,asses): 
        sum_of_scores=0                                  
        for student in self.students:
            sum_of_scores=+student.scores[asses-1]
        return sum_of_scores/len(self.students)


    def performance_for_all(self,sort_method):
        to_sort=self.students
        if sort_method=="alphabetically first name":
            for i in range(len(to_sort)-1):
                for k in range(len(to_sort)-i-1):
                    if to_sort[k].first>to_sort[k+1].first:
                        tmp=to_sort[k]
                        to_sort[k]=to_sort[k+1]
                        to_sort[k+1]=tmp
        if sort_method=="alphabetically last name":
            for i in range(len(to_sort)-1):
                for k in range(len(to_sort)-i-1):
                    if to_sort[k].last>to_sort[k+1].last:
                        tmp=to_sort[k]
                        to_sort[k]=to_sort[k+1]
                        to_sort[k+1]=tmp
        if sort_method=="by score":
            for i in range(len(to_sort)-1):
                for k in range(len(to_sort)-i-1):
                        if to_sort[k].performance()>to_sort[k+1].performance():
                            tmp=to_sort[k]
                            to_sort[k]=to_sort[k+1]
                            to_sort[k+1]=tmp
        
        return to_sort

    def total_score_all(self, sort_method):
        to_sort=self.students
        if sort_method=="first name":
            for i in range(len(to_sort)-1):
                for k in range(len(to_sort)-i-1):
                    if to_sort[k].first>to_sort[k+1].first:
                        tmp=to_sort[k]
                        to_sort[k]=to_sort[k+1]
                        to_sort[k+1]=tmp
        if sort_method=="last name":
            for i in range(len(to_sort)-1):
                for k in range(len(to_sort)-i-1):
                    if to_sort[k].last>to_sort[k+1].last:
                        tmp=to_sort[k]
                        to_sort[k]=to_sort[k+1]
                        to_sort[k+1]=tmp
        if sort_method=="score":
            for i in range(len(to_sort)-1):
                for k in range(len(to_sort)-i-1):
                        if to_sort[k].total()>to_sort[k+1].total():
                            tmp=to_sort[k]
                            to_sort[k]=to_sort[k+1]
                            to_sort[k+1]=tmp
        return to_sort
    
    def max_min(self,asses): #?
        pos_1=0
        pos_2=0
        maxn=self.students[0].scores[asses-1]
        for i in range(len(self.students)):
            if self.students[i].scores[asses-1]>maxn:
                maxn=self.students[i].scores[asses-1]
                pos_1=i
        max_stu=self.students[pos_1]
        minn=self.students[0].scores[asses-1]
        for j in range (len(self.students)):
            if self.students[i].scores[asses-1]<minn :
                minn=self.students[j].scores[asses-1]
                pos_2=j
        min_stu=self.students[pos_2]
        return max_stu,min_stu

class Student:

    def __init__(self,first,last,id_n,scores):
        self.first=first
        self.last=last
        self.id=id_n
        self.scores=scores
        self.n_modules=n_modules
    
    def performance(self,weights):
        for i in range(len(self.scores)):
            curr_score=self.scores[i]
            percent=(curr_score*weights[i])/100
            percent=+percent
        
        return percent
        
    def total(self):
        total_score=0
        for i in range(len(self.scores)): 
            total_score=total_score+self.scores[i]
        return total_score

#lists  
modules=[] # we store all the objects of the module class in this list
module_name=[] #we store all the names of the modules in this list
module_code=[] #we store all the modules codes in this list


students=[] # we store all the objects of the students class in this list
first_names=[] #we store all the first names of students in this list
last_names=[]  #we store all the last names of students in this list
student_ids=[] #we store all the ids of students in this list



print ("to start the program please enter all the inputs below:")
while True:
    try:  
        n_modules=int(input("Enter the number of modules in this semester(from 3 to 7 modules)"))
    except ValueError:
        print("Sorry, I didn't understand that Please enter real numbers only.")        
        continue
    if n_modules > 7:
        print("the max number of modules is 7")        
        continue
    if n_modules < 3:
        print("the min number of modules is 3")
        continue
    else:
        break

while True: 
    try:   
        num_students = int(input('Enter number of students from 3 to 100:'))
    except ValueError:
        print("Sorry, I didn't understand that Please enter real numbers only.")       
        continue
    if num_students > 100:
        print("the max number of modules is 100")        
        continue
    if num_students < 3:
        print("the min number of students is 3")
        continue
    else:
        break


for i in range(num_students):
    while True:
        firstname = input("enter first name")
        if firstname.isalpha():
            break
        print("Please enter characters A-Z only")
    while True:
        lastname = input("enter last name")
        if lastname.isalpha():
            break
        print("Please enter characters A-Z only")

    first_names.append(firstname)
    last_names.append(lastname)
    while True: 
        try:   
            student_ids.append(int(input('Enter student id:')))
        except ValueError:
            print("Sorry, I didn't understand that Please enter real numbers only.")       
            continue
        else:
            break


for g in range(n_modules):
    while True:
        modulename = input("enter module name")
        if modulename.isalpha():
            break
        print("Please enter characters A-Z only")
    
    module_name.append(modulename)

    while True:
        try:  
            module_code.append(int(input("Enter module code")))
        except ValueError:
            print("Sorry, I didn't understand that Please enter real numbers only.")        
            continue
        else:
            break
    while True:
        try:  
            num_assesments=int(input("number of assesments in this module: "))
        except ValueError:
            print("Sorry, I didn't understand that Please enter real numbers only.")        
            continue
        else:
            break

    weights=[]
    for i in range(num_assesments):
            while True:
                try:  
                    weights.append(float(input('Enter weight:')))
                except ValueError:
                    print("Sorry, I didn't understand that Please enter numbers or floats")        
                    continue
                else:
                    break


    students=[]
    for k in range(num_students):
        scores_current=[]
        for r in range(num_assesments):
            scores_current.append(int(input('Enter score for assment number '+str(r+1)+' for '+first_names[k]+' '+last_names[k] +' in '+module_name[g] +' module out of 100:')))
        students.append(Student(first_names[k],last_names[k],student_ids[k],scores_current))
    modules.append(Module(module_name[g],module_code[g],students,weights))
    

while True:
    while True:
        try:  
            task=int(input('Choose Task for Program: \n 1. Display average score for entire class for specific assignment \n 2.  display the average score for the module over all assessments. \n 3. Display total score for each student sorted by method \n 4. display academic preformance for each student sorted by method \n 5. Display maxumum and minimum for specific assigmnt \n 6. Display maximum and minimum for all module \n 7.close the program'))
        except ValueError:
            print("Sorry, I didn't understand that Please please choose a number between 1 and 7")        
            continue
        if task <=0:
            print("please choose a number between 1 and 7")
        if task > 7:
            print("please choose a number between 1 and 7")
        else:
            break

    if task ==1:
        module_num = int(input("enter modules number: "))
        assignment=int(input('Enter assignment number: '))
        spec=modules[module_num].average_score_spec(assignment)
        print(spec)
    if task==2:
        module_num = int(input("enter modules number: '"))
        average=modules[module_num].average_score_all()
        print(average)
    if task==3:
        module_num = int(input("enter modules number: "))
        sorting_method=int(input("Choose sorting method between 1. by score 2. alphabetically first name 3. alphabetically first name: "))
        if sorting_method==1:
            sorted_list2=modules[module_num].total_score_all('by score')
        if sorting_method==2:
            sorted_list2=modules[module_num].total_score_all('alphabetically first name')
        if sorting_method==3:
            sorted_list2=modules[module_num].total_score_all('alphabetically first name')
        for i in range(0,len(sorted_list2)):
            print(sorted_list2[i].first,sorted_list2[i].last,sorted_list2[i].total())
    if task==4:
        module_num = int(input("enter modules number'"))
        sorting_method=int(input("Choose sorting method between 1. by score 2. alphabetically first name 3. alphabetically first name"))
        if sorting_method==1:
            sorted_list=modules[module_num].performance_for_all('by score')
        if sorting_method==2:
            sorted_list=modules[module_num].performance_for_all('alphabetically first name')
        if sorting_method==3:
            sorted_list=modules[module_num].performance_for_all('alphabetically first name')
        for i in range(0,len(sorted_list)):
            print(sorted_list[i].first,sorted_list[i].last,sorted_list[i].performance())

    if task==5:
        module_num = int(input("enter modules number'"))
        assignment=int(input('Enter assignment number:'))
        # spec=m.average_score_spec(assignment)
        maxst,minst=modules[module_num].max_min(assignment)
        print('Student with Maximum score')
        print(maxst.first,maxst.last,maxst.id)
        print('Students with minimum score')
        print(minst.first,minst.last,minst.id)
    if task==6:
        module_num = int(input("enter modules number'"))
        sorted_list2=modules[module_num].total_score_all('by score')
        print('Student with maximum score in all module')
        print(sorted_list2[0].first,sorted_list2[0].last)
        print('Student with minimum score in all module')
        print(sorted_list2[num_students-1].first,sorted_list2[num_students-1].last)
    if task==7:
        break

        # if 100>=percent>=70:
        #     print('Excellent to Outstanding')
        #     print('Degree Class: First')
        # if 69>=percent>=60:
        #     print('Good to Very Good')
        #     print('Degree Class: First')
        # if 59>=percent>=50:
        #     print('Satisfying')
        #     print('Degree Class: First')
        # if 49>=percent>=40:
        #     print('Sufficient')
        #     print('Degree Class: First')
        # if 39>=percent>=0:
        #     print('Unsatisfactory ')
        #     print('Degree Class: First')
