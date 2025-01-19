var html = document.documentElement;

// PAGE LOADER
function hideLoader() {
  document.getElementById("loader").remove();
}

// ON PAGE LOADED
window.addEventListener("load", function () {
  hideLoader();

  if (this.document.getElementById("app-menu-drawer")) {
    document
      .getElementById("app-menu-scrollbar")
      .querySelector(".scrollbar-track-x")
      .remove();
  }
});

// TOGGLE LIGHT AND DARK MOOD

let themeMode = document.documentElement.getAttribute("data-theme-mode");

// Check if the theme is stored in localStorage
if (localStorage.getItem("theme-mode")) {
  themeMode = localStorage.getItem("theme-mode");
}

// Set the data-theme-mode attribute and class on the <html> element
document.documentElement.setAttribute("data-theme-mode", themeMode);
document.documentElement.classList.add(themeMode);

// Function to toggle the theme
function toggleThemeMode() {
  themeMode = themeMode === "light" ? "dark" : "light";
  document.documentElement.setAttribute("data-theme-mode", themeMode);
  document.documentElement.classList.remove("light", "dark");
  document.documentElement.classList.add(themeMode);
  localStorage.setItem("theme-mode", themeMode);
}
// localStorage.clear();

// INTIALIZE SMOOTH SCROLLBAR
let option = {
  continuousScrolling: false,
  alwaysShowTracks: true,
};
if (document.querySelector("[data-scrollbar]")) {
  Scrollbar.initAll(option);
}

// Component accordion
const accordButtons = document.querySelectorAll(".com-accordion-button");
accordButtons.forEach((accordBtn, index) => {
  accordBtn.addEventListener("click", () => {
    accordButtons.forEach((item, i) => {
      if (index !== i) {
        item.classList.remove("open");
      }
    });
    accordBtn.classList.toggle("open");
    accordBtn.parentElement.classList.toggle("open");
  });
});

// CHECK ALL CHECKBOX WITH ONE CLICK
function allCheck(event, inputs) {
  Array.from(document.querySelectorAll(`.${inputs}`)).forEach((input) => {
    if (event.target.checked) {
      input.checked = true;
    } else {
      input.checked = false;
    }
  });
}

// CHECK ALL NOTIFICATION
if (document.querySelector("#checkboxAllNotification")) {
  document
    .querySelector("#checkboxAllNotification")
    .addEventListener("change", (event) => {
      allCheck(event, "checkboxNotification");
    });
}

// CHECK ALL MAIL
if (document.querySelector("#checkboxAllEmail")) {
  document
    .querySelector("#checkboxAllEmail")
    .addEventListener("change", (event) => {
      allCheck(event, "checkboxEmail");
    });
}

// REPLACE ALL EMPTY LINK WITH VOID
document.querySelectorAll('[href="#"]').forEach((link) => {
  let js_void = "javascript:void(0)";
  link.setAttribute("href", js_void);
});

// CHOICE EMAIL INPUT
if (document.getElementById("choices-input")) {
  new Choices(document.getElementById("choices-input"), {
    removeItemButton: true,
    maxItemCount: 3,
    duplicateItemsAllowed: false,
    allowHTML: true,
  });
}

// COLOR PICKER
if (document.getElementById("color-picker")) {
  document.getElementById("color-picker").addEventListener("change", () => {
    document.querySelector(".color-value").textContent =
      document.getElementById("color-picker").value;
  });
}
if (document.querySelectorAll(".color-picker")) {
  document.querySelectorAll(".color-picker").forEach((picker) => {
    const updateColor = () => {
      const newColor = picker.value;
      picker.closest("label").style.backgroundColor = newColor;
    };

    updateColor();
    picker.addEventListener("input", updateColor); // Use "input" event for immediate color change
  });
}

// FILE INPUT
function uploadFile() {
  // single image uploader
  document.querySelectorAll(".img-src").forEach(function (fileInput) {
    fileInput.onchange = function () {
      const reader = new FileReader();
      // read the image file as a data URL.
      reader.readAsDataURL(this.files[0]);

      reader.onload = (e) => {
        this.classList.add("uploaded");
        this.closest(
          ".file-container"
        ).style.backgroundImage = `url("${e.target.result}")`;
      };
    };
  });

  // Single File Uploader
  document.querySelectorAll(".file-src").forEach(function (fileInput) {
    fileInput.onchange = function () {
      const reader = new FileReader();
      // read the file as a data URL.
      reader.readAsDataURL(this.files[0]);
      let value = this.value;

      reader.onload = () => {
        this.classList.add("uploaded");
        this.closest(".file-container").querySelector(".file-name").innerHTML =
          value.substring(value.lastIndexOf("\\") + 1);
      };
    };
  });
}
uploadFile();

// Initialize All Date Input Value as TODAY
if (document.querySelector("[type='date']")) {
  document.querySelector("[type='date']").valueAsDate = new Date();
}

