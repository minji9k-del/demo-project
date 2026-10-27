
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="동체시력 테스트",
    page_icon="🔴",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
    <style>
    html, body, [data-testid="stAppViewContainer"],
    [data-testid="stMain"], [data-testid="stMainBlockContainer"] {
        margin: 0 !important;
        padding: 0 !important;
        overflow: hidden !important;
    }
    [data-testid="stHeader"],
    [data-testid="stToolbar"],
    [data-testid="stDecoration"],
    [data-testid="stStatusWidget"],
    footer {
        display: none !important;
    }
    [data-testid="stMainBlockContainer"] {
        max-width: 100% !important;
        width: 100% !important;
    }
    iframe {
        display: block;
        border: 0 !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

game_html = r"""
<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<style>
* {
    box-sizing: border-box;
}

html, body {
    margin: 0;
    padding: 0;
    width: 100%;
    height: 100%;
    overflow: hidden;
    font-family: Arial, "Malgun Gothic", sans-serif;
    background: #f3f6fb;
    color: #202b3c;
}

body {
    display: flex;
    align-items: center;
    justify-content: center;
}

#app {
    width: 100%;
    height: 100%;
    min-height: 0;
    overflow: hidden;
    display: flex;
    justify-content: center;
    align-items: center;
    padding: 8px;
}

.screen {
    display: none;
    width: 100%;
    height: 100%;
    min-height: 0;
    max-width: 1100px;
    text-align: center;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    gap: 12px;
    overflow: hidden;
}

.screen.active {
    display: flex;
}

h1 {
    font-size: clamp(25px, 4vh, 40px);
    line-height: 1.15;
    margin: 0;
    color: #17243a;
}

.subtitle {
    margin: 0;
    font-size: clamp(13px, 2vh, 17px);
    color: #667085;
    line-height: 1.45;
}

.start-ball {
    width: clamp(54px, 9vh, 76px);
    height: clamp(54px, 9vh, 76px);
    border-radius: 50%;
    background: #f04444;
    box-shadow: 0 7px 0 #c92e2e, 0 12px 25px #f0444433;
    flex-shrink: 0;
}

button {
    border: 0;
    border-radius: 12px;
    padding: 12px 26px;
    min-height: 44px;
    font-size: clamp(14px, 2vh, 17px);
    font-weight: 700;
    cursor: pointer;
    background: #2563eb;
    color: white;
    box-shadow: 0 3px 0 #1748b2;
}

button:active {
    transform: translateY(2px);
    box-shadow: 0 1px 0 #1748b2;
}

button:disabled {
    opacity: .55;
    cursor: default;
}

#homeScreen {
    gap: clamp(10px, 2.3vh, 20px);
}

.rules {
    background: white;
    border: 1px solid #e2e8f0;
    border-radius: 16px;
    padding: clamp(10px, 2vh, 18px) clamp(15px, 3vw, 30px);
    width: min(100%, 500px);
    text-align: left;
    line-height: 1.65;
    font-size: clamp(12px, 1.8vh, 15px);
    color: #475467;
}

.rules strong {
    color: #202b3c;
}

#gameScreen {
    justify-content: flex-start;
    gap: 8px;
}

.topbar {
    width: 100%;
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 8px;
    flex-shrink: 0;
}

.pill {
    border-radius: 999px;
    padding: 7px 12px;
    background: white;
    border: 1px solid #e2e8f0;
    font-weight: 700;
    font-size: clamp(11px, 1.8vh, 15px);
    white-space: nowrap;
}

#timerPill {
    background: #fff7e6;
    border-color: #ffd591;
    color: #ad4e00;
    min-width: 145px;
}

#timerPill.urgent {
    background: #fff1f0;
    border-color: #ffccc7;
    color: #cf1322;
    animation: timerPulse .5s infinite alternate;
}

@keyframes timerPulse {
    from { transform: scale(1); }
    to { transform: scale(1.04); }
}

#stageTitle {
    font-size: clamp(18px, 2.8vh, 26px);
    margin: 0;
}

#instruction {
    font-size: clamp(12px, 1.8vh, 15px);
    margin: 0;
    color: #667085;
    flex-shrink: 0;
}

#arena {
    width: 100%;
    flex: 1;
    min-height: 100px;
    max-height: 470px;
    position: relative;
    overflow: hidden;
    border: 2px solid #d9e2f0;
    border-radius: 16px;
    background:
        radial-gradient(circle at 1px 1px, #dce4ef 1px, transparent 0)
        0 0 / 24px 24px,
        #ffffff;
}

.ball {
    width: 18px;
    height: 18px;
    position: absolute;
    border-radius: 50%;
    background: #f04444;
    box-shadow: 0 2px 0 #c92e2e;
    pointer-events: none;
}

.answerRow {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 8px;
    flex-wrap: wrap;
    width: 100%;
    flex-shrink: 0;
}

#answer {
    width: 110px;
    min-width: 80px;
    height: 44px;
    border: 2px solid #cbd5e1;
    border-radius: 10px;
    text-align: center;
    font-size: 20px;
    font-weight: 700;
    outline: none;
    background: white;
}

#answer:focus {
    border-color: #2563eb;
}

#checkBtn {
    min-width: 145px;
}

#feedback {
    min-height: 24px;
    font-size: clamp(13px, 1.9vh, 16px);
    font-weight: 700;
    margin: 0;
    flex-shrink: 0;
}

.good { color: #16803c; }
.bad { color: #d92d20; }
.neutral { color: #667085; }

#resultScreen {
    gap: clamp(8px, 2vh, 16px);
}

.resultScore {
    font-size: clamp(28px, 6vh, 54px);
    font-weight: 900;
    color: #2563eb;
}

#grade {
    font-size: clamp(22px, 4vh, 34px);
    font-weight: 900;
}

#resultMessage {
    margin: 0;
    font-size: clamp(13px, 2vh, 17px);
    color: #667085;
}

#finaleScreen {
    gap: 18px;
}

#finaleText {
    font-size: clamp(24px, 5vh, 42px);
    font-weight: 900;
    color: #2563eb;
    animation: pulse .55s infinite alternate;
}

@keyframes pulse {
    from { transform: scale(.98); }
    to { transform: scale(1.04); }
}

@media (max-height: 600px) {
    #app { padding: 5px; }
    .screen { gap: 7px; }
    #homeScreen { gap: 8px; }
    .rules { padding: 8px 14px; line-height: 1.45; }
    button { min-height: 38px; padding: 8px 18px; }
    #answer { height: 38px; }
    #arena { min-height: 80px; }
    .pill { padding: 5px 8px; }
    #timerPill { min-width: 120px; }
}

@media (max-width: 520px) {
    .topbar { gap: 4px; }
    .pill { padding: 6px; font-size: 10px; }
    #timerPill { min-width: 110px; }
}
</style>
</head>

<body>
<div id="app">

    <section id="homeScreen" class="screen active">
        <div class="start-ball"></div>
        <h1>동체시력 테스트</h1>
        <p class="subtitle">
            빠르게 움직이는 빨간 공은 모두 몇 개일까요?
        </p>

        <div class="rules">
            <strong>🎯 게임 방법</strong><br>
            1. 움직이는 빨간 공의 개수를 세어 보세요.<br>
            2. 위쪽에 표시되는 제한시간 안에 집중하세요.<br>
            3. 시간이 끝나면 공이 모두 사라져요.<br>
            4. 기억한 숫자를 입력하고 Enter를 누르세요.<br>
            <strong>총 7단계!</strong> 집중력을 발휘해 보세요.
        </div>

        <button id="startBtn">테스트 시작</button>
    </section>

    <section id="gameScreen" class="screen">
        <div class="topbar">
            <div class="pill" id="stagePill">1 / 7 단계</div>
            <div class="pill" id="timerPill">⏱ 남은 시간: 5.0초</div>
            <div class="pill" id="scorePill">현재 점수: 0점</div>
        </div>

        <h2 id="stageTitle">1단계</h2>
        <p id="instruction">빨간 공의 개수를 세어 보세요!</p>

        <div id="arena"></div>

        <div class="answerRow">
            <label for="answer">공의 개수</label>
            <input
                id="answer"
                type="number"
                min="1"
                max="99"
                inputmode="numeric"
                autocomplete="off"
                placeholder="숫자"
            >
            <button id="checkBtn">정답 확인</button>
        </div>

        <p id="feedback" class="neutral" aria-live="polite">
            공을 집중해서 세어 보세요!
        </p>
    </section>

    <section id="finaleScreen" class="screen">
        <div class="start-ball"></div>
        <div id="finaleText">두구두구두구두구… 짠!</div>
        <p class="subtitle">최종 결과를 공개합니다!</p>
    </section>

    <section id="resultScreen" class="screen">
        <h1>테스트 결과</h1>
        <div class="resultScore">
            <span id="finalScore">0</span> / 7점
        </div>
        <div id="grade">🙂 평범</div>
        <p id="resultMessage">테스트가 끝났어요!</p>
        <button id="restartBtn">다시 도전하기</button>
    </section>

</div>

<script>
const ranges = [
    [6, 8],
    [7, 9],
    [8, 10],
    [9, 12],
    [11, 13],
    [12, 15],
    [14, 16]
];

const homeScreen = document.getElementById("homeScreen");
const gameScreen = document.getElementById("gameScreen");
const finaleScreen = document.getElementById("finaleScreen");
const resultScreen = document.getElementById("resultScreen");
const arena = document.getElementById("arena");
const answer = document.getElementById("answer");
const checkBtn = document.getElementById("checkBtn");
const feedback = document.getElementById("feedback");
const stagePill = document.getElementById("stagePill");
const scorePill = document.getElementById("scorePill");
const timerPill = document.getElementById("timerPill");
const stageTitle = document.getElementById("stageTitle");
const instruction = document.getElementById("instruction");

let level = 1;
let score = 0;
let ballCount = 0;
let balls = [];
let duration = 5000;
let startTime = 0;
let animationId = null;
let timerId = null;
let roundEnded = false;
let roundChecked = false;
let lastFrame = 0;
let audioContext = null;
let lastWallSound = 0;
let showingFinale = false;
let focusTimer = null;
let finaleTimer = null;

function showScreen(screen) {
    [homeScreen, gameScreen, finaleScreen, resultScreen]
        .forEach(s => s.classList.remove("active"));
    screen.classList.add("active");
}

function randomInt(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

function initAudio() {
    try {
        if (!audioContext) {
            audioContext = new (
                window.AudioContext || window.webkitAudioContext
            )();
        }

        if (audioContext.state === "suspended") {
            audioContext.resume();
        }
    } catch (e) {}
}

function tone(freq, start, length, type = "sine", volume = 0.07) {
    if (!audioContext) return;

    try {
        const oscillator = audioContext.createOscillator();
        const gain = audioContext.createGain();

        oscillator.type = type;
        oscillator.frequency.setValueAtTime(freq, start);

        gain.gain.setValueAtTime(0.0001, start);
        gain.gain.exponentialRampToValueAtTime(volume, start + 0.012);
        gain.gain.exponentialRampToValueAtTime(0.0001, start + length);

        oscillator.connect(gain);
        gain.connect(audioContext.destination);

        oscillator.start(start);
        oscillator.stop(start + length + 0.02);
    } catch (e) {}
}

function playWallSound() {
    if (!audioContext) return;

    const now = audioContext.currentTime;
    if (now - lastWallSound < 0.075) return;

    lastWallSound = now;
    tone(650, now, 0.045, "sine", 0.025);
}

function playCorrectSound() {
    if (!audioContext) return;

    const now = audioContext.currentTime;
    [523, 659, 784, 1047].forEach((f, i) => {
        tone(f, now + i * 0.105, 0.15, "sine", 0.075);
    });
}

function playWrongSound() {
    if (!audioContext) return;

    const now = audioContext.currentTime;
    [440, 370, 294].forEach((f, i) => {
        tone(f, now + i * 0.16, 0.19, "triangle", 0.065);
    });
}

function playDrumroll() {
    if (!audioContext) return;

    const now = audioContext.currentTime;
    const beatCount = 22;
    const beatInterval = 0.075;

    for (let i = 0; i < beatCount; i++) {
        const t = now + i * beatInterval;
        const osc = audioContext.createOscillator();
        const gain = audioContext.createGain();

        osc.type = "triangle";
        osc.frequency.setValueAtTime(95 + Math.random() * 45, t);

        gain.gain.setValueAtTime(0.0001, t);
        gain.gain.exponentialRampToValueAtTime(0.13, t + 0.008);
        gain.gain.exponentialRampToValueAtTime(0.0001, t + 0.06);

        osc.connect(gain);
        gain.connect(audioContext.destination);

        osc.start(t);
        osc.stop(t + 0.07);
    }

    const revealTime = now + beatCount * beatInterval + 0.04;

    [523, 659, 784, 1047].forEach((f, i) => {
        tone(f, revealTime + i * 0.13, 0.35, "sine", 0.09);
    });
}

function stopAnimation() {
    if (animationId !== null) {
        cancelAnimationFrame(animationId);
        animationId = null;
    }

    if (timerId !== null) {
        clearTimeout(timerId);
        timerId = null;
    }
}

function updateTimer(timestamp) {
    const elapsed = timestamp - startTime;
    const remaining = Math.max(0, duration - elapsed);
    const seconds = (remaining / 1000).toFixed(1);

    timerPill.textContent = "⏱ 남은 시간: " + seconds + "초";

    if (remaining <= 2000 && remaining > 0) {
        timerPill.classList.add("urgent");
    } else {
        timerPill.classList.remove("urgent");
    }
}

function createBalls() {
    arena.innerHTML = "";
    balls = [];

    const width = Math.max(arena.clientWidth, 200);
    const height = Math.max(arena.clientHeight, 100);

    for (let i = 0; i < ballCount; i++) {
        const element = document.createElement("div");
        element.className = "ball";
        arena.appendChild(element);

        const speed = randomInt(
            150 + level * 25,
            190 + level * 32
        );

        const angle = Math.random() * Math.PI * 2;

        balls.push({
            element,
            x: 9 + Math.random() * Math.max(1, width - 18),
            y: 9 + Math.random() * Math.max(1, height - 18),
            vx: Math.cos(angle) * speed,
            vy: Math.sin(angle) * speed
        });
    }

    renderBalls();
}

function renderBalls() {
    balls.forEach(ball => {
        ball.element.style.left = (ball.x - 9) + "px";
        ball.element.style.top = (ball.y - 9) + "px";
    });
}

function animate(timestamp) {
    if (roundEnded || !gameScreen.classList.contains("active")) return;

    if (!lastFrame) lastFrame = timestamp;

    const delta = Math.min((timestamp - lastFrame) / 1000, 0.035);
    lastFrame = timestamp;

    updateTimer(timestamp);

    const width = arena.clientWidth;
    const height = arena.clientHeight;

    for (const ball of balls) {
        ball.x += ball.vx * delta;
        ball.y += ball.vy * delta;

        let hitWall = false;

        if (ball.x < 9) {
            ball.x = 9;
            ball.vx = Math.abs(ball.vx);
            hitWall = true;
        } else if (ball.x > width - 9) {
            ball.x = width - 9;
            ball.vx = -Math.abs(ball.vx);
            hitWall = true;
        }

        if (ball.y < 9) {
            ball.y = 9;
            ball.vy = Math.abs(ball.vy);
            hitWall = true;
        } else if (ball.y > height - 9) {
            ball.y = height - 9;
            ball.vy = -Math.abs(ball.vy);
            hitWall = true;
        }

        if (hitWall) playWallSound();
    }

    renderBalls();
    animationId = requestAnimationFrame(animate);
}

function endRoundByTimer() {
    if (roundEnded) return;

    roundEnded = true;
    stopAnimation();

    // 시간이 끝나면 표시 시간을 0초로 고정하고 공을 숨긴다.
    timerPill.textContent = "⏱ 남은 시간: 0.0초";
    timerPill.classList.add("urgent");

    balls.forEach(ball => {
        ball.element.style.display = "none";
    });

    instruction.textContent = "시간 종료! 기억한 공의 개수를 입력하세요.";
    feedback.textContent = "숫자를 입력한 뒤 Enter를 누르세요.";
    feedback.className = "neutral";

    answer.disabled = false;
    answer.focus();
}

function beginStage() {
    stopAnimation();
    clearTimeout(focusTimer);

    roundEnded = false;
    roundChecked = false;
    lastFrame = 0;
    lastWallSound = 0;

    ballCount = randomInt(
        ranges[level - 1][0],
        ranges[level - 1][1]
    );

    duration = Math.max(2300, 5000 - (level - 1) * 450);

    stagePill.textContent = level + " / 7 단계";
    scorePill.textContent = "현재 점수: " + score + "점";
    stageTitle.textContent = level + "단계";
    instruction.textContent = "빨간 공의 개수를 세어 보세요!";
    feedback.textContent = "공을 집중해서 세어 보세요!";
    feedback.className = "neutral";

    timerPill.textContent = "⏱ 남은 시간: " + (duration / 1000).toFixed(1) + "초";
    timerPill.classList.remove("urgent");

    answer.value = "";
    answer.disabled = false;
    checkBtn.disabled = false;
    checkBtn.textContent = "정답 확인";

    showScreen(gameScreen);
    createBalls();

    startTime = performance.now();

    animationId = requestAnimationFrame(animate);
    timerId = setTimeout(endRoundByTimer, duration);

    focusTimer = setTimeout(() => {
        if (!roundChecked && gameScreen.classList.contains("active")) {
            answer.focus();
        }
    }, 120);
}

function checkAnswer() {
    if (showingFinale) return;

    if (roundChecked) {
        if (level < 7) {
            level++;
            beginStage();
        } else {
            showResults();
        }
        return;
    }

    const raw = answer.value.trim();

    if (raw === "") {
        feedback.textContent = "먼저 공의 개수를 입력해 주세요!";
        feedback.className = "bad";
        answer.focus();
        return;
    }

    const guess = Number(raw);

    roundChecked = true;
    roundEnded = true;
    stopAnimation();

    // 답을 제출하면 남아 있는 공도 숨긴다.
    balls.forEach(ball => {
        ball.element.style.display = "none";
    });

    if (guess === ballCount) {
        score++;
        feedback.textContent = "정답이에요! 🎉";
        feedback.className = "good";
        playCorrectSound();
    } else {
        feedback.textContent = "아쉬워요! 정답은 " + ballCount + "개예요.";
        feedback.className = "bad";
        playWrongSound();
    }

    scorePill.textContent = "현재 점수: " + score + "점";
    instruction.textContent = "Enter를 다시 누르면 다음 단계로 넘어가요.";
    answer.disabled = true;
    checkBtn.textContent = level < 7 ? "다음 단계" : "결과 확인";
    checkBtn.focus();
}

function showResults() {
    if (showingFinale) return;

    showingFinale = true;
    stopAnimation();
    clearTimeout(focusTimer);

    showScreen(finaleScreen);
    checkBtn.disabled = true;
    playDrumroll();

    finaleTimer = setTimeout(() => {
        document.getElementById("finalScore").textContent = score;

        let grade = "";
        let message = "";

        if (score <= 2) {
            grade = "💩 최악";
            message = "괜찮아요! 다시 도전하면 더 잘할 수 있어요.";
        } else if (score <= 5) {
            grade = "🙂 평범";
            message = "좋아요! 조금 더 집중해서 도전해 보세요.";
        } else {
            grade = "⭐ 우수";
            message = "대단해요! 뛰어난 동체시력을 가졌네요!";
        }

        document.getElementById("grade").textContent = grade;
        document.getElementById("resultMessage").textContent = message;

        showScreen(resultScreen);
        checkBtn.disabled = false;
        showingFinale = false;
        document.getElementById("restartBtn").focus();
    }, 2400);
}

document.getElementById("startBtn").addEventListener("click", () => {
    initAudio();
    level = 1;
    score = 0;
    showingFinale = false;
    clearTimeout(finaleTimer);
    beginStage();
});

document.getElementById("restartBtn").addEventListener("click", () => {
    clearTimeout(finaleTimer);
    showingFinale = false;
    score = 0;
    level = 1;
    showScreen(homeScreen);
    document.getElementById("startBtn").focus();
});

checkBtn.addEventListener("click", checkAnswer);

answer.addEventListener("keydown", event => {
    if (event.key === "Enter") {
        event.preventDefault();
        checkAnswer();
    }
});

checkBtn.addEventListener("keydown", event => {
    if (event.key === "Enter" || event.key === " ") {
        event.preventDefault();
        checkAnswer();
    }
});

window.addEventListener("resize", () => {
    if (!gameScreen.classList.contains("active") || roundEnded) return;

    const width = arena.clientWidth;
    const height = arena.clientHeight;

    balls.forEach(ball => {
        ball.x = Math.max(9, Math.min(width - 9, ball.x));
        ball.y = Math.max(9, Math.min(height - 9, ball.y));
    });

    renderBalls();
});
</script>
</body>
</html>
"""

components.html(game_html, height=620, scrolling=False)
