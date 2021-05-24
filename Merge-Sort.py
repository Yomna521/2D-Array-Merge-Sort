#Question 1: 2D Merge sort 
from math import ceil

def merge_rows(top_left, top_right, bottom_left, bottom_right):
    tl_row=0
    tl_col=0    #top left index
    tr_row=0
    tr_col=0    #top right index
    bl_row=0
    bl_col=0    #bottom left index
    br_row=0
    br_col=0    #bottom right index
    array_row=0
    array_col=0     #merge index

    top_arr =[]
    bottom_arr=[]

    #sort top rows
    while(array_row<len(top_left) or array_row<len(top_right)):
        while tl_col<len(top_left[0]) and tr_col<len(top_right[0]):
            if(top_left[tl_row][tl_col]<top_right[tl_row][tr_col]):
                array[array_row][array_col] = top_left[tl_row][tl_col]
                tl_col += 1
            elif(top_left[tl_row][tl_col]>top_right[tr_row][tr_col]):
                array[array_row][array_col] = top_right[tr_row][tr_col]
                tr_col += 1
            array_col+=1
        while(tl_col<len(top_left[0])):
            array[array_row][array_col] = top_left[tl_row][tl_col]
            tl_col+=1
            array_col += 1
        while(tr_col<len(top_right[0])):
            array[array_row][array_col] = top_right[tr_row][tr_col]
            tr_col+=1
            array_col += 1
        array_row+=1
        array_col=0
        tr_col=0
        tl_col=0
        tr_row+=1
        tl_row+=1

    #sort bottom rows
    while array_row<len(bottom_left)+len(top_left) or array_row<len(bottom_right)+len(top_right):    
        while bl_col<len(bottom_left[0]) and br_col<len(bottom_right[0]):
            if(bottom_left[bl_row][bl_col]<bottom_right[br_row][br_col]):
                array[array_row][array_col] = bottom_left[bl_row][bl_col]
                bl_col += 1
            elif(bottom_left[bl_row][bl_col]>bottom_right[br_row][br_col]):
                array[array_row][array_col] = bottom_right[br_row][br_col]
                br_col += 1
            array_col+=1
        while(bl_col<len(bottom_left[0])):
            array[array_row][array_col] = bottom_left[bl_row][bl_col]
            bl_col+=1
            array_col += 1
        while(br_col<len(bottom_right[0])):
            array[array_row][array_col] = bottom_right[br_row][br_col]
            br_col+=1
            array_col += 1    
        array_row+=1
        bl_row+=1
        br_row+=1
        bl_col=0
        br_col=0
        array_col=0

    #Fill top array and bottom array
    if(len(top_left)>0 and len(bottom_left)>0):
        for i in range(len(top_left)):
            b=[]
            for j in range(len(top_left[0])+len(top_right[0])):
                b.append(array[i][j])
            top_arr.append(b)
        
        for i in range(len(bottom_left)):
            b=[]
            for j in range(len(bottom_left[0])+len(bottom_right[0])):
                b.append(array[i+len(top_left)][j])
            bottom_arr.append(b)
    return top_arr, bottom_arr

def merge_cols(top_arr, bottom_arr, array):
    array_row=0
    array_col=0
    top_row=0
    top_col=0
    bottom_row=0
    bottom_col=0

    while array_col<len(array[0]):
        while top_row<len(top_arr) and bottom_row<len(bottom_arr):
            if top_arr[top_row][top_col]<bottom_arr[bottom_row][bottom_col]:
                array[array_row][array_col]= top_arr[top_row][top_col]
                top_row+=1
            elif top_arr[top_row][top_col]>bottom_arr[bottom_row][bottom_col]:
                array[array_row][array_col]= bottom_arr[bottom_row][bottom_col]
                bottom_row+=1
            array_row+=1
        while top_row<len(top_arr):
            array[array_row][array_col]= top_arr[top_row][top_col]
            top_row+=1
            array_row+=1
        while bottom_row<len(bottom_arr):
            array[array_row][array_col]= bottom_arr[bottom_row][bottom_col]
            bottom_row+=1
            array_row+=1
        array_col+=1
        top_col+=1
        bottom_col+=1
        array_row=0
        top_row=0
        bottom_row=0

