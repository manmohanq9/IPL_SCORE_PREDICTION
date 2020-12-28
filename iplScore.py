from tkinter import *
from PIL import ImageTk,Image
from tkinter import ttk
import pandas as pd
from numpy import *
from sklearn.linear_model import LogisticRegression
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
import tkinter.messagebox as tmsg

root=Tk()
root.title("IPL SCORE PREDICTION")
root.geometry("1000x600+200+40")
root.resizable(width=0,height=0)

render = ImageTk.PhotoImage(Image.open("ipl1.jpg"))

img = Label(root, image=render)
img.place(x=0,y=0)

def reset():
    currentScorev.set("")
    wicketsv.set("")
    oversv.set("")
    ballsv.set("")
    player1v.set("")
    player2v.set("")
    displayv.set("")

def check_Dtype(x):
    try:
        return int(x)
    except ValueError :
        tmsg.showinfo("IPL PROJECTED SCORE", f"INVALID NUMBERS '{x}'")

def submit():
    # Importing the dataset
    import pandas as pd
    dataset = pd.read_csv('ipl.csv')
    X = dataset.iloc[:, [7, 8, 9, 12, 13]].values
    y = dataset.iloc[:, 14].values

    # Splitting the dataset into the Training set and Test set
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

    from sklearn.model_selection import StratifiedKFold
    kf = StratifiedKFold(n_splits=40)

    for ti, tti in kf.split(X, y):
        X_train, X_test, y_train, y_test = X[ti], X[tti], y[ti], y[tti]

    # Training the dataset
    from sklearn.ensemble import RandomForestRegressor
    reg = RandomForestRegressor(n_estimators=5)
    reg.fit(X_train, y_train)

    # Testing the dataset on trained model
    score = reg.score(X_test, y_test)
    print(score)

    a1 = int(currentScoretext.get())
    b1 = int(wicketstext.get())
    c1 = float((int(overstext.get() + ballstext.get()))/10)
    d1 = check_Dtype(player1text.get())
    e1 = check_Dtype(player2text.get())

    # Testing with input
    inputdata = array([[a1, b1, c1, d1, e1]])
    projectedScore = reg.predict(inputdata)

    for i in projectedScore:
        score = f" {int(i)}"
        displayv.set(score)

    tmsg.showinfo("Survival Probability", f"Projected Score is {score}")

currentScorev = StringVar()
wicketsv = StringVar()
oversv = StringVar()
ballsv = StringVar()
player1v = StringVar()
player2v = StringVar()
displayv = StringVar()

top = Label(root,text="IPL",font=("times new roman",60,"bold"),bg="darkblue",fg="white")
top.place(x=360,y=30,width=260,height=60)

top2 = Label(root,text="SCORE PREDICTION",font=("times new roman",18,"bold"),bg="darkblue",fg="white")
top2.place(x=360,y=100,width=260,height=30)

currentScore = Label(root,text="CURRENT SCORE",font=("times new roman",10,"bold"),bg="darkblue",fg="white")
currentScore.place(x=360,y=140,width=130,height=30)

currentScoretext=Entry(root,width=30,textvariable=currentScorev,font=("times new roman", 13, "bold"),)
currentScoretext.place(x=490, y=140,width=130,height=30 )

wickets = Label(root,text="WICKETS",font=("times new roman",10,"bold"),bg="darkblue",fg="white")
wickets.place(x=360,y=180,width=130,height=30)

wicketstext = ttk.Combobox(root,width=28,textvariable=wicketsv, font=("times new roman", 13, "bold"),state='readonly')
wicketstext['values']=("0","1","2","3","4","5","6","7","8","9")
wicketstext.place(x=490, y=180,width=130,height=30)

overs = Label(root,text="OVERS",font=("times new roman",10,"bold"),bg="darkblue",fg="white")
overs.place(x=360,y=220,width=65,height=30)

overstext = ttk.Combobox(root,width=28,textvariable=oversv, font=("times new roman", 13, "bold"),state='readonly')
overstext['values']=("1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20")
overstext.place(x=425, y=220,width=65,height=30)

balls = Label(root,text="BALLS",font=("times new roman",10,"bold"),bg="darkblue",fg="white")
balls.place(x=490,y=220,width=65,height=30)

ballstext = ttk.Combobox(root,width=28,textvariable=ballsv, font=("times new roman", 13, "bold"),state='readonly')
ballstext['values']=("1","2","3","4","5")
ballstext.place(x=555, y=220,width=65,height=30)

currentPlayerScores = Label(root,text="CURRENT PLAYERS SCORES",font=("times new roman",10,"bold"),bg="darkblue",fg="white")
currentPlayerScores.place(x=360,y=260,width=260,height=30)

player1 = Label(root,text="PLAYER 1",font=("times new roman",10,"bold"),bg="darkblue",fg="white")
player1.place(x=360,y=300,width=120,height=30)

player1text=Entry(root,width=30,textvariable=player1v,font=("times new roman", 13, "bold"),)
player1text.place(x=360, y=330,width=120,height=30 )

player2 = Label(root,text="PLAYER 2",font=("times new roman",10,"bold"),bg="darkblue",fg="white")
player2.place(x=500,y=300,width=120,height=30)

player2text=Entry(root,width=30,textvariable=player2v,font=("times new roman", 13, "bold"),)
player2text.place(x=500, y=330,width=120,height=30 )

reset_button = Button(root,text="RESET",command=reset,font=("times new roman",13,"bold"),bg="darkblue",fg="white")
reset_button.place(x=360,y=380,width=120,height=30)

display=Entry(root,width=30,textvariable=displayv,font=("times new roman", 40, "bold"),)
display.place(x=430, y=420,width=120,height=60 )

submit = Button(root,command=submit,text="PREDICT SCORE",font=("times new roman",10,"bold"),bg="darkblue",fg="white")
submit.place(x=500,y=380,width=120,height=30)

root.mainloop()