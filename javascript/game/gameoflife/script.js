var DISPLAY_WIDTH = 100;
var DISPLAY_HEIGHT = 100;
var CELLPADDING = 5;
var WIDTH = Math.floor(DISPLAY_WIDTH / CELLPADDING);
var HEIGHT = Math.floor(DISPLAY_HEIGHT / CELLPADDING);
var FPS = 1;

var gameState = {
    ctx: null,
    cells: [],
    lastUpdateTimestamp: 0
};

function main() {
    var canvas = document.getElementById("canvas");
    gameState.ctx = canvas.getContext("2d");

    init(gameState.ctx);
    window.requestAnimationFrame(loop);
}

function init(ctx) {
    drawGridLines(ctx);
}

function initCells() {
}

function loop(timestamp) {
    window.requestAnimationFrame(loop);

    var delta = timestamp - gameState.lastUpdateTimestamp;
    if (delta < 1000 / FPS) {
        return;
    }

    drawGridLines(gameState.ctx);

    gameState.lastUpdateTimestamp = timestamp;
}

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

function drawCells(ctx) {
    // TODO
}

window.onload = main;

