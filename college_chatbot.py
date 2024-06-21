def chatbot_response(user_input):
    user_input = user_input.lower()
    
    if "hello" in user_input or "hi" in user_input:
        return ("Hello! Welcome to Our College Info Bot. How can I assist you today?")
    elif "admission" in user_input or "apply" in user_input:
        return ("To apply to our college admission, please visit the admissions page on our college website. "
                "You can find information about the application process, required documents, and deadlines."
                "For More details ask about the departments as engineering, medical, arts, science.")
    elif "courses" in user_input or "programs" in user_input:
        return ("We offer a variety of undergraduate and postgraduate programs. "
                "Please specify if you're interested in a particular field or level of study."
                "For More details ask about the departments as engineering, medical, arts, science.")
    elif "campus life" in user_input or "facilities" in user_input:
        return ("Our campus offers state-of-the-art facilities including libraries, sports complexes, and student housing. "
                "We also have numerous clubs and organizations you can join.")
    elif "contact" in user_input or "reach" in user_input:
        return ("You can contact us via email at info@chettinad.edu or call us at (+91)  936-091-6784. "
                "Our office hours are Monday to Friday, 9 AM to 5 PM.")
    elif "scholarship" in user_input or "financial aid" in user_input:
        return ("We offer various scholarships and financial aid options for eligible students. "
                "Please visit our scholarships page for more information on how to apply.")
    elif "events" in user_input or "activities" in user_input:
        return ("Our university hosts a wide range of events throughout the year, including cultural festivals, academic conferences, "
                "and sports tournaments. Check our events calendar on the website for upcoming events.")
    elif "engineering" in user_input:
        return ("Our Engineering Department offers programs in Mechanical, Electrical, Computer, and Civil Engineering. "
                "Visit the Engineering Department page for more details about courses and faculty.")
    elif "medical" in user_input:
        return ("Our Medical School offers undergraduate and postgraduate programs in Medicine, Nursing, and Pharmacy. "
                "For more information, visit the Medical School page on our website.")
    elif "arts" in user_input:
        return ("The Arts Department offers programs in Fine Arts, Performing Arts, and Art History. "
                "You can find more information on the Arts Department page.")
    elif "science" in user_input:
        return ("Our Science Department offers programs in Physics, Chemistry, Biology, and Environmental Science. "
                "Please visit the Science Department page for more details.")
    elif "library" in user_input:
        return ("Our library is equipped with extensive resources, including books, journals, and digital media. "
                "It is open from 8 AM to 10 PM on weekdays and 10 AM to 6 PM on weekends.")
    elif "hostel" in user_input or "accommodation" in user_input:
        return ("We offer on-campus accommodation with various options to suit your needs. "
                "Visit our accommodation page for more information about the hostels and how to apply for a room.")
    elif "sports" in user_input or "gym" in user_input:
        return ("Our campus includes a fully equipped gym and various sports facilities, including basketball courts, a swimming pool, and a football field. "
                "Check the sports complex page for membership details and opening hours.")
    elif "bye" in user_input or "goodbye" in user_input:
        return ("Goodbye! If you have any other questions, feel free to ask anytime.")
    else:
        return ("I'm not sure how to help with that. Here are some topics you can ask about: "
                "admissions, courses, campus life, contact information, scholarships, events, engineering, medical, arts, science, library, accommodation, or sports.")

def main():
    print("Welcome to Our College Info Bot! Type 'exit' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Chatbot: Goodbye! Have a great day!")
            break
        response = chatbot_response(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    main()
