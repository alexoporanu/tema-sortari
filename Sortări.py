import random
from random import seed

seed(1)

import time

def random_list_generator(N, NMAX):
    lst=[]

    for i in range(N):
        lst.append(random.randint(0,NMAX))

    return lst




def reverse_sorted_list_generator(N,NMAX):
    lst=[]
    i=random.randint(N,NMAX)
    j=N-1

    while j>=0:
        lst.append(i)
        i-=1
        j-=1

    return lst



def sorted_list_generator(N,NMAX):

    lst=[]

    i=random.randint(0,NMAX-N)
    j=i+N-1

    while i<=j:
        lst.append(i)
        i+=1

    return lst



def almost_Sorted_generator(N,NMAX):
    lst=[]
    c=0

    for i in range(N):
        if i%5!=0:
            lst.append(c)
            c+=1
        else:
            lst.append(random.randint(0,NMAX))

    return lst


def almost_Reverse_Sorted_generator(N, NMAX):
    lst = []
    i = c =  NMAX

    while i > NMAX - N:
        if i%5==0:
            lst.append(random.randint(0,NMAX))
        else:
            lst.append(c)
            c-=1
        i -= 1

    return lst

def count_sort(L):
    freq=[]

    val_max=max(L)

    for i in range(val_max+1):
        freq.append(0)

    for x in L:
        freq[x]+=1

    SORTED=[]

    for i in range(val_max+1):
       while freq[i]!=0:
            SORTED.append(i)
            freq[i]-=1

    return SORTED

def bubble_sort(L):

    n=len(L)-1
    ok=0
    j=n

    while ok==0:
        ok=1
        for i in range(0,j):

            if L[i]>L[i+1]:
                aux=L[i]
                L[i]=L[i+1]
                L[i+1]=aux


            ok=0
        j-=1
    return L

def insertionSort(L):

    lg=len(L)

    for i in range(1, lg):

        key = L[i]

        j = i - 1
        while j >= 0 and key < L[j]:
            L[j + 1] = L[j]
            j -= 1
        L[j + 1] = key

    return L




def interclasare(A, B):
    a = len(A)
    b = len(B)
    i = 0
    j = 0
    C = []
    while i < a and j < b:
        if A[i] > B[j]:
            C.append(B[j])
            j += 1
        else:
            C.append(A[i])
            i += 1

    for k in range(i, len(A)):
        C.append(A[k])
    for k in range(j, len(B)):
        C.append(B[k])

    return C


def merge_sort(V, st, dr):

    mid = (st + dr) // 2


    if st == dr:
        return [V[mid]]

    if dr-st<=10:
        return insertionSort(V[st:dr+1])



    return interclasare(merge_sort(V, st, mid), merge_sort(V, mid + 1, dr))

def quick_sort(L):
    if L == []:
        return []

    if len(L) < 11:
        return insertionSort(L)

    k = random.randint(0, len(L) - 1)

    mai_mici = [x for x in L if x < L[k]]
    egale = [x for x in L if x == L[k]]
    mai_mari = [x for x in L if x > L[k]]


    return quick_sort(mai_mici) + egale + quick_sort(mai_mari)


