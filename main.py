import random
import time

import joblib
import numpy as np
import pandas as pd
import streamlit as st
def home_page():
        st.title("Mental Health in Tech Industry")
        # Changing the color and background
        st.markdown(
            """
            <style>
            .stApp { background-color: #D8DDD1; }
            h1 { color: #61724E; }

            /* Transition effect on images */
            .image-transition {
                transition: transform 0.3s ease-in-out;
            }
            .image-transition:hover {
                transform: scale(1.1);
            }

            /* Hover effect on captions */
            .caption-hover:hover {
                color: #A0325B;
                font-weight: bold;
            }
            </style>
            """,
            unsafe_allow_html=True
        )
        st.markdown(
            """
            <style>
            .green-text {
                color: #747057;
                font-size: 35px;
            }
            </style>
            """,
            unsafe_allow_html=True,
        )

        st.markdown(
            '<h1 class="green-text">Experiencing persistent feeling of stress, anxiety, or burnout in your workplace? '
            'You came to the right place!</h1>', unsafe_allow_html=True)

        # Adding the first image with transition effect
        image_url1 = 'https://64.media.tumblr.com/54ff87419f2149658cf390d1a0aef6ad/866f6b593c84ef90-47/s2048x3072/2e41e0abbab39821fba0e29728af4972ba2f3a4d.pnj'
        st.markdown(
            f'<div style="display: flex; justify-content: center;"><div class="image-transition"><img src="{image_url1}" alt="Image normal brain and Alzheimer" style="max-width: 700px;"></div></div>',
            unsafe_allow_html=True)

        # Adding the first image with transition effect
        image_url1 = 'https://64.media.tumblr.com/61d2fcd47402a4547db13ba4de37307f/866f6b593c84ef90-e7/s2048x3072/da59b1c0f86371f0e12fe25274dede3bd5de5b8e.pnj'
        st.markdown(
            f'<div style="display: flex; justify-content: center;"><div class="image-transition"><img src="{image_url1}" alt="Image normal brain and Alzheimer" style="max-width: 700px;"></div></div>',
            unsafe_allow_html=True)

        # Adding the first image with transition effect
        image_url1 = 'https://64.media.tumblr.com/fdc71827a4097a6fa3c980d7eb9d67da/866f6b593c84ef90-44/s2048x3072/cbcf6bab14cc29798098a2e728953dda6fdeb726.pnj'
        st.markdown(
            f'<div style="display: flex; justify-content: center;"><div class="image-transition"><img src="{image_url1}" alt="Image normal brain and Alzheimer" style="max-width: 700px;"></div></div>',
            unsafe_allow_html=True)



        # Adding the second image in an expander
        with st.expander("Causes of Mental Health"):
            image_url2 = 'https://64.media.tumblr.com/ddc4552cb5a99034ca239c6602a6b38c/866f6b593c84ef90-24/s2048x3072/451f1c16bf5fe3e77415f8ba67d8d73310bdab16.pnj'
            st.image(image_url2, caption='')

        # Adding the third image in an expander
        with st.expander("Symptoms of Alzheimer"):
            image_url3 = 'https://64.media.tumblr.com/350fbdc722bf2548daccf0ac43e14aa3/2613e0dcfd360416-d7/s2048x3072/61bffa955936a27760b29a5ba21d307109847bec.pnj'
            st.image(image_url3, caption='')

        st.header("", anchor="center")
        st.write("<h1 style='text-align: center;'>Love yourself </h1>", unsafe_allow_html=True)
        # Creating a grid layout for the images
        col1, col2 = st.columns(2)

        # Adding the first image to the first column
        with col1:
                image_url4 = 'https://64.media.tumblr.com/70c3866391ca38839d5451100a5df701/2613e0dcfd360416-23/s2048x3072/8434113b1ed8fdebf004449c75e1214c7252d20d.pnj'
                st.image(image_url4, caption='')

        # Adding the second image to the second column
        with col2:
                image_url5 = 'https://64.media.tumblr.com/aa6964678de7718c73c258bda0e3a0ea/2613e0dcfd360416-f5/s2048x3072/1edaff2a052fc42bb651ebaad26b74e25131d0d8.pnj'
                st.image(image_url5, caption='')



