from tkinter import *
import kmeans
import timeit
import matplotlib.pyplot as plt


##On clicking the toggle dimension button, changes dimension from 2 to 3 or v.v. for random generated method
def toggleDimension():

    #toggle between 2 dimensions and 3 dimensions
    global is2dim 
    temp = is2dim
    is2dim = not temp

    #Update the interface accordingly
    if (is2dim):
        lbl_dimension.configure(text="2D Selected")
        btn_dimension.configure(text="Select 3D Data")
    else:
        lbl_dimension.configure(text="3D Selcted")
        btn_dimension.configure(text="Select 2D Data")

##If CSV data is entered into the text box, run kmeans.py using this data
def execCSV():

    #Get the global variables that represent k and the CSV values, convert to int
    global numMeans
    global csvValues
    numMeans = int(txt_k.get())

    #Get CSV string
    csvValues = csvBox.get("1.0", END)

    #Run core program and count the time
    start = timeit.default_timer()
    if (numMeans != None):
        plt = kmeans.runCSV(numMeans, csvValues)
    stop = timeit.default_timer()
    timeTaken = stop - start

    #Print time taken to user
    lbl_timeTaken.configure(text=("Total Time Taken: ", timeTaken))

    #Show plot AFTER calculating the time taken to run the algorithm
    plt.show()

def execRand():

    #Get the global variables that represnet k and n (#points)
    global numMeans
    global numValues


    #go from boolean to int based on predefined logic
    dim = 2 if is2dim else 3

    #parse k and n as integers
    numMeans = int(txt_k.get())
    numValues = int(numRand.get())

    #Run core program and count the time taken
    start = timeit.default_timer()
    if (numMeans != None and numValues != None):
        plt = kmeans.runRand(numMeans, numValues, dim)
    stop = timeit.default_timer()
    timeTaken = stop - start

    #Print time taken to user
    lbl_timeTaken.configure(text=("Total Time Taken: ", timeTaken))

    #Show plot AFTER calculating the time taken to run the algorithm
    plt.show()


#Global variables
is2dim = True
rand = False
csvValues = ""
numValues = None
numMeans = None


#Define base window properties
window = Tk()
window.title("K-Means Solution")
window.geometry('800x600')

#Define column and row layouts
window.columnconfigure(0, weight = 1)
window.columnconfigure(1, weight = 1)
window.columnconfigure(2, weight = 1)
window.rowconfigure(0, weight = 1)
window.rowconfigure(1, weight = 1)
window.rowconfigure(2, weight = 3)
window.rowconfigure(3, weight = 1)
window.rowconfigure(4, weight = 1)

#Create the title label
lbl_Title = Label(window, text="K-Means")
lbl_Title.grid(column = 0, row = 0)

#Create prompt and text box for entering the # of means
lbl_k = Label(window, text = "Enter #means")
lbl_k.grid(column = 1, row = 0)
txt_k = Entry(window)
txt_k.grid(column = 2, row = 0)

#Create the prompt, text box and submit button to paste CSV data and run the algorithm
lbl_csv = Label(window, text = "Paste CSV here")
lbl_csv.grid(column = 0, row = 1)
csvBox = Text(window, width = 30)
csvBox.grid(column = 0, row = 2)
btn_csv = Button(window, text="Run Using CSV Values", command=execCSV)
btn_csv.grid(column = 0, row = 3)

#Create title for Random number info column
lbl_rand = Label(window, text = "Generate Random Values")
lbl_rand.grid(column = 1, row = 1)
#Create the prompt, text box and submit button to enter # of Random points and run algorithm
lbl_numRand = Label(window, text = "Enter the number of random variables")
lbl_numRand.grid(column = 1, row = 1)
numRand = Entry(window)
numRand.grid(column = 1, row = 2)
btn_rand = Button(window, text="Run Using Random Values", command=execRand)
btn_rand.grid(column = 1, row = 3 )

#Label and button to toggle between 2-d and 3-d data ONLY FOR RANDOM NUMBERS
btn_dimension = Button(window, text="Switch to 3-D Data", command=toggleDimension)
btn_dimension.grid(column = 2, row = 2)
lbl_dimension = Label(window, text="2-d Selected")
lbl_dimension.grid(column = 2, row = 1)

#Create the label for the total time takne, so that it can be updated when necessary
lbl_timeTaken = Label(window, text = "Total time taken:")
lbl_timeTaken.grid(column = 1, row = 4)

#Keep the GUI up and running
window.mainloop()
