# -*- coding: utf-8 -*-
"""Startup_ideas_generator.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1vgTKRZWDOoUQjEKZPJHP-xeLUXbcnGtW
"""

# Import the variables from Airtable API. These variables can be changed using Airtable API(airtable.com).

import random
import requests
AIRTABLE_API_TOKEN = "keyAfRIvXfE2kcqVG"

r = requests.get(
    url = "https://api.airtable.com/v0/appR2n5AWjflxYA9g/Imported%20table",
    params = {
        "maxRecords": 100,
        "view": "Grid view",
    },
    headers = {
        "Authorization": f"Bearer {AIRTABLE_API_TOKEN}"
    }
)
response = r.json()

texts = {}
for record in response["records"]:
    texts[record['fields']['Key']] = record['fields']['Value']

# A class for generating ideas
class Ideas_generator:
    def __init__(self, quiz, shares, generate_business_ideas):
        self.quiz = quiz
        self.shares = shares
        self.generate_business_ideas = generate_business_ideas
    def result(self):
        return self.generate_business_ideas

# A function that finds out the purpose of user
def purpose():
    pur_count = 0
    while pur_count < 1:
        purpose = input(texts['purpose_input']).lower()
        if purpose == texts['purpose_answer_1']:
            pur_count += 1
            purpose_file = open(texts['file_for_purpose'], "w")
            purpose_file.write(purpose)
            purpose_file.close()
            return purpose
        elif purpose == texts['purpose_answer_2']:
            pur_count += 1
            purpose_file = open(texts['file_for_purpose'], "w")
            purpose_file.write(purpose)
            purpose_file.close()
            
            new_file = open(texts['file_for_assistance'], "w")
            new_file.write(texts['negative_answer_to_assistance'])
            new_file.close()
            return purpose
        else:
            print(texts['print_else_purpose']) 

# A function to find out if the user need some assistance
def assistance(purpose):
    ass_count = 0
    while ass_count < 1:
        if purpose == texts['purpose_answer_1']:
            assistance = input(texts['assistance_input']).lower()
            if assistance == texts['assistance_return_if_1']:
                ass_count += 1
                new_file = open(texts['file_for_assist_record'], "w")
                new_file.write(assistance)
                new_file.close()
                return texts['assistance_return_after_1']
            elif assistance == texts['assistance_return_if_2']:
                ass_count += 1
                print(texts['assistance_print_after_2'])
                new_file = open(texts['file_for_assist_record'], "w")
                new_file.write(assistance)
                new_file.close()
                return texts['assistance_return_after_2']
            else:
                print(texts['assistance_else_check'])
        else:
            ass_count += 1
            return texts['assistance_if_purpose_answer_2']
    
# A funtion that opens the file for further usage depending on the purspose of the user
def purpose_result():
    read_file = open(texts['file_for_purpose'], "r")
    info_from_file = read_file.readline().strip()
    read_file.close()
    return info_from_file

# A funtion that opens the file for further usage depending if the assistance is needed
def assistance_needed():
    read_file = open(texts['file_for_assist_record'], "r")
    info_from_file = read_file.readline().strip()
    read_file.close()
    return info_from_file

# A function that interacts further with the user, and gives him possibility to get some support for his business if he wins the quiz
def quiz(assistance, assistance_needed):
    if assistance_needed == texts['assistance_return_if_1']:
        quit = ""
        while quit != texts['quiz_answer_2']:
            quiz = input(texts['quiz_input']).lower()
            if quiz == texts['quiz_answer_1']:
                count = 0
                gues_1 = 0
                gues_2 = 0
                gues_3 = 0
                while gues_1 < 3:
                    question_1 = input(texts['quiz_question_1_input_1_1'] + str(3-gues_1) + texts['quiz_question_1_input_1_2'])
                    if question_1 == texts['quiz_question_1_right_answer']:
                        print(texts['quiz_q_1_print_1_1'] + str(question_1) + texts['quiz_q_1_print_1_2'])
                        gues_1 +=1
                        count+=1
                        break
                    elif question_1 != texts['quiz_question_1_right_answer']:
                        print(str(question_1) +texts['quiz_q_1_print_2'])
                        gues_1 += 1
                while gues_2 < 3:
                    question_2 = input(texts['quiz_question_2_input_1_1']
                                       + str(3-gues_2) + texts['quiz_question_2_input_1_2']).lower()
                    if question_2 == texts['quiz_question_2_right_answer']:
                        print(texts['quiz_q_2_print_1_1'] + str(question_2) + texts['quiz_q_2_print_1_2'])
                        gues_2 +=1
                        count+=1
                        break
                    elif question_2 != texts['quiz_question_2_right_answer']:
                        print(str(question_2) +texts['quiz_q_2_print_2'])
                        gues_2 += 1
                while gues_3 < 3:
                    question_3 = input(texts['quiz_question_3_input_1_1'] + str(3-gues_3) + texts['quiz_question_3_input_1_2']).lower()
                    if question_3 == texts['quiz_question_3_right_answer']:
                        print(texts['quiz_q_3_print_1_1'] + str(question_3) + texts['quiz_q_3_print_1_2'])
                        gues_3 +=1
                        count+=1
                        break
                    elif question_3 != texts['quiz_question_3_right_answer']:
                        print(str(question_3) +texts['quiz_q_3_print_2'])
                        gues_3 += 1
                if count >= 2:
                    return texts['quiz_return_correct']
                else:
                    return texts['quiz_return_else_correct']
            elif quiz == texts['quiz_answer_2']:
                return texts['quiz_return_if_quiz_answer_2']
            else:
                print(texts['quiz_print_to_check'])
    elif assistance_needed == texts['assistance_return_if_2']:
        return texts['quiz_return_if_assistance_return_if_2']
    else:
        pass

