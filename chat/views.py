from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import ensure_csrf_cookie
import json
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
#from django.template.context_processors import csrf

# Create your views here.
@ensure_csrf_cookie
def index(request):
    return render(request, 'index.html')

@ensure_csrf_cookie
def chatmsg(request):
    if request.method == 'POST':
        input = json.loads(request.body.decode('utf-8'))
        input_text = input['name']
        print(input_text)
        return HttpResponse(json.dumps(input_text),  content_type="application/json")
        #handle bot message
        # response = auto_reply(input_text)
        # response_data = {}
        # response_data['result'] = 'true'
        # response_data['message'] = response
        # print(response)
        # return HttpResponse(json.dumps(response_data),  content_type="application/json")
    
def auto_reply(input_text):
    bot = ChatBot('MedBot')
    print(input_text)

    # bot = ChatBot('MedBot',
                  
    #             read_only = True, 
    #             preprocessors=['chatterbot.preprocessors.convert_to_ascii', 
    #                             'chatterbot.preprocessors.unescape_html',
    #                             'chatterbot.preprocessors.clean_whitespace'],
    #             logic_adapters = [
    #                 {
    #                     'import_path': 'chatterbot.logic.BestMatch',
    #                     'default_response': 'Sorry, I am unable to process your request. Please try again, or contact us for help.',
    #                     'maximum_similarity_threshold': 0.90
    #                 }
    #             ],)

    trainer = ListTrainer(bot)

    trainer.train([
        "Hi",
        "Hello",
        "Hey", 
        "How is going...",
        "Hello",
        "Hello, What you like to ask?",
    ])

    trainer.train([    
        "What is EC department? What is EC?",
        "EC means Electronic and Communication Major in the past but name changed to Department of Electronic Engineering.",
        "What can we learn in EC?",
        "You can learn and study about so many things like how digital signals process, how the large machines are controlled in factories, how the telecommunication and transmission work and you will also be learning about controllers and circuits from basic. You can choose what kind of fields you would like to learn.",
        "How many fields are there in EC major?",
        "There are so many fields in EC major but mainly these four specifications are popular among the students; Electronic Devices , Communication, Control, Embedded.",
    ])

    trainer.train([
        "What are the job opportunity in EC?",
        "Have you already known about what kind of fields are in EC?",
        "Yes",
        "Then, what field do you interested in?",
        "No",
        "You should learn about what kind of fields are in EC first.",
    ])
    
    trainer.train([
        "What is PLC? Explain about PLC field.",
        "A Programmable Logic Controller (PLC) is an industrial digital computer designed for the control and automation of manufacturing processes, such as assembly lines, machinery, or robotic devices. PLCs operate by continuously monitoring inputs (like sensors or user inputs) and making decisions based on programmed logic to control outputs (such as motors, lights, or valves). They are highly reliable and can be programmed using various languages, with ladder logic being the most common. PLCs are essential in automating processes in industries such as manufacturing, automotive, and utilities, ensuring precision, efficiency, and safety in operations.",
        "PLC",
        "A Programmable Logic Controller (PLC) is an industrial digital computer designed for the control and automation of manufacturing processes, such as assembly lines, machinery, or robotic devices. PLCs operate by continuously monitoring inputs (like sensors or user inputs) and making decisions based on programmed logic to control outputs (such as motors, lights, or valves). They are highly reliable and can be programmed using various languages, with ladder logic being the most common. PLCs are essential in automating processes in industries such as manufacturing, automotive, and utilities, ensuring precision, efficiency, and safety in operations.",
        "Where can I learn PLC?",
        "You can learn PLC in EC major fro FREE",
        "What are the job opportunity in PLC?",
        "You shouldn't follow the job, try to be good at something. When you specialized in something, people will come to offer you.",
        "the job opportunity of PLC",
        "You shouldn't follow the job, try to be good at something. When you specialized in something, people will come to offer you.",  
        ])
    
    trainer.train([
        "What is Electronic Device Field?",
        "Electronic Devices field mainly focuses on understanding the components, devices, and systems that manipulate electrical signals to perform tasks like amplification, switching, and information processing. From this field, student will gain these key skills like understanding the fundamental principles of semiconductor devices, ability to design, analyze, and simulate circuits involving transistors, diodes, and ICs, knowledge of how to implement these devices in real-world applications such as communication systems, power supplies, and computing.",
        "Electronic Device field",
        "Electronic Devices field mainly focuses on understanding the components, devices, and systems that manipulate electrical signals to perform tasks like amplification, switching, and information processing. From this field, student will gain these key skills like understanding the fundamental principles of semiconductor devices, ability to design, analyze, and simulate circuits involving transistors, diodes, and ICs, knowledge of how to implement these devices in real-world applications such as communication systems, power supplies, and computing.",
        "The job opportunities in electronic devices field",
        "The Electronic Devices field, being a core part of Electronics and Communication (EC) Engineering, offers a variety of job opportunities across different industries. Here are some of the key job opportunities in this field like Design Engineer who works on designing semiconductor devices like transistors, diodes, and ICs, Hardware Design Engineer who involved in the design of hardware components and circuits in consumer electronics devices, EV Design Engineer who works on electronic systems in electric vehicles, focusing on battery management, charging systems, and motor control",
    ])
    
    trainer.train([
        "What is Communication Field.",
        "In communication, you can divide into four main fields: Telecommunications, Microwave, Signal processing, Network. If you want to know about telecommunication field, please type ONE. If you want to know about microwave field, please type TWO. If you want to know about signal processing field, please type THREE. If you want to know about Network field, please type FOUR.",
        "Communication Field.",
        "In communication, you can divide into four main fields: Telecommunications, Microwave, Signal processing, Network. If you want to know about telecommunication field, please type ONE. If you want to know about microwave field, please type TWO. If you want to know about signal processing field, please type THREE. If you want to know about Network field, please type FOUR.",
        "Explain about Communication Field",
        "In communication, you can divide into four main fields: Telecommunications, Microwave, Signal processing, Network. If you want to know about telecommunication field, please type ONE. If you want to know about microwave field, please type TWO. If you want to know about signal processing field, please type THREE. If you want to know about Network field, please type FOUR.",
    ])  
      
    trainer.train([
        "ONE",
        "Telecommunications engineers install, maintain and repair public and private telephone systems and maintain, test and repair telecommunications cables.",
    ]) 
    
    trainer.train([    
        "TWO",
        "Microwave engineers emphasize microwave frequencies and components used in wireless communication system, antenna design, antenna radiation patterns and radar system.",
    ]) 
    
    trainer.train([    
        "THREE",
        "A signal processing engineers are specialists in signal processing techniques who analyze and modify digital signals to improve accuracy and reliability.",
    ]) 
    
    trainer.train([   
        "FOUR",
        "Network engineers design, implement and maintain computer network in a computer or organizations. They must provide network operation efficiently and security.",
    ]) 
     
    trainer.train([ 
        "What is Control Field?",
        "A control engineers organize and regulate any components of automation and production processes. PLC programming and computer algorithms can all be learned through specialization in this discipline. If you want to know about PLC, please type PLC.",
        "Control Field",
        "A control engineers organize and regulate any components of automation and production processes. PLC programming and computer algorithms can all be learned through specialization in this discipline. If you want to know about PLC, please type PLC.",
        "Explain about Control Field?",
        "A control engineers organize and regulate any components of automation and production processes. PLC programming and computer algorithms can all be learned through specialization in this discipline. If you want to know about PLC, please type PLC.",       
    ])
    
    trainer.train([
        "Embedded field",
        "Embedded field refers to embedded systems specifically designed for communication-related applications. These systems integrate both hardware and software to perform dedicated communication tasks and are a crucial part of modern electronic communication systems. Microcontrollers are often at the core of embedded systems, designed to handle specific tasks, such as signal modulation, control of communication devices, or processing sensor data. Embedded systems in communication devices are typically programmed using C, C++, or assembly language to ensure efficiency and speed. Embedded systems are widely used in telecommunication devices such as routers, modems, satellite communication devices, mobile phones, and base stations to handle data transmission and reception.",
        "What is Embedded field?",
        "Embedded field refers to embedded systems specifically designed for communication-related applications. These systems integrate both hardware and software to perform dedicated communication tasks and are a crucial part of modern electronic communication systems. Microcontrollers are often at the core of embedded systems, designed to handle specific tasks, such as signal modulation, control of communication devices, or processing sensor data. Embedded systems in communication devices are typically programmed using C, C++, or assembly language to ensure efficiency and speed. Embedded systems are widely used in telecommunication devices such as routers, modems, satellite communication devices, mobile phones, and base stations to handle data transmission and reception.",
    ])
    
    trainer.train([
        "Resistor. What is Resistor?",
        "A resistor is a passive electrical component that resists the flow of electric current in a circuit. It provides a precise amount of resistance, measured in ohms (Ω), to control the current flow or divide voltages. Resistors are among the most common and essential components used in both analog and digital circuits.",
    ]) 
       
    trainer.train([
        "Capacitor. Explain about Capacitor?",
        "A capacitor is a passive electrical component that stores and releases electrical energy in a circuit. It consists of two conductive plates separated by an insulating material called the dielectric. When a voltage is applied across the plates, an electric field develops across the dielectric, causing a build-up of electric charge. This stored charge can be released later when needed.",  
    ])
    
    trainer.train([
        "Diode. Introduction to Diode.",
        "A diode is a passive electronic component that allows current to flow in only one direction. It has two terminals: the anode (positive) and the cathode (negative). When the anode is connected to a higher voltage than the cathode, the diode conducts electricity (this is called forward bias). If the voltage is reversed, the diode blocks current (this is called reverse bias).",
    ])
       
    trainer.train([
        "What is your phone number? How do I reach you? How do I contact you? How do I call you?",
        "Our number is 01**23**45",
        "What is your address? Where are you located?",
        "You can find us at No. 45, 8th Cross, Oakwood Street",
    ])

    trainer.train([
        "Thank you!",
        "You're most welcome!",
        "Thanks!",
        "Of course!",
        ])

    value =bot.get_response(input_text)

    return str(value)

    