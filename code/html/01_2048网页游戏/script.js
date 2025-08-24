// 初始化游戏板
const board = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
];

// 获取游戏板元素
const gameBoard = document.getElementById('game-board');

// 生成初始的两个数字
function generateInitialNumbers() {
    addRandomTile();
    addRandomTile();
    updateBoard();
}

// 添加随机数字到空白格子
function addRandomTile() {
    const emptyCells = [];
    for (let i = 0; i < 4; i++) {
        for (let j = 0; j < 4; j++) {
            if (board[i][j] === 0) {
                emptyCells.push({ row: i, col: j });
            }
        }
    }

    if (emptyCells.length > 0) {
        const randomIndex = Math.floor(Math.random() * emptyCells.length);
        const { row, col } = emptyCells[randomIndex];
        board[row][col] = Math.random() < 0.9 ? 2 : 4;
    }
}

// 更新游戏板的显示
function updateBoard() {
    gameBoard.innerHTML = '';
    for (let i = 0; i < 4; i++) {
        for (let j = 0; j < 4; j++) {
            const tile = document.createElement('div');
            tile.classList.add('tile');
            if (board[i][j] !== 0) {
                tile.textContent = board[i][j];
                tile.style.backgroundColor = getTileColor(board[i][j]);
            }
            gameBoard.appendChild(tile);
        }
    }
}

// 根据数字返回不同的背景颜色
function getTileColor(value) {
    switch (value) {
        case 2: return '#eee4da';
        case 4: return '#ede0c8';
        case 8: return '#f2b179';
        case 16: return '#f59563';
        case 32: return '#f67c5f';
        case 64: return '#f65e3b';
        case 128: return '#edcf72';
        case 256: return '#edcc61';
        case 512: return '#edc850';
        case 1024: return '#edc53f';
        case 2048: return '#edc22e';
        default: return '#3c3a32';
    }
}

// 处理按键事件
document.addEventListener('keydown', function (event) {
    let moved = false;
    switch (event.key) {
        case 'ArrowUp':
            moved = moveUp();
            break;
        case 'ArrowDown':
            moved = moveDown();
            break;
        case 'ArrowLeft':
            moved = moveLeft();
            break;
        case 'ArrowRight':
            moved = moveRight();
            break;
    }

    if (moved) {
        addRandomTile();
        updateBoard();
    }
});

// 向上移动
function moveUp() {
    let moved = false;
    for (let col = 0; col < 4; col++) {
        const newCol = [];
        for (let row = 0; row < 4; row++) {
            if (board[row][col] !== 0) {
                newCol.push(board[row][col]);
            }
        }

        for (let i = 0; i < newCol.length - 1; i++) {
            if (newCol[i] === newCol[i + 1]) {
                newCol[i] *= 2;
                newCol.splice(i + 1, 1);
            }
        }

        while (newCol.length < 4) {
            newCol.push(0);
        }

        for (let row = 0; row < 4; row++) {
            if (board[row][col] !== newCol[row]) {
                moved = true;
            }
            board[row][col] = newCol[row];
        }
    }
    return moved;
}

// 向下移动
function moveDown() {
    let moved = false;
    for (let col = 0; col < 4; col++) {
        const newCol = [];
        for (let row = 3; row >= 0; row--) {
            if (board[row][col] !== 0) {
                newCol.push(board[row][col]);
            }
        }

        for (let i = 0; i < newCol.length - 1; i++) {
            if (newCol[i] === newCol[i + 1]) {
                newCol[i] *= 2;
                newCol.splice(i + 1, 1);
            }
        }

        while (newCol.length < 4) {
            newCol.push(0);
        }
        newCol.reverse();

        for (let row = 0; row < 4; row++) {
            if (board[row][col] !== newCol[row]) {
                moved = true;
            }
            board[row][col] = newCol[row];
        }
    }
    return moved;
}

// 向左移动
function moveLeft() {
    let moved = false;
    for (let row = 0; row < 4; row++) {
        const newRow = [];
        for (let col = 0; col < 4; col++) {
            if (board[row][col] !== 0) {
                newRow.push(board[row][col]);
            }
        }

        for (let i = 0; i < newRow.length - 1; i++) {
            if (newRow[i] === newRow[i + 1]) {
                newRow[i] *= 2;
                newRow.splice(i + 1, 1);
            }
        }

        while (newRow.length < 4) {
            newRow.push(0);
        }

        for (let col = 0; col < 4; col++) {
            if (board[row][col] !== newRow[col]) {
                moved = true;
            }
            board[row][col] = newRow[col];
        }
    }
    return moved;
}

// 向右移动
function moveRight() {
    let moved = false;
    for (let row = 0; row < 4; row++) {
        const newRow = [];
        for (let col = 3; col >= 0; col--) {
            if (board[row][col] !== 0) {
                newRow.push(board[row][col]);
            }
        }

        for (let i = 0; i < newRow.length - 1; i++) {
            if (newRow[i] === newRow[i + 1]) {
                newRow[i] *= 2;
                newRow.splice(i + 1, 1);
            }
        }

        while (newRow.length < 4) {
            newRow.push(0);
        }
        newRow.reverse();

        for (let col = 0; col < 4; col++) {
            if (board[row][col] !== newRow[col]) {
                moved = true;
            }
            board[row][col] = newRow[col];
        }
    }
    return moved;
}

// 开始游戏
generateInitialNumbers();