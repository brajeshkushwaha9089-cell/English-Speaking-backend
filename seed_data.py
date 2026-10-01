"""
English Speaking Coach - Comprehensive Seed Learning Data
Covers: Lessons, Grammar, Speaking Exercises, Conversation Scenarios, Pronunciation, Sentence Builder & Challenges.
All content is strictly in English for total language immersion.
"""

LESSONS = [
    # Beginner
    {"id": "b1", "level": "Beginner", "title": "Self Introduction & Greetings", "duration": "10 min", "xp": 50,
     "description": "Learn to introduce yourself confidently in English with name, occupation, and hometown.",
     "key_points": ["Greetings (Hi, Hello, Good morning)", "Stating your name & role", "Describing where you live"]},
    {"id": "b2", "level": "Beginner", "title": "Talking About Your Family", "duration": "12 min", "xp": 50,
     "description": "Describe your family members, their professions, and your relationships.",
     "key_points": ["Family vocabulary (siblings, parents, cousins)", "Possessive pronouns (my, his, her)", "Simple present verbs"]},
    {"id": "b3", "level": "Beginner", "title": "Daily Routine & Schedules", "duration": "15 min", "xp": 60,
     "description": "Express your morning, afternoon, and evening routine in natural English.",
     "key_points": ["Time expressions (at 7 AM, in the evening)", "Frequency adverbs (always, usually, sometimes)", "Action verbs"]},
    {"id": "b4", "level": "Beginner", "title": "Hobbies & Free Time", "duration": "12 min", "xp": 50,
     "description": "Talk about what you enjoy doing in your leisure hours and on weekends.",
     "key_points": ["Likes and dislikes (I enjoy, I prefer, I dislike)", "Sports and music vocabulary", "Expressing excitement"]},
    {"id": "b5", "level": "Beginner", "title": "Food, Meals & Ordering", "duration": "15 min", "xp": 60,
     "description": "Learn polite phrases for dining at restaurants and ordering food.",
     "key_points": ["Polite requests (Could I have, I would like)", "Taste adjectives (delicious, spicy, sweet)", "Asking for the bill"]},
    {"id": "b6", "level": "Beginner", "title": "Directions & Places in Town", "duration": "12 min", "xp": 50,
     "description": "Ask for directions and understand instructions to navigate a city.",
     "key_points": ["Prepositions of place (next to, opposite, across from)", "Imperative directions (turn left, go straight)", "Landmark terms"]},
    {"id": "b7", "level": "Beginner", "title": "Shopping & Prices", "duration": "12 min", "xp": 50,
     "description": "Practice conversational transactions in stores, discussing sizes, colors, and prices.",
     "key_points": ["Asking prices (How much is this?)", "Expressing preferences", "Discounts and payments"]},
    {"id": "b8", "level": "Beginner", "title": "Weather & Seasons", "duration": "10 min", "xp": 40,
     "description": "Discuss seasonal weather, temperatures, and everyday climate conditions.",
     "key_points": ["Weather adjectives (sunny, chilly, humid)", "Making small talk about weather", "Describing outdoor plans"]},
    {"id": "b9", "level": "Beginner", "title": "Describing People & Appearances", "duration": "15 min", "xp": 60,
     "description": "Use descriptive vocabulary to talk about height, hair, clothing, and personality.",
     "key_points": ["Adjectives of physical appearance", "Personality traits (kind, humorous, hardworking)", "Using 'looks like'"]},
    {"id": "b10", "level": "Beginner", "title": "Making Plans & Future Intentions", "duration": "15 min", "xp": 60,
     "description": "Form sentences about upcoming events using 'going to' and 'will'.",
     "key_points": ["Future intentions ('I am going to visit')", "Making invitations ('Would you like to come?')", "Confirming times"]},

    # Intermediate
    {"id": "i1", "level": "Intermediate", "title": "Narrating Past Experiences & Stories", "duration": "18 min", "xp": 80,
     "description": "Share engaging personal anecdotes using Past Simple and Past Continuous.",
     "key_points": ["Sequential linkers (Suddenly, Meanwhile, In the end)", "Past tenses contrast", "Maintaining listener interest"]},
    {"id": "i2", "level": "Intermediate", "title": "Giving Opinions & Polite Disagreement", "duration": "15 min", "xp": 75,
     "description": "Express your thoughts respectfully in discussions and academic settings.",
     "key_points": ["Stating viewpoint (In my perspective, As far as I see)", "Polite disagreement (I see your point, however)", "Giving reasons"]},
    {"id": "i3", "level": "Intermediate", "title": "Job Interviews: Strengths & Weaknesses", "duration": "20 min", "xp": 90,
     "description": "Master professional answers to common hiring and HR interview questions.",
     "key_points": ["Professional adjectives", "STAR method framework", "Turning weaknesses into growth"]},
    {"id": "i4", "level": "Intermediate", "title": "Phone & Video Call Etiquette", "duration": "15 min", "xp": 75,
     "description": "Handle formal and casual phone conversations, leave voicemails, and manage audio glitches.",
     "key_points": ["Professional greetings & identification", "Handling bad connection politely", "Leaving clear voicemails"]},
    {"id": "i5", "level": "Intermediate", "title": "Solving Problems & Making Suggestions", "duration": "18 min", "xp": 80,
     "description": "Propose constructive solutions in workplace and team discussions.",
     "key_points": ["Conditional suggestions ('What if we...', 'How about...')", "Evaluating pros and cons", "Consensus building"]},
    {"id": "i6", "level": "Intermediate", "title": "Expressing Regret & Hypotheticals", "duration": "18 min", "xp": 85,
     "description": "Use conditionals to discuss missed opportunities and alternative pasts.",
     "key_points": ["Third conditional structures ('If I had known...')", "Modal verbs of deduction ('should have', 'could have')", "Reflective communication"]},
    {"id": "i7", "level": "Intermediate", "title": "Workplace Email & Formal Chats", "duration": "15 min", "xp": 75,
     "description": "Transition spoken communication into crisp, professional workplace interactions.",
     "key_points": ["Professional sign-offs and salutations", "Action item clarity", "Tone modulation"]},
    {"id": "i8", "level": "Intermediate", "title": "Describing Trends & Graphs", "duration": "20 min", "xp": 90,
     "description": "Discuss business metrics, statistical trends, rises, falls, and plateaus.",
     "key_points": ["Trend verbs (soared, declined, fluctuated)", "Adverbs of degree (dramatically, steadily)", "Summarizing findings"]},
    {"id": "i9", "level": "Intermediate", "title": "Travel Emergencies & Hotel Bookings", "duration": "16 min", "xp": 80,
     "description": "Solve flight delays, room complaints, and customs queries when travelling abroad.",
     "key_points": ["Assertive yet polite problem reporting", "Requesting replacements or refunds", "Airport terminology"]},
    {"id": "i10", "level": "Intermediate", "title": "Emotional Intelligence & Empathy", "duration": "18 min", "xp": 85,
     "description": "Comfort friends, celebrate colleagues' success, and build deeper connections in English.",
     "key_points": ["Empathetic phrases ('I can imagine how tough that is')", "Active listening signals", "Celebratory language"]},

    # Advanced
    {"id": "a1", "level": "Advanced", "title": "Delivering Impactful Presentations", "duration": "25 min", "xp": 120,
     "description": "Command audience attention, structure persuasive narratives, and deliver seamless slide transitions.",
     "key_points": ["Hooking the audience in 30 seconds", "Signposting phrases", "Handling tough Q&A questions"]},
    {"id": "a2", "level": "Advanced", "title": "Persuasive Negotiation & Compromise", "duration": "25 min", "xp": 120,
     "description": "Negotiate contracts, salaries, and compromises with tact and assertiveness.",
     "key_points": ["Concession language ('We would be willing if...')", "BATNA concept communication", "Securing win-win outcomes"]},
    {"id": "a3", "level": "Advanced", "title": "Debating Contemporary Global Issues", "duration": "22 min", "xp": 110,
     "description": "Construct airtight logical arguments on technology, climate, and ethics.",
     "key_points": ["Rebuttal strategies", "Rhetorical question deployment", "Avoiding fallacies"]},
    {"id": "a4", "level": "Advanced", "title": "Nuanced Idioms & Metaphorical English", "duration": "20 min", "xp": 100,
     "description": "Incorporate idiomatic expressions naturally without sounding forced or outdated.",
     "key_points": ["Contextual nuance", "Business idioms ('cut corners', 'move the needle')", "Cultural connotations"]},
    {"id": "a5", "level": "Advanced", "title": "Public Speaking & Keynote Delivery", "duration": "30 min", "xp": 150,
     "description": "Master cadence, pause control, vocal inflection, and emotional resonance on stage.",
     "key_points": ["The power of deliberate silence", "Vocal variety and pitch modulation", "Storytelling hooks"]}
]