def prediction_page():

        st.subheader('Take a Test, you might need some help!')
        st.markdown(
            """
            <style>
            .stApp { background-color: #D8DDD1; }
            h1 { color: #61724E; }
            </style>
            """,
            unsafe_allow_html=True
        )
        # show_form = st.button("Start the test!")
        # if show_form:
        columns = ['Age', 'Gender', 'Self_Employed',
                   'Family_History',
                   'Work_Interference', 'Employees_Num', 'Remote_Working',
                   'Technology_Company', 'Company_Benefits', 'Healthcare_Options',
                   'Wellness_Program', 'Resources', 'Anonymity', 'Medical_Leave',
                   'Mental_Consequence', 'Physical_Consequence', 'Discuss_Coworkers',
                   'Discuss_Supervisor', 'Mental_Interview', 'Physical_Interview',
                   'Mental_VS_Physical', 'Observed_Consequence']
        df = pd.DataFrame(index=range(1), columns=columns)

        with st.form("Form"):

            df['Age'] = st.number_input('How old are you?', step=1.0, format='%.0f', min_value=15.0, max_value=100.0)
            df['Gender'] = st.selectbox('What is your gender?', ['Female', 'Male', 'Others'])
            df['Self_Employed'] = st.selectbox('Are you self-employed?', ['Yes', 'No'])
            df['Family_History'] = st.selectbox('Do your family members have mental illness history?', ['No', 'Yes'])
            df['Work_Interference'] = st.select_slider('If you have a mental health condition, do you feel '
                                                       'that it interferes with your work?',
                                                       options=['Never', 'Rarely', 'Sometimes', 'Often'])
            df['Employees_Num'] = st.select_slider('How may employees does your company/organisation have?',
                                                   ['1-5', '6-25', '26-100', '100-500', '500-1000', 'More than 1000'])
            df['Remote_Working'] = st.selectbox('Are you working remotely? (At least 50% of the time)', ['No', 'Yes'])
            df['Technology_Company'] = st.selectbox('Is your employer primarily a tech company/organisation',
                                                    ['No', 'Yes'])
            df['Company_Benefits'] = st.selectbox('Does your employer provide mental health benefits?',
                                                  ['No', 'Yes', 'Don\'t know'])
            df['Healthcare_Options'] = st.selectbox('Do you know the options for mental health care your employer '
                                                    'provides?', ['No', 'Yes', 'Not Sure'])
            df['Wellness_Program'] = st.selectbox('Has your employer ever discussed mental health as part of '
                                                  'an employee wellness program?', ['No', 'Yes', 'Don\'t know'])
            df['Resources'] = st.selectbox('Does your employer provide resources to learn more about mental health '
                                           'issues and how to seek help?', ['No', 'Yes', 'Don\'t know'])
            df['Anonymity'] = st.selectbox('Is your anonymity protected if you choose to take advantage of mental '
                                           'health or substance abuse treatment resources?',
                                           ['No', 'Yes', 'Don\'t know'])
            df['Medical_Leave'] = st.select_slider('How easy is it for you to take medical leave for a mental health '
                                                   'condition?', options=['Very Easy', 'Somewhat Easy', 'Don\'t Know',
                                                                          'Somewhat Difficult', 'Very Difficult'])
            df['Mental_Consequence'] = st.selectbox('Do you think that discussing a mental health issue with your '
                                                    'employer would have negative consequences?',
                                                    ['No', 'Yes', 'Maybe'])
            df['Physical_Consequence'] = st.selectbox('Do you think that discussing a physical health issue with your '
                                                      'employer would have negative consequences?', ['No', 'Yes',
                                                                                                     'Maybe'])
            df['Discuss_Coworkers'] = st.selectbox('Would you be willing to discuss a mental health issue with your '
                                                   'coworkers?', ['No', 'Yes', 'Some of them'])
            df['Discuss_Supervisor'] = st.selectbox('Would you be willing to discuss a mental health issue with your '
                                                    'direct supervisor(s)?', ['No', 'Yes', 'Some of them'])
            df['Mental_Interview'] = st.selectbox('Would you bring up a mental health issue with a potential employer '
                                                  'in an interview?', ['No', 'Yes', 'Maybe'])
            df['Physical_Interview'] = st.selectbox('Would you bring up a physical health issue with a potential '
                                                    'employer in an interview?', ['No', 'Yes', 'Maybe'])
            df['Mental_VS_Physical'] = st.selectbox('Do you feel that your employer takes mental health as seriously '
                                                    'as physical health?', ['No', 'Yes', 'Don\'t Know'])
            df['Observed_Consequence'] = st.selectbox('Have you heard of or observed negative consequences for '
                                                      'coworkers with mental health conditions in your workplace?',
                                                      ['No', 'Yes'])

            submit_button = st.form_submit_button("Submit")

            if submit_button:
                test = pd.read_csv('C:\\Users\\ANISMUNIRAH\\PycharmProjects\\MentalHealth\\venv\\mental_health_in_tech-main\\output.csv')
                test = test.loc[:, test.columns != 'Seek_Treatment']
                test.loc[len(test)] = df.loc[0]

                model = joblib.load('C:\\Users\\ANISMUNIRAH\\PycharmProjects\\MentalHealth\\venv\\mental_health_in_tech-main\\model1.pkl')
                scaler = joblib.load('C:\\Users\\ANISMUNIRAH\\PycharmProjects\\MentalHealth\\venv\\mental_health_in_tech-main\\scaler1.pkl')

                for column in test.columns:
                    if column == 'Age' or column == 'Seek_Treatment':
                        continue
                    else:
                        encoder = joblib.load('C:\\Users\\ANISMUNIRAH\\PycharmProjects\\MentalHealth\\venv\\mental_health_in_tech-main\\'f'{column}_encoder.pkl')
                        test[column] = encoder.fit_transform(test[column])

                test[['Age']] = scaler.transform(test[['Age']])
                user_input = np.array([test.loc[len(test) - 1]])
                # st.write(user_input)

                proba = model.predict_proba(user_input)
                prediction = model.predict(user_input)
                probability = proba[0, 1]
                progress = 0
                st.success("Form Submitted")
                progress_text = st.empty()
                progress_container = st.empty()
                while progress <= probability * 100:
                    time.sleep(0.008)
                    progress += 1
                    progress_container.progress(progress)
                    progress_text.subheader(f"Probability: {progress:.2f} %")
                progress_text.subheader(f"Probability: {probability * 100:.2f} %")

                if prediction < 0.25:
                    msgs = ["It seems like you're currently in a good mental state and managing well. Continue to "
                            "prioritize self-care and maintain healthy habits to support your overall well-being.",
                            "Your mental well-being appears to be strong, but remember to seek support if you ever "
                            "feel overwhelmed or need someone to talk to."]
                    rand = random.randint(0, 1)
                    msg = msgs[rand]
                elif prediction < 0.5:
                    msgs = ["If you're experiencing occasional or mild symptoms that don't significantly impact "
                            "your daily life, self-care practices and seeking support from friends or loved ones "
                            "may be helpful.",
                            "While you might not require immediate treatment, it could be beneficial to monitor "
                            "your symptoms and consider seeking professional help if they worsen or persist."]
                    rand = random.randint(0, 1)
                    msg = msgs[rand]
                elif prediction < 0.75:
                    msgs = ["If you're finding that your symptoms are significantly affecting your daily life, "
                            "relationships, or work, it's important to reach out to a mental health professional "
                            "for a comprehensive assessment.",
                            "A mental health provider can help identify the underlying causes of your concerns and "
                            "develop a tailored treatment plan to address them effectively.",
                            "Seeking support from a mental health professional is a courageous step towards "
                            "improving your well-being. They have the expertise to guide you through this process."]
                    rand = random.randint(0, 2)
                    msg = msgs[rand]
                else:
                    msgs = ["I'm really concerned about what you're experiencing. It's crucial to seek immediate help "
                            "from a mental health professional or a local crisis hotline. They can provide the "
                            "support you need during this difficult time.",
                            "If you're in a crisis or feel like you're in immediate danger, please don't hesitate "
                            "to contact emergency services or go to the nearest emergency room. They are equipped "
                            "to handle urgent mental health situations.",
                            "Your safety and well-being are of utmost importance. Please reach out to a mental "
                            "health professional or a helpline right away. They are trained to provide the "
                            "assistance you need in this critical situation."]
                    rand = random.randint(0, 2)
                    msg = msgs[rand]

                st.write('You are fine!' if prediction < 0.5 else 'You need some treatment.')
                st.write(msg)


