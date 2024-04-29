def ask_question(question, answers):
    print(question)
    print("HeiHei, hva kan jeg hjelp deg med?:")
    for i, answer in enumerate(answers, start=1):
        print(f"{i}. {answer}")

    user_input = input("Enter the number of your answer (1-4): ")
    try:
        answer_index = int(user_input) - 1
        if 0 <= answer_index < len(answers):
            response = {
                1: "Prøv en annen lader, hvis det ikke funker kan du komme på IKT så skal vi se hva vi kan gjøre",
                2: "Hold inne på knappen i 15 sekunder, hvis det ikke funker kan du komme på IKT så skal vi se hva vi kan gjøre",
                3: "Det vil kreve at PCen blir sent på reprasjon, det vil bli en egenandel på 500kr, Du vil få en låne PC til din er ferdig på reprasjon",
                4: "HMMMM, kom net på IKT så skla vi se om vi kan få orden på det"
            }.get(answer_index, "Invalid choice.")
            print(response)
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")
    except ValueError:
        print("Invalid input. Please enter a number.")

question = "What is the capital of France?"
answers = ["PC vil ikke lade", "PC skrur seg ikke pa", "Skjerm er odelagt", "Vet ikke"]


ask_question(question, answers)