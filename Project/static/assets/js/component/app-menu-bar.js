// Declare for First Layer Dropdown Buttons
let topLayerButtons = document.querySelectorAll(".dropdown-button.top-layer");

// Loop all The First Layer Dropdown Buttons
topLayerButtons.forEach((topLayerBtn, index) => {
  // Declare for First Layer Dropdown Content
  const firstLayerDropdownContent = topLayerBtn.nextElementSibling;

  // Init for First Layer Dropdown Content Height
  let firstLayerDropdownContentHeight = firstLayerDropdownContent.scrollHeight;

  // Declare For All Drowpdown Content Container(ul)
  const firstLayerContentContainer =
    firstLayerDropdownContent.firstElementChild;

  // Init for Second Layer Dropdown Buttons
  let secondLayerButtonsArray = [];

  topLayerBtn.addEventListener("click", function () {
    // Set the Height For The Dropdown Content
    firstLayerDropdownContentHeight = this.nextElementSibling.scrollHeight;

    if (document.documentElement.getAttribute("data-sidebar-size") != "sm") {
      // Check if There Are Available Dropdown Content
      if (firstLayerDropdownContent) {
        topLayerBtn.classList.toggle("show");
        //  Check The First Layer Dropdown Content Height
        if (firstLayerDropdownContent.style.maxHeight) {
          // If Height Then Set The Height To NULL
          firstLayerDropdownContent.style.maxHeight = null;
        } else {
          // Else Set The Height
          firstLayerDropdownContent.style.maxHeight =
            firstLayerDropdownContentHeight + "px";
        }
      }

      // Loop All Top Layer Button For Unclicke Buttons
      topLayerButtons.forEach((topLayerNotClickedBtn, i) => {
        // Check If The Buttons Is Not Clicked
        if (index != i && topLayerNotClickedBtn.nextElementSibling) {
          topLayerNotClickedBtn.classList.remove("show");
          // Set All Not Click Button Content TO null
          topLayerNotClickedBtn.nextElementSibling.style.maxHeight = null;
        }
      });
    }
  });

  // Loop All Dropdown Container For Second Layer Dropdown Buttons
  for (let i = 0; i < firstLayerContentContainer.children.length; i++) {
    const element = firstLayerContentContainer.children[i];

    // If find the Buttons then push them on the array
    if (element.firstElementChild.classList.contains("second-layer")) {
      secondLayerButtonsArray.push(element.firstElementChild);
    }
  }

  // Check If the Array is not Empty
  if (secondLayerButtonsArray.length > 0) {
    secondLayerButtonsArray.forEach((secondLayerBtn, secondLayerBtnIndex) => {
      // Declare For The Second Layer Dropdown Content
      const secondLayerDropdownContent = secondLayerBtn.nextElementSibling;

      secondLayerBtn.addEventListener("click", function () {
        // Reserve Clicked Dropdown Content Height
        let secondLayerDropdownContentHeight =
          this.nextElementSibling.scrollHeight;

        if (
          document.documentElement.getAttribute("data-sidebar-size") != "sm"
        ) {
          if (secondLayerDropdownContent) {
            secondLayerBtn.classList.toggle("show");

            //  Check The Second Layer Dropdown Content Height
            if (secondLayerDropdownContent.style.maxHeight) {
              // If Height Then Set The Height To NULL
              secondLayerDropdownContent.style.maxHeight = null;
            } else {
              // Else Update First Layer Dropdown Content Height
              firstLayerDropdownContent.style.maxHeight =
                firstLayerDropdownContentHeight +
                secondLayerDropdownContentHeight +
                "px";

              // And Set Second Layer Dropdown Content Height
              secondLayerDropdownContent.style.maxHeight =
                secondLayerDropdownContentHeight + "px";
            }
          }

          // Loop All Second Layer Button For Unclicked Buttons
          secondLayerButtonsArray.forEach((secondLayerNotClickedBtn, i) => {
            if (
              secondLayerBtnIndex != i &&
              secondLayerNotClickedBtn.nextElementSibling &&
              topLayerBtn.classList.contains("show")
            ) {
              secondLayerNotClickedBtn.classList.remove("show");
              // Set All Not Click Button Content TO null
              secondLayerNotClickedBtn.nextElementSibling.style.maxHeight =
                null;
            }
          });
        }
      });
    });
  }
});
