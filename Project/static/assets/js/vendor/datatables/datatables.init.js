// BASIC DATA TABLE
new DataTable("#basicDataTable", {
  pagingType: "simple_numbers",
  language: {
    paginate: {
      previous: "<i class='ri-arrow-left-line text-inherit'></i>",
      next: "<i class='ri-arrow-right-line text-inherit'></i>",
    },
    searchPlaceholder: "Search records...",
  },
});

// ROW SELECTION DELETION (SINGLE ROW)
const rowSelectionDeletion = new DataTable("#rowSelectionDeletion", {
  pagingType: "simple_numbers",
  language: {
    paginate: {
      previous: "<i class='ri-arrow-left-line text-inherit'></i>",
      next: "<i class='ri-arrow-right-line text-inherit'></i>",
    },
    searchPlaceholder: "Search records...",
  },
});

rowSelectionDeletion.on("click", "tbody tr", (e) => {
  let classList = e.currentTarget.classList;

  if (classList.contains("selected")) {
    classList.remove("selected");
  } else {
    rowSelectionDeletion
      .rows(".selected")
      .nodes()
      .each((row) => row.classList.remove("selected"));
    classList.add("selected");
  }
});

document
  .querySelector("#deleteRowButton")
  .addEventListener("click", function () {
    rowSelectionDeletion.row(".selected").remove().draw(false);
  });
