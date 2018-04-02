from tkinter import *
import kmeans
import timeit
import matplotlib.pyplot as plt
def clickedRandom():
    lbl_Rnad.configure(text="button clicked")

def toggleDimension():

    global is2dim
    
    temp = is2dim
    is2dim = not temp
    
    if (is2dim):
        lbl_dimension.configure(text="2D Selected")
        btn_dimension.configure(text="Select 3D Data")
    else:
        lbl_dimension.configure(text="3D Selcted")
        btn_dimension.configure(text="Select 2D Data")
def execCSV():
    global numMeans
    global csvValues

    dim = 2 if is2dim else 3

    

    numMeans = int(txt_k.get())

    csvValues = csvBox.get("1.0", END)

    start = timeit.default_timer()
    if (numMeans != None):
        plt = kmeans.runCSV(numMeans, csvValues, dim)
        
    stop = timeit.default_timer()
    timeTaken = stop - start

    lbl_timeTaken.configure(text=("Total Time Taken: ", timeTaken))
    
    plt.show()

def execRand():

    global numMeans
    global numValues
    
    dim = 2 if is2dim else 3

    

    numMeans = int(txt_k.get())

    numValues = int(numRand.get())

    start = timeit.default_timer()
    if (numMeans != None and numValues != None):
        plt = kmeans.runRand(numMeans, numValues, dim)
        
    stop = timeit.default_timer()
    timeTaken = stop - start

    lbl_timeTaken.configure(text=("Total Time Taken: ", timeTaken))

    plt.show()
    

    


is2dim = True
rand = False
csvValues = ""



numValues = None
numMeans = None

window = Tk()

window.title("K-Means Solution")
window.geometry('800x600')

window.columnconfigure(0, weight = 1)
window.columnconfigure(1, weight = 1)
window.columnconfigure(2, weight = 1)

window.rowconfigure(0, weight = 1)
window.rowconfigure(1, weight = 1)
window.rowconfigure(2, weight = 3)
window.rowconfigure(3, weight = 1)
window.rowconfigure(4, weight = 1)




lbl_Title = Label(window, text="K-Means")
lbl_Title.grid(column = 0, row = 0)

lbl_k = Label(window, text = "Enter #means")
lbl_k.grid(column = 1, row = 0)

txt_k = Entry(window)
txt_k.grid(column = 2, row = 0)

lbl_csv = Label(window, text = "Paste CSV here")
lbl_csv.grid(column = 0, row = 1)

lbl_rand = Label(window, text = "Generate Random Values")
lbl_rand.grid(column = 1, row = 1)

lbl_dimension = Label(window, text="2-d Selected")
lbl_dimension.grid(column = 2, row = 1)



csvBox = Text(window, width = 30)
csvBox.grid(column = 0, row = 2)

btn_csv = Button(window, text="Run Using CSV Values", command=execCSV)
btn_csv.grid(column = 0, row = 3)



lbl_numRand = Label(window, text = "Enter the number of random variables")
lbl_numRand.grid(column = 1, row = 1)

numRand = Entry(window)
numRand.grid(column = 1, row = 2)

btn_rand = Button(window, text="Run Using Random Values", command=execRand)
btn_rand.grid(column = 1, row = 3 )



btn_dimension = Button(window, text="Switch to 3-D Data", command=toggleDimension)
btn_dimension.grid(column = 2, row = 2)

lbl_timeTaken = Label(window, text = "Total time taken:")
lbl_timeTaken.grid(column = 1, row = 4)

window.mainloop()