# A funtion that finds out if the user wants further help to develop on the idea he will choose
def shares(purpose_result):
    if purpose_result == texts['purpose_answer_2']:
        return texts['shares_return_if_purpose_answer_2']
    elif purpose_result == texts['purpose_answer_1']:
        shares = ""
        while shares != texts['shares_input_answer_2']:
            shares = input(texts['shares_input_1']).lower()
            if shares == texts['shares_input_answer_1']:
                return texts['shares_return_if_shares_input_answer_1']
            elif shares == texts['shares_input_answer_2']:
                return texts['shares_return_if_shares_input_answer_2']
            else:
                print(texts['shares_print_to_check'])
    else:
        pass

# A function that takes random ideas from imported files and suggest to the user
def generate_business_ideas(purpose_result):
    ideas_dictionary_b = {}
    selected_ideas_b_art = []
    selected_ideas_b_it = []
    selected_ideas_b_automotive = []
    selected_ideas_b_business_and_consumer_service = []
    selected_ideas_b_consulting_services = []
    selected_ideas_b_entertainment = []
    
    quit = 0
    all_ideas = [texts['idea_1'], texts['idea_2'], texts['idea_3'], texts['idea_4'],
                    texts['idea_5'], texts['idea_6']]
    if purpose_result == texts['purpose_answer_1']:
        while quit < 1:
            topic = input(texts['gen_b_ideas_topic_input_1']).lower()
            if topic in all_ideas:
                idea = random.choice(open(topic.capitalize()+'.txt').read().splitlines())
                print(texts['gen_b_ideas_print_1'], idea)
                if topic == all_ideas[0]:
                    selected_ideas_b_art.append(idea)
                    ideas_dictionary_b[topic] = selected_ideas_b_art
                elif topic == all_ideas[1]:
                    selected_ideas_b_it.append(idea)
                    ideas_dictionary_b[topic] = selected_ideas_b_it
                elif topic == all_ideas[2]:
                    selected_ideas_b_automotive.append(idea)
                    ideas_dictionary_b[topic] = selected_ideas_b_automotive    
                elif topic == all_ideas[3]:
                    selected_ideas_b_business_and_consumer_service.append(idea)
                    ideas_dictionary_b[topic] = selected_ideas_b_business_and_consumer_service
                elif topic == all_ideas[4]:
                    selected_ideas_b_consulting_services.append(idea)
                    ideas_dictionary_b[topic] = selected_ideas_b_consulting_services
                elif topic == all_ideas[5]:
                    selected_ideas_b_entertainment.append(idea)
                    ideas_dictionary_b[topic] = selected_ideas_b_entertainment
                another_trial = input(texts['gen_b_ideas_input_1_2nd_trial_input'])
                if another_trial == texts['gen_b_ideas_input_1_2nd_trial_answer_1']:
                    pass
                elif another_trial == texts['gen_b_ideas_input_1_2nd_trial_answer_2']:
                    quit += 1
                else:
                    pass
            elif topic == texts['gen_b_ideas_topic_input_1_answer']:
                quit += 1
            else:
                pass
    elif purpose_result == texts['purpose_answer_2']:
        while quit < 1:
                topic = input(texts['gen_b_ideas_topic_input_2']).lower()
                if topic == texts['gen_b_ideas_topic_input_2_answer_1'] or topic == texts['gen_b_ideas_topic_input_2_answer_2']:
                    idea = random.choice(open(topic.capitalize()+'.txt').read().splitlines())
                    print(texts['gen_b_ideas_print_2'], idea)
                    if topic == all_ideas[0]:
                        selected_ideas_b_art.append(idea)
                        ideas_dictionary_b[topic] = selected_ideas_b_art
                    elif topic == all_ideas[5]:
                        selected_ideas_b_entertainment.append(idea)
                        ideas_dictionary_b[topic] = selected_ideas_b_entertainment
                    another_trial_b = input(texts['gen_b_ideas_input_2_2nd_trial_input'])
                    if another_trial_b == texts['gen_b_ideas_input_2_2nd_trial_answer_1']:
                        pass
                    elif another_trial_b == texts['gen_b_ideas_input_2_2nd_trial_answer_2']:
                        quit += 1
                    else:
                        pass
                elif topic == texts['gen_b_ideas_topic_input_2_answer']:
                    quit += 1
                else:
                    pass                
    else:
        pass
    print(texts['gen_b_ideas_final_print'])
    return ideas_dictionary_b

result_1 = Ideas_generator(quiz(assistance(purpose()), assistance_needed()), shares(purpose_result()), generate_business_ideas(purpose_result()))

# Returns the list of selected business topics and generated ideas for the user
print(result_1.result())