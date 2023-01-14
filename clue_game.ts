let notecard: string[][] = [[], [], [], [], [], []];
let possibilities: number[][];
let unowned_cards: number[][] = [[0,1,2,3,4,5], 
                                [6,7,8,9,10,11], 
                                [12,13,14,15,16,17,18,19,20]]
let answers: number[];
let players: string[];

function init(p: string[]) {
    players = p;
    for(let i = 0; i < players.length; i++) {
        possibilities.push(new Array(24).fill(0))
        answers.push(new Array(21).fill(players.length))
    }
}