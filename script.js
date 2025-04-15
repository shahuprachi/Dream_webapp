// Optional confirmation message on dream submission
document.addEventListener("DOMContentLoaded", function () {
  const form = document.querySelector("form");

  if (form) {
    form.addEventListener("submit", function () {
      alert("✅ Your dream has been submitted successfully!");
    });
  }

  // Highlight dream entries on hover
  const dreamCards = document.querySelectorAll(".dream-entry");
  dreamCards.forEach((card) => {
    card.addEventListener("mouseover", () => {
      card.style.backgroundColor = "#f0f4ff";
    });
    card.addEventListener("mouseout", () => {
      card.style.backgroundColor = "#fff";
    });
  });
});
