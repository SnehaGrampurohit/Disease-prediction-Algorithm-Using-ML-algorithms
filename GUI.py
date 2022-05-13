from tkinter import *
from disease_prediction import *
def DecisionTree():

    from sklearn import tree

    clf3 = tree.DecisionTreeClassifier()   # empty model of the decision tree
    clf3 = clf3.fit(X,y)

    # calculating accuracy-------------------------------------------------------------------
    from sklearn.metrics import accuracy_score
    y_pred=clf3.predict(X_test)
    print(accuracy_score(y_test, y_pred))
    print(accuracy_score(y_test, y_pred,normalize=False))
    # -----------------------------------------------------

    psymptoms = [Symptom1.get(),Symptom2.get(),Symptom3.get(),Symptom4.get(),Symptom5.get()]

    for k in range(0,len(l1)):
        # print (k,)
        for z in psymptoms:
            if(z==l1[k]):
                l2[k]=1

    inputtest = [l2]
    predict = clf3.predict(inputtest)
    predicted=predict[0]

    h='no'
    for a in range(0,len(disease)):
        if(predicted == a):
            h='yes'
            break


    if (h=='yes'):
        t1.delete("1.0", END)
        t1.insert(END, disease[a])
    else:
        t1.delete("1.0", END)
        t1.insert(END, "Not Found")


def randomforest():
    from sklearn.ensemble import RandomForestClassifier
    clf4 = RandomForestClassifier()
    clf4 = clf4.fit(X,np.ravel(y))

    # calculating accuracy-------------------------------------------------------------------
    from sklearn.metrics import accuracy_score
    y_pred=clf4.predict(X_test)
    print(accuracy_score(y_test, y_pred))
    print(accuracy_score(y_test, y_pred,normalize=False))
    # -----------------------------------------------------

    psymptoms = [Symptom1.get(),Symptom2.get(),Symptom3.get(),Symptom4.get(),Symptom5.get()]

    for k in range(0,len(l1)):
        for z in psymptoms:
            if(z==l1[k]):
                l2[k]=1

    inputtest = [l2]
    predict = clf4.predict(inputtest)
    predicted=predict[0]

    h='no'
    for a in range(0,len(disease)):
        if(predicted == a):
            h='yes'
            break

    if (h=='yes'):
        t2.delete("1.0", END)
        t2.insert(END, disease[a])
    else:
        t2.delete("1.0", END)
        t2.insert(END, "Not Found")


def NaiveBayes():
    from sklearn.naive_bayes import GaussianNB
    gnb = GaussianNB()
    gnb=gnb.fit(X,np.ravel(y))

    # calculating accuracy-------------------------------------------------------------------
    from sklearn.metrics import accuracy_score
    y_pred=gnb.predict(X_test)
    print(accuracy_score(y_test, y_pred))
    print(accuracy_score(y_test, y_pred,normalize=False))
#    # -----------------------------------------------------

    psymptoms = [Symptom1.get(),Symptom2.get(),Symptom3.get(),Symptom4.get(),Symptom5.get()]
    for k in range(0,len(l1)):
        for z in psymptoms:
            if(z==l1[k]):
                l2[k]=1

   inputtest = [l2]
    predict = gnb.predict(inputtest)
   predicted=predict[0]

    h='no'
    for a in range(0,len(disease)):
        if(predicted == a):
            h='yes'
           break

   if (h=='yes'):
        t3.delete("1.0", END)
        t3.insert(END, disease[a])
    else:
        t3.delete("1.0", END)
        t3.insert(END, "Not Found")

