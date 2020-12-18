class Module:
    def __init__(self,name,code,n_assesments,students):
        self.name=name 
        self.code=code
        self.n_assesments=n_assesments
        self.students=students
   
    def average_score_all(self):                                         
        for student in self.students:                         
            for k in student.scores:                          
                sum_of_scores=0
                sum_of_scores=sum_of_scores+k
        return sum_of_scores/self.n_assesments/self.n_students           



    def average_score_spec(self,asses):                                  
        for student in self.students:
            sum_of_scores=0 
            sum_of_scores=sum_of_scores+student.scores[asses-1]
        return sum_of_scores/self.n_assesments


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
                        if to_sort[k].total()>to_sort[k+1].total():
                            tmp=to_sort[k]
                            to_sort[k]=to_sort[k+1]
                            to_sort[k+1]=tmp
        return to_sort
    def max_min(self,asses):
        pos_1=0
        pos_2=0

        maxn=self.students[0].scores[asses-1]
        for i in range(len(self.students)):
            print('inside loop')
            print(self.students[i].scores[asses-1],'compare')
            print(maxn,'current')
            if self.students[i].scores[asses-1]>maxn:
                print(self.students[i].scores[asses-1],'check max')
                maxn=self.students[i].scores[asses-1]
                pos_1=i
                print(pos_1,'pos1')
        max_stu=self.students[pos_1]
        minn=self.students[0].scores[asses-1]
        for j in range (len(self.students)):
            print('inside second loop')
            if self.students[i].scores[asses-1]<minn :
                print(self.students[j].scores[asses-1],'check min')
                minn=self.students[j].scores[asses-1]
                pos_2=j
                print(pos_2,'pos2')
        min_stu=self.students[pos_2]
        print('helloooooo')
        return max_stu,min_stu

class Student:
    def __init__(self,first,last,id_n,scores,weights,n_scores):
        self.first=first
        self.last=last
        self.id=id_n
        self.scores=scores

        self.weights=weights
        self.n_scores=n_scores
    
    
    def performance(self):
        for i in range(self.n_scores):
            curr_score=self.scores[i]
            percent=(curr_score*self.weights[i])/100
            percent=+percent
        # print('final percent',percent)
        
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
        return percent
        
    def total(self):
        total_score=0
        for i in range(self.n_scores): 
            total_score=total_score+self.scores[i]
        return total_score

#lists  
modules=[]  
module_name=[]
module_code=[]
n_assesments=[]
scores_current=[]

students=[]
first_names=[]
last_names=[]
student_ids=[]
weights=[]
scores=[]


print ("to start the program please enter all the inputs below:")
n_modules=int(input("Enter the number of modules in this semester(from 3 to 5 modules)"))

for g in range(n_modules):
    module_name.append(input('Enter module name:'))
    module_code.append(int(input("Enter moudule code")))
    num_assesments=int(input("number of assesments in this module"))
    for i in range(num_assesments):
        weights.append(float(input('Enter weight:')))

        

num_students = int(input('Enter number of students:'))

for i in range(num_students):
    first_names.append(input('Enter first name:'))
    last_names.append(input('Enter last name:'))
    student_ids.append(input('Enter student id:'))
    for j in (weights):
        scores_current.append(int(input('Enter score out of 100:')))
        scores.append(scores_current)
 



        
            

# the part were we append the objects in lists for the classes
for q in range(num_students):
    s=Student(first_names[q],last_names[q],student_ids[q],scores[q],weights,num_assesments)
    students.append(s)
    
for w in range(n_modules):
    m=Module(module_name,module_code,num_assesments,num_students,students)
    modules.append(m)
    


while True:
    task=int(input('Choose Task for Program: \n 1. Display average score for entire class for specific assignment \n 2.  display the average score for the module over all assessments. \n 3. Display total score for each student sorted by method \n 4. display academic preformance for each student sorted by method \n 5. Display maxumum and minimum for specific assigmnt \n 6. Display maximum and minimum for all module'))

    if task ==1:
        assignment=int(input('Enter assignment number:'))
        spec=m.average_score_spec(assignment)
        print(spec)
    if task==2:
        average=m.average_score_all()
        print(average)
    if task==3:
        sorting_method=int(input("Choose sorting method between 1. by score 2. alphabetically first name 3. alphabetically first name"))
        if sorting_method==1:
            sorted_list2=m.total_score_all('by score')
        if sorting_method==2:
            sorted_list2=m.total_score_all('alphabetically first name')
        if sorting_method==3:
            sorted_list2=m.total_score_all('alphabetically first name')
        for i in range(0,len(sorted_list2)):
            print(sorted_list2[i].first,sorted_list2[i].last,sorted_list2[i].total())
    if task==4:
        sorting_method=int(input("Choose sorting method between 1. by score 2. alphabetically first name 3. alphabetically first name"))
        if sorting_method==1:
            sorted_list=m.performance_for_all('by score')
        if sorting_method==2:
            sorted_list=m.performance_for_all('alphabetically first name')
        if sorting_method==3:
            sorted_list=m.performance_for_all('alphabetically first name')
        for i in range(0,len(sorted_list)):
            print(sorted_list[i].first,sorted_list[i].last,sorted_list[i].performance())

    if task==5:
        assignment=int(input('Enter assignment number:'))
        # spec=m.average_score_spec(assignment)
        maxst,minst=m.max_min(assignment)
        print('Student with Maximum score')
        print(maxst.first,maxst.last,maxst.id)
        print('Students with minimum score')
        print(minst.first,minst.last,minst.id)
    if task==6:
        sorted_list2=m.total_score_all('by score')
        print('Student with maximum score in all module')
        print(sorted_list2[0].first,sorted_list2[0].last)
        print('Student with minimum score in all module')
        print(sorted_list2[num_students-1].first,sorted_list2[num_students-1].last)


