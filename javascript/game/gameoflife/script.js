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
    drawCells(ctx);
    drawGridLines(ctx);
}

/**
 * initCells allocates and initializes the game state 2D array of cells.
 * All cells start off dead.
 */
function initCells() {
    for (var i = 0; i < HEIGHT; i++) {
        var row = [];
        for (var j = 0; j < WIDTH; j++) {
            row[j] = Math.floor(Math.random() * 2);
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

    var ctx = gameState.ctx;
    updateCellStates();
    drawCells(ctx);
    drawGridLines(ctx);

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
 * updateCellStates checks the neighbors of each cell and determines if cell is
 * dead or alive.
 */
function updateCellStates() {
    var cells = gameState.cells;
    var futureCells = [];
    initCells(futureCells);
    for (var i = 0; i < HEIGHT; i++) {
        var row = [];
        for (var j = 0; j < WIDTH; j++) {
            var cellState = cells[i][j];
            var neighborCount = countNeighbors(i, j);
            if (cellState == CELLSTATE_ALIVE && neighborCount < 2) {
                row[j] = CELLSTATE_DEAD;
            } else if (cellState == CELLSTATE_ALIVE && neighborCount > 3) {
                row[j] = CELLSTATE_DEAD;
            } else if (cellState == CELLSTATE_DEAD && neighborCount == 3) {
                row[j] = CELLSTATE_ALIVE;
            }
        }
        futureCells[i] = row;
    }
    gameState.cells = futureCells;
}

/**
 * countNeighbors counts the number of living cells around the current cell.
 */
function countNeighbors(x, y) {
    var cells = gameState.cells;
    var count = 0;

    // Top left.
    if (x > 0 && y > 0 && cells[y - 1][x - 1] == CELLSTATE_ALIVE) {
        count++;
    }

    // Top.
    if (y > 0 && cells[y - 1][x] == CELLSTATE_ALIVE) {
        count++;
    }

    // Top right.
    if (x < WIDTH - 1 && y > 0 && cells[y - 1][x + 1] == CELLSTATE_ALIVE) {
        count++;
    }

    // Left.
    if (x > 0 && cells[y][x - 1] == CELLSTATE_ALIVE) {
        count++;
    }

    // Right.
    if (x < WIDTH - 1 && cells[y][x + 1] == CELLSTATE_ALIVE) {
        count++;
    }

    // Bottom left.
    if (x < 0 && y < HEIGHT - 1 && cells[y + 1][x - 1] == CELLSTATE_ALIVE) {
        count++;
    }

    // Bottom.
    if (y < HEIGHT - 1 && cells[y + 1][x] == CELLSTATE_ALIVE) {
        count++;
    }

    // Bottom right.
    if (x < WIDTH - 1 && y < HEIGHT - 1 && cells[y + 1][x + 1] == CELLSTATE_ALIVE) {
        count++;
    }

    return count;
}

/**
 * drawCells draws the cells on the canvas.
 */
function drawCells(ctx) {
    for (var i = 0; i < HEIGHT; i++) {
        for (var j = 0; j < WIDTH; j++) {
            if (gameState.cells[i][j] == CELLSTATE_ALIVE) {
                ctx.fillStyle = 'black';
                ctx.fillRect(
                    j * CELLPADDING,
                    i * CELLPADDING, CELLPADDING, CELLPADDING,
                );
            } else {
                ctx.fillStyle = 'white';
                ctx.fillRect(
                    j * CELLPADDING,
                    i * CELLPADDING, CELLPADDING, CELLPADDING,
                );
            }
        }
    }
}

window.onload = main;