def merge_1d_row(left,right,array):
    i = 0
    j = 0
    k = 0
    while (i<len(left) and j<len(right)):
        if(left[i]<right[j]):
            array[k] = left[i]
            i = i+1
        else:
            array[k] = right[j]
            j = j+1
        
    k = k+1
    
    while(i<len(left)):
        array[k] = left[i]
        i = i+1
        k = k+1
        
    while(j<len(right)):
        array[k] = right[j]
        j = j+1
        k = k+1

def merge_1d_col(top, bottom, array):
    i = 0
    j = 0
    k = 0
        
    while (i<len(top) and j<len(bottom)):
        if(top[i]<bottom[j]):
            array[k][0] = top[i]
            i = i+1
        else:
            array[k][0] = bottom[j]
            j = j+1
        
        k = k+1
        
    while(i<len(top)):
        array[k][0] = top[i]
        i = i+1
        k = k+1
        
    while(j<len(bottom)):
        array[k][0] = bottom[j]
        j = j+1
        k = k+1

def mergesort_1d_col(array):
    if(len(array)<2):
        return
    mid = ceil(len(array[0])/2)
    top = []
    bottom = []

    for i in range(mid):
        top.append(array[i][0])
    for i in range(mid, len(array)):
        bottom.append(array[i][0])
    
    mergesort_1d_col(top)
    mergesort_1d_col(bottom)

    merge_1d_col(top, bottom, array)

def mergesort_1d_row(array):
    if(len(array)<2):
        return
    mid = ceil(len(array)/2)
    left = []
    right = []

    for i in range(mid):
        left.append(array[i])
    for i in range(mid, len(array)):
        right.append(array[i])
    
    mergesort_1d_row(left)
    mergesort_1d_row(right)

    merge_1d_row(left, right, array)

def mergesort_2d(array):
    if len(array)<2 and len(array[0])<2:
        return
    elif len(array)<2:
        #1D horizontal array
        mergesort_1d_row(array[0])
    elif len(array[0])<2:
        #1D vertical array
        mergesort_1d_col(array)
    else:
        #2d array
        mid_row = ceil(len(array)/2)
        mid_col = ceil(len(array[0])/2)

        #create empty matrices
        top_left = []
        top_right= []
        bottom_left= []
        bottom_right = []
        
        row_size=len(array)
        col_size=len(array[0])

        for array_row in range(mid_row):
            b = []
            for array_col in range(mid_col):
                b.append(array[array_row][array_col])
            top_left.append(b)

        for array_row in range(mid_row):
            b = []
            for array_col in range(mid_col,col_size):
                b.append(array[array_row][array_col])
            top_right.append(b)

        for array_row in range(mid_row,row_size):
            b = []
            for array_col in range(mid_col):
                b.append(array[array_row][array_col])
            bottom_left.append(b)
            
        for array_row in range(mid_row,row_size):
            b = []
            for array_col in range(mid_col,col_size):
                b.append(array[array_row][array_col])
            bottom_right.append(b)
        
        
        mergesort_2d(top_left)
        mergesort_2d(top_right)
        mergesort_2d(bottom_left)
        mergesort_2d(bottom_right)
        
        top_arr, bottom_arr = merge_rows(top_left, top_right, bottom_left, bottom_right)
        merge_cols(top_arr, bottom_arr, array)

def input_array():
    size = input().split()
    m=int(size[0])
    n=int(size[1])
    l = input()
    l = l.split()
    a = [int(i) for i in l]

    array = []
    x=0
    while x<m*n:
        for i in range(m):
            b=[]
            for j in range(n):
                b.append(a[x])
                x+=1
            array.append(b)
    return array

if __name__ == "__main__":
    array = input_array()
    mergesort_2d(array)
    for i in range(len(array)):
        for j in range(len(array[0])):
            print(array[i][j], end=" ")
