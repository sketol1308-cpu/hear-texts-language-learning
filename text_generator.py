import random

class TextGenerator:
    def __init__(self):
        self.texts = self._load_texts()

    def _load_texts(self):
        """Load all predefined texts with questions for each language, level, and topic"""
        return {
            "English": {
                "beginner": {
                    "daily_life": [
                        {
                            "text": "My name is Anna. I am a student. I live in a small house with my family. Every morning, I wake up at seven o'clock. I eat breakfast with my mother and father. I like toast and orange juice. After breakfast, I go to school. I walk to school because it is near my house. At school, I learn many things. I like math and art. My teacher is very nice. After school, I come home and do my homework. In the evening, I play with my dog. His name is Max. I love my life.",
                            "questions": [
                                "What is the girl's name?",
                                "What time does she wake up?",
                                "What does she eat for breakfast?",
                                "How does she go to school?",
                                "What is her dog's name?"
                            ]
                        },
                        {
                            "text": "Today is Saturday. I do not go to school on Saturday. I stay at home with my family. In the morning, I help my mother clean the house. We wash the dishes and sweep the floor. Then I play video games with my brother. He is twelve years old. I am ten. For lunch, we eat sandwiches. In the afternoon, we go to the park. I like to run and play on the swings. My brother likes to play football. We have fun together. At night, we watch a movie. I am happy.",
                            "questions": [
                                "What day is it?",
                                "What does the child do in the morning?",
                                "How old is the brother?",
                                "What do they eat for lunch?",
                                "What does the brother like to do at the park?"
                            ]
                        }
                    ],
                    "travel": [
                        {
                            "text": "I am on vacation. I am at the beach with my family. The weather is very hot and sunny. The water is blue and beautiful. I swim in the sea every day. My sister builds sandcastles. They are very big. My father reads a book under an umbrella. My mother takes many photos. At night, we eat fish at a restaurant. The food is delicious. I love the beach. This is a great vacation.",
                            "questions": [
                                "Where is the family?",
                                "What is the weather like?",
                                "What does the sister do?",
                                "What does the father do?",
                                "What do they eat at night?"
                            ]
                        }
                    ],
                    "nature": [
                        {
                            "text": "I like nature. I live near a forest. There are many trees and flowers. I see birds every day. They sing beautiful songs. In the forest, there are rabbits and squirrels. I like to watch them. Sometimes I see a deer. Deer are very shy. Near my house, there is a small river. The water is clean and cold. Fish swim in the river. I sit by the river and listen to the water. It is very peaceful. I love nature.",
                            "questions": [
                                "Where does the person live?",
                                "What animals are in the forest?",
                                "What is near the house?",
                                "What do the birds do?",
                                "How is the water in the river?"
                            ]
                        }
                    ],
                    "technology": [
                        {
                            "text": "I have a computer. It is on my desk. I use my computer every day. I play games and watch videos. I also do my homework on the computer. My father has a laptop. He uses it for work. My mother has a smartphone. She calls her friends and takes photos. We have a television in the living room. We watch movies together. Technology is very useful. It helps us every day.",
                            "questions": [
                                "Where is the computer?",
                                "What does the person do on the computer?",
                                "What does the father use for work?",
                                "What does the mother do with her smartphone?",
                                "Where is the television?"
                            ]
                        }
                    ],
                    "family": [
                        {
                            "text": "My family is not very big. I have a mother, a father, and one sister. My mother's name is Lisa. She is a doctor. She helps sick people. My father's name is John. He works in an office. My sister is called Emma. She is eight years old. I am eleven. We live in a nice house with a garden. We have a cat named Whiskers. On Sundays, we eat dinner together. My grandmother sometimes visits us. I love my family very much.",
                            "questions": [
                                "How many people are in the family?",
                                "What is the mother's job?",
                                "What is the sister's name?",
                                "What pet do they have?",
                                "Who visits them sometimes?"
                            ]
                        }
                    ],
                    "school": [
                        {
                            "text": "I go to school every day. My school is big and has many classrooms. I am in class 5B. My favorite subject is English. I also like music and sports. My best friend is called Tom. We sit together in class. Our teacher is Mrs. Brown. She is very kind. We have lessons from eight to two. At lunch, I eat in the cafeteria. After school, I take the bus home. I like my school.",
                            "questions": [
                                "What class is the student in?",
                                "What is their favorite subject?",
                                "What is the best friend's name?",
                                "What is the teacher's name?",
                                "How does the student go home?"
                            ]
                        }
                    ],
                    "hobbies": [
                        {
                            "text": "I have many hobbies. I like to read books. My favorite books are about animals. I also like to draw pictures. I draw cats and dogs. On weekends, I play football with my friends. We play in the park. My brother likes video games. He plays every day. My sister likes to dance. She takes dance lessons on Tuesdays. Hobbies are fun. They make me happy.",
                            "questions": [
                                "What does the person like to read about?",
                                "What animals do they draw?",
                                "Where do they play football?",
                                "What does the brother like?",
                                "When does the sister have dance lessons?"
                            ]
                        }
                    ],
                    "food": [
                        {
                            "text": "I like food very much. For breakfast, I eat cereal with milk. Sometimes I have eggs and toast. For lunch, I usually eat a sandwich. My favorite sandwich has cheese and ham. For dinner, my mother cooks pasta or rice with vegetables. I love pizza too. We order pizza on Fridays. I don't like fish very much. My favorite drink is apple juice. I also like chocolate milk.",
                            "questions": [
                                "What do they eat for breakfast?",
                                "What is in their favorite sandwich?",
                                "What does the mother cook for dinner?",
                                "When do they order pizza?",
                                "What is their favorite drink?"
                            ]
                        }
                    ],
                    "shopping": [
                        {
                            "text": "Today I go shopping with my mother. We go to the supermarket. We need milk, bread, and eggs. My mother buys fruits and vegetables too. I want some chocolate. My mother says okay. The supermarket is very big. There are many people. We pay at the cashier. The total is twenty euros. We put the bags in the car. Then we go home. Shopping is fun.",
                            "questions": [
                                "Who goes shopping?",
                                "What do they need to buy?",
                                "What does the child want?",
                                "How much do they pay?",
                                "How do they carry the bags?"
                            ]
                        }
                    ],
                    "sports": [
                        {
                            "text": "I love sports. My favorite sport is basketball. I play basketball every Wednesday. My team has ten players. We practice in the school gym. I am not very tall, but I am fast. My friend plays tennis. He has lessons on Saturdays. My sister swims in a pool. She is very good. In summer, we play football outside. Sports are good for health. They make you strong.",
                            "questions": [
                                "What is their favorite sport?",
                                "When do they play basketball?",
                                "How many players are on the team?",
                                "What sport does the friend play?",
                                "What does the sister do?"
                            ]
                        }
                    ],
                    "health": [
                        {
                            "text": "It is important to be healthy. I try to eat good food. Fruits and vegetables are healthy. I drink water every day. I also sleep eight hours every night. Exercise is important too. I walk to school every morning. On weekends, I ride my bike. When I am sick, I go to the doctor. The doctor gives me medicine. I wash my hands before eating. Being healthy makes me happy.",
                            "questions": [
                                "What foods are healthy?",
                                "How many hours do they sleep?",
                                "How do they go to school?",
                                "What do they do on weekends?",
                                "When do they wash their hands?"
                            ]
                        }
                    ],
                    "weather": [
                        {
                            "text": "Today the weather is nice. The sun is shining. It is warm outside. I wear a t-shirt and shorts. In winter, it is very cold. Sometimes it snows. I wear a jacket and boots. I like to play in the snow. In autumn, the leaves fall from trees. They are red and yellow. Spring is my favorite season. The flowers bloom and birds sing. I check the weather every morning.",
                            "questions": [
                                "What is the weather like today?",
                                "What do they wear in winter?",
                                "What color are the leaves in autumn?",
                                "What is their favorite season?",
                                "When do flowers bloom?"
                            ]
                        }
                    ],
                    "city": [
                        {
                            "text": "I live in a big city. There are many tall buildings. Cars and buses drive on the streets. People walk on the sidewalks. Near my house, there is a park. I play there with my friends. There is also a library. I borrow books from the library. The city has many shops and restaurants. My favorite restaurant sells ice cream. The city is noisy but fun. I like living here.",
                            "questions": [
                                "What is near the house?",
                                "Where do they play with friends?",
                                "What do they do at the library?",
                                "What does the favorite restaurant sell?",
                                "How is the city described?"
                            ]
                        }
                    ],
                    "transport": [
                        {
                            "text": "There are many ways to travel. I take the bus to school. The bus is yellow. My father drives a car to work. My mother rides a bicycle. Bicycles are good for the environment. In big cities, people use the subway. Trains are very fast. Airplanes fly in the sky. They take people to other countries. I want to travel by airplane one day. I like watching the cars go by.",
                            "questions": [
                                "How does the child go to school?",
                                "What color is the bus?",
                                "What does the mother ride?",
                                "What do people use in big cities?",
                                "Where do airplanes take people?"
                            ]
                        }
                    ],
                    "environment": [
                        {
                            "text": "We must take care of our planet. The Earth is our home. We should not throw trash on the ground. We put trash in the bin. We can recycle paper and plastic. This helps the environment. We should save water. I turn off the tap when I brush my teeth. Trees are important. They give us clean air. We should plant more trees. Everyone can help the planet.",
                            "questions": [
                                "Where should we put trash?",
                                "What can we recycle?",
                                "How can we save water?",
                                "Why are trees important?",
                                "Who can help the planet?"
                            ]
                        }
                    ]
                },
                "intermediate": {
                    "daily_life": [
                        {
                            "text": "Sarah works as a nurse at the city hospital. Her job is challenging but rewarding. She usually starts her shift at six in the morning and works until two in the afternoon. During her shift, she takes care of many patients. She checks their temperature, gives them medicine, and makes sure they are comfortable. Sarah loves helping people feel better. After work, she goes to the gym to exercise. She believes that staying healthy is important, especially for someone in the medical field. In the evenings, she enjoys cooking dinner for her family. Her husband, Tom, is a teacher. They have two children who are in elementary school. On weekends, the family likes to go hiking in the nearby mountains or visit their grandparents in the countryside.",
                            "questions": [
                                "What is Sarah's profession?",
                                "What time does her shift start and end?",
                                "What does she do after work?",
                                "What is her husband's job?",
                                "What does the family do on weekends?"
                            ]
                        }
                    ],
                    "travel": [
                        {
                            "text": "Last summer, my friends and I decided to travel to Spain. We had been planning the trip for months and were excited to finally go. We flew from London to Barcelona, which took about two hours. Barcelona was amazing. The architecture was stunning, especially the famous Sagrada Familia church designed by Gaudi. We spent three days exploring the city, visiting museums, and enjoying the local food. The tapas were delicious, and we tried paella for the first time. After Barcelona, we took a train to Madrid, the capital city. Madrid had a different atmosphere but was equally beautiful. We visited the Prado Museum and saw paintings by famous artists. The trip was unforgettable, and we promised to travel together again next year.",
                            "questions": [
                                "Where did they travel to?",
                                "How long was the flight from London to Barcelona?",
                                "What famous church did they see?",
                                "How did they get from Barcelona to Madrid?",
                                "What museum did they visit in Madrid?"
                            ]
                        }
                    ],
                    "nature": [
                        {
                            "text": "The Amazon rainforest is one of the most important ecosystems on Earth. It covers a vast area in South America, primarily in Brazil. The rainforest is home to millions of species of plants, animals, and insects. Many of these species cannot be found anywhere else in the world. The Amazon River flows through the forest and is the second longest river in the world. Scientists believe that the rainforest produces about twenty percent of the world's oxygen. Unfortunately, deforestation is a serious problem. Every year, large areas of the forest are cut down for farming and logging. Many organizations are working to protect the Amazon and save its incredible biodiversity. It is crucial that we take action to preserve this natural wonder for future generations.",
                            "questions": [
                                "Where is the Amazon rainforest located?",
                                "What percentage of the world's oxygen does it produce?",
                                "What river flows through the forest?",
                                "What is causing problems for the rainforest?",
                                "Why is it important to protect the Amazon?"
                            ]
                        }
                    ],
                    "technology": [
                        {
                            "text": "Artificial intelligence is changing the way we live and work. AI systems can now perform tasks that previously required human intelligence. For example, virtual assistants like Siri and Alexa can answer questions, play music, and control smart home devices. Self-driving cars use AI to navigate roads and avoid obstacles. In medicine, AI helps doctors diagnose diseases more accurately. However, some people are worried about the impact of AI on employment. As machines become smarter, some jobs may disappear. Experts believe that new types of jobs will be created, but workers will need to learn new skills. Despite the challenges, AI has the potential to solve many of the world's problems, from climate change to healthcare.",
                            "questions": [
                                "What are some examples of virtual assistants?",
                                "How do self-driving cars use AI?",
                                "How does AI help in medicine?",
                                "What are some people worried about?",
                                "What will workers need to do as AI develops?"
                            ]
                        }
                    ]
                },
                "advanced": {
                    "daily_life": [
                        {
                            "text": "The concept of work-life balance has become increasingly significant in contemporary society, particularly as the boundaries between professional and personal life continue to blur. With the advent of remote work and digital communication tools, many employees find themselves constantly connected to their jobs, even during what should be their leisure time. This perpetual connectivity can lead to burnout, a state of chronic stress that manifests through emotional exhaustion, cynicism, and reduced professional efficacy. Mental health professionals emphasize the importance of establishing clear boundaries between work and personal activities. Strategies such as designating specific work hours, creating a dedicated workspace at home, and deliberately disconnecting from work-related communications during evenings and weekends can significantly improve overall well-being. Furthermore, companies are beginning to recognize that employees who maintain a healthy balance tend to be more productive, creative, and loyal. Progressive organizations are implementing policies such as flexible working hours, mental health days, and mandatory vacation time to support their workforce.",
                            "questions": [
                                "What factors have contributed to the blurring of work-life boundaries?",
                                "What is burnout and how does it manifest?",
                                "What strategies can help maintain work-life balance?",
                                "How do companies benefit from employees with good work-life balance?",
                                "What policies are progressive organizations implementing?"
                            ]
                        }
                    ],
                    "travel": [
                        {
                            "text": "Sustainable tourism has emerged as a critical consideration for travelers who wish to explore the world while minimizing their environmental and cultural impact. Traditional mass tourism often leads to overcrowding at popular destinations, environmental degradation, and the commodification of local cultures. In contrast, sustainable tourism emphasizes responsible travel practices that conserve natural resources, respect indigenous communities, and support local economies. Travelers can adopt various strategies to reduce their footprint, such as choosing eco-friendly accommodations that utilize renewable energy and implement water conservation measures. Additionally, supporting locally-owned businesses and purchasing handcrafted goods directly from artisans ensures that tourism revenue benefits the community rather than international corporations. Some destinations have implemented visitor caps to prevent overtourism, while others have invested in infrastructure that reduces the environmental impact of tourism activities. Carbon offset programs allow travelers to compensate for the emissions generated by their flights, though critics argue that such programs should not be seen as a substitute for reducing travel-related emissions altogether.",
                            "questions": [
                                "What are the negative effects of traditional mass tourism?",
                                "How does sustainable tourism differ from conventional tourism?",
                                "What strategies can travelers use to reduce their environmental impact?",
                                "How can tourists ensure their spending benefits local communities?",
                                "What is the purpose of carbon offset programs, and what criticism do they face?"
                            ]
                        }
                    ],
                    "nature": [
                        {
                            "text": "Climate change represents one of the most pressing challenges facing humanity in the twenty-first century. The scientific consensus is unequivocal: global temperatures are rising at an unprecedented rate due to human activities, primarily the burning of fossil fuels and deforestation. The consequences of this warming are already visible across the planet. Arctic sea ice is melting at an alarming pace, contributing to rising sea levels that threaten coastal communities worldwide. Extreme weather events, including hurricanes, droughts, and wildfires, are becoming more frequent and severe. Biodiversity is declining as species struggle to adapt to rapidly changing conditions. The Paris Agreement of 2015 represented a landmark moment in international climate diplomacy, with nations committing to limit global warming to well below two degrees Celsius above pre-industrial levels. However, current pledges remain insufficient to achieve this goal. Scientists warn that without drastic reductions in greenhouse gas emissions within the next decade, the world will face irreversible environmental damage with catastrophic consequences for ecosystems and human civilization alike.",
                            "questions": [
                                "What is the scientific consensus on the cause of rising global temperatures?",
                                "What are some visible consequences of climate change mentioned in the text?",
                                "What was the significance of the Paris Agreement?",
                                "Why are current international pledges considered insufficient?",
                                "What do scientists warn about the coming decade?"
                            ]
                        }
                    ],
                    "technology": [
                        {
                            "text": "The proliferation of social media platforms has fundamentally transformed how individuals communicate, consume information, and form communities. While these platforms have democratized content creation and enabled unprecedented global connectivity, they have also introduced significant challenges to society. Algorithmic content curation, designed to maximize user engagement, often creates echo chambers where individuals are exposed primarily to information that reinforces their existing beliefs. This phenomenon has been linked to increased political polarization and the spread of misinformation. Privacy concerns have intensified as platforms collect vast amounts of personal data for targeted advertising. The psychological effects of social media use, particularly among adolescents, have become a subject of intense research and debate. Studies suggest correlations between heavy social media use and increased rates of anxiety, depression, and feelings of inadequacy. Regulatory bodies worldwide are grappling with how to address these issues while preserving the benefits of digital communication. Proposed solutions range from stricter data protection laws to mandatory algorithmic transparency and age verification measures.",
                            "questions": [
                                "How has social media transformed communication and community formation?",
                                "What are echo chambers and how do algorithms contribute to them?",
                                "What privacy concerns are associated with social media platforms?",
                                "What psychological effects of social media have researchers identified?",
                                "What types of regulations are being proposed to address social media challenges?"
                            ]
                        }
                    ]
                }
            },
            "French": {
                "beginner": {
                    "daily_life": [
                        {
                            "text": "Je m'appelle Marie. J'ai douze ans. J'habite dans une petite ville en France. J'ai une famille: ma mère, mon père et mon frère. Mon frère s'appelle Lucas. Il a dix ans. Chaque matin, je me lève à sept heures. Je prends le petit déjeuner avec ma famille. Je mange des croissants et je bois du lait. Après, je vais à l'école. J'aime l'école. Ma matière préférée est le français. Après l'école, je rentre à la maison. Je fais mes devoirs. Le soir, je regarde la télévision avec ma famille. J'aime ma vie.",
                            "questions": [
                                "Comment s'appelle la fille?",
                                "Quel âge a-t-elle?",
                                "Comment s'appelle son frère?",
                                "Qu'est-ce qu'elle mange au petit déjeuner?",
                                "Quelle est sa matière préférée?"
                            ]
                        },
                        {
                            "text": "C'est le week-end. Je ne vais pas à l'école. Je reste à la maison. Le matin, je fais la grasse matinée. Je me lève à dix heures. Ma mère prépare le petit déjeuner. Nous mangeons des crêpes. C'est délicieux! L'après-midi, je joue avec mes amis. Nous allons au parc. Je fais du vélo. Mon ami joue au football. Le soir, ma famille va au restaurant. Nous mangeons de la pizza. J'adore le week-end.",
                            "questions": [
                                "Pourquoi ne va-t-elle pas à l'école?",
                                "À quelle heure se lève-t-elle?",
                                "Qu'est-ce qu'ils mangent au petit déjeuner?",
                                "Que fait son ami au parc?",
                                "Où va la famille le soir?"
                            ]
                        }
                    ],
                    "travel": [
                        {
                            "text": "Je suis en vacances. Je suis à la mer avec ma famille. Le temps est beau. Il fait chaud et le soleil brille. La mer est bleue. Je nage tous les jours. C'est super! Mon père fait de la plongée. Ma mère lit un livre sur la plage. Ma sœur collectionne des coquillages. Le soir, nous mangeons des fruits de mer. Le poisson est très bon. J'aime les vacances à la mer.",
                            "questions": [
                                "Où est la famille?",
                                "Quel temps fait-il?",
                                "Que fait le père?",
                                "Que fait la mère?",
                                "Qu'est-ce qu'ils mangent le soir?"
                            ]
                        }
                    ],
                    "nature": [
                        {
                            "text": "J'aime la nature. Il y a une forêt près de ma maison. La forêt est grande et belle. Il y a beaucoup d'arbres et de fleurs. J'entends les oiseaux chanter. C'est magnifique! Dans la forêt, il y a des animaux. Je vois des lapins et des écureuils. Parfois, je vois un cerf. Les cerfs sont timides. Il y a aussi une rivière. L'eau est claire. Je m'assieds près de la rivière. C'est calme et paisible.",
                            "questions": [
                                "Qu'est-ce qu'il y a près de la maison?",
                                "Quels animaux sont dans la forêt?",
                                "Que font les oiseaux?",
                                "Comment est l'eau de la rivière?",
                                "Comment sont les cerfs?"
                            ]
                        }
                    ],
                    "technology": [
                        {
                            "text": "J'ai un ordinateur. Il est dans ma chambre. J'utilise mon ordinateur tous les jours. Je joue à des jeux vidéo. Je regarde des vidéos aussi. Je fais mes devoirs sur l'ordinateur. Mon père a un téléphone portable. Il envoie des messages à ses amis. Ma mère utilise une tablette. Elle lit des livres numériques. Nous avons une télévision dans le salon. Nous regardons des films ensemble. La technologie est très utile.",
                            "questions": [
                                "Où est l'ordinateur?",
                                "Que fait-il sur l'ordinateur?",
                                "Qu'est-ce que le père utilise?",
                                "Que fait la mère avec sa tablette?",
                                "Où est la télévision?"
                            ]
                        }
                    ]
                },
                "intermediate": {
                    "daily_life": [
                        {
                            "text": "Sophie est médecin dans un hôpital parisien. Elle travaille depuis dix ans dans le service de pédiatrie. Son travail est exigeant mais elle adore s'occuper des enfants malades. Elle commence sa journée à huit heures du matin. D'abord, elle fait le tour des chambres pour voir ses patients. Elle vérifie leur état de santé et discute avec les parents. Sophie passe environ une heure à examiner chaque enfant. L'après-midi, elle a des consultations dans son cabinet. Le soir, elle rentre chez elle vers dix-neuf heures. Elle habite avec son mari et leurs deux enfants dans un appartement près de la Tour Eiffel. Le week-end, la famille aime visiter les musées ou se promener dans les jardins du Luxembourg.",
                            "questions": [
                                "Quel est le métier de Sophie?",
                                "Dans quel service travaille-t-elle?",
                                "Que fait-elle le matin à l'hôpital?",
                                "À quelle heure rentre-t-elle chez elle?",
                                "Que fait la famille le week-end?"
                            ]
                        }
                    ],
                    "travel": [
                        {
                            "text": "L'été dernier, j'ai fait un voyage inoubliable au Maroc. J'ai pris l'avion de Paris à Marrakech. Le vol a duré trois heures. Quand je suis arrivé, la chaleur était intense. Marrakech est une ville fascinante avec ses souks colorés et son architecture traditionnelle. J'ai visité la célèbre place Jemaa el-Fna où les vendeurs, les musiciens et les conteurs créent une atmosphère unique. J'ai goûté le tajine et le couscous marocains qui étaient délicieux. Ensuite, j'ai fait une excursion dans le désert du Sahara. Nous avons dormi dans un camp de tentes sous les étoiles. C'était une expérience magique. Ce voyage m'a permis de découvrir une culture riche et accueillante.",
                            "questions": [
                                "Combien de temps a duré le vol?",
                                "Qu'est-ce qui rend la place Jemaa el-Fna spéciale?",
                                "Quels plats marocains a-t-il goûtés?",
                                "Où ont-ils dormi dans le désert?",
                                "Comment décrit-il la culture marocaine?"
                            ]
                        }
                    ],
                    "nature": [
                        {
                            "text": "Les Alpes françaises sont une destination magnifique pour les amoureux de la nature. Ces montagnes majestueuses offrent des paysages à couper le souffle tout au long de l'année. En hiver, des milliers de skieurs viennent profiter des pistes enneigées. Les stations comme Chamonix et Courchevel sont mondialement connues. En été, les randonneurs explorent les sentiers alpins et admirent les lacs cristallins. La faune alpine est diverse: on peut observer des marmottes, des chamois et parfois des aigles royaux. Le Mont Blanc, le plus haut sommet d'Europe occidentale, attire des alpinistes du monde entier. Malheureusement, le changement climatique affecte les glaciers qui reculent d'année en année. Il est essentiel de protéger cet environnement fragile pour les générations futures.",
                            "questions": [
                                "Quelles stations de ski sont mentionnées?",
                                "Que font les visiteurs en été?",
                                "Quels animaux peut-on observer dans les Alpes?",
                                "Quel est le plus haut sommet d'Europe occidentale?",
                                "Quel problème environnemental affecte les Alpes?"
                            ]
                        }
                    ],
                    "technology": [
                        {
                            "text": "Les réseaux sociaux ont transformé notre façon de communiquer. Aujourd'hui, des milliards de personnes utilisent des plateformes comme Facebook, Instagram et Twitter chaque jour. Ces outils permettent de rester en contact avec des amis et de la famille partout dans le monde. Ils facilitent aussi le partage d'informations et la création de communautés en ligne. Cependant, les réseaux sociaux présentent également des risques. La désinformation se propage rapidement, et certains utilisateurs passent trop de temps devant leurs écrans. Les experts s'inquiètent particulièrement de l'impact sur les jeunes. Des études montrent un lien entre l'utilisation excessive des réseaux sociaux et l'anxiété ou la dépression. Il est important d'utiliser ces technologies de manière équilibrée et de vérifier les informations avant de les partager.",
                            "questions": [
                                "Quelles plateformes de réseaux sociaux sont mentionnées?",
                                "Quels sont les avantages des réseaux sociaux?",
                                "Quels risques présentent les réseaux sociaux?",
                                "Pourquoi les experts s'inquiètent-ils pour les jeunes?",
                                "Quel conseil est donné à la fin du texte?"
                            ]
                        }
                    ]
                },
                "advanced": {
                    "daily_life": [
                        {
                            "text": "La question de l'équilibre entre vie professionnelle et vie personnelle est devenue un sujet de préoccupation majeur dans la société française contemporaine. Avec l'essor du télétravail, accéléré par la pandémie de Covid-19, les frontières entre le bureau et le domicile se sont considérablement estompées. De nombreux salariés éprouvent des difficultés à déconnecter, consultant leurs courriels professionnels tard le soir ou pendant les week-ends. Cette hyper-connexion peut engendrer un épuisement professionnel, communément appelé burn-out, qui se manifeste par une fatigue chronique, un cynisme accru et une diminution de l'efficacité au travail. Face à ce constat, le législateur français a instauré le droit à la déconnexion en 2017, obligeant les entreprises de plus de cinquante salariés à négocier des accords sur ce sujet. Par ailleurs, certaines organisations expérimentent la semaine de quatre jours, estimant que des employés reposés sont plus productifs et créatifs. Cette évolution reflète une prise de conscience collective de l'importance du bien-être au travail.",
                            "questions": [
                                "Quel événement a accéléré le développement du télétravail?",
                                "Qu'est-ce que le burn-out et comment se manifeste-t-il?",
                                "Qu'est-ce que le droit à la déconnexion instauré en 2017?",
                                "Quelle expérimentation certaines entreprises mènent-elles?",
                                "Pourquoi considère-t-on que des employés reposés sont bénéfiques pour l'entreprise?"
                            ]
                        }
                    ],
                    "travel": [
                        {
                            "text": "Le tourisme de masse représente un défi considérable pour de nombreuses destinations à travers le monde. Venise, Barcelone et Amsterdam figurent parmi les villes européennes les plus touchées par ce phénomène. L'afflux massif de visiteurs engendre une pression insoutenable sur les infrastructures locales, la hausse des prix de l'immobilier qui chasse les résidents du centre-ville, et la transformation des quartiers historiques en zones commerciales standardisées. Face à cette situation, plusieurs municipalités ont mis en place des mesures restrictives. Venise a instauré une taxe d'entrée pour les visiteurs d'un jour, tandis qu'Amsterdam limite la construction de nouveaux hôtels et interdit les visites guidées dans le quartier rouge. Le concept de tourisme durable gagne en importance, encourageant les voyageurs à privilégier les destinations moins fréquentées, à séjourner plus longtemps dans chaque lieu et à respecter les communautés locales. Cette approche nécessite une prise de conscience individuelle mais aussi des politiques publiques cohérentes à l'échelle internationale.",
                            "questions": [
                                "Quelles villes européennes sont particulièrement touchées par le tourisme de masse?",
                                "Quels problèmes le tourisme de masse engendre-t-il?",
                                "Quelle mesure Venise a-t-elle instaurée?",
                                "Quelles restrictions Amsterdam a-t-elle mises en place?",
                                "Quels comportements le tourisme durable encourage-t-il?"
                            ]
                        }
                    ],
                    "nature": [
                        {
                            "text": "La biodiversité mondiale connaît un déclin alarmant qui constitue une menace existentielle pour l'humanité. Selon les scientifiques, nous traversons actuellement la sixième extinction de masse de l'histoire de la Terre, la première causée par une seule espèce: l'être humain. Les causes de cette érosion de la biodiversité sont multiples: la destruction des habitats naturels au profit de l'agriculture intensive, la surexploitation des ressources marines, la pollution plastique qui envahit les océans, et bien sûr, le changement climatique qui modifie les écosystèmes plus rapidement que les espèces ne peuvent s'adapter. En France, la population d'oiseaux a diminué de trente pour cent en trois décennies, tandis que soixante-quinze pour cent des insectes volants ont disparu en Europe. Ces chiffres sont d'autant plus préoccupants que les insectes jouent un rôle crucial dans la pollinisation des cultures. Des initiatives de conservation existent, comme la création d'aires marines protégées ou la restauration des zones humides, mais elles restent insuffisantes face à l'ampleur du défi.",
                            "questions": [
                                "Qu'est-ce qui distingue la sixième extinction de masse des précédentes?",
                                "Quelles sont les principales causes du déclin de la biodiversité?",
                                "Quel pourcentage d'oiseaux a disparu en France en trois décennies?",
                                "Pourquoi la disparition des insectes est-elle particulièrement préoccupante?",
                                "Quelles initiatives de conservation sont mentionnées?"
                            ]
                        }
                    ],
                    "technology": [
                        {
                            "text": "L'intelligence artificielle suscite autant d'espoirs que d'inquiétudes dans notre société. Les avancées récentes dans le domaine du traitement du langage naturel ont permis le développement d'assistants virtuels capables de converser de manière étonnamment fluide avec les humains. Dans le secteur médical, des algorithmes diagnostiquent certains cancers avec une précision supérieure à celle des médecins. L'IA optimise également la consommation énergétique des bâtiments et améliore l'efficacité des chaînes logistiques. Cependant, ces technologies soulèvent des questions éthiques fondamentales. Les biais présents dans les données d'entraînement peuvent conduire à des discriminations algorithmiques, notamment dans les systèmes de recrutement ou de justice prédictive. La question de la responsabilité en cas d'erreur d'un système autonome reste juridiquement floue. Par ailleurs, l'impact sur l'emploi préoccupe de nombreux économistes: si l'IA crée de nouveaux métiers, elle en détruit également, et la transition pourrait être douloureuse pour des millions de travailleurs. Une régulation adaptée apparaît nécessaire pour encadrer le développement de ces technologies tout en préservant leur potentiel d'innovation.",
                            "questions": [
                                "Dans quel domaine l'IA peut-elle surpasser les performances humaines selon le texte?",
                                "Qu'est-ce que les discriminations algorithmiques et comment se produisent-elles?",
                                "Quel problème juridique pose l'utilisation de systèmes autonomes?",
                                "Quel est l'impact potentiel de l'IA sur l'emploi?",
                                "Quelle solution est proposée pour encadrer le développement de l'IA?"
                            ]
                        }
                    ]
                }
            },
            "German": {
                "beginner": {
                    "daily_life": [
                        {
                            "text": "Ich heiße Thomas. Ich bin zwölf Jahre alt. Ich wohne in Berlin mit meiner Familie. Meine Familie ist nicht groß. Ich habe eine Mutter, einen Vater und eine Schwester. Meine Schwester heißt Anna. Sie ist zehn Jahre alt. Jeden Morgen stehe ich um sieben Uhr auf. Ich frühstücke mit meiner Familie. Ich esse Brot mit Butter und Marmelade. Ich trinke Milch. Nach dem Frühstück gehe ich zur Schule. Die Schule ist nicht weit. Ich gehe zu Fuß. In der Schule lerne ich Deutsch, Mathematik und Englisch. Nach der Schule mache ich meine Hausaufgaben. Am Abend spiele ich mit meiner Schwester.",
                            "questions": [
                                "Wie heißt der Junge?",
                                "Wie alt ist er?",
                                "Wie heißt seine Schwester?",
                                "Was isst er zum Frühstück?",
                                "Wie kommt er zur Schule?"
                            ]
                        },
                        {
                            "text": "Heute ist Samstag. Ich muss nicht zur Schule gehen. Am Wochenende schlafe ich lange. Ich stehe um zehn Uhr auf. Meine Mutter macht Pfannkuchen. Sie sind sehr lecker. Nach dem Frühstück helfe ich meinem Vater im Garten. Wir pflanzen Blumen. Am Nachmittag treffe ich meine Freunde. Wir gehen in den Park. Wir spielen Fußball. Das macht viel Spaß. Am Abend essen wir Pizza. Wir schauen einen Film zusammen. Ich liebe das Wochenende.",
                            "questions": [
                                "Welcher Tag ist es?",
                                "Um wie viel Uhr steht er auf?",
                                "Was macht die Mutter zum Frühstück?",
                                "Was machen sie im Park?",
                                "Was essen sie am Abend?"
                            ]
                        }
                    ],
                    "travel": [
                        {
                            "text": "Ich bin im Urlaub. Ich bin am Meer mit meiner Familie. Das Wetter ist schön. Die Sonne scheint. Es ist warm. Das Meer ist blau und klar. Ich schwimme jeden Tag. Das Wasser ist nicht kalt. Mein Vater macht Fotos. Meine Mutter liest ein Buch. Mein Bruder baut Sandburgen. Sie sind sehr groß. Am Abend essen wir im Restaurant. Wir essen Fisch und Pommes. Das Essen schmeckt gut. Ich mag den Urlaub am Meer sehr.",
                            "questions": [
                                "Wo ist die Familie?",
                                "Wie ist das Wetter?",
                                "Was macht der Vater?",
                                "Was baut der Bruder?",
                                "Was essen sie im Restaurant?"
                            ]
                        }
                    ],
                    "nature": [
                        {
                            "text": "Ich liebe die Natur. In der Nähe von meinem Haus gibt es einen Wald. Der Wald ist groß und grün. Es gibt viele Bäume und Blumen. Ich höre die Vögel singen. Das ist schön. Im Wald leben viele Tiere. Ich sehe Kaninchen und Eichhörnchen. Manchmal sehe ich ein Reh. Rehe sind sehr scheu. Es gibt auch einen kleinen See. Das Wasser ist klar. Ich sitze am See und höre die Natur. Es ist sehr ruhig und friedlich. Ich gehe oft in den Wald.",
                            "questions": [
                                "Was gibt es in der Nähe vom Haus?",
                                "Welche Tiere leben im Wald?",
                                "Was machen die Vögel?",
                                "Wie ist das Wasser im See?",
                                "Wie sind die Rehe?"
                            ]
                        }
                    ],
                    "technology": [
                        {
                            "text": "Ich habe einen Computer. Er steht auf meinem Schreibtisch. Ich benutze meinen Computer jeden Tag. Ich spiele Spiele und schaue Videos. Ich mache auch meine Hausaufgaben am Computer. Mein Vater hat ein Handy. Er telefoniert mit seinen Freunden. Meine Mutter hat ein Tablet. Sie liest Nachrichten darauf. Wir haben einen Fernseher im Wohnzimmer. Am Abend schauen wir zusammen Filme. Die Technologie ist sehr nützlich. Sie hilft uns jeden Tag.",
                            "questions": [
                                "Wo steht der Computer?",
                                "Was macht er am Computer?",
                                "Was hat der Vater?",
                                "Was macht die Mutter mit dem Tablet?",
                                "Wo ist der Fernseher?"
                            ]
                        }
                    ]
                },
                "intermediate": {
                    "daily_life": [
                        {
                            "text": "Markus arbeitet als Ingenieur bei einem großen Automobilhersteller in München. Sein Arbeitstag beginnt normalerweise um acht Uhr morgens. Er fährt mit der U-Bahn zur Arbeit, weil der Verkehr in München oft sehr stark ist. Im Büro arbeitet er an der Entwicklung neuer Elektroautos. Die Automobilindustrie verändert sich schnell, und Markus muss ständig neue Technologien lernen. Nach der Arbeit geht er dreimal pro Woche ins Fitnessstudio. Sport ist ihm wichtig, um gesund zu bleiben. Am Wochenende verbringt er Zeit mit seiner Familie. Er ist verheiratet und hat zwei Kinder. Die Familie macht gern Ausflüge in die bayerischen Alpen. Im Winter fahren sie Ski, und im Sommer wandern sie auf den Berggipfeln. Markus schätzt die gute Work-Life-Balance, die sein Arbeitgeber ermöglicht.",
                            "questions": [
                                "Was ist Markus von Beruf?",
                                "Wie kommt er zur Arbeit und warum?",
                                "Woran arbeitet er im Büro?",
                                "Wie oft geht er ins Fitnessstudio?",
                                "Was macht die Familie am Wochenende?"
                            ]
                        }
                    ],
                    "travel": [
                        {
                            "text": "Letztes Jahr habe ich eine unvergessliche Reise nach Österreich gemacht. Ich bin mit dem Zug von Berlin nach Wien gefahren. Die Zugfahrt dauerte etwa acht Stunden, aber die Landschaft war wunderschön. Wien ist eine fantastische Stadt mit einer reichen Geschichte. Ich habe das Schloss Schönbrunn besucht, wo früher die österreichischen Kaiser wohnten. Die Architektur war beeindruckend. Ich habe auch die berühmte Wiener Staatsoper gesehen und ein klassisches Konzert gehört. Das Essen in Wien war köstlich. Ich habe Wiener Schnitzel und Apfelstrudel probiert. Nach drei Tagen in Wien bin ich nach Salzburg weitergefahren. Salzburg ist die Geburtsstadt von Mozart. Ich habe sein Geburtshaus besucht und die Festung Hohensalzburg besichtigt. Diese Reise hat mir viel über die österreichische Kultur beigebracht.",
                            "questions": [
                                "Wie ist er nach Wien gereist?",
                                "Was hat er im Schloss Schönbrunn erfahren?",
                                "Welche österreichischen Gerichte hat er probiert?",
                                "Warum ist Salzburg berühmt?",
                                "Was hat er in Salzburg besichtigt?"
                            ]
                        }
                    ],
                    "nature": [
                        {
                            "text": "Der Schwarzwald im Südwesten Deutschlands ist eines der bekanntesten Naturgebiete des Landes. Mit seinen dichten Wäldern, malerischen Dörfern und traditionellen Bauernhöfen zieht er jedes Jahr Millionen von Besuchern an. Die Region ist bekannt für ihre Kuckucksuhren, die hier seit Jahrhunderten hergestellt werden. Wanderer können auf zahlreichen markierten Wegen die Natur erkunden. Der Westweg ist einer der ältesten und beliebtesten Fernwanderwege Deutschlands. Im Schwarzwald gibt es auch viele Wasserfälle und kristallklare Seen. Die Tierwelt ist vielfältig: Rothirsche, Wildschweine und sogar Luchse leben in den Wäldern. Leider bedroht der Klimawandel auch diese Region. Längere Trockenperioden und Borkenkäferbefall setzen den Fichtenwäldern zu. Naturschützer arbeiten daran, die Wälder widerstandsfähiger zu machen.",
                            "questions": [
                                "Wo liegt der Schwarzwald?",
                                "Wofür ist die Region traditionell bekannt?",
                                "Was ist der Westweg?",
                                "Welche Tiere leben im Schwarzwald?",
                                "Welche Probleme bedrohen den Schwarzwald?"
                            ]
                        }
                    ],
                    "technology": [
                        {
                            "text": "Deutschland ist ein führendes Land in der Entwicklung von Industrie 4.0, der vierten industriellen Revolution. In modernen Fabriken arbeiten Roboter und Menschen zusammen. Sensoren sammeln Daten von Maschinen, und künstliche Intelligenz optimiert die Produktionsprozesse. Diese Entwicklung bringt sowohl Chancen als auch Herausforderungen mit sich. Einerseits werden viele Produkte effizienter und günstiger hergestellt. Andererseits machen sich viele Arbeitnehmer Sorgen um ihre Arbeitsplätze. Die Bundesregierung investiert in Weiterbildungsprogramme, damit die Menschen neue digitale Fähigkeiten erlernen können. Auch der Datenschutz ist ein wichtiges Thema. Die Europäische Datenschutz-Grundverordnung (DSGVO) schützt die persönlichen Daten der Bürger. Experten betonen, dass technologischer Fortschritt und soziale Verantwortung Hand in Hand gehen müssen.",
                            "questions": [
                                "Was ist Industrie 4.0?",
                                "Wie arbeiten Roboter und Menschen in modernen Fabriken zusammen?",
                                "Worüber machen sich viele Arbeitnehmer Sorgen?",
                                "Was macht die Bundesregierung, um den Menschen zu helfen?",
                                "Was ist die DSGVO?"
                            ]
                        }
                    ]
                },
                "advanced": {
                    "daily_life": [
                        {
                            "text": "Die Vereinbarkeit von Familie und Beruf stellt in der modernen deutschen Gesellschaft nach wie vor eine erhebliche Herausforderung dar. Obwohl Deutschland über ein vergleichsweise großzügiges Elterngeldsystem verfügt und der Rechtsanspruch auf einen Kitaplatz besteht, kämpfen viele Familien mit der praktischen Umsetzung. Besonders Frauen unterbrechen häufig ihre Karriere oder reduzieren ihre Arbeitszeit nach der Geburt eines Kindes, was langfristige Auswirkungen auf ihr Einkommen und ihre Rentenansprüche hat. Dieses Phänomen wird als Gender Pay Gap und Gender Pension Gap bezeichnet. Die Coronapandemie hat diese Ungleichheiten noch verschärft, da die Schließung von Schulen und Kindertagesstätten die Betreuungslast überwiegend auf die Schultern der Mütter verlagerte. Unternehmen erkennen zunehmend, dass flexible Arbeitsmodelle, Homeoffice-Möglichkeiten und eine familienfreundliche Unternehmenskultur entscheidend sind, um qualifizierte Fachkräfte zu gewinnen und zu halten. Die gesellschaftliche Debatte über eine gerechtere Verteilung von Care-Arbeit gewinnt an Dynamik.",
                            "questions": [
                                "Welche Maßnahmen zur Familienunterstützung existieren in Deutschland?",
                                "Was versteht man unter dem Gender Pay Gap und Gender Pension Gap?",
                                "Wie hat die Coronapandemie die Vereinbarkeit von Familie und Beruf beeinflusst?",
                                "Welche Maßnahmen ergreifen Unternehmen, um familienfreundlicher zu werden?",
                                "Worüber wird gesellschaftlich zunehmend debattiert?"
                            ]
                        }
                    ],
                    "travel": [
                        {
                            "text": "Der Overtourismus hat sich zu einem drängenden Problem für zahlreiche europäische Reiseziele entwickelt. Städte wie Dubrovnik, Venedig und Barcelona ächzen unter dem Ansturm von Millionen Touristen jährlich. Die Auswirkungen sind vielfältig: überlastete Infrastruktur, steigende Lebenshaltungskosten für Einheimische, Verdrängung traditioneller Geschäfte durch Souvenirläden und eine zunehmende Erosion der lokalen Identität. Kreuzfahrtschiffe, die täglich Tausende von Passagieren in historische Zentren entlassen, stehen besonders in der Kritik. Venedig hat inzwischen große Kreuzfahrtschiffe aus der Lagune verbannt. Dubrovnik begrenzt die Anzahl der täglichen Besucher. Auch in Deutschland sind beliebte Ziele wie die Romantische Straße oder Schloss Neuschwanstein vom Massentourismus betroffen. Nachhaltige Tourismuskonzepte gewinnen an Bedeutung. Sie umfassen die Förderung weniger bekannter Reiseziele, die Entzerrung saisonaler Spitzenzeiten und die stärkere Einbindung lokaler Gemeinschaften in touristische Wertschöpfungsketten.",
                            "questions": [
                                "Welche europäischen Städte sind besonders vom Overtourismus betroffen?",
                                "Welche negativen Auswirkungen hat der Massentourismus auf lokale Gemeinschaften?",
                                "Welche Maßnahme hat Venedig gegen Kreuzfahrtschiffe ergriffen?",
                                "Welche deutschen Reiseziele sind vom Massentourismus betroffen?",
                                "Was beinhalten nachhaltige Tourismuskonzepte?"
                            ]
                        }
                    ],
                    "nature": [
                        {
                            "text": "Die Energiewende stellt Deutschland vor gewaltige Herausforderungen, bietet jedoch auch enorme Chancen für den Umweltschutz und die wirtschaftliche Entwicklung. Nach der Reaktorkatastrophe von Fukushima im Jahr 2011 beschloss die Bundesregierung den schrittweisen Ausstieg aus der Kernenergie, der 2023 vollzogen wurde. Gleichzeitig treibt das Land den Ausbau erneuerbarer Energiequellen voran. Windkraft und Solarenergie decken mittlerweile einen erheblichen Anteil des deutschen Strombedarfs. Allerdings stößt der Ausbau auf Widerstand: Anwohner protestieren gegen Windräder in ihrer Nachbarschaft, und der Netzausbau, der den Strom von den Windparks im Norden zu den Industriezentren im Süden transportieren soll, verzögert sich. Die Dekarbonisierung der Industrie, insbesondere der Stahl- und Chemiebranchen, erfordert massive Investitionen in grünen Wasserstoff. Kritiker bemängeln, dass der Kohleausstieg bis 2038 zu langsam erfolgt und Deutschland seine Klimaziele verfehlen könnte. Die Debatte um den optimalen Energiemix und die faire Verteilung der Kosten wird die deutsche Politik noch Jahre beschäftigen.",
                            "questions": [
                                "Was führte zum Beschluss des Atomausstiegs in Deutschland?",
                                "Welchen Anteil decken erneuerbare Energien am Strombedarf?",
                                "Welche Hindernisse gibt es beim Ausbau der Windenergie?",
                                "Warum ist grüner Wasserstoff für die Industrie wichtig?",
                                "Welche Kritik gibt es am Zeitplan des Kohleausstiegs?"
                            ]
                        }
                    ],
                    "technology": [
                        {
                            "text": "Die digitale Transformation des Gesundheitswesens schreitet in Deutschland nur langsam voran, obwohl die Potenziale enorm sind. Die elektronische Patientenakte, die seit 2021 schrittweise eingeführt wird, soll medizinische Daten zentral verfügbar machen und die Behandlungsqualität verbessern. Telemedizinische Konsultationen ermöglichen es Patienten, ärztlichen Rat zu erhalten, ohne die eigenen vier Wände verlassen zu müssen. Besonders in ländlichen Regionen mit Ärztemangel könnte dies die Versorgungssituation verbessern. Künstliche Intelligenz unterstützt Radiologen bei der Auswertung von Bildgebungsverfahren und erkennt Tumore mit einer Genauigkeit, die menschliche Experten übertrifft. Dennoch bestehen erhebliche Bedenken hinsichtlich des Datenschutzes. Gesundheitsdaten gehören zu den sensibelsten persönlichen Informationen, und Sicherheitsvorfälle könnten das Vertrauen der Bevölkerung nachhaltig erschüttern. Hinzu kommt, dass viele Arztpraxen technisch nicht ausreichend ausgestattet sind und ältere Patienten Schwierigkeiten mit digitalen Anwendungen haben. Eine erfolgreiche Digitalisierung erfordert sowohl Investitionen in die technische Infrastruktur als auch in die digitale Kompetenz aller Beteiligten.",
                            "questions": [
                                "Was ist die elektronische Patientenakte und wann wurde sie eingeführt?",
                                "Welche Vorteile bietet die Telemedizin für ländliche Regionen?",
                                "Wie unterstützt künstliche Intelligenz die medizinische Diagnostik?",
                                "Welche Bedenken bestehen bei der Digitalisierung des Gesundheitswesens?",
                                "Was ist für eine erfolgreiche Digitalisierung des Gesundheitswesens erforderlich?"
                            ]
                        }
                    ]
                }
            }
        }

    def generate(self, language, level, topic, word_count):
        """Generate a text based on language, level, topic, and word count"""
        try:
            texts_for_topic = self.texts[language][level][topic]
            selected = random.choice(texts_for_topic)
            return {
                "text": selected["text"],
                "questions": selected["questions"]
            }
        except KeyError:
            return {
                "text": f"No text available for {language} / {level} / {topic}. Please try a different combination.",
                "questions": ["What combination would you like to try?"]
            }
