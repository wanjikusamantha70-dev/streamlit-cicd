import streamlit as st
from calculator import calculate_score, get_result

st.set_page_config(
    page_title = 'Student Performance Predictor',
    page_icon = '🎓'
)

st.title('🎓 Student Performance Predictor')

st.write('Enter the student\'s information below to calculate their performance.')

student_name = st.text_input('Student Name')

study_hours = st.number_input(
    'Study hours per day',
    min_value = 0.0,
    max_value = 10.0,
    value = 8.0
)

attendance = st.number_input(
    'Attendance (in percentage)',
    min_value = 0.0,
    max_value =100.0,
    value = 50.0
)

assignment_score =st.number_input(
    'Assignment score (in percentage)',
    min_value = 0.0,
    max_value = 100.0,
    value = 50.0
)

if st.button('Calculate Performance'):
    if student_name == '':
        st.warning('Please enter the student\'s name.')
    else:
        score = calculate_score(study_hours, attendance, assignment_score)
        result = get_result(score)

        st.subheader(f'Results for {student_name}')
        st.metric (
            'Performance Score',
            f'{score}%'
        )

        if result == 'PASS':
            st.success('PASS 🎉')
        else:
            st.warning('FAIL 😞')

    