GRAMMAR_TOPICS = [
    {"id": "g1", "title": "Present Simple vs Present Continuous", "level": "Beginner",
     "rule": "Use Present Simple for daily habits and permanent facts. Use Present Continuous for actions happening right now.",
     "pattern": "Subject + Base Verb / Subject + am/is/are + Verb-ing",
     "examples": ["I drink coffee every morning.", "I am drinking coffee right now."],
     "mistake": "Don't say: 'I am drinking coffee every morning.' (Habits take Present Simple).",
     "speaking_application": "Speak 3 sentences describing what you do every day, and 2 sentences describing what you are doing this exact moment."},
    
    {"id": "g2", "title": "Past Simple & Regular/Irregular Verbs", "level": "Beginner",
     "rule": "Use Past Simple for completed actions in the past at a specific time.",
     "pattern": "Subject + Past Form (Verb-ed or Irregular form)",
     "examples": ["I visited London last summer.", "She wrote an inspiring article yesterday."],
     "mistake": "Don't say: 'I didn't went there.' Say: 'I didn't go there.' (After 'did not', use base verb).",
     "speaking_application": "Narrate 3 things you accomplished yesterday from morning to evening."},

    {"id": "g3", "title": "Articles: A, An, and The", "level": "Beginner",
     "rule": "Use 'a/an' for general, unspecific singular nouns. Use 'the' for specific items known to both speaker and listener.",
     "pattern": "A + consonant sound | An + vowel sound | The + specific noun",
     "examples": ["I bought an umbrella.", "The umbrella I bought is yellow."],
     "mistake": "Don't say: 'He is engineer.' Say: 'He is an engineer.' (Always use an article with singular professions).",
     "speaking_application": "Pick three objects in your room and describe them using appropriate articles."},

    {"id": "g4", "title": "Present Perfect: Experiences & Results", "level": "Intermediate",
     "rule": "Use Present Perfect when past events connect to the present or when the exact time of experience is unimportant.",
     "pattern": "Subject + have/has + Past Participle (V3)",
     "examples": ["I have visited five countries.", "She has already submitted her project."],
     "mistake": "Don't say: 'I have seen him yesterday.' (Specific past times like 'yesterday' require Past Simple: 'I saw him yesterday').",
     "speaking_application": "Tell your coach about 3 exciting things you have done in your life and 1 thing you haven't done yet."},

    {"id": "g5", "title": "Modal Verbs: Can, Could, Should, Must", "level": "Intermediate",
     "rule": "Modal verbs express ability, possibility, advice, or strict obligation.",
     "pattern": "Subject + Modal + Base Verb",
     "examples": ["You should practice speaking daily.", "I can solve this challenge.", "You must wear a helmet."],
     "mistake": "Don't say: 'You should to practice.' (Never use 'to' after modal verbs like should/can/must).",
     "speaking_application": "Give 3 pieces of practical advice to someone starting to learn English."},

    {"id": "g6", "title": "Second Conditional: Dreams & Hypotheticals", "level": "Intermediate",
     "rule": "Use Second Conditional for imaginary, unlikely, or hypothetical situations in the present or future.",
     "pattern": "If + Subject + Past Simple, Subject + would + Base Verb",
     "examples": ["If I won a million dollars, I would travel the entire world.", "If I were you, I would accept that offer."],
     "mistake": "Say: 'If I were you' rather than 'If I was you' in formal and standard English.",
     "speaking_application": "Complete this sentence out loud and explain why: 'If I had superpower, I would...'"},

    {"id": "g7", "title": "Passive Voice in Professional English", "level": "Intermediate",
     "rule": "Use Passive Voice when the action or result is more important than who performed it.",
     "pattern": "Subject + Form of 'be' + Past Participle",
     "examples": ["The report was finalized on Monday.", "Over 500 new features have been released."],
     "mistake": "Avoid overusing passive voice when personal responsibility is expected.",
     "speaking_application": "Describe how your favorite dish or a software application is produced using passive voice."},

    {"id": "g8", "title": "Reported Speech & Indirect Statements", "level": "Intermediate",
     "rule": "Use Reported Speech to communicate what someone else stated without quoting them verbatim.",
     "pattern": "Speaker + said that + Backshifted Tense",
     "examples": ["Direct: 'I am tired.' -> Reported: 'He said that he was tired.'"],
     "mistake": "Remember to backshift tenses: 'is' becomes 'was', 'will' becomes 'would'.",
     "speaking_application": "Summarize a conversation you had with a family member or friend earlier today."},

    {"id": "g9", "title": "Essential Phrasal Verbs in Conversation", "level": "Intermediate",
     "rule": "Phrasal verbs combine a verb with a preposition to create a new figurative meaning.",
     "pattern": "Verb + Particle (on, off, up, down, out, away)",
     "examples": ["Figure out (understand/solve)", "Give up (quit)", "Call off (cancel)", "Bring up (mention)"],
     "mistake": "Be careful with separable vs inseparable phrasal verbs.",
     "speaking_application": "Use 'look forward to', 'run into', and 'turn out' in a short 30-second speech."},

    {"id": "g10", "title": "Third Conditional: Regrets & Past Alternatives", "level": "Advanced",
     "rule": "Use Third Conditional to imagine a different past outcome that did not happen.",
     "pattern": "If + Subject + had + V3, Subject + would have + V3",
     "examples": ["If I had studied harder, I would have passed with distinction.", "If we had left earlier, we wouldn't have missed the flight."],
     "mistake": "Don't say: 'If I would have known...' Say: 'If I had known...' in the if-clause.",
     "speaking_application": "Reflect on a past decision and talk about how things would have been different if you made another choice."}
]

