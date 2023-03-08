import random
import tkinter as tk

def diagnose_symptoms(symptoms):
    """
    This function takes in a list of symptoms and returns a diagnosis
    based on those symptoms.
    """
    possible_diagnoses = ["Common cold", "Flu", "Strep throat", "Pneumonia"]
    return random.choice(possible_diagnoses)

def diagnose_symptoms_gui():
    """
    This function is called when the user clicks the "Diagnose" button.
    It gets the symptoms from the input box, diagnoses the condition based
    on those symptoms, and displays the diagnosis in the output box.
    """
    symptoms = input_box.get()
    symptoms = symptoms.split(",")
    diagnosis = diagnose_symptoms(symptoms)
    output_box.delete("1.0", tk.END)
    output_box.insert(tk.END, "Based on your symptoms, you may have: " + diagnosis)

# Create the tkinter window and widgets
window = tk.Tk()
window.title("Medical Help Tool")

input_label = tk.Label(window, text="Enter your symptoms (separated by commas):")
input_label.pack()

input_box = tk.Entry(window)
input_box.pack()

diagnose_button = tk.Button(window, text="Diagnose", command=diagnose_symptoms_gui)
diagnose_button.pack()

output_label = tk.Label(window, text="Diagnosis:")
output_label.pack()

output_box = tk.Text(window, height=5)
output_box.pack()

# Start the tkinter event loop
window.mainloop()
