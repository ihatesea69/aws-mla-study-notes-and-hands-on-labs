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
    let userAnswers = {}; // { questionId: answer (string or array) }

    // Load Questions
    const jsonPath = '../../assets/questions.json';

    fetch(jsonPath)
        .then(response => {
            if (!response.ok) {
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
        const shuffled = [...all].sort(() => 0.5 - Math.random());
        return shuffled.slice(0, count);
    }

    // Fisher-Yates shuffle for scrambling options
    function shuffleArray(array) {
        const arr = [...array];
        for (let i = arr.length - 1; i > 0; i--) {
            const j = Math.floor(Math.random() * (i + 1));
            [arr[i], arr[j]] = [arr[j], arr[i]];
        }
        return arr;
    }

    function renderQuiz(questions) {
        questionsListEl.innerHTML = '';
        
        questions.forEach((q, index) => {
            const card = document.createElement('div');
            card.className = 'quiz-question-card';
            card.dataset.id = q.id;
            card.dataset.type = q.type || 'multiple_choice';
            
            // Question Type Badge
            const typeBadge = document.createElement('div');
            typeBadge.className = 'question-type-badge';
            if (q.type === 'multiple_response') {
                typeBadge.innerHTML = `<span class="badge badge-warning">Select ${q.required_answers || 2}</span>`;
            } else if (q.type === 'ordering') {
                typeBadge.innerHTML = `<span class="badge badge-info">Ordering</span>`;
            }
            card.appendChild(typeBadge);
            
            // Question Text
            const qTitle = document.createElement('div');
            qTitle.innerHTML = `<strong>Q${index + 1}.</strong> ${formatText(q.question)}`;
            card.appendChild(qTitle);
            
            // Options Container
            const optsList = document.createElement('ul');
            optsList.className = 'quiz-options';
            
            // Explanation Container (Hidden initially)
            const explanationDiv = document.createElement('div');
            explanationDiv.className = 'quiz-feedback';
            explanationDiv.style.display = 'none';
            explanationDiv.innerHTML = `
                <p>Correct Answer: <strong class="correct-badge">${q.answer}</strong></p>
                <hr>
                <p><strong>Explanation:</strong></p>
                <p>${formatText(q.explanation)}</p>
            `;
            
            // Check Answer Button (for multi-select and ordering)
            const checkBtn = document.createElement('button');
            checkBtn.className = 'md-button md-button--primary';
            checkBtn.textContent = 'Check Answer';
            checkBtn.style.marginTop = '1rem';
            checkBtn.style.display = 'none';
            
            if (q.options && q.options.length > 0) {
                // Scramble options (except for ordering questions)
                const displayOptions = q.type === 'ordering' ? q.options : shuffleArray(q.options);
                
                if (q.type === 'multiple_response') {
                    // Multiple Response: allow selecting multiple
                    const requiredCount = q.required_answers || 2;
                    let selectedOptions = [];
                    
                    displayOptions.forEach(opt => {
                        const li = document.createElement('li');
                        li.className = 'quiz-option';
                        li.dataset.val = opt.id;
                        li.innerHTML = `<span class="eliminate-btn" title="Right-click to eliminate">✕</span>${opt.text}`;
                        
                        // Right-click to eliminate/restore option
                        li.addEventListener('contextmenu', (e) => {
                            e.preventDefault();
                            if (userAnswers[q.id]) return;
                            li.classList.toggle('eliminated');
                        });
                        
                        li.addEventListener('click', () => {
                            if (userAnswers[q.id]) return; // Already answered
                            
                            const idx = selectedOptions.indexOf(opt.id);
                            if (idx > -1) {
                                selectedOptions.splice(idx, 1);
                                li.classList.remove('selected');
                            } else {
                                if (selectedOptions.length < requiredCount) {
                                    selectedOptions.push(opt.id);
                                    li.classList.add('selected');
                                }
                            }
                            
                            // Show/hide check button
                            checkBtn.style.display = selectedOptions.length === requiredCount ? 'block' : 'none';
                        });
                        
                        optsList.appendChild(li);
                    });
                    
                    checkBtn.addEventListener('click', () => {
                        if (userAnswers[q.id]) return;
                        
                        const userAnswer = selectedOptions.sort().join(',');
                        const correctAnswer = q.answer.split(',').sort().join(',');
                        userAnswers[q.id] = userAnswer;
                        
                        const isCorrect = userAnswer === correctAnswer;
                        
                        // Visual feedback
                        Array.from(optsList.children).forEach(li => {
                            const optId = li.dataset.val;
                            const isInCorrectAnswer = q.answer.split(',').includes(optId);
                            const isSelected = selectedOptions.includes(optId);
                            
                            if (isInCorrectAnswer) {
                                li.style.backgroundColor = 'rgba(76, 175, 80, 0.2)';
                                li.style.borderColor = '#4caf50';
                            } else if (isSelected) {
                                li.style.backgroundColor = 'rgba(244, 67, 54, 0.2)';
                                li.style.borderColor = '#f44336';
                            }
                        });
                        
                        card.style.borderLeft = isCorrect ? '5px solid #4caf50' : '5px solid #f44336';
                        checkBtn.style.display = 'none';
                        explanationDiv.style.display = 'block';
                    });
                    
                } else if (q.type === 'matching') {
                    // Matching: render prompts with dropdown choices
                    const promptCount = q.options.length;
                    const choices = shuffleArray(q.matching_choices || []);
                    let matchSelections = {};
                    
                    // Create a dedicated check button for matching
                    const matchCheckBtn = document.createElement('button');
                    matchCheckBtn.className = 'md-button md-button--primary';
                    matchCheckBtn.textContent = 'Check Matches';
                    matchCheckBtn.style.marginTop = '1rem';
                    matchCheckBtn.style.display = 'none';
                    
                    q.options.forEach((prompt, idx) => {
                        const li = document.createElement('li');
                        li.className = 'quiz-option matching-option';
                        li.dataset.val = prompt.id;
                        
                        const select = document.createElement('select');
                        select.className = 'matching-select';
                        select.dataset.promptId = prompt.id;
                        
                        const defaultOpt = document.createElement('option');
                        defaultOpt.value = '';
                        defaultOpt.textContent = '-- Select --';
                        select.appendChild(defaultOpt);
                        
                        choices.forEach(choice => {
                            const choiceOpt = document.createElement('option');
                            choiceOpt.value = choice.id;
                            choiceOpt.textContent = choice.text;
                            select.appendChild(choiceOpt);
                        });
                        
                        select.addEventListener('change', () => {
                            if (userAnswers[q.id]) return;
                            matchSelections[prompt.id] = select.value;
                            
                            const assignedCount = Object.values(matchSelections).filter(v => v !== '').length;
                            matchCheckBtn.style.display = assignedCount === promptCount ? 'block' : 'none';
                        });
                        
                        li.appendChild(select);
                        
                        const textSpan = document.createElement('span');
                        textSpan.textContent = ` ${prompt.text}`;
                        li.appendChild(textSpan);
                        
                        optsList.appendChild(li);
                    });
                    
                    matchCheckBtn.addEventListener('click', () => {
                        if (userAnswers[q.id]) return;
                        
                        // Build user's matches: "1-A,2-B,3-C"
                        const userMatches = Object.keys(matchSelections)
                            .sort()
                            .map(k => `${k}-${matchSelections[k]}`)
                            .join(',');
                        
                        userAnswers[q.id] = userMatches;
                        
                        const isCorrect = userMatches === q.answer;
                        card.style.borderLeft = isCorrect ? '5px solid #4caf50' : '5px solid #f44336';
                        matchCheckBtn.style.display = 'none';
                        explanationDiv.style.display = 'block';
                        
                        // Disable selects
                        optsList.querySelectorAll('select').forEach(sel => sel.disabled = true);
                    });
                    
                    card.appendChild(optsList);
                    card.appendChild(matchCheckBtn);
                    card.appendChild(explanationDiv);
                    questionsListEl.appendChild(card);
                    return; // Skip normal append
                    
                } else if (q.type === 'ordering') {
                    // Ordering: render with dropdowns
                    const stepCount = q.options.length;
                    let orderSelections = {};
                    
                    // Shuffle the display order of steps
                    const shuffledSteps = shuffleArray([...q.options]);
                    
                    // Create a dedicated check button for ordering
                    const orderCheckBtn = document.createElement('button');
                    orderCheckBtn.className = 'md-button md-button--primary';
                    orderCheckBtn.textContent = 'Check Order';
                    orderCheckBtn.style.marginTop = '1rem';
                    orderCheckBtn.style.display = 'none';
                    
                    shuffledSteps.forEach((opt, optIdx) => {
                        const li = document.createElement('li');
                        li.className = 'quiz-option ordering-option';
                        li.dataset.val = opt.id;
                        
                        const select = document.createElement('select');
                        select.className = 'ordering-select';
                        select.dataset.optId = opt.id;
                        
                        const defaultOpt = document.createElement('option');
                        defaultOpt.value = '';
                        defaultOpt.textContent = 'Step ?';
                        select.appendChild(defaultOpt);
                        
                        for (let s = 1; s <= stepCount; s++) {
                            const stepOpt = document.createElement('option');
                            stepOpt.value = String(s);
                            stepOpt.textContent = `Step ${s}`;
                            select.appendChild(stepOpt);
                        }
                        
                        select.addEventListener('change', () => {
                            if (userAnswers[q.id]) return;
                            orderSelections[opt.id] = select.value;
                            
                            // Check if all steps are assigned
                            const assignedCount = Object.values(orderSelections).filter(v => v !== '').length;
                            orderCheckBtn.style.display = assignedCount === stepCount ? 'block' : 'none';
                        });
                        
                        li.appendChild(select);
                        
                        const textSpan = document.createElement('span');
                        textSpan.textContent = ' ' + opt.text;
                        li.appendChild(textSpan);
                        
                        optsList.appendChild(li);
                    });
                    
                    orderCheckBtn.addEventListener('click', () => {
                        if (userAnswers[q.id]) return;
                        
                        // Build user's order: step1=optId, step2=optId, ...
                        const userOrder = [];
                        for (let s = 1; s <= stepCount; s++) {
                            const optId = Object.keys(orderSelections).find(k => orderSelections[k] === String(s));
                            if (optId) userOrder.push(optId);
                        }
                        
                        const userAnswer = userOrder.join(',');
                        const correctAnswer = q.answer;
                        userAnswers[q.id] = userAnswer;
                        
                        const isCorrect = userAnswer === correctAnswer;
                        card.style.borderLeft = isCorrect ? '5px solid #4caf50' : '5px solid #f44336';
                        orderCheckBtn.style.display = 'none';
                        explanationDiv.style.display = 'block';
                        
                        // Disable selects
                        optsList.querySelectorAll('select').forEach(sel => sel.disabled = true);
                    });
                    
                    card.appendChild(optsList);
                    card.appendChild(orderCheckBtn);
                    card.appendChild(explanationDiv);
                    questionsListEl.appendChild(card);
                    return; // Skip normal append at end (we're in forEach)
                    
                } else {
                    // Multiple Choice (default): single select with instant feedback
                    displayOptions.forEach(opt => {
                        const li = document.createElement('li');
                        li.className = 'quiz-option';
                        li.dataset.val = opt.id;
                        li.innerHTML = `<span class="eliminate-btn" title="Right-click to eliminate">✕</span>${opt.text}`;
                        
                        // Right-click to eliminate/restore option
                        li.addEventListener('contextmenu', (e) => {
                            e.preventDefault();
                            if (userAnswers[q.id]) return;
                            li.classList.toggle('eliminated');
                        });
                        
                        li.addEventListener('click', () => {
                            if (userAnswers[q.id]) return;
                            
                            userAnswers[q.id] = opt.id;
                            li.classList.add('selected');
                            
                            const isCorrect = opt.id === q.answer;
                            
                            if (isCorrect) {
                                li.style.backgroundColor = 'rgba(76, 175, 80, 0.2)';
                                li.style.borderColor = '#4caf50';
                                card.style.borderLeft = '5px solid #4caf50';
                            } else {
                                li.style.backgroundColor = 'rgba(244, 67, 54, 0.2)';
                                li.style.borderColor = '#f44336';
                                card.style.borderLeft = '5px solid #f44336';
                                
                                const correctLi = Array.from(optsList.children).find(child => child.dataset.val === q.answer);
                                if (correctLi) {
                                    correctLi.style.backgroundColor = 'rgba(76, 175, 80, 0.2)';
                                    correctLi.style.borderColor = '#4caf50';
                                }
                            }
                            
                            explanationDiv.style.display = 'block';
                        });
                        
                        optsList.appendChild(li);
                    });
                }
            } else {
                // No options: just reveal button
                const revealBtn = document.createElement('button');
                revealBtn.className = 'md-button';
                revealBtn.textContent = 'Reveal Answer';
                revealBtn.style.marginTop = '1rem';
                revealBtn.addEventListener('click', () => {
                    explanationDiv.style.display = 'block';
                    revealBtn.style.display = 'none';
                    userAnswers[q.id] = "REVEALED";
                });
                optsList.appendChild(revealBtn);
            }
            
            card.appendChild(optsList);
            card.appendChild(checkBtn);
            card.appendChild(explanationDiv);
            questionsListEl.appendChild(card);
        });
    }

    function calculateScore() {
        let correct = 0;
        let scorableTotal = 0;
        
        currentQuizQuestions.forEach(q => {
            if (q.options && q.options.length > 0 && q.type !== 'ordering') {
                scorableTotal++;
                
                if (q.type === 'multiple_response') {
                    const userAnswer = userAnswers[q.id] || '';
                    const correctAnswer = q.answer.split(',').sort().join(',');
                    const userSorted = userAnswer.split(',').sort().join(',');
                    if (userSorted === correctAnswer) {
                        correct++;
                    }
                } else {
                    if (userAnswers[q.id] === q.answer) {
                        correct++;
                    }
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
        const percentage = score.total > 0 ? Math.round((score.correct / score.total) * 100) : 0;
        
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