SPEAKING_EXERCISES = [
    {"id": "s1", "title": "Introduce Yourself", "level": "Beginner", "prep_seconds": 15, "speak_seconds": 60,
     "prompts": ["What is your full name?", "Where are you currently living?", "What are your core interests?", "What is your main English learning goal?"]},
    {"id": "s2", "title": "Describe Your Typical Day", "level": "Beginner", "prep_seconds": 15, "speak_seconds": 60,
     "prompts": ["What time do you usually wake up?", "What are your morning rituals?", "How do you spend your afternoons?", "How do you unwind before sleep?"]},
    {"id": "s3", "title": "Talk About Your Best Friend", "level": "Beginner", "prep_seconds": 15, "speak_seconds": 60,
     "prompts": ["Who is your closest companion?", "How did you first meet?", "What personality qualities make them special?", "What do you enjoy doing together?"]},
    {"id": "s4", "title": "My Favorite Meal & Cuisine", "level": "Beginner", "prep_seconds": 15, "speak_seconds": 60,
     "prompts": ["What is your favorite dish?", "What ingredients go into making it?", "Where is the best place to eat it?", "Why do you recommend it?"]},
    {"id": "s5", "title": "Is Online Learning Better Than In-Person?", "level": "Intermediate", "prep_seconds": 20, "speak_seconds": 90,
     "prompts": ["What are the key benefits of virtual classrooms?", "What are the major drawbacks or isolation issues?", "Which format do you personally prefer and why?"]},
    {"id": "s6", "title": "Job Interview: Describe a Difficult Challenge", "level": "Intermediate", "prep_seconds": 20, "speak_seconds": 90,
     "prompts": ["What was the situation and goal?", "What specific obstacle arose?", "What concrete actions did you take?", "What was the final positive outcome?"]},
    {"id": "s7", "title": "Describe an Inspiring Leader or Teacher", "level": "Intermediate", "prep_seconds": 20, "speak_seconds": 90,
     "prompts": ["Who has made the strongest positive impact on you?", "What specific values do they model?", "Can you recall a piece of advice they offered?"]},
    {"id": "s8", "title": "Should AI Replace Repetitive Human Jobs?", "level": "Advanced", "prep_seconds": 30, "speak_seconds": 120,
     "prompts": ["Which industries are seeing the greatest disruption?", "How should workers adapt their skillsets?", "What ethical guardrails should society establish?"]},
    {"id": "s9", "title": "Pitch a New Tech Product or Startup Idea", "level": "Advanced", "prep_seconds": 30, "speak_seconds": 120,
     "prompts": ["What painful problem does your idea address?", "Who is your target customer?", "What is your unique competitive advantage?"]}
]

