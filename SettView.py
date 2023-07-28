import tkinter as tk
from tkinter import simpledialog, messagebox
from datetime import datetime, timedelta
#import ExcelData
from ExcelData import ExcelData
import openpyxl
from tkinter import Entry, ttk
import tkinter as tk
from ttkbootstrap import Style
from tkcalendar import DateEntry
from ttkbootstrap.constants import *
from ttkbootstrap.constants import *

class SettView:
    def __init__(self, root):
        self.root = root
        self.fixedSize(self.root) #Fixed size
        self.disableResizing(self.root) #Disable resizing

        self.finalCabDetailsLst=[]

        countRow=0

        big_font = ("Helvetica", 20)

        self.no_of_days_stay = tk.Label(self.root, text="Easy Settlement", font=big_font,fg="white", bg="blue")
        # Use grid to place the counter_label
        self.no_of_days_stay.grid(row=countRow, column=0, padx=20,pady=20)

        countRow+=1        

        self.no_of_days_stay = tk.Label(self.root, text="Sttarting date: (Ex..'2023-07-26')", font=("Lucida Grande", 18))
        # Use grid to place the counter_label
        self.no_of_days_stay.grid(row=countRow, column=0, padx=20,pady=20)

        countRow+=1
        
        # Create a Text widget
        #self.date_entry = tk.Text(self.root, height=30, width=50, wrap="word")

        self.date_entry = tk.Entry(self.root)
        self.date_entry.grid(row=countRow, column=0, padx=20,pady=20)
        #date_entry.pack(padx=10, pady=10)

        countRow+=1

        self.no_of_days_stay = tk.Label(self.root, text="No Of Days", font=("Lucida Grande", 18))
        # Use grid to place the counter_label
        self.no_of_days_stay.grid(row=countRow, column=0, padx=20,pady=20)

        countRow+=1


        # Define the list of options for the dropdown (1 to 20)
        self.options = list(range(1, 101))

        self.days_dropdown = ttk.Combobox(root, values=self.options,state="readonly")
        self.days_dropdown.grid(row=countRow, column=0, padx=20,pady=20)
        # Set a default value for the dropdown
        self.days_dropdown.set("Select")
        #click anywhere to get dropdown
        self.days_dropdown.bind("<1>", self.open_dropdown)

        countRow+=1

        # Create a Beautify button
        self.typeit_button = ttk.Button(self.root, text="Start Cab!", command=self.cabSettlementFromTo)
        self.typeit_button.grid(row=countRow, column=0)
        #submit_button.pack()

        countRow+=1

        #Close button
        self.close_btn_frame = ttk.Frame(self.root, width=200, height=100, borderwidth=1, padding=10)
        self.close_btn_frame.grid(row=countRow, column=0)


        self.close_btn = ttk.Button(self.close_btn_frame, text="Close It", style='Warning-outline.TButton', command=lambda: self.closeIt(self.root))
        self.close_btn.grid(row=countRow, column=0)
        
        



    def disableResizing(self,rootRef):
        rootRef.resizable(False, False)

    def closeIt(self,rootRef):
        rootRef.destroy()

    def open_dropdown(self, event):
        self.days_dropdown.focus_set()  # Set focus on the combobox to open the dropdown

    def fixedSize(self,rootRef):
        window_width = 375
        window_height = 450
        #rootRef.geometry(f"{window_width}x{window_height}")
        self.center_windowOrg(rootRef,window_width,window_height)


    def center_windowMod(rootRef):
        rootRef.update_idletasks()
        screen_width = rootRef.winfo_screenwidth()
        screen_height = rootRef.winfo_screenheight()
        window_width = rootRef.winfo_width()
        window_height = rootRef.winfo_height()
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        rootRef.geometry(f"+{x}+{y}")

    def center_windowOrg(self,rootRef, width, height):
        # Get the screen width and height
        screen_width = rootRef.winfo_screenwidth()
        screen_height = rootRef.winfo_screenheight()

        # Calculate the x and y position to center the window
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2

        # Set the window's position
        rootRef.geometry(f"{width}x{height}+{x}+{y}")

    def center_windowUpd(self,rootRef, width, height):
        rootRef.update_idletasks()
        # Get the screen width and height
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        window_width = rootRef.winfo_width()
        window_height = rootRef.winfo_height()

        # Calculate the x and y position to center the window
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2

        # Set the window's position
        rootRef.geometry(f"{width}x{height}+{x}+{y}")

    
    def cabSettlementFromTo(self):
        start_date = '2023-07-26'
        #start_date = self.date_entry.get(1.0, tk.END)
        if len(start_date)<=0:
            start_date = '2023-07-26'
        #noOfDaysStay = 1
        noOfDaysStay = self.days_dropdown.get()
        self.date_plus_100_days(start_date,int(noOfDaysStay))

    

    def date_plus_100_days(self,start_date,no_of_days):
        #start_date_str = '2023-07-26'
        # Convert the input string to a datetime object
        start_date = datetime.strptime(start_date, '%Y-%m-%d')
        
        # Calculate the end date by adding 100 days
        end_date = start_date + timedelta(days=no_of_days)
        # Create a loop to iterate from start_date to end_date
        current_date = start_date
        morning = True
        while current_date <= end_date:
            proceedWithDate = current_date.strftime('%Y-%m-%d')
            #print(current_date.strftime('%Y-%m-%d'))
            #if window destroy only then call
            for i in range(2):
                self.used_cab_yes_no(proceedWithDate,morning)
                morning = not morning
            #book_ride_window.wait_window(book_ride_window)
            
            current_date += timedelta(days=1)

        #print(self.finalCabDetailsLst)
        if(len(self.finalCabDetailsLst)>0):
            self.generate_excel(self.finalCabDetailsLst)

    

    def generate_excel(self, excelDataLst):

        dataofAllRow = []

        for i in range(len(excelDataLst)):
            dataOfRow = []
            print(excelDataLst[i].date)
            dataOfRow.append(excelDataLst[i].date)
            print(excelDataLst[i].booked)
            dataOfRow.append(excelDataLst[i].booked)
            print(excelDataLst[i].price)
            dataOfRow.append(excelDataLst[i].price)
            print(excelDataLst[i].hotelOffice)
            dataOfRow.append(excelDataLst[i].hotelOffice)

            dataofAllRow.append(dataOfRow)

        #self.saveExcel(dataofAllRow)
        

        

    def saveExcel(self,dataofAllRow):
        workbook = openpyxl.Workbook()
        sheet = workbook.active

        # Add headers to the sheet
        sheet.append(['Date',"Hotel or Office" ,'Booked', 'Price'])

        # Add sample data rows
        #data = [
         #   ['Alice', 30, 50000.0],
          #  ['Bob', 25, 60000.0],
           # ['Charlie', 35, 55000.0]
        #]

        for row in dataofAllRow:
            sheet.append(row)

        # Save the workbook to a file
        workbook.save('FinalExcel.xlsx')
        print("Excel file generated successfully!")



    def used_cab_yes_no(self,bookDate,morning):
        # Create a new window using Toplevel
        book_ride_window = tk.Toplevel(self.root)
        book_ride_window.title("Cab Book")

        # Set the window size and position
        self.center_windowOrg(book_ride_window,350,250)
        #book_ride_window.geometry("300x200+200+200")

        #book_ride_window.attributes('-alpha', 0.5)
        #book_ride_window.attributes('-fullscreen', True)
        #book_ride_window.attributes('-topmost', True)

        morEven = "Morning" if morning else "Evening"
        hotelOrOffice = "Hotel to Office" if morning else "Office to Hotel"
        # Add a label to the new window
        book_ride_check_label = tk.Label(book_ride_window, text="Booked ride on : "+bookDate+"\n"+morEven,)
        book_ride_check_label.grid(row=0, column=0, padx=20,pady=20)
        #label.pack(pady=10)
            

        # Function to handle the Yes button
        def on_yes():
            # Ask the user to enter their name
            user_name = simpledialog.askstring("Cab Ride Yes", "Please enter amount")
            if user_name:
                message = f"You chose Yes, {user_name}!"
                #self.finalCabDetailsLst.append(int(user_name))
                row = ExcelData(bookDate,"YES",int(user_name),hotelOrOffice)
                self.finalCabDetailsLst.append(row)
                #print(row.date)
                #messagebox.showinfo("Result", message)
            else:
                msg="You choose yes"
                #self.finalCabDetailsLst.append(0)
                #messagebox.showinfo("Result", "You chose Yes!")
                row = ExcelData(bookDate,"NO",0,hotelOrOffice)
                self.finalCabDetailsLst.append(row)
            book_ride_window.destroy()

        # Function to handle the No button
        def on_no():
            msg="You choose no"
            #self.finalCabDetailsLst.append(0)
            row = ExcelData(bookDate,"NO",0,hotelOrOffice)
            self.finalCabDetailsLst.append(row)
            #messagebox.showinfo("Result", "You chose No!")
            book_ride_window.destroy()


        

        # Align the button to the left
        yes_button = tk.Button(book_ride_window, text="Yes", command=on_yes)
        yes_button.grid(row=1, column=0, padx=20, pady=20, sticky="w")

        # Align the button to the right
        no_button = tk.Button(book_ride_window, text="No", command=on_no)
        no_button.grid(row=1, column=1, padx=20, pady=20, sticky="e")

        # Add Yes and No buttons to the new window
        #yes_button = tk.Button(book_ride_window, text="Yes", command=on_yes)
        #yes_button = tk.Button(dialog_window, text="Yes")
        #yes_button.pack(side=tk.LEFT, padx=10)

        #no_button = tk.Button(book_ride_window, text="No", command=on_no)
        #no_button = tk.Button(dialog_window, text="No")
        #no_button.pack(side=tk.RIGHT, padx=10)

        book_ride_window.wait_window(book_ride_window)
        

        

'''



        # Create a custom style for the green button
        book_ride_window.tk.call('source', 'lightthemes.tcl')
        book_ride_window.tk.call('set_theme', 'dark')
        book_ride_window.tk.call('ttk::style', 'theme', 'use', 'light')
        new_style = ttk.Style(book_ride_window)
        new_style.configure('Green.TButton', foreground='white', background='green')


        # Create a custom style for the red button
        book_ride_window.tk.call('source', 'darkthemes.tcl')
        book_ride_window.tk.call('set_theme', 'light')
        book_ride_window.tk.call('ttk::style', 'theme', 'use', 'dark')
        new_style = ttk.Style(book_ride_window)
        new_style.configure('Red.TButton', foreground='white', background='red')




'''