def BFPRT(A):
        if len(A) <= 5:
            return sorted(A)[len(A) // 2]

        grupuri = [sorted(A[i:i + 5]) for i in range(0, len(A), 5)]

        mediane = [grup[len(grup) // 2] for grup in grupuri]

        return BFPRT(mediane)


def quick_sort_BFPRT(L):
        if L == []:
            return []

        if len(L) < 11:
            return insertionSort(L)

        bfprt = BFPRT(L)

        mai_mici = [x for x in L if x < bfprt]
        egale = [x for x in L if x == bfprt]
        mai_mari = [x for x in L if x > bfprt]

        return quick_sort(mai_mici) + egale + quick_sort(mai_mari)



def countsort(L,exp):
    freq=[]

    for i in range(10):
        freq.append([])


    for number in L:
        freq[(number//exp)%10].append(number)

    L=[]

    for i in range(10):
        L+=freq[i]

    return L

def radix_sort(L):

    nrcif_max=len(str(max([number for number in L])))
    i=1
    exp=1

    while i<=nrcif_max:
        L=countsort(L,exp)
        exp*=10
        i+=1

    return L


def log_2(x):
    c=0

    while x!=1:
        x//=2
        c+=1
    return c

def count_sort_2(L,exp):
    freq=[]

    for i in range(2):
        freq.append([])

    for number in L:
        freq[(number>>exp)%2].append(number)

    L=[]

    for i in range(2):
        L+=freq[i]

    return L




def radix_sort_2(L):

    log2=log_2(max(L))

    exp=0


    while exp<=log2+1:
        L=count_sort_2(L,exp)
        exp+=1

    return L

def log_4(x):
    c=0

    while x!=1:
        x//=2
        c+=1
    return c

def count_sort_4(L,exp):
    freq=[]

    for i in range(4):
        freq.append([])

    for number in L:
        freq[(number>>(2*exp))%4].append(number)

    L=[]

    for i in range(4):
        L+=freq[i]

    return L



def radix_sort_4(L):

    log4=log_4(max(L))

    exp=0


    while exp<=log4:
        L=count_sort_4(L,exp)
        exp+=1

    return L

def este_sortat(L):
    for i in range(len(L)-1):
        if L[i]>L[i+1]:
            return "Nu a sortat bine"

    return "A sortat bine"


fisier=open("teste.in")

T=int(fisier.readline())



while T:
    lista=fisier.readline().strip("\n").split()

    N=int(lista[0])

    NMAX=int(lista[1])

    tip=lista[2]

    T-=1

    de_sortat=[]

    if tip=="sorted":
        de_sortat=sorted_list_generator(N,NMAX)
    else:
        if tip=="reverseSorted":
            de_sortat=reverse_sorted_list_generator(N,NMAX)
        else:
            if tip=="random":
                de_sortat=random_list_generator(N,NMAX)
            else:
                if tip=="almostSorted":
                    de_sortat=almost_Sorted_generator(N,NMAX)
                else:
                    if tip=="almostReverseSorted":
                        de_sortat=almost_Reverse_Sorted_generator(N,NMAX)

    print("\t\t", "N=",N,"  NMAX=",NMAX," ", "  caz:", tip, sep="")
    print()

    de_sortat_sorted = de_sortat.copy()
    test_sorted = de_sortat.copy()

    start = time.time()

    sorted(de_sortat_sorted)

    print("Timpul de executie pentru sorted din Python este de ", time.time() - start, " secunde.", sep="")
    print(este_sortat(sorted(test_sorted)), ".", sep="")
    print()






    de_sortat_count = de_sortat.copy()
    test_count = de_sortat.copy()

    start = time.time()

    count_sort(de_sortat_count)

    print("Timpul de executie pentru count sort este de ", time.time() - start, " secunde.", sep="")
    print(este_sortat(count_sort(test_count)), ".", sep="")
    print()






    if N<100000:


        de_sortat_bubble = de_sortat.copy()
        test_bubble = de_sortat.copy()

        start = time.time()

        bubble_sort(de_sortat_bubble)

        print("Timpul de executie pentru bubble sort este de ", time.time() - start, " secunde.", sep="")
        print(este_sortat(bubble_sort(test_bubble)), ".", sep="")
        print()
    else:
        print("Bubble sort nu poate sorta.")
        print()







    de_sortat_merge=de_sortat.copy()
    test_merge=de_sortat.copy()

    start=time.time()

    merge_sort(de_sortat_merge,0,len(de_sortat_merge)-1)

    print("Timpul de executie pentru merge sort este de ", time.time()-start, " secunde.", sep="" )
    print(este_sortat(merge_sort(de_sortat_merge,0,len(de_sortat_merge)-1)), ".", sep="")
    print()







    de_sortat_quick=de_sortat.copy()
    test_quick=de_sortat.copy()

    start=time.time()

    quick_sort(de_sortat_quick)

    print("Timpul de executie pentru quick sort este de ", time.time()-start, " secunde.", sep="")
    print( este_sortat(quick_sort(test_quick)), ".", sep="")
    print()





    de_sortat_bfprt=de_sortat.copy()
    test_bfprt=de_sortat.copy()

    start=time.time()

    quick_sort_BFPRT(de_sortat_bfprt)

    print("Timpul de executie pentru quick sort (BFPRT) este de ", time.time()-start, " secunde.",  sep="")
    print( este_sortat(quick_sort_BFPRT(test_bfprt)), ".", sep="")
    print()



    de_sortat_radix=de_sortat.copy()
    test_radix=de_sortat.copy()

    start=time.time()

    radix_sort(de_sortat_radix)

    print("Timpul de executie pentru radix sort cu baza 10 este de ", time.time()-start, " secunde.", sep="")
    print( este_sortat(radix_sort(test_radix)), ".", sep="")
    print()






    de_sortat_radix2=de_sortat.copy()
    test_radix2=de_sortat.copy()

    start=time.time()

    radix_sort_2(de_sortat_radix2)

    print("Timpul de executie pentru radix sort cu baza 2 este de ", time.time()-start, " secunde.", sep="")
    print( este_sortat(radix_sort_2(test_radix2)), ".", sep="")
    print()






    de_sortat_radix4 = de_sortat.copy()
    test_radix4 = de_sortat.copy()

    start = time.time()

    radix_sort_4(de_sortat_radix4)

    print("Timpul de executie pentru radix sort cu baza 4 este de ", time.time() - start, " secunde.", sep="")
    print(este_sortat(radix_sort_4(test_radix4)), ".", sep="")
    print()


    print("\n\n\n\n\n")









