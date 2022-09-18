var CELLPADDING = 5
var DISPLAY_WIDTH = 100
var DISPLAY_HEIGHT = 100
var FPS = 1

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
    drawGridLines(ctx, 0, 0, DISPLAY_WIDTH, DISPLAY_HEIGHT, CELLPADDING);
}

function initCells() {
}

function loop(timestamp) {
    window.requestAnimationFrame(loop);

    var delta = timestamp - gameState.lastUpdateTimestamp;
    if (delta < 1000 / FPS) {
        return;
    }

    drawGridLines(gameState.ctx, 0, 0, DISPLAY_WIDTH, DISPLAY_HEIGHT, CELLPADDING);

    gameState.lastUpdateTimestamp = timestamp;
}

function drawGridLines(ctx, topX, topY, width, height, padding) {
    for (var x = topX; x < width; x += padding) {
        ctx.moveTo(x + padding, topX);
        ctx.lineTo(x + padding, height);
    }
    for (var y = topY; y < height; y += padding) {
        ctx.moveTo(topY, y + padding);
        ctx.lineTo(width, y + padding);
    }
    ctx.strokeStyle = "lightgrey";
    ctx.stroke();
}

function drawCells(ctx) {
    // TODO
}

window.onload = main;