// INITIALIZE HEADER LANGUAGE
function setLanguage(lang) {
  switch (lang) {
    case "en":
      document.getElementById("header-lang-img").src =
        "assets/images/flag/us.svg";
      document.getElementById("header-lang-img").title = "English";
      break;
    case "sp":
      document.getElementById("header-lang-img").src =
        "assets/images/flag/es.svg";
      document.getElementById("header-lang-img").title = "Spanish";
      break;
    case "fr":
      document.getElementById("header-lang-img").src =
        "assets/images/flag/fr.svg";
      document.getElementById("header-lang-img").title = "French";
      break;
    case "it":
      document.getElementById("header-lang-img").src =
        "assets/images/flag/it.svg";
      document.getElementById("header-lang-img").title = "Italy";
      break;
    case "ar":
      document.getElementById("header-lang-img").src =
        "assets/images/flag/ar.svg";
      document.getElementById("header-lang-img").title = "Arabic";
      break;
  }
}
if (document.getElementById("dropdownLanguage")) {
  document
    .getElementById("dropdownLanguage")
    .addEventListener("click", (event) => {
      setLanguage(event.target.getAttribute("data-lang"));
    });
}

// Input range slide
document.querySelectorAll(".range-wrapper").forEach((rangeWrapper) => {
  const rangeInput = rangeWrapper.querySelector(".range-input");
  const rangeLine = rangeWrapper.querySelector(".range-line");
  const rangeHandler = rangeWrapper.querySelector(".range-handler");
  const rangeNumber = rangeWrapper.querySelectorAll(".range-number");
  const incrementButton =
    rangeWrapper.parentElement.querySelector(".range-increment");
  const decrementButton =
    rangeWrapper.parentElement.querySelector(".range-decrement");

  const rangeInputSlider = () => {
    if (rangeNumber.length) {
      rangeNumber.forEach((number) => (number.textContent = rangeInput.value));
    }

    const tooltipPosition = rangeInput.value / rangeInput.max;
    const space = rangeInput.offsetWidth - rangeHandler.offsetWidth;

    rangeHandler.style.left = tooltipPosition * space + "px";
    rangeLine.style.width = rangeInput.value + "%";
  };

  if (incrementButton) {
    incrementButton.addEventListener("click", function () {
      rangeInput.value = Math.min(
        parseInt(rangeInput.value) + 1,
        parseInt(rangeInput.max)
      );
      rangeInput.dispatchEvent(new Event("input"));
    });
  }

  if (decrementButton) {
    decrementButton.addEventListener("click", function () {
      rangeInput.value = Math.max(
        parseInt(rangeInput.value) - 1,
        parseInt(rangeInput.min)
      );
      rangeInput.dispatchEvent(new Event("input"));
    });
  }

  rangeInput.addEventListener("input", rangeInputSlider);
  rangeInputSlider();
});

// COUNTER NUMBER
(function counter() {
  const counters = document.querySelectorAll(".counter-value");

  if (counters.length) {
    counters.forEach((counter) => {
      const value = counter.getAttribute("data-value");
      const inc = value / 300;
      let count = 0;
      function pad(toPad, padChar, length) {
        return String(toPad).length < length
          ? new Array(length - String(toPad).length + 1).join(padChar) +
              String(toPad)
          : toPad;
      }
      function numberWithCommas(x) {
        return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
      }
      const updateCount = () => {
        count += inc;
        if (count < value) {
          counter.innerText = pad(numberWithCommas(count.toFixed(0)), "0", "2");
          setTimeout(updateCount, 1);
        } else {
          counter.innerText = pad(numberWithCommas(value), "0", "2");
        }
      };
      updateCount();
    });
  }
})();

// INITIALIZE CURRENT DATE
(function getCurrentTime() {
  const date = new Date();
  const day = [
    "Sunday",
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Sunday",
  ];
  const month = [
    "Jan",
    "Feb",
    "Mar",
    "Apr",
    "May",
    "Jun",
    "Jul",
    "Aug",
    "Sept",
    "Oct",
    "Nov",
    "Dec",
  ];
  const dayName = date.getDay();
  const todayDate = date.getDate();
  const monthName = date.getMonth();
  const year = date.getFullYear();
  document
    .querySelectorAll(".today")
    .forEach(
      (date) =>
        (date.innerHTML = `${day[dayName]}, ${todayDate} ${month[monthName]} ${year}`)
    );
})();

// INITIALIZE SUMMERNOTE
document.addEventListener("DOMContentLoaded", function () {
  const customTextArea = document.querySelectorAll(".summernote");
  customTextArea.forEach((textarea) => {
    $(textarea).summernote({
      placeholder: "Write your description here...",
      tabsize: 2,
      height: 200,
      toolbar: [
        ["style", ["style"]],
        ["font", ["bold", "underline", "clear"]],
        ["fontname", ["fontname"]],
        ["color", ["color"]],
        ["para", ["ul", "ol", "paragraph"]],
        ["height", ["height"]],
        ["table", ["table"]],
        ["insert", ["link", "picture", "video"]],
        ["view", ["fullscreen", "codeview", "help"]],
      ],
    });
  });
});

// TOGGLE PASSWORD
const inputTypeToggler = document.querySelectorAll(".inputTypeToggle");
inputTypeToggler.forEach(function (checkbox) {
  checkbox.addEventListener("change", function () {
    let passwordInput = this.parentElement.parentElement.children[0];

    passwordInput.type = this.checked ? "text" : "password";
  });
});

// STICKY NAVIGATION BAR
window.addEventListener("scroll", function () {
  const header = document.querySelector(".sticky-header");
  const header_height = header.offsetHeight;
  if (window.scrollY > header_height + 50) {
    header.classList.add("fixed_top");
  } else if (window.scrollY < header_height) {
    header.classList.remove("fixed_top");
  }
});
