// function checkAnswer(quizIndex, correctAnswerIndex) {
//     console.log("In checkAnswer with" + quizIndex + " and " + correctAnswerIndex)
//     const selectedOption = document.querySelector(`input[name="quiz-${quizIndex}"]:checked`);
//     if (selectedOption) {
//         const isCorrect = parseInt(selectedOption.value) === correctAnswerIndex;
//         alert(isCorrect ? "Correct!" : "Incorrect!");
//         // Display the explanation
//         const explanation = selectedOption.closest('.quiz').querySelector('.explanation');
//         if (explanation) {
//             explanation.style.display = 'block';
//         }
//     } else {
//         alert("Please select an answer.");
//     }
// }


document.addEventListener('DOMContentLoaded', () => {
  
  document.querySelectorAll('.question').forEach((question) => {
    let form = question.querySelector('form');
    let correctAnswer = question.dataset.correctAnswer; // Get correct answer from data attribute
    
    form.addEventListener('submit', (event) => {
      event.preventDefault();

      // Get the selected answer
      let selectedAnswer = form.querySelector('input[name^="quiz"]:checked');

      // Reset previous markings
      resetFieldset(question);

      if (selectedAnswer) {
        // Check if the selected answer is correct
        if (selectedAnswer.value === correctAnswer) {
          // Mark the correct answer
          selectedAnswer.parentElement.classList.add('correct');
          // Show the explanation
          question.querySelector('.explanation').style.display = 'block';
        } else {
          // Mark the selected answer as incorrect
          selectedAnswer.parentElement.classList.add('wrong');
        }
      }
    });
  });
});

function resetFieldset(question) {
  const fieldsetChildren = question.querySelectorAll('div');
  fieldsetChildren.forEach((child) => {
    child.classList.remove('wrong');
    child.classList.remove('correct');
  });

  // Hide the explanation again
  const explanation = question.querySelector('.explanation');
  if (explanation) {
    explanation.style.display = 'none';
  }
}


