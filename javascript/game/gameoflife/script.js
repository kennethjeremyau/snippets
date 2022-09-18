// Display width of the game board.
var DISPLAY_WIDTH = 100;

// Display height of the game board.
var DISPLAY_HEIGHT = 100;

// Width of each cell.
var CELLPADDING = 5;

// Number of cells across the board.
var WIDTH = Math.floor(DISPLAY_WIDTH / CELLPADDING);

// Number of cells along the board.
var HEIGHT = Math.floor(DISPLAY_HEIGHT / CELLPADDING);

// Frames per second.
var FPS = 1;

// Enum representing a dead cell.
var CELLSTATE_DEAD = 0;

// Enum representing a living cell.
var CELLSTATE_ALIVE = 1;

// Global game state. This is global because window.requestAnimationFrame
// cannot be passed any variables.
var gameState = {
    ctx: null,
    cells: [],
    lastUpdateTimestamp: 0
};

/**
* main is the main function.
*/
function main() {
    var canvas = document.getElementById("canvas");
    gameState.ctx = canvas.getContext("2d");

    init(gameState.ctx);
    window.requestAnimationFrame(loop);
}

/**
* init initializes the game.
*/
function init(ctx) {
    initCells();
    drawGridLines(ctx);
}

/**
* initCells allocates and initializes the game state 2D array of cells.
* All cells start of dead.
*/
function initCells() {
    for (var i = 0; i < HEIGHT; i++) {
        var row = [];
        for (var j = 0; j < WIDTH; j++) {
            row[j] = CELLSTATE_DEAD;
        }
        gameState.cells[i] = row;
    }
}

/** 
* loop is the main game loop as dictated by the browser.
*/
function loop(timestamp) {
    window.requestAnimationFrame(loop);

    var delta = timestamp - gameState.lastUpdateTimestamp;
    if (delta < 1000 / FPS) {
        return;
    }

    drawGridLines(gameState.ctx);

    gameState.lastUpdateTimestamp = timestamp;
}

/**
* drawGridLines draws the lines of the grid on the canvas.
*/
function drawGridLines(ctx) {
    for (var x = 0; x < DISPLAY_WIDTH; x += CELLPADDING) {
        ctx.moveTo(x + CELLPADDING, 0);
        ctx.lineTo(x + CELLPADDING, DISPLAY_HEIGHT);
    }
    for (var y = 0; y < DISPLAY_HEIGHT; y += CELLPADDING) {
        ctx.moveTo(0, y + CELLPADDING);
        ctx.lineTo(DISPLAY_WIDTH, y + CELLPADDING);
    }
    ctx.strokeStyle = "lightgrey";
    ctx.stroke();
}

/**
* drawCells draws the cells on the canvas.
*/
function drawCells(ctx) {
    // TODO
}

window.onload = main;

