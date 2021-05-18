# Starter code for CS 165B HW2 Spring 2019

def L2_distance(test,cen):
    distance = 0 
    for i in range(len(test)):
        distance += (cen[i]-test[i])**2              
    dis = distance**.5  
    return dis
    
    

def run_train_test(training_input, testing_input):
    """
    Implement the training and testing procedure here. You are permitted
    to use additional functions but DO NOT change this function definition.
    You are permitted to use the numpy library but you must write
    your own code for the linear classifier.

    Inputs:
        training_input: list form of the training file
            e.g. [[3, 5, 5, 5],[.3, .1, .4],[.3, .2, .1]...]
        testing_input: list form of the testing file

    Output:
        Dictionary of result values

        IMPORTANT: YOU MUST USE THE SAME DICTIONARY KEYS SPECIFIED

        Example:
            return {
                "tpr": #your_true_positive_rate,
                "fpr": #your_false_positive_rate,
                "error_rate": #your_error_rate,
                "accuracy": #your_accuracy,
                "precision": #your_precision
            }
    """

    # TODO: IMPLEMENT
    dimension = len(training_input[1])

    start = 1
    end = training_input[0][1]+1
    cen = list()
    start = 0
    end = 1
    for num in range(1,len(training_input[0])):
        start = end
        end += training_input[0][num]
        center_dimension = [0]*dimension
        for i in range(start,end):
            for j in range(dimension):
                center_dimension[j] += training_input[i][j]
        for k in range(dimension):
            center_dimension[k] = center_dimension[k]/training_input[0][num]
        cen.append(center_dimension)
#         if num < (len(training_input[0])-1):
#             start = end
#             end += training_input[0][num+1]
#         print(start,end)
#     print(cen)

    
    true_class = list()
    
#     start = 1
#     end = training_input[0][1]+1
    set_num = 0
    for num in range(1,len(testing_input[0])):
#         print(len(testing_input[0]))
        
        for i in range(testing_input[0][num]):
            true_class.append(set_num)
        set_num += 1
#     print(true_class)
    
    
    pred_class = list()
    

    for i in range(1,len(testing_input)):
        best_res = 1e8
        class_res = 0
        for se in range(len(cen)):

            res = L2_distance(testing_input[i],cen[se])
            if res < best_res:
                best_res = res
                class_res = se
        pred_class.append(class_res)  
#     print(pred_class)
        
    little_matrix = list()
    
    for each in range(len(cen)):
        tp = 0
        fp = 0
        fn = 0
        tn = 0
        for index in range(len(pred_class)):
            if pred_class[index] == true_class[index] and pred_class[index] == each:
                tp += 1
        for index in range(len(pred_class)):
            if pred_class[index] != true_class[index] and pred_class[index] == each:
                fp += 1
        for index in range(len(pred_class)):
            if pred_class[index] != true_class[index] and true_class[index] == each:
                fn += 1
        for index in range(len(pred_class)):
            if true_class[index] != each and pred_class[index] != each:
                tn += 1
        matrix = [tp,fp,fn,tn]
        little_matrix.append(matrix)
#     print(little_matrix)
    TPR = 0
    for i in range (len(cen)):
        TPR += (little_matrix[i][0])/(little_matrix[i][0]+little_matrix[i][2])
    tpr = TPR / len(cen)
    
    FPR = 0
    for i in range (len(cen)):
        FPR += (little_matrix[i][1])/(little_matrix[i][1]+little_matrix[i][3])
    fpr = FPR / len(cen)

    error_rate_nice = 0
    for i in range (len(cen)):
        error_rate_nice += (little_matrix[i][1]+little_matrix[i][2])/(len(testing_input)-1)
        
    error_rate = (error_rate_nice)/len(cen)
        
    accuracy = 1- error_rate
    
    precision_nice = 0
    for i in range (len(cen)):        
        precision_nice += little_matrix[i][0]/(testing_input[0][i+1])
        
    precision = (precision_nice)/len(cen)
        
    return {"tpr": tpr,"fpr": fpr,"error_rate": error_rate,"accuracy": accuracy,"precision": precision
            }
            
#     return {"tpr": 0,"fpr": 0,"error_rate": 0,"accuracy": 0,"precision": 0
#             }
            