def prevention_page():
    st.title("Prevention is Better Than Cure")
    st.markdown(
        """
        <style>
        .stApp { background-color: #D8DDD1; }
        h1 { color: #61724E; }
        </style>
        """,
        unsafe_allow_html=True
    )
    st.caption(
        "<p style='font-size: 20px; text-align: center; font-style: italic;'>When it comes to health, prevention is better than a cure. The concept of proactive awareness and preventative interventions being more "
        "effective than later remedial action has never been more relevant in mental health.</p>", unsafe_allow_html=True)

    # Adding the first image
    image_url1 ='https://64.media.tumblr.com/58dfb5b23a9c547975f1043aae6717da/2613e0dcfd360416-92/s2048x3072/cc9c5913aec2eab4bb9869d95c9e33b0c946147d.pnj'
    st.markdown(f'<div style="display: flex; justify-content: center;"><div class="image-transition"><img src="{image_url1}" alt="" style="max-width: 650px;"></div></div>', unsafe_allow_html=True)

    # Adding the first image
    image_url1 = 'https://64.media.tumblr.com/25f771269a6a9f9e0e532db9309a7f42/2613e0dcfd360416-1a/s2048x3072/14bf1236c4a3d28e3a48321885c818044801293e.pnj'
    st.markdown(
        f'<div style="display: flex; justify-content: center;"><div class="image-transition"><img src="{image_url1}" alt="" style="max-width: 650px;"></div></div>',
        unsafe_allow_html=True)


