import streamlit as st  
  
# Load the HTML file  
with open('index.html', 'r') as f:  
    html = f.read()  
  
# Define the application's functionality  
def calculate_grades(*args):  

    # Get the values from the input fields  
    absences = st.session_state.absences  
    prelim = st.session_state.prelim  
    quizzes = st.session_state.quizzes  
    requirements = st.session_state.requirements  
    recitation = st.session_state.recitation  
    results = st.session_state.results  
  
    # Validate input values for prelim, quizzes, requirements, and recitation  
    if any(value < 0 or value > 100 for value in [prelim, quizzes, requirements, recitation]):  
        results = "Please input a valid numerical value, ranging from 0 to 100."  
        return  
  
    # Check for automatic fail due to absences  
    if absences >= 4:  
       results = "FAILED due to excessive absences."  
       return  
  
    # Calculate attendance grade  
    attendance = max(0, 100 - (absences * 10))  
  
    # Calculate class standing  
    class_standing = (0.4 * quizzes) + (0.3 * requirements) + (0.3 * recitation)  
  
    # Calculate prelim grade  
    prelim_grade = (0.6 * prelim) + (0.1 * attendance) + (0.3 * class_standing)  

    # Ensure prelim grade is within 0 to 100  
    prelim_grade = max(0, min(100, prelim_grade))  
    
    # Calculate required midterm and final grades for passing the subject and Dean's Lister  
    passing_grade = 75  
    deans_lister_grade = 90  
    
    # Calculate required midterm and final grades  
    midterm_weight = .3  
    final_weight = .5  
    remains_passing = passing_grade - (prelim_grade * .2)  
    required_passing = remains_passing / (midterm_weight + final_weight)  
  
    # Calculate required midterm and final grades to be a Dean's Lister  
    remains_dean = deans_lister_grade - (prelim_grade * .2)  
    required_dean = remains_dean / (midterm_weight + final_weight)  
  
    # Display results  
    message = f"Prelim Grade: {prelim_grade:.2f}<br>"  
    if prelim_grade >= 75:  
       message += f"Keep up the great work! You passed based on your Prelim grade!<br>"  
       message += f"To pass with 75%, you need to get at least {required_passing:.2f} in both your Midterm and Final grades.<br>"  
       message += f"To achieve 90%, you need to get at least {required_dean:.2f} in both your Midterm and Final grades."  

    results = message  
  
# Render the HTML file  
st.write(html)  
  
# Create input fields and store values in session state  
st.text_input("Absences", key="absences")  
st.text_input("Prelim", key="prelim")  
st.text_input("Quizzes", key="quizzes")  
st.text_input("Requirements", key="requirements")  
st.text_input("Recitation", key="recitation")  
  
# Bind the calculate_grades function to the button click event  
st.button("Calculate", on_click=calculate_grades)  
  
# Display results  
st.write(st.session_state.results)