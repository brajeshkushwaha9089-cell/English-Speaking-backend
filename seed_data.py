"""
English Speaking Coach - Comprehensive Seed Learning Data
Covers: Lessons, Grammar Curriculum (40 Topics), Common Mistakes (26 Items),
Grammar Comparisons (15 Pairs), AI Knowledge Base, Speaking Exercises,
Conversation Scenarios, Pronunciation, Sentence Builder & Daily Challenges.
All content is strictly in English for complete linguistic immersion.
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

# Complete 40-Topic Grammar Curriculum from Beginner to Advanced
GRAMMAR_CURRICULUM = [
    # --- LEVEL: BEGINNER (A1) ---
    {
        "id": "g1",
        "title": "Present Simple Tense",
        "level": "Beginner",
        "category": "tenses",
        "formula": "Subject + Base Verb (add -s/-es for he/she/it)",
        "explanation": "Use Present Simple for daily habits, permanent truths, routines, and scheduled events.",
        "examples": [
            "I drink black coffee every morning.",
            "The sun rises in the east.",
            "She works as a software developer in Bengaluru.",
            "Do you speak English fluently?"
        ],
        "mistake": "Don't say: 'He go to office every day.' Say: 'He goes to office every day.'",
        "speaking_prompt": "Speak 3 sentences describing your regular daily morning routine."
    },
    {
        "id": "g2",
        "title": "Present Continuous Tense",
        "level": "Beginner",
        "category": "tenses",
        "formula": "Subject + am/is/are + Verb-ing",
        "explanation": "Use Present Continuous for actions occurring at this exact moment or temporary ongoing situations.",
        "examples": [
            "I am practicing my English pronunciation right now.",
            "They are developing a new web application.",
            "She is reading an interesting novel this week.",
            "Why are you looking at your watch?"
        ],
        "mistake": "Don't say: 'I am knowing him.' Say: 'I know him.' (Stative verbs like know/love/understand don't take -ing).",
        "speaking_prompt": "Describe 3 things that are happening around you right now."
    },
    {
        "id": "g3",
        "title": "Articles: A, An, The & Zero Article",
        "level": "Beginner",
        "category": "parts_of_speech",
        "formula": "A + consonant sound | An + vowel sound | The + specific item | No article + plurals/general",
        "explanation": "'A/An' introduces non-specific singular countable nouns based on sound (an hour, a university). 'The' refers to known, unique, or previously mentioned nouns.",
        "examples": [
            "I saw an eagle soaring over a mountain.",
            "The eagle landed on the tallest tree.",
            "She is studying at a university in Canada.",
            "Honesty is the best policy. (Zero article for abstract concepts)"
        ],
        "mistake": "Don't say: 'He is engineer.' Say: 'He is an engineer.' (Always use an article with singular professions).",
        "speaking_prompt": "Look around your room and describe three objects using appropriate articles."
    },
    {
        "id": "g4",
        "title": "Nouns & Pronouns: Subject, Object & Possessive",
        "level": "Beginner",
        "category": "parts_of_speech",
        "formula": "Subject (I/He) -> Object (Me/Him) -> Possessive (My/His/Mine/His)",
        "explanation": "Subject pronouns perform the action; object pronouns receive it. Possessive adjectives describe nouns, while possessive pronouns replace them.",
        "examples": [
            "She invited me to her presentation.",
            "This laptop is mine, but the charger is his.",
            "Between you and me, the project is succeeding.",
            "They congratulated us on our achievement."
        ],
        "mistake": "Don't say: 'Between you and I.' Say: 'Between you and me.' (Prepositions take object pronouns).",
        "speaking_prompt": "Speak 3 sentences introducing your best friend using subject, object, and possessive pronouns."
    },
    {
        "id": "g5",
        "title": "Past Simple: Regular & Irregular Verbs",
        "level": "Beginner",
        "category": "tenses",
        "formula": "Subject + Verb-2 (ed/irregular) | Negative: did not + Base Verb",
        "explanation": "Use Past Simple for completed actions at a finished time in the past (yesterday, last year, in 2020).",
        "examples": [
            "I visited Mumbai last December.",
            "She wrote an inspiring article yesterday.",
            "We did not receive the confirmation email.",
            "What did you learn in yesterday's session?"
        ],
        "mistake": "Don't say: 'I didn't went there.' Say: 'I didn't go there.' (After 'did/didn't', always use the base verb).",
        "speaking_prompt": "Narrate 3 things you accomplished yesterday from morning until evening."
    },
    {
        "id": "g6",
        "title": "Prepositions of Place: In, On, At",
        "level": "Beginner",
        "category": "parts_of_speech",
        "formula": "At (specific point) | On (surface / street) | In (enclosed 3D space / city / country)",
        "explanation": "'At' denotes specific points (at the door, at 5 PM). 'On' is for surfaces (on the table) and streets (on MG Road). 'In' is for enclosed areas, cities, and countries (in Delhi, in India).",
        "examples": [
            "We met at the airport entrance.",
            "The notebook is resting on the desk.",
            "She lives in Bengaluru and works in a modern tech park.",
            "I will see you at the bus stop on Main Street."
        ],
        "mistake": "Don't say: 'I live at India.' Say: 'I live in India.' (Large areas require 'in').",
        "speaking_prompt": "Describe where you live, where your workplace/college is, and where you meet friends."
    },

    # --- LEVEL: ELEMENTARY (A2) ---
    {
        "id": "g7",
        "title": "Past Continuous Tense",
        "level": "Elementary",
        "category": "tenses",
        "formula": "Subject + was/were + Verb-ing",
        "explanation": "Use Past Continuous for an action that was ongoing in the past when another short action interrupted it.",
        "examples": [
            "I was cooking dinner when the phone rang.",
            "They were driving to Jaipur while it was raining heavily.",
            "What were you doing at 8 PM yesterday?",
            "She was preparing her slides all night."
        ],
        "mistake": "Don't say: 'When he arrived, I cooked.' Say: 'When he arrived, I was cooking.'",
        "speaking_prompt": "Describe what you were doing yesterday at 2 PM, 6 PM, and 9 PM."
    },
    {
        "id": "g8",
        "title": "Future Simple: Will vs Going to",
        "level": "Elementary",
        "category": "tenses",
        "formula": "Will + Base Verb (Instant decisions/predictions) vs Be going to + Base Verb (Prior plans)",
        "explanation": "Use 'will' for spontaneous decisions, offers, and promises. Use 'going to' for plans decided before speaking and predictions based on present evidence.",
        "examples": [
            "The phone is ringing. I will answer it! (Spontaneous decision)",
            "I am going to start learning Python next Monday. (Prior plan)",
            "Look at those dark clouds! It is going to rain. (Evidence)",
            "I promise I will help you with your presentation."
        ],
        "mistake": "Don't say: 'Tomorrow I will meet him at 10 (fixed ticket booked).' Say: 'I am meeting / I am going to meet him.'",
        "speaking_prompt": "State two plans you already decided for next week, and one spontaneous promise."
    },
    {
        "id": "g9",
        "title": "Adjectives & Adverbs: Comparison & Order",
        "level": "Elementary",
        "category": "parts_of_speech",
        "formula": "Adjective + er / more + Adjective | Superlative: the -est / the most",
        "explanation": "Adjectives modify nouns; adverbs modify verbs, adjectives, or other adverbs. Comparative compares two; superlative compares three or more.",
        "examples": [
            "This framework is faster and more scalable than the older one.",
            "She speaks English exceptionally fluently.",
            "He bought a beautiful, handcrafted Indian silk scarf.",
            "Bengaluru is one of the most vibrant tech hubs in Asia."
        ],
        "mistake": "Don't say: 'She is more taller than me.' Say: 'She is taller than me.' (Never double comparatives).",
        "speaking_prompt": "Compare two cities, smartphones, or programming languages in three spoken sentences."
    },
    {
        "id": "g10",
        "title": "Prepositions of Time: At, On, In, For, Since",
        "level": "Elementary",
        "category": "parts_of_speech",
        "formula": "At + exact time | On + day/date | In + month/year/season | For + duration | Since + starting point",
        "explanation": "'At 6 PM', 'on Monday', 'in July / in 2026'. Use 'for' with time spans (for 3 hours) and 'since' with reference points (since 9 AM).",
        "examples": [
            "Our team sync begins at 9:30 AM on Tuesday.",
            "India launched its mission in August 2023.",
            "I have been studying for four hours.",
            "She has worked here since January."
        ],
        "mistake": "Don't say: 'I am waiting here since 2 hours.' Say: 'I have been waiting here for 2 hours.'",
        "speaking_prompt": "State when you woke up today, your favorite day of the week, and how long you have lived in your city."
    },
    {
        "id": "g11",
        "title": "Modal Verbs: Can, Could, May, Might",
        "level": "Elementary",
        "category": "modals",
        "formula": "Subject + Modal + Base Verb (Never add 'to')",
        "explanation": "'Can' expresses present ability and informal permission. 'Could' expresses past ability or polite requests. 'May/Might' express possibility and formal permission.",
        "examples": [
            "I can code in JavaScript and Python.",
            "Could you please repeat that explanation?",
            "It might rain this evening, so carry an umbrella.",
            "May I ask a clarifying question regarding the roadmap?"
        ],
        "mistake": "Don't say: 'I can to speak English.' Say: 'I can speak English.' (Never use 'to' after modal verbs).",
        "speaking_prompt": "Politely ask for permission, express one skill you have, and one future possibility."
    },
    {
        "id": "g12",
        "title": "Zero & First Conditionals",
        "level": "Elementary",
        "category": "conditionals",
        "formula": "Zero: If + Present Simple, Present Simple | First: If + Present Simple, will + Base Verb",
        "explanation": "Zero Conditional states scientific facts and universal truths. First Conditional expresses real, probable future conditions and their consequences.",
        "examples": [
            "If you heat water to 100°C, it boils. (Zero)",
            "If it rains tomorrow, we will reschedule the outdoor cricket match. (First)",
            "If you practice speaking daily, your fluency will skyrocket.",
            "If she studies diligently, she will clear the interview."
        ],
        "mistake": "Don't say: 'If it will rain, I will stay home.' Say: 'If it rains, I will stay home.' (No 'will' inside the if-clause).",
        "speaking_prompt": "Create 2 First Conditional sentences about your career and language goals."
    },

    # --- LEVEL: INTERMEDIATE (B1) ---
    {
        "id": "g13",
        "title": "Present Perfect Tense",
        "level": "Intermediate",
        "category": "tenses",
        "formula": "Subject + have/has + Past Participle (V3)",
        "explanation": "Connects past actions to the present. Used for life experiences (without specific date), recent actions with present impact, and unfinished time periods.",
        "examples": [
            "I have completed three full-stack projects this quarter.",
            "She has already spoken with the hiring manager.",
            "Have you ever travelled outside your country?",
            "They have lived in Delhi for seven years."
        ],
        "mistake": "Don't say: 'I have seen him yesterday.' Say: 'I saw him yesterday.' (Specific past time markers require Past Simple).",
        "speaking_prompt": "Share 3 achievements you have completed and 1 experience you have never had."
    },
    {
        "id": "g14",
        "title": "Present Perfect Continuous Tense",
        "level": "Intermediate",
        "category": "tenses",
        "formula": "Subject + have/has been + Verb-ing",
        "explanation": "Emphasizes the duration of an ongoing action that began in the past and is still actively continuing right now.",
        "examples": [
            "I have been coding this application since 8 AM.",
            "She has been learning English for six months.",
            "They have been discussing the architecture for two hours.",
            "Why are your eyes red? Have you been staring at the monitor all night?"
        ],
        "mistake": "Don't say: 'I am working here since 2 years.' Say: 'I have been working here for 2 years.'",
        "speaking_prompt": "Describe an activity or hobby you have been doing continuously and for how long."
    },
    {
        "id": "g15",
        "title": "Past Perfect Tense",
        "level": "Intermediate",
        "category": "tenses",
        "formula": "Subject + had + Past Participle (V3)",
        "explanation": "Used for an action that happened before another action in the past (the 'past of the past').",
        "examples": [
            "When I reached the station, the train had already left.",
            "She had finished her presentation before the director arrived.",
            "I realized I had forgotten my room keys in the taxi.",
            "They had tested the backend thoroughly prior to deployment."
        ],
        "mistake": "Don't use Past Perfect for a single past action. Don't say: 'I had eaten dinner yesterday.' Say: 'I ate dinner yesterday.'",
        "speaking_prompt": "Tell a short story about arriving somewhere only to find something had already taken place."
    },
    {
        "id": "g16",
        "title": "Modal Verbs: Should, Must, Have To, Ought To",
        "level": "Intermediate",
        "category": "modals",
        "formula": "Should/Ought to (Advice) | Must (Strong internal obligation) | Have to (External rule)",
        "explanation": "'Should' offers good advice. 'Must' signifies personal conviction or urgent rule. 'Have to' expresses objective necessity imposed by laws or circumstances.",
        "examples": [
            "You should review your resume before sending it.",
            "Drivers must stop when the traffic light turns red.",
            "I have to wake up early tomorrow because my flight departs at 6 AM.",
            "You ought to respect the team's working agreements."
        ],
        "mistake": "Don't say: 'You must to submit.' Say: 'You must submit.'",
        "speaking_prompt": "Give 3 recommendations to a junior developer or a student preparing for interviews."
    },
    {
        "id": "g17",
        "title": "Second Conditional: Hypotheticals & Dreams",
        "level": "Intermediate",
        "category": "conditionals",
        "formula": "If + Subject + Past Simple, Subject + would + Base Verb",
        "explanation": "Expresses imaginary, unreal, or highly improbable situations in the present or future.",
        "examples": [
            "If I had ten million dollars, I would establish an open-source research lab.",
            "If I were you, I would accept the job offer in Singapore.",
            "What would you do if you won the lottery tomorrow?",
            "She would travel more frequently if she had more leisure time."
        ],
        "mistake": "Say: 'If I were you' rather than 'If I was you' in standard English.",
        "speaking_prompt": "Answer aloud: 'If I could master any skill in 24 hours, what would it be and why?'"
    },
    {
        "id": "g18",
        "title": "Active vs Passive Voice: Present & Past",
        "level": "Intermediate",
        "category": "voice_speech",
        "formula": "Object + Form of 'be' + Past Participle (V3) (+ by Subject)",
        "explanation": "Use Passive Voice when the action or receiver is more important than the doer, or when the agent is unknown or obvious.",
        "examples": [
            "Active: Alexander Graham Bell invented the telephone.",
            "Passive: The telephone was invented by Alexander Graham Bell.",
            "Active: Millions of developers use React daily.",
            "Passive: React is used by millions of developers daily."
        ],
        "mistake": "Don't omit the auxiliary 'be'. Don't say: 'The letter sent yesterday.' Say: 'The letter was sent yesterday.'",
        "speaking_prompt": "Describe three famous inventions or software tools using Passive Voice."
    },
    {
        "id": "g19",
        "title": "Direct & Indirect (Reported) Speech: Statements",
        "level": "Intermediate",
        "category": "voice_speech",
        "formula": "Subject + said (that) + Backshifted Tense",
        "explanation": "When reporting what someone said in the past, shift tenses one step backward: Present Simple -> Past Simple, Present Perfect -> Past Perfect, will -> would.",
        "examples": [
            "Direct: 'I am working on the database.' -> Reported: He said that he was working on the database.",
            "Direct: 'I have fixed the issue.' -> Reported: She stated that she had fixed the issue.",
            "Direct: 'I will call you tonight.' -> Reported: Kabir mentioned that he would call me that night."
        ],
        "mistake": "Don't forget pronoun shifts: 'I' changes to 'he/she'. Don't say: 'He said that I will come.'",
        "speaking_prompt": "Report 2 things your colleague or friend told you earlier today."
    },
    {
        "id": "g20",
        "title": "Conjunctions & Linking Words",
        "level": "Intermediate",
        "category": "parts_of_speech",
        "formula": "Although/Even though + Clause | Despite/In spite of + Noun/V-ing | However + Clause",
        "explanation": "Contrasting ideas require distinct syntax. 'Although' takes a full subject + verb clause, while 'despite' takes a noun phrase or gerund.",
        "examples": [
            "Although it rained heavily, we thoroughly enjoyed the cricket tournament.",
            "Despite the heavy rain, we thoroughly enjoyed the tournament.",
            "The challenge was arduous; however, our team delivered on schedule.",
            "She joined the startup because of the visionary leadership."
        ],
        "mistake": "Don't combine 'although' and 'but'. Don't say: 'Although it rained, but we went out.' Say: 'Although it rained, we went out.'",
        "speaking_prompt": "Make two contrast sentences using 'Although' and 'Despite'."
    },
    {
        "id": "g21",
        "title": "Subject-Verb Agreement",
        "level": "Intermediate",
        "category": "structure",
        "formula": "Singular Subject -> Singular Verb | Plural Subject -> Plural Verb",
        "explanation": "Indefinite pronouns (everyone, someone, nobody, each) take singular verbs. Either/or follows the closest subject. Uncountable nouns are singular.",
        "examples": [
            "Everyone in the auditorium is listening attentively.",
            "Neither the teacher nor the students were aware of the change.",
            "The news about the economy is encouraging.",
            "A basket of fresh apples was placed on the dining table."
        ],
        "mistake": "Don't say: 'Everyone have their own dreams.' Say: 'Everyone has their own dreams.'",
        "speaking_prompt": "Speak 3 sentences starting with 'Everyone', 'Neither... nor', and 'The quality of...'"
    },

    # --- LEVEL: UPPER-INTERMEDIATE (B2) ---
    {
        "id": "g22",
        "title": "Past Perfect Continuous Tense",
        "level": "Upper-Intermediate",
        "category": "tenses",
        "formula": "Subject + had been + Verb-ing",
        "explanation": "Emphasizes the continuous duration of an action that was happening up until a specific point in the past.",
        "examples": [
            "She had been working at Microsoft for five years before she launched her own venture.",
            "His eyes were tired because he had been debugging the server logs all night.",
            "They had been negotiating for three weeks when the contract was finally signed."
        ],
        "mistake": "Don't confuse with Past Continuous. Use Past Perfect Continuous when the duration prior to a past event is highlighted.",
        "speaking_prompt": "Describe an effort you had been making before achieving an important milestone."
    },
    {
        "id": "g23",
        "title": "Future Continuous & Future Perfect",
        "level": "Upper-Intermediate",
        "category": "tenses",
        "formula": "Future Cont: will be + V-ing | Future Perf: will have + V3",
        "explanation": "Future Continuous describes actions in progress at a specific future time. Future Perfect describes actions that will be completed by a future deadline.",
        "examples": [
            "This time tomorrow, I will be flying over the Himalayas.",
            "By December 2026, I will have completed my master's degree.",
            "They will have launched the mobile app before the festival season begins."
        ],
        "mistake": "Don't say: 'By next year, I will finish.' Say: 'By next year, I will have finished.' (Time limit requires Future Perfect).",
        "speaking_prompt": "State where you will be at 8 PM tonight, and what you will have accomplished by year's end."
    },
    {
        "id": "g24",
        "title": "Third Conditional: Past Regrets & What-Ifs",
        "level": "Upper-Intermediate",
        "category": "conditionals",
        "formula": "If + Subject + had + V3, Subject + would have + V3",
        "explanation": "Imagines an alternative past scenario that did not occur and speculates on its hypothetical outcome.",
        "examples": [
            "If I had studied harder for the entrance test, I would have secured admission to IIT.",
            "If we had left ten minutes earlier, we would not have missed our flight.",
            "She would have accepted the offer if the compensation had met her expectations."
        ],
        "mistake": "Don't say: 'If I would have known...' Say: 'If I had known...' in the if-clause.",
        "speaking_prompt": "Reflect on a past decision and discuss how things would have turned out differently."
    },
    {
        "id": "g25",
        "title": "Reported Questions & Imperatives",
        "level": "Upper-Intermediate",
        "category": "voice_speech",
        "formula": "Subject + asked if/whether (Yes/No) | Subject + asked Wh-word + Subject + Verb",
        "explanation": "In indirect questions, the question word order reverts to standard statement order (Subject + Verb), with no auxiliary do/did.",
        "examples": [
            "Direct: 'Where do you live?' -> Indirect: He asked me where I lived.",
            "Direct: 'Are you ready?' -> Indirect: Priya asked whether I was ready.",
            "Direct: 'Please turn down the volume.' -> Indirect: She asked him to turn down the volume."
        ],
        "mistake": "Don't keep question word order. Don't say: 'He asked me where did I live.' Say: 'He asked me where I lived.'",
        "speaking_prompt": "Report a question a colleague or interviewer asked you recently."
    },
    {
        "id": "g26",
        "title": "Relative Clauses: Defining vs Non-Defining",
        "level": "Upper-Intermediate",
        "category": "structure",
        "formula": "Defining (essential info, no commas, who/that/which) | Non-defining (extra info, commas, who/which)",
        "explanation": "Defining clauses identify which person/thing is meant. Non-defining clauses provide supplementary details set off by commas (never use 'that' in non-defining).",
        "examples": [
            "The engineer who architected this microservice received an award. (Defining)",
            "Bengaluru, which is known as India's Silicon Valley, attracts global tech leaders. (Non-defining)",
            "The smartphone that I purchased yesterday has an exceptional battery life."
        ],
        "mistake": "Never use 'that' in a non-defining clause between commas. Don't say: 'My car, that is red, is fast.'",
        "speaking_prompt": "Describe your hometown or current company using both a defining and non-defining relative clause."
    },
    {
        "id": "g27",
        "title": "Gerunds vs Infinitives",
        "level": "Upper-Intermediate",
        "category": "parts_of_speech",
        "formula": "Verb + -ing (Gerund) vs Verb + to-infinitive",
        "explanation": "Certain verbs require gerunds (enjoy, avoid, consider, suggest). Others require infinitives (decide, hope, plan, promise). Some change meaning (remember to lock vs remember locking).",
        "examples": [
            "I enjoy coding clean, maintainable user interfaces.",
            "We decided to migrate our infrastructure to the cloud.",
            "Remember to submit your code before the deadline! (Duty)",
            "I remember meeting the CEO at last year's tech summit. (Memory)"
        ],
        "mistake": "Don't say: 'I look forward to meet you.' Say: 'I look forward to meeting you.' ('To' here is a preposition).",
        "speaking_prompt": "Use 'enjoy', 'decide', and 'look forward to' in 3 spoken sentences."
    },
    {
        "id": "g28",
        "title": "Modals of Deduction: Must have, Can't have, Might have",
        "level": "Upper-Intermediate",
        "category": "modals",
        "formula": "Modal + have + Past Participle (V3)",
        "explanation": "Speculates about past events with varying levels of certainty. 'Must have' (almost certain it happened), 'can't have' (impossible), 'might/could have' (possible).",
        "examples": [
            "The lights are off; they must have left the office.",
            "He can't have committed that blunder; he is an extremely meticulous architect.",
            "She didn't answer her phone; she might have been in an executive meeting."
        ],
        "mistake": "Don't use 'can have' for positive deduction. Use 'could have' or 'must have'.",
        "speaking_prompt": "Deduce why your favorite app experienced downtime or why a package arrived late."
    },

    # --- LEVEL: ADVANCED (C1) ---
    {
        "id": "g29",
        "title": "Mixed Conditionals",
        "level": "Advanced",
        "category": "conditionals",
        "formula": "Type 1: If + had + V3, would + Base Verb (Past cause, Present outcome)",
        "explanation": "Combines different time references across clauses, typically linking an unreal past condition with a present state of affairs.",
        "examples": [
            "If I had learned full-stack architecture earlier, I would be leading this engineering team today.",
            "If she were more organized, she would not have misplaced the vital project contracts.",
            "If India had not invested in digital infrastructure decades ago, we would not have the thriving UPI ecosystem we enjoy now."
        ],
        "mistake": "Avoid rigidly matching tenses when the cause is firmly in the past but the result persists in the present.",
        "speaking_prompt": "Describe a past educational choice and how it directly shapes your present professional reality."
    },
    {
        "id": "g30",
        "title": "Inversion for Emphasis & Formality",
        "level": "Advanced",
        "category": "structure",
        "formula": "Negative Adverb + Auxiliary + Subject + Main Verb",
        "explanation": "Placing negative or restrictive adverbs (rarely, seldom, hardly, never, not only) at the sentence opening inverts subject and auxiliary for rhetorical elegance.",
        "examples": [
            "Rarely have I witnessed such profound dedication to engineering excellence.",
            "Not only did they deliver ahead of schedule, but they also reduced infrastructure costs by 40%.",
            "Hardly had we launched the feature when traffic surged tenfold.",
            "Under no circumstances should production keys be committed to source control."
        ],
        "mistake": "Remember the inverted word order: 'Rarely have I seen', NOT 'Rarely I have seen'.",
        "speaking_prompt": "Deliver a formal 20-second statement starting with 'Not only did...' or 'Rarely have I...'"
    },
    {
        "id": "g31",
        "title": "Cleft Sentences for Laser Focus",
        "level": "Advanced",
        "category": "structure",
        "formula": "It is/was [Focus] that... | What [Clause] is/was...",
        "explanation": "Cleft structures split a single sentence into two clauses to shine a theatrical spotlight on the most crucial piece of information.",
        "examples": [
            "Standard: Vikram solved the database concurrency deadlock.",
            "Cleft: It was Vikram who solved the database concurrency deadlock.",
            "Standard: We need clear communication.",
            "Cleft: What we need most urgently is transparent cross-functional communication."
        ],
        "mistake": "Keep the verb agreement aligned with the grammatical subject: 'What we need is...' not 'What we need are...'",
        "speaking_prompt": "Emphasize your strongest professional value using a 'What I bring to the table is...' cleft sentence."
    },
    {
        "id": "g32",
        "title": "The Subjunctive Mood in Professional English",
        "level": "Advanced",
        "category": "structure",
        "formula": "Verb of urgency (demand/insist/recommend) + that + Subject + Base Verb",
        "explanation": "Used after expressions of necessity, urgency, or formal requests. The verb in the dependent clause remains in its bare base form with no -s or past markers.",
        "examples": [
            "The security officer insisted that every developer enable multi-factor authentication immediately.",
            "I recommend that he be appointed to lead the architectural review board.",
            "It is imperative that the database be backed up before running the schema migration."
        ],
        "mistake": "Don't add '-s': 'I recommend that he attend the conference', NOT 'that he attends'.",
        "speaking_prompt": "Propose a critical operational guideline using 'I insist that...' or 'It is essential that...'"
    },
    {
        "id": "g33",
        "title": "Advanced Passive: Causative & Reporting",
        "level": "Advanced",
        "category": "voice_speech",
        "formula": "Have/Get something done | It is believed that... / Subject is said to + Base Verb",
        "explanation": "Causatives express arranging for others to execute tasks. Advanced reporting passives maintain journalistic and executive distance.",
        "examples": [
            "We had our cloud infrastructure audited by an independent cyber-security firm.",
            "The AI model is said to surpass previous industry benchmarks by 25%.",
            "It is widely acknowledged that continuous practice is the cornerstone of fluency."
        ],
        "mistake": "Don't confuse active and causative: 'I repaired my car' (I did it) vs 'I had my car repaired' (mechanic did it).",
        "speaking_prompt": "Describe a service or task you had someone else perform for you recently."
    },
    {
        "id": "g34",
        "title": "Nuance & Softening in Spoken English",
        "level": "Advanced",
        "category": "structure",
        "formula": "Past tenses as polite cushions | Modal softening | Indirect phrasing",
        "explanation": "Master native conversational tact. Instead of abrupt commands, native speakers deploy polite cushions to disagree diplomatically and pitch suggestions.",
        "examples": [
            "Blunt: I want to talk to you. -> Softened: I was wondering if you might have five minutes for a quick chat.",
            "Blunt: You are wrong. -> Softened: I see your perspective, though our telemetry data suggests a slightly different pattern.",
            "Softened: Would you happen to have the updated slide deck handy?"
        ],
        "mistake": "Avoid sounding unintentionally aggressive in meetings by omitting conversational softening phrases.",
        "speaking_prompt": "Transform a blunt workplace request into a polite, softened executive inquiry."
    },
    {
        "id": "g35",
        "title": "Essential Phrasal Verbs: Separable vs Inseparable",
        "level": "Intermediate",
        "category": "structure",
        "formula": "Verb + Particle (e.g. Turn down, Look up, Run into, Give up)",
        "explanation": "Phrasal verbs combine a verb with a particle to create idiomatic meanings. Separable verbs can place a noun or pronoun between verb and particle (turn it off). Inseparable verbs must keep the particle attached (look after someone).",
        "examples": [
            "Please turn off the lights before leaving the conference hall.",
            "I ran into an old college friend at the international tech symposium.",
            "Never give up on your spoken English journey.",
            "Could you look up that documentation for me?"
        ],
        "mistake": "With pronouns, separable verbs MUST separate. Say: 'Turn it off', NOT 'Turn off it'.",
        "speaking_prompt": "Use 'look forward to', 'run into', and 'turn out' in a 30-second spoken update."
    },
    {
        "id": "g36",
        "title": "Question Tags & Spoken Confirmation",
        "level": "Elementary",
        "category": "structure",
        "formula": "Positive Statement -> Negative Tag | Negative Statement -> Positive Tag",
        "explanation": "Tags turn statements into confirmation questions. If the main sentence is positive, the tag is negative. If negative, the tag is positive.",
        "examples": [
            "You are a software engineer, aren't you?",
            "She didn't finish the deployment yet, did she?",
            "It is a lovely day, isn't it?",
            "We have completed all test cases, haven't we?"
        ],
        "mistake": "Don't use 'isn't it?' or 'no?' for all statements. Match the auxiliary verb and subject pronoun.",
        "speaking_prompt": "Form 3 confirmation statements with question tags about your colleagues, weather, and schedule."
    },
    {
        "id": "g37",
        "title": "Clauses of Purpose & Result",
        "level": "Upper-Intermediate",
        "category": "structure",
        "formula": "In order to / So as to + Base Verb | So that + Clause | So / Such... that (Result)",
        "explanation": "Express intent and consequence cleanly. 'In order to' expresses purpose with an infinitive. 'So that' takes a clause with a modal (can/could/would). 'Such [adjective + noun] that' emphasizes extreme results.",
        "examples": [
            "I wake up at 6 AM in order to practice English speaking without distraction.",
            "We optimized the database queries so that API responses would load under 50ms.",
            "It was such an inspiring keynote that the entire auditorium gave a standing ovation."
        ],
        "mistake": "Don't say: 'I wake up for to practice.' Say: 'I wake up to practice' or 'in order to practice'.",
        "speaking_prompt": "Explain why you are learning English using 'in order to' and 'so that'."
    },
    {
        "id": "g38",
        "title": "Expressing Preference: Prefer vs Would Rather",
        "level": "Intermediate",
        "category": "structure",
        "formula": "Prefer + Noun/Gerund + TO + Noun/Gerund | Would rather + Base Verb + THAN + Base Verb",
        "explanation": "'Prefer' takes the preposition 'to' (prefer tea to coffee). 'Would rather' is followed by bare infinitives and 'than' (would rather drink tea than coffee).",
        "examples": [
            "I prefer working remotely to commuting two hours every morning.",
            "I would rather master one programming language thoroughly than learn ten superficially.",
            "She prefers reading books to watching mindless video reels."
        ],
        "mistake": "Don't say: 'I prefer tea than coffee.' Say: 'I prefer tea to coffee.'",
        "speaking_prompt": "State two professional preferences using 'prefer... to' and 'would rather... than'."
    },
    {
        "id": "g39",
        "title": "Used to vs Be Used to vs Get Used to",
        "level": "Upper-Intermediate",
        "category": "structure",
        "formula": "Used to + Base Verb (Past habit) | Be used to + Noun/V-ing (Accustomed) | Get used to + Noun/V-ing (Process)",
        "explanation": "'Used to' describes a past habit no longer true. 'Be used to' means something is normal and familiar. 'Get used to' describes the process of becoming comfortable with something new.",
        "examples": [
            "I used to live in a small village, but now I live in a metro city.",
            "I am used to waking up early because I have done it for years.",
            "It took me several weeks to get used to speaking English in team meetings."
        ],
        "mistake": "After 'be used to' and 'get used to', always use a gerund (-ing) or noun: 'I am used to living alone', NOT 'live alone'.",
        "speaking_prompt": "Share one thing you used to do in the past, and one thing you recently got used to."
    },
    {
        "id": "g40",
        "title": "Causative Verbs: Have, Make, Let & Get",
        "level": "Advanced",
        "category": "structure",
        "formula": "Make someone do (Force) | Let someone do (Allow) | Have someone do / Get someone to do (Arrange)",
        "explanation": "Causatives express causing another person to act. 'Make' and 'Let' take bare infinitives. 'Have someone do' takes bare infinitive. 'Get someone to do' takes a to-infinitive.",
        "examples": [
            "The director made the team redo the testing phase before launch.",
            "She let her junior colleague lead the client presentation.",
            "I had the technician service my laptop.",
            "We managed to get the client to approve the expanded scope."
        ],
        "mistake": "'Get' requires 'to', while 'have' does not. Say: 'I got him to help me', but 'I had him help me'.",
        "speaking_prompt": "Describe a project or event where you had someone assist you or let someone take the lead."
    }
]

# Aliases for backwards compatibility with earlier endpoints
GRAMMAR_TOPICS = GRAMMAR_CURRICULUM

# Curated 26 Real-World Common Mistakes with explanations, rules, and audio
COMMON_GRAMMAR_MISTAKES = [
    {
        "id": "m1",
        "wrong": "I am agree with you.",
        "right": "I agree with you.",
        "rule": "Verb vs Adjective",
        "explanation": "'Agree' is already a verb, not an adjective. You do not need the auxiliary 'am'.",
        "category": "Verbs",
        "level": "Beginner",
        "audio_text": "I agree with you."
    },
    {
        "id": "m2",
        "wrong": "She don't know the answer.",
        "right": "She doesn't know the answer.",
        "rule": "Subject-Verb Agreement",
        "explanation": "Third-person singular subjects (He, She, It) require 'doesn't' (does not), never 'don't'.",
        "category": "Tenses",
        "level": "Beginner",
        "audio_text": "She doesn't know the answer."
    },
    {
        "id": "m3",
        "wrong": "I didn't went there yesterday.",
        "right": "I didn't go there yesterday.",
        "rule": "Past Simple Negation",
        "explanation": "The auxiliary 'did' already carries the past tense. The main verb that follows must be in its base form.",
        "category": "Tenses",
        "level": "Beginner",
        "audio_text": "I didn't go there yesterday."
    },
    {
        "id": "m4",
        "wrong": "He is married with a doctor.",
        "right": "He is married to a doctor.",
        "rule": "Preposition Collocation",
        "explanation": "In English, one is married 'to' someone, not 'with' someone.",
        "category": "Prepositions",
        "level": "Beginner",
        "audio_text": "He is married to a doctor."
    },
    {
        "id": "m5",
        "wrong": "I have lived here since five years.",
        "right": "I have lived here for five years.",
        "rule": "Since vs For",
        "explanation": "Use 'for' with durations of time (5 years, 3 days). Use 'since' with specific starting points (since 2021, since Monday).",
        "category": "Prepositions",
        "level": "Elementary",
        "audio_text": "I have lived here for five years."
    },
    {
        "id": "m6",
        "wrong": "I look forward to meet you.",
        "right": "I look forward to meeting you.",
        "rule": "Gerund after Preposition",
        "explanation": "In 'look forward to', 'to' is a preposition, not part of an infinitive. Prepositions are followed by gerunds (-ing).",
        "category": "Verbs",
        "level": "Intermediate",
        "audio_text": "I look forward to meeting you."
    },
    {
        "id": "m7",
        "wrong": "He is engineer in Pune.",
        "right": "He is an engineer in Pune.",
        "rule": "Singular Countable Articles",
        "explanation": "Singular countable professions must always take an indefinite article: 'a doctor', 'an engineer', 'a teacher'.",
        "category": "Articles",
        "level": "Beginner",
        "audio_text": "He is an engineer in Pune."
    },
    {
        "id": "m8",
        "wrong": "I have seen him yesterday.",
        "right": "I saw him yesterday.",
        "rule": "Past Simple vs Present Perfect",
        "explanation": "Specific past time markers like 'yesterday', 'last night', or 'in 2019' prohibit Present Perfect. Use Past Simple.",
        "category": "Tenses",
        "level": "Beginner",
        "audio_text": "I saw him yesterday."
    },
    {
        "id": "m9",
        "wrong": "Although it was raining, but we attended the meet.",
        "right": "Although it was raining, we attended the meet.",
        "rule": "Double Conjunctions",
        "explanation": "Never pair 'although' with 'but'. Use one or the other, never both in the same sentence.",
        "category": "Conjunctions",
        "level": "Elementary",
        "audio_text": "Although it was raining, we attended the meet."
    },
    {
        "id": "m10",
        "wrong": "She is more taller than her sister.",
        "right": "She is taller than her sister.",
        "rule": "Double Comparatives",
        "explanation": "Short one-syllable adjectives form comparatives with -er (taller). Never add 'more' before an -er adjective.",
        "category": "Adjectives",
        "level": "Beginner",
        "audio_text": "She is taller than her sister."
    },
    {
        "id": "m11",
        "wrong": "I lost the 8 AM metro train.",
        "right": "I missed the 8 AM metro train.",
        "rule": "Miss vs Lose",
        "explanation": "You 'lose' items you can't find (keys, phone). You 'miss' scheduled transport or opportunities (train, flight, chance).",
        "category": "Vocabulary",
        "level": "Beginner",
        "audio_text": "I missed the 8 AM metro train."
    },
    {
        "id": "m12",
        "wrong": "Everyone have their own problems.",
        "right": "Everyone has their own problems.",
        "rule": "Indefinite Pronoun Agreement",
        "explanation": "'Everyone', 'everybody', 'someone', and 'nobody' are grammatically singular and require singular verbs (has, is).",
        "category": "Agreement",
        "level": "Elementary",
        "audio_text": "Everyone has their own problems."
    },
    {
        "id": "m13",
        "wrong": "If I will go to Delhi, I will call you.",
        "right": "If I go to Delhi, I will call you.",
        "rule": "First Conditional Clauses",
        "explanation": "In conditional sentences, never use 'will' in the 'if' condition clause. Use Present Simple.",
        "category": "Conditionals",
        "level": "Elementary",
        "audio_text": "If I go to Delhi, I will call you."
    },
    {
        "id": "m14",
        "wrong": "You must to complete this today.",
        "right": "You must complete this today.",
        "rule": "Bare Infinitive after Modals",
        "explanation": "Modal verbs (must, can, could, should, will, would) are followed directly by base verbs without 'to'.",
        "category": "Modals",
        "level": "Beginner",
        "audio_text": "You must complete this today."
    },
    {
        "id": "m15",
        "wrong": "He gave me an advice.",
        "right": "He gave me some advice.",
        "rule": "Uncountable Nouns",
        "explanation": "'Advice' is an uncountable noun. It cannot take 'an' or plural 'advices'. Say 'some advice' or 'a piece of advice'.",
        "category": "Nouns",
        "level": "Intermediate",
        "audio_text": "He gave me some advice."
    },
    {
        "id": "m16",
        "wrong": "She explained me the entire concept.",
        "right": "She explained the entire concept to me.",
        "rule": "Ditransitive Verb Patterns",
        "explanation": "'Explain' does not take a direct personal object. You explain something 'to' somebody.",
        "category": "Verbs",
        "level": "Intermediate",
        "audio_text": "She explained the entire concept to me."
    },
    {
        "id": "m17",
        "wrong": "I did a mistake in the calculation.",
        "right": "I made a mistake in the calculation.",
        "rule": "Make vs Do Collocations",
        "explanation": "You 'make' a mistake, a decision, a phone call. You 'do' homework, chores, business.",
        "category": "Collocations",
        "level": "Beginner",
        "audio_text": "I made a mistake in the calculation."
    },
    {
        "id": "m18",
        "wrong": "According to me, this approach is best.",
        "right": "In my opinion, this approach is best.",
        "rule": "Stylistic Idiom",
        "explanation": "'According to' is used to cite external sources (According to experts, According to the report). For your own perspective, use 'In my opinion' or 'From my perspective'.",
        "category": "Style",
        "level": "Intermediate",
        "audio_text": "In my opinion, this approach is best."
    },
    {
        "id": "m19",
        "wrong": "I am good in English speaking.",
        "right": "I am good at English speaking.",
        "rule": "Adjective + Preposition",
        "explanation": "Skills and proficiencies take the preposition 'at': good at math, great at programming, skilled at negotiation.",
        "category": "Prepositions",
        "level": "Beginner",
        "audio_text": "I am good at English speaking."
    },
    {
        "id": "m20",
        "wrong": "Can you borrow me your pen?",
        "right": "Can you lend me your pen?",
        "rule": "Borrow vs Lend",
        "explanation": "'Borrow' means to take temporarily (Can I borrow your pen?). 'Lend' means to give temporarily (Can you lend me your pen?).",
        "category": "Vocabulary",
        "level": "Beginner",
        "audio_text": "Can you lend me your pen?"
    },
    {
        "id": "m21",
        "wrong": "There is many people in the hall.",
        "right": "There are many people in the hall.",
        "rule": "Existential There Agreement",
        "explanation": "'People' is plural, so existential 'there' requires the plural auxiliary 'are'.",
        "category": "Agreement",
        "level": "Beginner",
        "audio_text": "There are many people in the hall."
    },
    {
        "id": "m22",
        "wrong": "I prefer tea than coffee.",
        "right": "I prefer tea to coffee.",
        "rule": "Comparative Preposition",
        "explanation": "The verb 'prefer' takes the preposition 'to', never 'than'.",
        "category": "Prepositions",
        "level": "Elementary",
        "audio_text": "I prefer tea to coffee."
    },
    {
        "id": "m23",
        "wrong": "I am thinking to buy a new laptop.",
        "right": "I am thinking of buying a new laptop.",
        "rule": "Verb Complementation",
        "explanation": "'Think of' or 'think about' takes a gerund (-ing) when considering future actions.",
        "category": "Verbs",
        "level": "Intermediate",
        "audio_text": "I am thinking of buying a new laptop."
    },
    {
        "id": "m24",
        "wrong": "Between you and I, the product is ready.",
        "right": "Between you and me, the product is ready.",
        "rule": "Prepositional Pronoun Case",
        "explanation": "Prepositions like 'between' govern object pronouns (me, him, her, us, them), never subject pronouns.",
        "category": "Pronouns",
        "level": "Intermediate",
        "audio_text": "Between you and me, the product is ready."
    },
    {
        "id": "m25",
        "wrong": "No one know the exact answer.",
        "right": "No one knows the exact answer.",
        "rule": "Singular Subject Agreement",
        "explanation": "'No one' is grammatically singular and requires the singular verb with -s.",
        "category": "Agreement",
        "level": "Beginner",
        "audio_text": "No one knows the exact answer."
    },
    {
        "id": "m26",
        "wrong": "I have been knowing him for ten years.",
        "right": "I have known him for ten years.",
        "rule": "Stative Verbs in Continuous",
        "explanation": "'Know' is a stative verb representing a cognitive state. It cannot be used in continuous tenses. Use Present Perfect Simple.",
        "category": "Tenses",
        "level": "Intermediate",
        "audio_text": "I have known him for ten years."
    }
]

# Side-by-side Grammar Comparison Pairs (Difference Finder)
GRAMMAR_COMPARISONS = [
    {
        "id": "cmp1",
        "termA": "Since",
        "termB": "For",
        "summary": "'Since' marks a specific starting point in time. 'For' measures total elapsed duration.",
        "ruleA": "Used with a specific point in time or event: since 2018, since Monday, since 9 AM, since I graduated.",
        "ruleB": "Used with a duration or quantity of time: for 5 hours, for 3 years, for a long time, for two weeks.",
        "examplesA": ["I have been working here since 2021.", "She has been coding since 8 AM."],
        "examplesB": ["I have lived here for five years.", "We talked for forty minutes."],
        "trick": "Ask yourself: Can you see it on a clock/calendar? If YES -> 'Since'. Is it a counted span of time? -> 'For'."
    },
    {
        "id": "cmp2",
        "termA": "Although",
        "termB": "Despite / In spite of",
        "summary": "Both express contrast. 'Although' is a conjunction followed by a full clause; 'Despite' is a preposition followed by a noun or gerund.",
        "ruleA": "Requires a Subject + Verb clause: Although + [Subject + Verb].",
        "ruleB": "Requires a noun phrase, pronoun, or gerund: Despite + [Noun / -ing]. Never say 'despite of'.",
        "examplesA": ["Although he was tired, he finished the project.", "Although it rained, we enjoyed the trip."],
        "examplesB": ["Despite being tired, he finished the project.", "Despite the heavy rain, we enjoyed the trip."],
        "trick": "Count the verbs: If the contrast clause has a verb, use 'Although'. If it's just a noun, use 'Despite'."
    },
    {
        "id": "cmp3",
        "termA": "Make",
        "termB": "Do",
        "summary": "'Make' is for creating, producing, or building something new. 'Do' is for actions, duties, chores, and general work.",
        "ruleA": "Collocates with: make a decision, make a mistake, make money, make tea, make an excuse, make progress.",
        "ruleB": "Collocates with: do homework, do business, do chores, do the dishes, do your best, do a favor.",
        "examplesA": ["Don't be afraid to make mistakes while speaking.", "Let's make a quick plan."],
        "examplesB": ["I need to do my daily English exercises.", "Could you do me a quick favor?"],
        "trick": "Did you produce a tangible result or decision? Use 'Make'. Is it an activity or chore? Use 'Do'."
    },
    {
        "id": "cmp4",
        "termA": "Say",
        "termB": "Tell",
        "summary": "'Say' focuses on the words uttered (Say something). 'Tell' focuses on instructing or informing someone (Tell someone something).",
        "ruleA": "Does not take a personal object immediately: Say [words] (or say TO someone).",
        "ruleB": "Requires a personal object immediately: Tell [someone] [something].",
        "examplesA": ["What did he say during the meeting?", "She said that she was thrilled."],
        "examplesB": ["Please tell me your story.", "He told his manager about the bug."],
        "trick": "Tell requires a person: Tell ME, Tell HIM, Tell US. Never 'Say me'."
    },
    {
        "id": "cmp5",
        "termA": "Will",
        "termB": "Going to",
        "summary": "'Will' is for spontaneous instant decisions, promises, and offers. 'Going to' is for pre-planned intentions and evidence-based predictions.",
        "ruleA": "Decided at the moment of speaking: 'The bell rang. I'll open it!'",
        "ruleB": "Decided prior to the conversation: 'I am going to purchase a laptop next week.'",
        "examplesA": ["I will certainly help you with your interview prep.", "I think it will be sunny."],
        "examplesB": ["Look at those black storm clouds! It is going to rain.", "We are going to visit Jaipur in November."],
        "trick": "Spontaneous thought? -> 'Will'. Pre-existing plan or visible evidence? -> 'Going to'."
    },
    {
        "id": "cmp6",
        "termA": "In time",
        "termB": "On time",
        "summary": "'On time' means punctual according to a strict schedule. 'In time' means early enough before a deadline or emergency.",
        "ruleA": "In time = with enough margin to spare before something happens (in time for dinner, in time to catch the train).",
        "ruleB": "On time = exact scheduled minute (neither early nor late).",
        "examplesA": ["We arrived at the airport just in time to clear security.", "Call the doctor in time."],
        "examplesB": ["The Rajdhani Express departed precisely on time at 4:30 PM.", "Always be on time for meetings."],
        "trick": "Opposite of 'on time' is late. Opposite of 'in time' is too late."
    },
    {
        "id": "cmp7",
        "termA": "Few / A few",
        "termB": "Little / A little",
        "summary": "'Few' is used with countable plural nouns. 'Little' is used with uncountable singular nouns.",
        "ruleA": "Countable: 'A few friends' (some, positive), 'Few friends' (almost none, negative).",
        "ruleB": "Uncountable: 'A little water' (some, positive), 'Little water' (almost none, negative).",
        "examplesA": ["I have a few questions about your presentation.", "Few people understand this complex algorithm."],
        "examplesB": ["I need a little more time to complete testing.", "There was little hope of saving the legacy codebase."],
        "trick": "Without 'a', both 'few' and 'little' have a pessimistic, negative tone (almost none)."
    },
    {
        "id": "cmp8",
        "termA": "Borrow",
        "termB": "Lend",
        "summary": "'Borrow' means to receive or take something temporarily with permission. 'Lend' means to give something temporarily.",
        "ruleA": "Subject receives: I borrow [from someone].",
        "ruleB": "Subject gives: I lend [to someone].",
        "examplesA": ["May I borrow your textbook for tonight's revision?", "She borrowed 1,000 rupees."],
        "examplesB": ["Could you lend me your vehicle for an hour?", "The bank lends money to startups."],
        "trick": "Borrow = Take IN. Lend = Give OUT."
    },
    {
        "id": "cmp9",
        "termA": "Because",
        "termB": "Because of / Due to",
        "summary": "'Because' is a conjunction followed by a subject and verb. 'Because of' is a preposition followed by a noun phrase.",
        "ruleA": "Because + [Subject + Verb]: 'We stayed indoors because it was raining.'",
        "ruleB": "Because of / Due to + [Noun / Gerund]: 'We stayed indoors because of the heavy rain.'",
        "examplesA": ["He succeeded because he worked tirelessly.", "I called because I needed guidance."],
        "examplesB": ["The flight was delayed because of dense fog.", "Due to high traffic, the servers scaled up."],
        "trick": "Has a verb? -> 'Because'. Just a noun? -> 'Because of / Due to'."
    },
    {
        "id": "cmp10",
        "termA": "Beside",
        "termB": "Besides",
        "summary": "'Beside' means next to or at the side of. 'Besides' means in addition to or furthermore.",
        "ruleA": "Preposition of physical location: sit beside me, stand beside the podium.",
        "ruleB": "Preposition or linking adverb: 'Besides Python, what languages do you know?'",
        "examplesA": ["She sat beside the director during the board meeting.", "The notebook is beside the laptop."],
        "examplesB": ["Besides coding, he has a deep passion for classical music.", "I have no other plans besides this."],
        "trick": "Remember the 's' in besides = 'Something extra' (in addition)."
    },
    {
        "id": "cmp11",
        "termA": "Affect",
        "termB": "Effect",
        "summary": "'Affect' is almost always a VERB meaning to influence. 'Effect' is almost always a NOUN meaning the result.",
        "ruleA": "Verb: The policy change will affect all team members.",
        "ruleB": "Noun: The new policy had an immediate positive effect on productivity.",
        "examplesA": ["Lack of sleep severely affects cognitive performance.", "Don't let setbacks affect your morale."],
        "examplesB": ["The greenhouse effect is accelerating global climate change.", "What was the effect of that change?"],
        "trick": "RAVEN: Remember Affect is a Verb, Effect is a Noun."
    },
    {
        "id": "cmp12",
        "termA": "Raise",
        "termB": "Rise",
        "summary": "'Raise' is transitive (requires an object: you raise something). 'Rise' is intransitive (no object: something goes up on its own).",
        "ruleA": "Subject + Raise + Object: The company raised salaries by 15%. Raise your hand.",
        "ruleB": "Subject + Rise: The sun rises in the east. Temperatures are rising across the country.",
        "examplesA": ["Please raise your hand if you have a question.", "They raised 5 million dollars in funding."],
        "examplesB": ["Smoke rose into the winter sky.", "The GDP of India continues to rise steadily."],
        "trick": "Raise needs a target (raise something). Rise happens by itself."
    },
    {
        "id": "cmp13",
        "termA": "Lie",
        "termB": "Lay",
        "summary": "'Lie' means to recline or rest oneself (no object). 'Lay' means to put or place an object down.",
        "ruleA": "Lie (past: lay, participle: lain): 'I need to lie down for twenty minutes.'",
        "ruleB": "Lay (past: laid, participle: laid): 'Please lay the documents on the conference table.'",
        "examplesA": ["Don't lie on the cold floor.", "He lay awake thinking about the architecture."],
        "examplesB": ["She laid the baby gently in the cradle.", "Lay your cards on the table."],
        "trick": "Lay = put down something. Lie = recline yourself."
    },
    {
        "id": "cmp14",
        "termA": "Each",
        "termB": "Every",
        "summary": "'Each' views members of a group as distinct individuals (for 2 or more). 'Every' views all members collectively together (for 3 or more).",
        "ruleA": "Focuses on individuality: 'Each student received a personalized certificate.'",
        "ruleB": "Focuses on the entire collection: 'Every participant attended the closing ceremony.'",
        "examplesA": ["Each of the two candidates brought unique strengths.", "Look at each line of code carefully."],
        "examplesB": ["I read technical articles every single morning.", "Every team member contributed."],
        "trick": "If there are only TWO items, you MUST use 'Each' (Each hand, each side of the road)."
    },
    {
        "id": "cmp15",
        "termA": "Used to",
        "termB": "Be used to",
        "summary": "'Used to + Base Verb' describes a past habit no longer true. 'Be used to + V-ing' means accustomed or familiar with something.",
        "ruleA": "Past habit: I used to play cricket every evening when I was in school.",
        "ruleB": "Accustomed now: I am used to waking up early at 5 AM.",
        "examplesA": ["She used to commute by train before she bought a car.", "We used to live in Hyderabad."],
        "examplesB": ["He is used to working in high-pressure startup environments.", "Are you used to the spicy food?"],
        "trick": "If you see 'am/is/are/was/were' before 'used to', you MUST add '-ing' to the following verb."
    }
]

# AI Grammar Knowledge Base for instant context-aware answers
AI_GRAMMAR_KNOWLEDGE_BASE = {
    "although": {
        "meaning": "'Although' is a conjunction meaning 'in spite of the fact that' or 'even though'. It is used to link two contrasting ideas in a single sentence.",
        "part_of_speech": "Conjunction",
        "cefr": "B1",
        "formula": "Although + [Subject + Verb clause], [Main clause].",
        "examples": [
            "Although the exam was challenging, Priya passed with top honors.",
            "Although he works remotely, he maintains close bonds with his teammates.",
            "We decided to go for an evening run although it was drizzling."
        ],
        "collocations": ["although it is true that", "although not necessary", "although difficult"],
        "mistake": "Never pair 'although' with 'but' in the same sentence. Say: 'Although it rained, we went out', NOT 'Although it rained, but we went out.'",
        "speaking_drill": "Speak one sentence contrasting your busy schedule with your daily English practice using 'Although'."
    },
    "despite": {
        "meaning": "'Despite' is a preposition meaning 'without being affected by' or 'in spite of'. Unlike 'although', it takes a noun phrase or a gerund (-ing), never a full clause.",
        "part_of_speech": "Preposition",
        "cefr": "B2",
        "formula": "Despite + [Noun phrase or Verb-ing], [Main clause].",
        "examples": [
            "Despite the heavy monsoon rain, the flight landed safely on time.",
            "Despite having no prior coding experience, she built a full-stack web app in six months.",
            "He remained calm despite the intense pressure from leadership."
        ],
        "collocations": ["despite the fact that", "despite all odds", "despite severe warnings"],
        "mistake": "Never say 'despite of'. Say 'despite the rain' or 'in spite of the rain'.",
        "speaking_drill": "Speak one sentence describing an obstacle you overcame using 'Despite'."
    },
    "since and for": {
        "meaning": "'Since' points to a specific beginning timestamp, while 'For' measures total elapsed duration.",
        "part_of_speech": "Prepositions / Adverbs of Time",
        "cefr": "A2 - B1",
        "formula": "Present Perfect + Since [Starting point] | Present Perfect + For [Duration]",
        "examples": [
            "I have been living in this city since 2018.",
            "I have lived in this city for six years.",
            "She has been studying software architecture since 9 AM.",
            "She has been studying for five hours."
        ],
        "collocations": ["since then", "since childhood", "for ages", "for a while"],
        "mistake": "Don't say: 'I am here since 3 days.' Say: 'I have been here for 3 days.'",
        "speaking_drill": "State how long you have lived in your home using both 'since' and 'for'."
    },
    "i have went": {
        "meaning": "'I have went' is incorrect because the auxiliary verb 'have' must always be followed by the Past Participle (V3), which is 'gone' (or 'been'), not the Past Simple form 'went' (V2).",
        "part_of_speech": "Verb Tense Correction",
        "cefr": "A2",
        "formula": "Subject + have/has + Past Participle (V3) -> 'I have gone' or 'I went'",
        "examples": [
            "Incorrect: 'I have went to Mumbai last month.' -> Correct: 'I went to Mumbai last month.' (Past Simple)",
            "Incorrect: 'I have went there many times.' -> Correct: 'I have been there many times.' (Present Perfect)"
        ],
        "mistake": "Go -> Went (V2, past simple alone) -> Gone (V3, with have/has/had).",
        "speaking_drill": "Say aloud: 'I have been to three cities in India, and last summer I went to Delhi.'"
    },
    "present perfect": {
        "meaning": "The Present Perfect tense connects completed past actions to the present moment. It emphasizes either life experiences, ongoing duration, or recent actions with visible consequences right now.",
        "part_of_speech": "Tense Aspect",
        "cefr": "B1",
        "formula": "Subject + have/has + Past Participle (V3)",
        "examples": [
            "I have finished my assignment; now I can relax.",
            "Have you ever presented in front of an international audience?",
            "He has worked on cloud systems for over eight years.",
            "The team has just deployed the update to production."
        ],
        "collocations": ["already", "just", "yet", "ever", "never", "so far", "recently"],
        "mistake": "Never combine Present Perfect with specific finished past times. Don't say: 'I have completed it yesterday.' Say: 'I completed it yesterday.'",
        "speaking_drill": "Speak 2 sentences about things you have accomplished this month."
    }
}

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
     "tip": "Use Second Conditional when imagining hypothetical improvements."},
    {"id": "sb6", "scrambled": ["was", "written", "The", "by", "report", "Sarah"],
     "correct": "The report was written by Sarah",
     "grammar_pattern": "Passive Voice: Object + was + V3 + by Agent",
     "tip": "In passive sentences, the recipient of the action comes first."},
    {"id": "sb7", "scrambled": ["been", "for", "have", "hours", "coding", "I", "three"],
     "correct": "I have been coding for three hours",
     "grammar_pattern": "Present Perfect Continuous: Subject + have been + V-ing + for Duration",
     "tip": "Use 'have been + -ing' to emphasize ongoing activity still in progress."},
    {"id": "sb8", "scrambled": ["Although", "rained", "it", "we", "the", "attended", "match"],
     "correct": "Although it rained we attended the match",
     "grammar_pattern": "Conjunction Clause: Although + Clause 1 + Clause 2",
     "tip": "Never put 'but' in the main clause when using 'Although'."}
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
    {"id": "dc4", "title": "Ask AI Grammar Coach a Question", "xp": 40, "type": "grammar",
     "task": "Check a sentence or ask for a grammar rule breakdown using the AI Coach.",
     "target_count": 1},
    {"id": "dc5", "title": "Hold a 2-Minute Dialogue with AI", "xp": 60, "type": "conversation",
     "task": "Engage in an interactive roleplay session with your chosen coach.",
     "target_seconds": 120}
]
