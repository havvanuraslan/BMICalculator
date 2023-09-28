from tkinter import *

#window
window = Tk()
window.title("BMI Calculator")
window.minsize(width=300, height=300)


weight_label = Label(text="Enter Your Weight(kg)", fg="black", padx=10, pady=10)
weight_label.pack()
weight_entry = Entry(width=20)
weight_entry.pack()
height_label = Label(text="Enter Your Height(cm)", fg="black", padx=10, pady=10)
height_label.pack()
height_entry = Entry(width=20)
height_entry.pack()

def calculate_bmi():
    user_weight = weight_entry.get()
    user_height = height_entry.get()
    if user_height == "" or user_weight == "":
        result_label.config(text="Please enter weight and height!")
    else:
        try:
            user_bmi = float(user_weight)/(float(user_height)/100) ** 2
            if user_bmi < 16:
                result_label.config(text=f"your bmi: {round(user_bmi, 2)}. You are severely thin")
            elif 16 <= user_bmi < 17:
                result_label.config(text=f"your bmi: {round(user_bmi, 2)}. You are moderately thin")
            elif 17 <= user_bmi < 18.5:
                result_label.config(text=f"your bmi: {round(user_bmi, 2)}. You are mild thin")
            elif 18.5 <= user_bmi < 25:
                result_label.config(text=f"your bmi: {round(user_bmi, 2)}. You are normal")
            elif 25 <= user_bmi < 30:
                result_label.config(text=f"your bmi: {round(user_bmi, 2)}. You are overweight")
            elif 30 <= user_bmi < 35:
                result_label.config(text=f"your bmi: {round(user_bmi, 2)}. You are obese class I")
            elif 35 <= user_bmi < 40:
                result_label.config(text=f"your bmi: {round(user_bmi, 2)}. You are obese class II")
            elif user_bmi >= 40:
                result_label.config(text=f"your bmi: {round(user_bmi, 2)}. You are obese class III")
        except:
            result_label.config(text="Please enter a valid number!")


calculate_button = Button(text="calculate", command=calculate_bmi, padx=10)
calculate_button.pack()

result_label = Label(padx=10, pady=10)
result_label.pack()

window.mainloop()