#gui_stuff------------------------------------------------------------------------------------
if __name__=='__main__':
    root = Tk()
    root.configure(background='skyblue')

    # entry variables
    Symptom1 = StringVar()
    Symptom1.set(None)
    Symptom2 = StringVar()
    Symptom2.set(None)
    Symptom3 = StringVar()
    Symptom3.set(None)
    Symptom4 = StringVar()
    Symptom4.set(None)
    Symptom5 = StringVar()
    Symptom5.set(None)
    Name = StringVar()

    # Heading
    w2 = Label(root, justify=CENTER, text="Disease Predictor using Machine Learning", fg="black", bg="skyblue")
    w2.config(font=("Elephant", 30))
    w2.grid(row=1, column=0, columnspan=2, padx=100)

    # labels
    NameLb = Label(root, text="Patient's Name", fg="black", bg="skyblue")
    NameLb.grid(row=6, column=0, pady=15, sticky=W)
    NameLb.config(font=("Aharoni", 20))

    S1Lb = Label(root, text="Symptom 1", fg="black", bg="skyblue")
    S1Lb.grid(row=7, column=0, pady=10, sticky=W)
    S1Lb.config(font=("Aharoni", 20))

    S2Lb = Label(root, text="Symptom 2", fg="black", bg="skyblue")
    S2Lb.grid(row=8, column=0, pady=10, sticky=W)
    S2Lb.config(font=("Aharoni", 20))

    S3Lb = Label(root, text="Symptom 3", fg="black", bg="skyblue")
    S3Lb.grid(row=9, column=0, pady=10, sticky=W)
    S3Lb.config(font=("Aharoni", 20))

    S4Lb = Label(root, text="Symptom 4", fg="black", bg="skyblue")
    S4Lb.grid(row=10, column=0, pady=10, sticky=W)
    S4Lb.config(font=("Aharoni", 20))

    S5Lb = Label(root, text="Symptom 5", fg="black", bg="skyblue")
    S5Lb.grid(row=11, column=0, pady=10, sticky=W)
    S5Lb.config(font=("Aharoni", 20))

    lrLb = Label(root, text="DecisionTree", fg="black", bg="skyblue")
    lrLb.grid(row=15, column=0, pady=10,sticky=W)
    lrLb.config(font=("Aharoni", 20))

    destreeLb = Label(root, text="RandomForest", fg="black", bg="skyblue")
    destreeLb.grid(row=17, column=0, pady=10, sticky=W)
    destreeLb.config(font=("Aharoni", 20))

    ranfLb = Label(root, text="NaiveBayes", fg="black", bg="skyblue")
    ranfLb.grid(row=19, column=0, pady=10, sticky=W)
    ranfLb.config(font=("Aharoni", 20))
    # entries
    OPTIONS = sorted(l1)

    NameEn = Entry(root, textvariable=Name)
    NameEn.grid(row=6, column=1)

    S1En = OptionMenu(root, Symptom1,*OPTIONS)
    S1En.grid(row=7, column=1)

    S2En = OptionMenu(root, Symptom2,*OPTIONS)
    S2En.grid(row=8, column=1)

    S3En = OptionMenu(root, Symptom3,*OPTIONS)
    S3En.grid(row=9, column=1)

    S4En = OptionMenu(root, Symptom4,*OPTIONS)
    S4En.grid(row=10, column=1)

    S5En = OptionMenu(root, Symptom5,*OPTIONS)
    S5En.grid(row=11, column=1)


    dst = Button(root, text="DecisionTree", command=DecisionTree,bg="green",fg="yellow")
    dst.grid(row=8, column=3, padx=10)

    rnf = Button(root, text="Randomforest", command=randomforest,bg="green",fg="yellow")
    rnf.grid(row=9, column=3, padx=10)

    lr = Button(root, text="NaiveBayes", command=NaiveBayes,bg="green",fg="yellow")
    lr.grid(row=10, column=3, padx=10)

    #textfileds
    t1 = Text(root, height=1, width=40,bg="white",fg="red")
    t1.grid(row=15, column=1, padx=10)

    t2 = Text(root, height=1, width=40,bg="white",fg="red")
    t2.grid(row=17, column=1, padx=10)

    t3 = Text(root, height=1, width=40,bg="white",fg="red")
    t3.grid(row=19, column=1, padx=10)

    root.mainloop()
