questions = [
    {
        "prompt" : "In welchem Jahr gewann Deutschland letztmalig die EM?",
        "options" : ["A: 2021", "B: 1992", "C: 1996", "D: 1980"], 
        "answer" : "C"
    },
    {
        "prompt": "Wer war der Torschützenkönig der EM 2016?",
        "options": ["A: Cristiano Ronaldo", "B: Antoine Griezmann", "C: Gareth Bale", "D: Dimitri Payet"],
        "answer": "B"
    },
    {
        "prompt": "Welche Mannschaft gewann die erste EM im Jahr 1960?",
        "options": ["A: Spanien", "B: Sowjetunion", "C: Italien", "D: Deutschland"],
        "answer": "B"
    },
    {
        "prompt": "Wer erzielte das 'Golden Goal' im EM-Finale 2000?",
        "options": ["A: Thierry Henry", "B: David Trezeguet", "C: Zinedine Zidane", "D: Robert Pires"],
        "answer": "B"
    },
    {
        "prompt": "In welchem Land fand die EM 2008 statt?",
        "options": ["A: Deutschland", "B: Österreich und Schweiz", "C: Portugal", "D: Niederlande"],
        "answer": "B"
    },
    {
        "prompt": "Wie viele Mannschaften nahmen an der EM 2016 teil?",
        "options": ["A: 16", "B: 20", "C: 24", "D: 32"],
        "answer": "C"
    },
    {
        "prompt": "Welcher Spieler hat die meisten Tore in der Geschichte der EM erzielt?",
        "options": ["A: Michel Platini", "B: Cristiano Ronaldo", "C: Alan Shearer", "D: Thierry Henry"],
        "answer": "B"
    },
    {
        "prompt": "Welches Team besiegte Deutschland im Finale der EM 1992?",
        "options": ["A: Schweden", "B: Dänemark", "C: Niederlande", "D: Frankreich"],
        "answer": "B"
    },
    {
        "prompt": "Welches Land gewann die EM 2004 als Außenseiter?",
        "options": ["A: Portugal", "B: Griechenland", "C: Spanien", "D: Tschechien"],
        "answer": "B"
    },
    {
        "prompt": "Wer war der Trainer der deutschen Nationalmannschaft bei der EM 2012?",
        "options": ["A: Jürgen Klinsmann", "B: Joachim Löw", "C: Ottmar Hitzfeld", "D: Rudi Völler"],
        "answer": "B"
    },
    {
        "prompt": "Welches Land hat zusammen mit Spanien die meisten EM-Titel gewonnen?",
        "options": ["A: Deutschland", "B: Niderlande", "C: Italien", "D: Frankreich"],
        "answer": "A"
    },
    {
        "prompt": "Welcher Spieler erzielte das entscheidende Tor im EM-Finale 2016?",
        "options": ["A: Cristiano Ronaldo", "B: Nani", "C: Éder", "D: João Moutinho"],
        "answer": "C"
    },
    {
        "prompt": "In welchem Jahr fand die erste EM mit 24 Mannschaften statt?",
        "options": ["A: 2008", "B: 2012", "C: 2016", "D: 2020"],
        "answer": "C"
    },
    {
        "prompt": "Welches Land war Gastgeber der EM 1996?",
        "options": ["A: Deutschland", "B: England", "C: Frankreich", "D: Italien"],
        "answer": "B"
    },
    {
        "prompt": "Wer wurde zum besten Spieler der EM 2008 gewählt?",
        "options": ["A: Xavi Hernandez", "B: Cristiano Ronaldo", "C: Andrés Iniesta", "D: Luca Modric"],
        "answer": "A"
    },
    {
        "prompt": "Welche beiden Länder haben sich die Gastgeberrolle der EM 2012 geteilt?",
        "options": ["A: Polen und Ukraine", "B: Österreich und Schweiz", "C: Belgien und Niederlande", "D: Spanien und Portugal"],
        "answer": "A"
    },
    {
        "prompt": "Wer war der Kapitän der spanischen Mannschaft, die die EM 2008 gewann?",
        "options": ["A: Iker Casillas", "B: Carles Puyol", "C: Xavi Hernandez", "D: Fernando Torres"],
        "answer": "A"
    },
    {
        "prompt": "Welche Mannschaft besiegte Italien im Finale der EM 2012?",
        "options": ["A: Spanien", "B: Deutschland", "C: Frankreich", "D: Portugal"],
        "answer": "A"
    },
    {
        "prompt": "In welchem Jahr gewann die Niederlande ihre einzige EM?",
        "options": ["A: 1980", "B: 1984", "C: 1988", "D: 1992"],
        "answer": "C"
    },
    {
        "prompt": "Welcher deutsche Spieler erzielte den Siegtreffer im EM-Finale 1996?",
        "options": ["A: Oliver Bierhoff", "B: Jürgen Klinsmann", "C: Matthias Sammer", "D: Andreas Möller"],
        "answer": "A"
    },
    {
        "prompt": "Welches Land war Gastgeber der EM 2004?",
        "options": ["A: Portugal", "B: Griechenland", "C: Spanien", "D: Italien"],
        "answer": "A"
    },
    {
        "prompt": "Wer war der jüngste Spieler, der jemals bei einer EM spielte?",
        "options": ["A: Wayne Rooney", "B: Jude Bellingham", "C: Kylian Mbappé", "D: Lamine Yamal"],
        "answer": "D"
    },
    {
        "prompt": "Welche Mannschaft erreichte das Finale der EM 2000, verlor aber gegen Frankreich?",
        "options": ["A: Italien", "B: Portugal", "C: Niederlande", "D: Deutschland"],
        "answer": "A"
    },
    {
        "prompt": "Welches Land war Gastgeber der EM 1992?",
        "options": ["A: Schweden", "B: Dänemark", "C: England", "D: Frankreich"],
        "answer": "A"
    },
    {
        "prompt": "Welches Land war Gastgeber der EM 1984?",
        "options": ["A: Spanien", "B: Frankreich", "C: Deutschland", "D: Italien"],
        "answer": "B"
    },
]

def runGame(questions):
    score = 0
    for question in questions:
        print(question["prompt"])
        for option in question["options"]:
            print(option)
        answer = input("Bitte gebe deine Antwort(A, B, C oder D) ein:").upper()
        if answer == question["answer"]:
            print("Super! Deine Antwort ist richtig!\n")
            score += 1
        else: 
            print("Leider die falsche Antwort.\n")
    print(f"Du hast {score} von {len(questions)} Punkten erreicht.")
    

runGame(questions)