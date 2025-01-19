document.querySelectorAll(".prism-toggle").forEach((element) => {
  element.addEventListener("click", function () {
    let carElement = this.parentNode.parentNode;
    this.children[1].classList.toggle("ri-code-line");
    this.children[1].classList.toggle("ri-code-s-slash-line");

    if (!carElement.children[1].classList.contains("hidden")) {
      carElement.children[1].classList.add("hidden");
      carElement.children[2].classList.remove("hidden");
    } else {
      carElement.children[1].classList.remove("hidden");
      carElement.children[2].classList.add("hidden");
    }
  });
});

// Aleart Close
document.querySelectorAll(".close-button").forEach((button) => {
  button.addEventListener("click", function () {
    this.parentNode.classList.add("hidden");
  });
});
