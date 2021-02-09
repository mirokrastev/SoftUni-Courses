function solve(cardFace, cardSuit) {
    let mapper = {
        'S': '\u2660',
        'H': '\u2665',
        'D': '\u2666',
        'C': '\u2663'
    }
    let validCardFaces = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

    if (!mapper.hasOwnProperty(cardSuit) || !validCardFaces.includes(cardFace)) throw new Error();

    class Card {
        constructor(cardFace, cardSuit) {
            this.cardFace = cardFace;
            this.cardSuit = cardSuit;
        }

        toString() {
            return `${this.cardFace}${mapper[this.cardSuit]}`;
        }
    }

    return new Card(cardFace, cardSuit);
}