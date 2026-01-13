---
hide:
  - navigation
---

# Random Practice Quiz

Customize your practice session by choosing the number of questions.

<div id="quiz-app-container" class="quiz-container">
    <div id="quiz-setup" class="quiz-section">
        <h3>Quiz Configuration</h3>
        <p>Total questions available: <span id="total-questions-count">...</span></p>
        <div class="form-group">
            <label for="question-count">Number of Questions:</label>
            <input type="number" id="question-count" min="1" max="50" value="10">
        </div>
        <button id="start-quiz-btn" class="md-button md-button--primary">Start Quiz</button>
    </div>

    <div id="quiz-interface" class="quiz-section" style="display: none;">
        <div class="quiz-progress">
            Question <span id="current-q-num">1</span> of <span id="total-q-num">10</span>
        </div>

        <div id="quiz-questions-list">
            <!-- Questions will be injected here -->
        </div>

        <button id="submit-quiz-btn" class="md-button md-button--primary">Submit Answers</button>
    </div>

    <div id="quiz-results" class="quiz-section" style="display: none;">
        <h3>Quiz Results</h3>
        <div class="score-display">
            Score: <span id="score-text"></span>
        </div>
        <button id="retry-quiz-btn" class="md-button">Try Another Quiz</button>
        <div id="results-breakdown"></div>
    </div>

</div>

<style>
.quiz-container {
    max-width: 800px;
    margin: 2rem auto;
    padding: 1rem;
    background: var(--md-code-bg-color);
    border-radius: 8px;
}
.quiz-section {
    padding: 1rem;
}
.form-group {
    margin-bottom: 1rem;
}
input[type="number"] {
    padding: 0.5rem;
    border-radius: 4px;
    border: 1px solid var(--md-default-fg-color--lightest);
}
.quiz-question-card {
    background: var(--md-default-bg-color);
    padding: 1.5rem;
    margin-bottom: 1.5rem;
    border-radius: 8px;
    box-shadow: 0 2px 5px rgba(0,0,0,0.05);
    border: 1px solid transparent;
}
.quiz-question-card.correct {
    border-color: #4caf50;
}
.quiz-question-card.incorrect {
    border-color: #f44336;
}
.quiz-options {
    list-style: none;
    padding: 0;
    margin: 1rem 0;
}
.quiz-option {
    padding: 0.75rem;
    margin: 0.5rem 0;
    border: 1px solid var(--md-default-fg-color--lightest);
    border-radius: 4px;
    cursor: pointer;
    transition: all 0.2s;
}
.quiz-option:hover {
    background: var(--md-accent-fg-color--transparent);
}
.quiz-option.selected {
    background: var(--md-accent-fg-color);
    color: white;
    border-color: var(--md-accent-fg-color);
}
.quiz-feedback {
    margin-top: 1rem;
    padding: 1rem;
    background: var(--md-code-bg-color);
    border-radius: 4px;
    font-size: 0.9em;
}
.correct-badge {
    color: #4caf50;
    font-weight: bold;
}
.incorrect-badge {
    color: #f44336;
    font-weight: bold;
}
/* Question Type Badges */
.question-type-badge {
    margin-bottom: 0.5rem;
}
.badge {
    display: inline-block;
    padding: 0.25rem 0.5rem;
    border-radius: 4px;
    font-size: 0.75rem;
    font-weight: bold;
    text-transform: uppercase;
}
.badge-warning {
    background: #ff9800;
    color: white;
}
.badge-info {
    background: #2196f3;
    color: white;
}
/* Ordering Question Styles */
.ordering-option {
    display: flex;
    align-items: center;
    gap: 1rem;
}
.ordering-select {
    padding: 0.5rem;
    border-radius: 4px;
    border: 1px solid var(--md-default-fg-color--lightest);
    background: var(--md-default-bg-color);
    min-width: 100px;
}
.ordering-select:disabled {
    opacity: 0.6;
    cursor: not-allowed;
}
/* Option Elimination Feature */
.quiz-option {
    position: relative;
}
.eliminate-btn {
    position: absolute;
    right: 10px;
    top: 50%;
    transform: translateY(-50%);
    color: var(--md-default-fg-color--light);
    opacity: 0.3;
    cursor: pointer;
    font-size: 0.8rem;
}
.quiz-option:hover .eliminate-btn {
    opacity: 0.7;
}
.quiz-option.eliminated {
    text-decoration: line-through;
    opacity: 0.5;
    background: rgba(128, 128, 128, 0.1) !important;
    border-color: var(--md-default-fg-color--lightest) !important;
}
.quiz-option.eliminated .eliminate-btn {
    color: #f44336;
    opacity: 1;
}
</style>
