def plusMinus(arr):
    # Write your code here
    positives_count = 0
    negative_count = 0
    zero_count = 0
    for i in range(len(arr)):
        if(arr[i] > 0):
            positives_count += 1
        elif(arr[i] < 0):
            negative_count += 1
        elif(arr[i] == 0):
            zero_count += 1
    positives = positives_count/len(arr)
    negatives = negative_count/len(arr)
    zeros = zero_count/len(arr)
    print(positives)
    print(negatives)
    print(zeros)