def aboutus_page():
    st.markdown(
        """
        <style>
        .centered {
            display: flex;
            justify-content: center;
        }
        .stApp {
            background-color: #D8DDD1;
        }
        h1 {
            color: #61724E;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.markdown('<div class="centered"><h1>Get To Know the Masterminds</h1></div>', unsafe_allow_html=True)
    # Adding the first image
    image_url1 = 'https://64.media.tumblr.com/850c77a6bfc13ebc3131c08a5fdc9c76/4f3fd61635fc6764-11/s640x960/bffe6ac496b5fcb88333128d30ff4ebd6dbf8ebc.pnj'
    st.markdown(
        f'<div style="display: flex; justify-content: center;"><div class="image-transition"><img src="{image_url1}" alt="" style="max-width: 700px;"></div></div>',
        unsafe_allow_html=True)

    st.header("", anchor="center")
    # st.write("<h1 style='text-align: center;'>To contact us: </h1>", unsafe_allow_html=True)

    image_url1 = 'https://64.media.tumblr.com/a711134014bcd77d604895dd61499aae/e921d5f88410c82e-72/s1280x1920/5ce38dcda678d2c1c7de1ec013c6eab25eccfb74.pnj'
    st.markdown(
        f'<div style="display: flex; justify-content: center;"><div class="image-transition"><img src="{image_url1}" alt="" style="max-width: 300px;"></div></div>',
        unsafe_allow_html=True)



def main():
    st.markdown(
        """
        <style>
        .navbar .radio { 
            display: flex; 
            justify-content: center; 
            align-items: center; 
            background-color: #A0325B; 
            color: white; 
            padding: 8px 16px; 
            border-radius: 8px; 
            cursor: pointer; 
            margin-bottom: 16px; 
            font-size: 18px; 
            font-weight: bold;
            border: none;
            outline: none;
            transition: background-color 0.3s;
        }
        .navbar .radio:hover {
            background-color: #801A41;
        }
        .navbar .radio:checked {
            background-color: #801A41;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.sidebar.markdown(
        """
        <style>
        .sidebar .radio { 
            display: flex; 
            justify-content: center; 
            align-items: center; 
            background-color: #A0325B; 
            color: white; 
            padding: 8px 16px; 
            border-radius: 8px; 
            cursor: pointer; 
            margin-bottom: 16px; 
            font-size: 18px; 
            font-weight: bold;
            border: none;
            outline: none;
            transition: background-color 0.3s;
        }
        .sidebar .radio:hover {
            background-color: #801A41;
        }
        .sidebar .radio:checked {
            background-color: #801A41;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    tabs = ["Home", "Test", "Prevention","About Us"]
    selected_tab = st.sidebar.selectbox("Navigation", tabs, index=0, key="navigation")

    if selected_tab == "Home":
        home_page()
    elif selected_tab == "Test":
        prediction_page()
    elif selected_tab == "Prevention":
        prevention_page()
    elif selected_tab == "About Us":
        aboutus_page()


if '__main__' == __name__:
    main()

