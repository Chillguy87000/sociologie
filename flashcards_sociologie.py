from genanki import Deck, Note, Model, Package

my_model = Model(
    1607392319,
    "Flashcard Model",
    fields=[
        {"name": "Question"},
        {"name": "Answer"}
    ],
    templates=[
        {
            "name": "Card 1",
            "qfmt": "{{Question}}",
            "afmt": "{{FrontSide}}<hr id='answer'>{{Answer}}",
        },
    ],
)

deck = Deck(
    2059400110,
    "Sociologie Classique : Weber, Marx et Durkheim"
)

flashcards = [
    ("Quels sont les trois grands types de bouleversements au XIXᵉ siècle mentionnés dans le texte ?", "Politiques, économiques et industriels, sociaux."),
    ("Quel phénomène est lié à l'urbanisation au XIXᵉ siècle ?", "Le développement du statut de salarié."),
    ("Quels sont les idéologies politiques nées au XIXᵉ siècle ?", "Communisme, anarchisme, fascisme."),
    ("Quelles lois ont permis l'accès à l'éducation au XIXᵉ siècle en France ?", "Les lois Ferry."),
    ("Quelle société sociologique Weber a-t-il cofondée en 1909 ?", "La société allemande de sociologie."),
    ("Quels sont les quatre types d’actions selon Weber ?", "Traditionnelles, affectuelles, rationnelles en valeur, rationnelles en finalité."),
    ("Comment Weber définit-il l’État ?", "Une communauté humaine qui revendique le monopole de la violence physique légitime sur un territoire."),
    ("Quelle opposition se trouve derrière les trois types de domination selon Weber ?", "Domination impersonnelle/personnelle et quotidienne/extra-quotidienne."),
    ("Qu'est-ce que la 'routinisation du charisme' selon Weber ?", "C'est le processus par lequel une domination charismatique devient traditionnelle ou légale pour durer."),
    ("Quels sont les trois types de légitimité de la domination selon Weber ?", "Rationnelle-légale, traditionnelle, charismatique."),
    ("Quelle théorie centrale explique la pensée marxiste ?", "Le matérialisme historique."),
    ("Quelles sont les deux formes de classes sociales selon Marx ?", "Classes 'en soi' et 'pour soi'."),
    ("Pourquoi Marx critique-t-il la religion ?", "Parce qu'elle masque les inégalités réelles et offre un bonheur illusoire."),
    ("Quels sont les sept classes sociales identifiées par Marx au XIXᵉ siècle ?", "Bourgeoisie, petite bourgeoisie, classe ouvrière (prolétariat), lumpenprolétariat, paysannerie."),
    ("Quelle est la différence entre les classes 'en soi' et 'pour soi' selon Marx ?", "'En soi' : existence théorique. 'Pour soi' : conscience collective et mobilisation."),
    ("Quelle œuvre majeure Marx a-t-il rédigée avec Engels ?", "Le Manifeste du parti communiste."),
    ("Quelle distinction clé Durkheim fait-il concernant les formes de solidarité ?", "Solidarité mécanique et solidarité organique."),
    ("Quelle était le premier ouvrage majeur de Durkheim ?", "De la division du travail social."),
    ("Quel événement a particulièrement mobilisé Durkheim politiquement ?", "L'Affaire Dreyfus."),
    ("Quelle est la revue fondée par Durkheim en 1887 ?", "L'Année sociologique."),
    ("Quels sont les rôles de l’État dans une société à solidarité organique selon Durkheim ?", "Régulation et entraide."),
    ("Comment Weber définit-il le champ religieux ?", "Un espace où des acteurs religieux et profanes sont en concurrence pour manipuler les biens de salut."),
    ("Quelles sont les deux figures majeures du champ religieux selon Weber ?", "Le prophète et le prêtre."),
    ("Selon Durkheim, quelle opposition est au cœur du religieux ?", "Le sacré et le profane."),
    ("Quel est le point commun central des analyses religieuses de Weber, Marx et Durkheim ?", "La religion est une émanation de l’organisation sociale."),
    ("Quel lien commun Marx et Weber établissent-ils entre religion et économie ?", "Un lien étroit, mais avec des causalités différentes."),
]

for question, answer in flashcards:
    note = Note(
        model=my_model,
        fields=[question, answer]
    )
    deck.add_note(note)

Package(deck).write_to_file("Sociologie_Classique.apkg")