CONVERSATION_SCENARIOS = [
    {"id": "c1", "title": "At a Coffee Shop", "category": "Daily Life", "level": "Beginner",
     "ai_role": "Barista", "user_role": "Customer",
     "initial_message": "Good morning! Welcome to Brew & Bean. What can I get started for you today?",
     "goals": ["Order your beverage of choice", "Specify size and milk preference", "Ask for the total price and pay"]},
    {"id": "c2", "title": "College Campus: Meeting a Classmate", "category": "Campus Life", "level": "Beginner",
     "ai_role": "Fellow Student (Rohan)", "user_role": "New Student",
     "initial_message": "Hey there! Are you also in Professor David's computer science lecture?",
     "goals": ["Introduce yourself politely", "Share what major you are pursuing", "Ask where the nearest campus library is"]},
    {"id": "c3", "title": "Job Interview: First Round", "category": "Career", "level": "Intermediate",
     "ai_role": "Hiring Manager (Sarah)", "user_role": "Job Candidate",
     "initial_message": "Welcome! Thank you for joining us today. Could you start by walking me through your background and interest in this role?",
     "goals": ["Give a succinct 3-part professional background", "Highlight a relevant technical skill", "Express enthusiasm for the company"]},
    {"id": "c4", "title": "Asking for Directions in a New City", "category": "Travel", "level": "Beginner",
     "ai_role": "Local Resident", "user_role": "Tourist",
     "initial_message": "Excuse me, you look a bit lost. Can I help you find something?",
     "goals": ["Explain where you are trying to go", "Clarify walking vs metro transit", "Thank them warmly for their guidance"]},
    {"id": "c5", "title": "Doctor's Appointment: Describing Symptoms", "category": "Health", "level": "Intermediate",
     "ai_role": "Doctor Adams", "user_role": "Patient",
     "initial_message": "Hello, please have a seat. What brings you into the clinic today?",
     "goals": ["Describe where the discomfort or pain is located", "Explain how many days it has persisted", "Ask about medication and precautions"]}
]

