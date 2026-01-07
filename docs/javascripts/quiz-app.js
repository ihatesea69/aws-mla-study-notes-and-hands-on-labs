document.addEventListener('DOMContentLoaded', function() {
    const container = document.getElementById('quiz-app-container');
    if (!container) return; // Not on the quiz page

    // DOM Elements
    const setupSection = document.getElementById('quiz-setup');
    const quizSection = document.getElementById('quiz-interface');
    const resultSection = document.getElementById('quiz-results');
    
    const countInput = document.getElementById('question-count');
    const startBtn = document.getElementById('start-quiz-btn');
    const submitBtn = document.getElementById('submit-quiz-btn');
    const retryBtn = document.getElementById('retry-quiz-btn');
    
    const questionsListEl = document.getElementById('quiz-questions-list');
    const totalQuestionsCountEl = document.getElementById('total-questions-count');
    const currentQNumEl = document.getElementById('current-q-num');
    const totalQNumEl = document.getElementById('total-q-num');
    
    let allQuestions = [];
    let currentQuizQuestions = [];
    let userAnswers = {}; // { questionId: selectedOptionId }

    // Load Questions
    // Trying relative path assuming standard structure: /practice-exams/quiz-mode/ -> ../../assets/questions.json
    // Or if site_url path is involved, we might need adjustments. 
    // Let's try to detect the path.
    const jsonPath = '../../assets/questions.json';

    fetch(jsonPath)
        .then(response => {
            if (!response.ok) {
                // Fallback for flat URL structure or different nesting
                return fetch('../assets/questions.json');
            }
            return response;
        })
        .then(response => response.json())
        .then(data => {
            allQuestions = data;
            if (totalQuestionsCountEl) {
                totalQuestionsCountEl.textContent = allQuestions.length;
                countInput.max = allQuestions.length;
            }
        })
        .catch(err => {
            console.error('Error loading questions:', err);
            container.innerHTML = '<div class="admonition failure"><p class="admonition-title">Error</p><p>Could not load questions bank. Please check network connection or file path.</p></div>';
        });

    // Start Quiz
    startBtn.addEventListener('click', () => {
        const count = parseInt(countInput.value) || 10;
        const requestedCount = Math.min(Math.max(1, count), allQuestions.length);
        
        currentQuizQuestions = getRandomQuestions(allQuestions, requestedCount);
        totalQNumEl.textContent = requestedCount;
        userAnswers = {};
        
        renderQuiz(currentQuizQuestions);
        
        setupSection.style.display = 'none';
        quizSection.style.display = 'block';
        resultSection.style.display = 'none';
        window.scrollTo(0, 0);
    });

    // Submit Quiz
    submitBtn.addEventListener('click', () => {
        const score = calculateScore();
        showResults(score);
        
        quizSection.style.display = 'none';
        resultSection.style.display = 'block';
        window.scrollTo(0, 0);
    });

    // Retry
    retryBtn.addEventListener('click', () => {
        resultSection.style.display = 'none';
        setupSection.style.display = 'block';
        userAnswers = {};
        questionsListEl.innerHTML = '';
    });

    // Helper Functions
    function getRandomQuestions(all, count) {
        // Fisher-Yates shuffle copy
        const shuffled = [...all].sort(() => 0.5 - Math.random());
        return shuffled.slice(0, count);
    }

    function renderQuiz(questions) {
        questionsListEl.innerHTML = '';
        
        questions.forEach((q, index) => {
            const card = document.createElement('div');
            card.className = 'quiz-question-card';
            card.dataset.id = q.id;
            
            // Question Text
            const qTitle = document.createElement('div');
            qTitle.innerHTML = `<strong>Q${index + 1}.</strong> ${formatText(q.question)}`;
            card.appendChild(qTitle);
            
            // Options
            const optsList = document.createElement('ul');
            optsList.className = 'quiz-options';
            
            // Explanation Container (Hidden initially)
            const explanationDiv = document.createElement('div');
            explanationDiv.className = 'quiz-feedback';
            explanationDiv.style.display = 'none'; // Hidden by default
            explanationDiv.innerHTML = `
                <p>Correct Answer: <strong class="correct-badge">${q.answer}</strong></p>
                <hr>
                <p><strong>Explanation:</strong></p>
                <p>${formatText(q.explanation)}</p>
            `;
            
            if (q.options && q.options.length > 0) {
                q.options.forEach(opt => {
                    const li = document.createElement('li');
                    li.className = 'quiz-option';
                    li.dataset.val = opt.id;
                    li.innerHTML = `<strong>${opt.id}.</strong> ${opt.text}`;
                    
                    li.addEventListener('click', () => {
                        // Prevent changing answer if already answered
                        if (userAnswers[q.id]) return;
                        
                        // Save answer
                        userAnswers[q.id] = opt.id;
                        li.classList.add('selected');
                        
                        // Check correctness
                        const isCorrect = opt.id === q.answer;
                        
                        // Visual Feedback
                        if (isCorrect) {
                            li.style.backgroundColor = 'rgba(76, 175, 80, 0.2)'; // Green tint
                            li.style.borderColor = '#4caf50';
                            card.style.borderLeft = '5px solid #4caf50';
                        } else {
                            li.style.backgroundColor = 'rgba(244, 67, 54, 0.2)'; // Red tint
                            li.style.borderColor = '#f44336';
                            card.style.borderLeft = '5px solid #f44336';
                            
                            // Highlight the correct one
                            const correctLi = Array.from(optsList.children).find(child => child.dataset.val === q.answer);
                            if (correctLi) {
                                correctLi.style.backgroundColor = 'rgba(76, 175, 80, 0.2)';
                                correctLi.style.borderColor = '#4caf50';
                            }
                        }
                        
                        // Show Explanation
                        explanationDiv.style.display = 'block';
                    });
                    
                    optsList.appendChild(li);
                });
            } else {
                // No options (e.g. Ordering or Matching questions without MCQ choices)
                const revealBtn = document.createElement('button');
                revealBtn.className = 'md-button';
                revealBtn.textContent = 'Reveal Answer';
                revealBtn.style.marginTop = '1rem';
                revealBtn.addEventListener('click', () => {
                    explanationDiv.style.display = 'block';
                    revealBtn.style.display = 'none';
                    // Mark as viewed/answered (but effectively neutral for scoring loop unless logic adapted)
                    userAnswers[q.id] = "REVEALED";
                });
                optsList.appendChild(revealBtn);
            }
            
            card.appendChild(optsList);
            card.appendChild(explanationDiv);
            questionsListEl.appendChild(card);
        });
    }

    function calculateScore() {
        let correct = 0;
        let scorableTotal = 0;
        
        currentQuizQuestions.forEach(q => {
            // Only score questions that have options
            if (q.options && q.options.length > 0) {
                scorableTotal++;
                if (userAnswers[q.id] === q.answer) {
                    correct++;
                }
            }
        });
        
        return {
            correct: correct,
            total: scorableTotal
        };
    }

    function showResults(score) {
        const scoreTextEl = document.getElementById('score-text');
        const percentage = Math.round((score.correct / score.total) * 100);
        
        let message = "";
        if (percentage >= 72) {
             message = "<br><span style='color: #4caf50'>PASSED! Great job!</span>";
        } else {
             message = "<br><span style='color: #f44336'>FAILED. Keep practicing!</span>";
        }
        
        scoreTextEl.innerHTML = `${score.correct} / ${score.total} (${percentage}%)${message}`;
        
        const resultsContainer = document.getElementById('results-breakdown');
        resultsContainer.innerHTML = '<p>Review your answers above before trying again.</p>';
    }

    function formatText(text) {
        if (!text) return '';
        return text.replace(/\n/g, '<br>');
    }
});
