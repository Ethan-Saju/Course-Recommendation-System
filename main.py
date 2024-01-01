import tkinter as tk
from tkinter import ttk
from course_rec import predictions

# Create the main application window
app = tk.Tk()
app.title("Course Recommendation System")
app.configure(bg='#2C3E50')  # Set background color to a dark color

# Function to generate course recommendation


def generate_course():
    user_name = name_var.get()
    user_education = education_var.get()
    user_year = year_var.get()
    selected_field = field_var.get()
    selected_interest = interest_var.get()

    # Call the predictions function from the model file
    recommended_course = predictions(selected_field, selected_interest)

    # Display the recommended course along with user information
    result_label.config(
        text=f" Recommended Course: {recommended_course}")


# Define fields, interests, education levels, and years
fields = ['Data Science', 'Internet of Things',
          'Artificial Intelligence', 'Electronics', 'Cyber Security']
interests = ['Art', 'Music', 'Biology', 'Graphic Design', 'Marketing']
education_levels = ['Undergraduate', 'Postgraduate']

# Create and place widgets with updated colors
name_label = ttk.Label(app, text="Your Name:",
                       background='#2C3E50', foreground='white')
name_var = ttk.Entry(app)

education_label = ttk.Label(
    app, text="Level of Education:", background='#2C3E50', foreground='white')
education_var = ttk.Combobox(app, values=education_levels)

year_label = ttk.Label(
    app, text="Year:", background='#2C3E50', foreground='white')
year_var = ttk.Combobox(app, values=[])

field_label = ttk.Label(app, text="Select Field:",
                        background='#2C3E50', foreground='white')
field_var = ttk.Combobox(app, values=fields)

interest_label = ttk.Label(
    app, text="Select Interest:", background='#2C3E50', foreground='white')
interest_var = ttk.Combobox(app, values=interests)

# Simplified button style
generate_button = ttk.Button(
    app, text="Generate Course", command=generate_course, style='TButton')

result_label = ttk.Label(app, text="Recommended Course: ",
                         background='#2C3E50', foreground='white')

# Grid layout
name_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
name_var.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

education_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
education_var.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

year_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")
year_var.grid(row=2, column=1, padx=10, pady=10, sticky="ew")

field_label.grid(row=3, column=0, padx=10, pady=10, sticky="w")
field_var.grid(row=3, column=1, padx=10, pady=10, sticky="ew")

interest_label.grid(row=4, column=0, padx=10, pady=10, sticky="w")
interest_var.grid(row=4, column=1, padx=10, pady=10, sticky="ew")

generate_button.grid(row=5, column=0, columnspan=2, pady=10)

result_label.grid(row=6, column=0, columnspan=2, pady=10)

# Function to update year options based on education level


def update_years(*args):
    selected_education = education_var.get()
    if selected_education == 'Undergraduate':
        year_var['values'] = ['1', '2', '3', '4']
    elif selected_education == 'Postgraduate':
        year_var['values'] = ['1', '2']


# Bind the function to the education level combobox
education_var.bind("<<ComboboxSelected>>", update_years)

# Run the application
app.mainloop()