SENTENCE_BUILDER_ITEMS = [
    {"id": "sb1", "scrambled": ["English", "practice", "I", "every", "morning"],
     "correct": "I practice English every morning",
     "grammar_pattern": "Subject + Verb + Object + Time Expression",
     "tip": "Time expressions like 'every morning' or 'yesterday' naturally sit at the beginning or very end of an English sentence."},
    {"id": "sb2", "scrambled": ["waiting", "for", "She", "bus", "is", "the"],
     "correct": "She is waiting for the bus",
     "grammar_pattern": "Present Continuous: Subject + is + Verb-ing + Prepositional Phrase",
     "tip": "'Wait' requires the preposition 'for' when specifying what or whom you are waiting on."},
    {"id": "sb3", "scrambled": ["to", "want", "I", "fluency", "achieve", "speaking"],
     "correct": "I want to achieve speaking fluency",
     "grammar_pattern": "Subject + Verb + Infinitive (to + verb) + Compound Noun",
     "tip": "Verbs like 'want', 'hope', and 'decide' are followed by an infinitive with 'to'."},
    {"id": "sb4", "scrambled": ["already", "submitted", "Have", "you", "assignment", "your"],
     "correct": "Have you already submitted your assignment",
     "grammar_pattern": "Present Perfect Question: Auxiliary Have + Subject + Adverb + V3 + Object",
     "tip": "In questions, the auxiliary verb comes before the subject: 'Have you...'"},
    {"id": "sb5", "scrambled": ["more", "would", "If", "practiced", "I", "I", "confident", "be"],
     "correct": "If I practiced more I would be confident",
     "grammar_pattern": "Second Conditional: If + Past Simple + Would + Base Verb",
     "tip": "Use Second Conditional when imagining hypothetical improvements."}
]

PRONUNCIATION_TOPICS = [
    {"id": "p1", "title": "Syllable Stress in Multi-syllable Words", "level": "Beginner",
     "explanation": "In English, one syllable in every word is stressed louder, longer, and with higher pitch.",
     "examples": [
         {"word": "comfortable", "stress": "COM-for-ta-ble (not com-FOR-ta-ble)", "audio_hint": "Focus on the first syllable 'COM'"},
         {"word": "photograph", "stress": "PHO-to-graph", "audio_hint": "First syllable stressed"},
         {"word": "photographer", "stress": "pho-TOG-ra-pher", "audio_hint": "Stress shifts to the second syllable 'TOG'"}
     ]},
    {"id": "p2", "title": "Connected Speech & Contractions", "level": "Intermediate",
     "explanation": "Native speakers blend word boundaries together rather than pausing between each individual word.",
     "examples": [
         {"word": "going to -> gonna", "stress": "I'm gonna attend the meeting", "audio_hint": "Natural conversational cadence"},
         {"word": "want to -> wanna", "stress": "Do you wanna practice English?", "audio_hint": "Fast linking sounds"},
         {"word": "could have -> could've", "stress": "You could've told me earlier", "audio_hint": "Soft 've' ending"}
     ]},
    {"id": "p3", "title": "Intonation: Rising vs Falling Pitch", "level": "Intermediate",
     "explanation": "Statements and open questions fall in pitch at the end. Yes/No questions rise in pitch.",
     "examples": [
         {"word": "Where do you live? ↘", "stress": "Falling pitch at the end", "audio_hint": "Open information request"},
         {"word": "Do you speak English? ↗", "stress": "Rising pitch at the end", "audio_hint": "Yes/No question check"}
     ]}
]

DAILY_CHALLENGES = [
    {"id": "dc1", "title": "Introduce Yourself to the World", "xp": 50, "type": "speaking",
     "task": "Speak for at least 45 seconds introducing your background, passions, and ambition.",
     "target_seconds": 45},
    {"id": "dc2", "title": "Learn 5 High-Impact Business Words", "xp": 40, "type": "vocabulary",
     "task": "Review and master 5 professional workplace words in your vocabulary deck.",
     "target_count": 5},
    {"id": "dc3", "title": "Complete 3 Sentence Builder Puzzles", "xp": 45, "type": "grammar",
     "task": "Assemble 3 scrambled sentences without making syntax errors.",
     "target_count": 3},
    {"id": "dc4", "title": "Hold a 2-Minute Dialogue with AI", "xp": 60, "type": "conversation",
     "task": "Engage in an interactive roleplay session with your chosen coach.",
     "target_seconds": 120}
]
